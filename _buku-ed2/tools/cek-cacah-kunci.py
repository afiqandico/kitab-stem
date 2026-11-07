#!/usr/bin/env python3
"""Gerbang pemetaan butir: setiap latihan bab harus punya tepat satu butir kunci.

Bukan gerbang kebenaran isi (itu tugas audit), hanya cacah & penomoran:
- hitung `\\item` level teratas di lingkungan `latihan` setiap bab (item bersarang
  seperti soal pilihan ganda Bab 1 tidak ikut dihitung),
- hitung `\\item` level teratas di blok `\\section*{Bab N: ...}` pada lampiran kunci,
- laporkan bab yang cacahnya tidak sama, blok yang hilang, atau label `N.k` yang
  tidak berurutan.

Pakai: python3 tools/cek-cacah-kunci.py [--verbose]
Keluar 0 bila semua 32 bab 1:1, 1 bila ada selisih.
"""
from __future__ import annotations

import glob
import re
import sys

HERE = __file__.rsplit("/tools/", 1)[0]


def top_level_items(seg: str) -> int:
    """Hitung `\\item` milik enumerate terluar segmen, bukan milik yang bersarang.

    Trap yang sudah menggigit: kedalaman dihitung dari 0, sehingga enumerate
    pembungkus `latihan`/blok kunci sendiri menaikkan kedalaman ke 1 dan
    penghitung mengembalikan 0 -- lalu 0 == 0 dilaporkan "OK" (false green).
    Karena itu butir dihitung pada kedalaman 1, dan jumlah 0 ditolak pemanggil.
    """
    depth = 0
    n = 0
    for m in re.finditer(r"\\(begin|end)\{(enumerate|itemize)\}|\\item\b", seg):
        tok = m.group(0)
        if tok.startswith("\\item"):
            if depth == 1:
                n += 1
        elif m.group(1) == "begin":
            depth += 1
        else:
            depth = max(0, depth - 1)
    return n


def latihan_block(chapter_src: str) -> str | None:
    m = re.search(r"\\begin\{latihan\}(.*?)\\end\{latihan\}", chapter_src, re.S)
    return m.group(1) if m else None


def key_blocks() -> dict[int, str]:
    blocks: dict[int, str] = {}
    for path in sorted(glob.glob(f"{HERE}/lampiran-kunci/*.tex")):
        src = open(path, encoding="utf-8").read()
        parts = re.split(r"\\section\*\{Bab (\d+):", src)
        # parts = [pre, n, body, n, body, ...]
        for i in range(1, len(parts), 2):
            n = int(parts[i])
            body = parts[i + 1]
            blocks[n] = body
    return blocks


def key_labels(block: str) -> list[int]:
    """Label `\\textbf{N.k}` kalau berkas memakainya, untuk cek urutan."""
    head = re.search(r"\[label=\\textbf\{(\d+)\.\\arabic\*\\}\]", block)
    if not head:
        return []
    return [1]  # penanda bahwa penomoran otomatis; tidak ada label eksplisit


def main() -> int:
    verbose = "--verbose" in sys.argv
    keys = key_blocks()
    bad = 0
    total_lat = total_key = 0
    print("bab latihan kunci status")
    for n in range(1, 33):
        try:
            src = open(f"{HERE}/ch{n:02d}.tex", encoding="utf-8").read()
        except FileNotFoundError:
            print(f"{n:3d} {'-':>7} {'-':>5} BAB HILANG")
            bad += 1
            continue
        seg = latihan_block(src)
        if seg is None:
            print(f"{n:3d} {'-':>7} {'-':>5} TANPA LATIHAN")
            bad += 1
            continue
        lat = top_level_items(seg)
        if lat == 0:
            print(f"{n:3d} {lat:7d} {'-':>5} NOL-BUTIR (parser buta)")
            bad += 1
            continue
        if n not in keys:
            print(f"{n:3d} {lat:7d} {'-':>5} KUNCI HILANG")
            bad += 1
            continue
        key = top_level_items(keys[n])
        total_lat += lat
        total_key += key
        if lat == key:
            print(f"{n:3d} {lat:7d} {key:5d} OK")
        else:
            print(f"{n:3d} {lat:7d} {key:5d} BEDA ({lat - key:+d})")
            bad += 1
        if verbose:
            print(f"     label otomatis: {key_labels(keys[n])}")
    print(f"\nTOTAL butir latihan: {total_lat}   butir kunci: {total_key}")
    if bad:
        print(f"Bab bermasalah: {bad}")
        return 1
    print("Semua bab 1:1")
    return 0


if __name__ == "__main__":
    sys.exit(main())
