#!/usr/bin/env python3
"""Uji gerbang cek-belakang.py: satu kontrol positif + empat cacat yang ditanam.

Kalau gerbang menerima berkas yang masih Indonesia, atau melewatkan satu butir yang
hilang / satu angka yang berubah, semua laporan "OK" di atasnya tidak berarti apa-apa.
Self-test ini memakai tempfile: sumber dan sasaran palsu, tidak menyentuh berkas nyata.

    python3 tools/uji-cek-belakang.py        # harus 'N/N PASS', exit 0
"""
from __future__ import annotations

import importlib.util
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
EN = os.path.dirname(HERE)


def muat():
    spec = importlib.util.spec_from_file_location("cekbel", os.path.join(HERE, "cek-belakang.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CB = muat()
HASIL: list[tuple[str, bool, str]] = []


def periksa(nama: str, harus_gagal: bool, catatan: str) -> None:
    masalah = CB.cek(nama)
    lulus = bool(masalah) == harus_gagal
    HASIL.append((nama, lulus, f"{catatan}: {'ditolak' if masalah else 'diterima'} {masalah[:2]}"))


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        sumdir = os.path.join(tmp, "sumber")
        sardir = os.path.join(tmp, "sasaran")
        os.makedirs(sumdir, exist_ok=True)
        os.makedirs(sardir, exist_ok=True)
        CB.SUMBER, CB.SASARAN, CB.BAGIAN = sumdir, sardir, {"uji": ("uji", 0.75, 1.35)}

        asli = open(os.path.join(EN, "belakang", "_sumber", "lampB.tex"), encoding="utf-8").read()
        open(os.path.join(sumdir, "uji.tex"), "w", encoding="utf-8").write(asli)

        # Baselin: kata fungsi Indonesia diganti penanda Inggris, bukan terjemahan sungguhan.
        # Tujuannya hanya menguji mekanisme gerbang (residu, jumlah butir, angka, matematika).
        baseline = re.sub(r"\b(" + "|".join(sorted(CB.KATA_ID)) + r")\b", "the", asli, flags=re.I)
        p = os.path.join(sardir, "uji-en.tex")
        open(p, "w", encoding="utf-8").write(baseline)
        periksa("uji", False, "baseline bersih (kontrol positif)")

        # F1: satu butir daftar dihapus
        baris = [l for l in baseline.split("\n") if l.lstrip().startswith("\\item")]
        cacat = baseline.replace(baris[3], "", 1)
        open(p, "w", encoding="utf-8").write(cacat)
        periksa("uji", True, "F1 butir \\item dihapus")

        # F2: satu angka di dalam matematika diubah
        m = re.search(r"\$[^$]*\d[^$]*\$", baseline)
        assert m, "sumber tidak memuat matematika berangka"
        rusak = m.group(0)
        angka_baru = re.sub(r"\d", lambda d: str((int(d.group(0)) + 1) % 10), rusak)
        cacat = baseline.replace(rusak, angka_baru, 1)
        open(p, "w", encoding="utf-8").write(cacat)
        periksa("uji", True, "F2 angka dalam matematika diubah")

        # F3: satu paragraf masih Indonesia
        cacat = baseline + "\n\nTerjemahan ini belum selesai dan bagian ini masih berbahasa Indonesia karena ada yang tertinggal di berkas.\n"
        open(p, "w", encoding="utf-8").write(cacat)
        periksa("uji", True, "F3 prosa Indonesia tertinggal")

        # F4: diringkas (hilang hampir separuh)
        cacat = "\n".join(baseline.split("\n")[: len(baseline.split("\n")) // 2])
        open(p, "w", encoding="utf-8").write(cacat)
        periksa("uji", True, "F4 isi diringkas")

        # F5: label dihapus
        cacat = re.sub(r"\\label\{[^}]*\}", "", baseline, count=1)
        open(p, "w", encoding="utf-8").write(cacat)
        periksa("uji", True, "F5 label hilang")

    lulus = sum(1 for _, ok, _ in HASIL if ok)
    for nama, ok, catatan in HASIL:
        print(f"{'PASS' if ok else 'GAGAL'} {nama}: {catatan}")
    print(f"\n{lulus}/{len(HASIL)} PASS")
    return 0 if lulus == len(HASIL) else 1


if __name__ == "__main__":
    sys.exit(main())
