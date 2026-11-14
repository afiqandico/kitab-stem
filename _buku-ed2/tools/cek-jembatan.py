#!/usr/bin/env python3
"""Periksa kelengkapan "Jembatan pemahaman" di setiap bab edisi kedua.

Pemakaian:  python3 tools/cek-jembatan.py [--ketat]
  (tanpa --ketat) melaporkan cakupan, keluar 0 bila tidak ada bab yang rusak sintaks blok
  --ketat         keluar 1 bila ada bab yang belum lengkap (untuk gerbang rilis)

Blok yang diperiksa (urutan wajib seperti di PANDUAN-BAB-ED2.md):
  1. bagian      \\section{Jembatan pemahaman...}
  2. analogi     \\subsection{Analogi nyata...}
  3. manual      \\subsection{Hitung manual dulu}
  4. kamus       \\subsection{Kamus baca simbol}
  5. keamanan    \\subsection{Kenapa ini penting untuk keamanan?}
  6. tangan      \\subsection{Latihan menghitung dengan tangan}
  7. kode        \\subsection{Dari kertas ke kode} + \\begin{lab} + \\begin{verbatim}
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BAB = os.path.join(os.path.dirname(HERE), "_buku-ed2")
if not os.path.isdir(BAB):
    BAB = os.path.dirname(HERE)

BLOK = [
    ("bagian", r"\\section\{Jembatan pemahaman"),
    ("analogi", r"\\subsection\{Analogi nyata"),
    ("manual", r"\\subsection\{Hitung manual dulu\}"),
    ("kamus", r"\\subsection\{Kamus baca simbol\}"),
    ("keamanan", r"\\subsection\{Kenapa ini penting untuk keamanan\?\}"),
    ("tangan", r"\\subsection\{Latihan menghitung dengan tangan\}"),
    ("kode", r"\\subsection\{Dari kertas ke kode\}"),
]


def periksa(path: str) -> tuple[dict[str, bool], list[str]]:
    s = open(path, encoding="utf-8", errors="replace").read()
    hasil = {nama: bool(re.search(pola, s)) for nama, pola in BLOK}
    # blok kode wajib benar-benar memuat lab + verbatim, bukan hanya judulnya
    hasil["kode"] = (
        hasil["kode"]
        and "\\begin{lab}" in s
        and "\\begin{verbatim}" in s
    )
    catatan: list[str] = []
    if hasil["bagian"]:
        # urutan: bagian harus muncul sebelum blok kode di berkas
        urut = [s.find(pola) for _, pola in BLOK]
        urut = [i for i in urut if i >= 0]
        if urut != sorted(urut):
            catatan.append("urutan blok tidak sesuai")
    return hasil, catatan


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ketat", action="store_true", help="keluar 1 bila ada bab belum lengkap")
    ap.add_argument("--bab", help="hanya periksa satu bab, mis. ch25")
    args = ap.parse_args()

    pola = os.path.join(BAB, (args.bab or "ch*") + ".tex")
    berkas = sorted(glob.glob(pola))
    if not berkas:
        print(f"tidak ada berkas cocok: {pola}")
        return 2

    lengkap, belum = [], []
    lebar = max(len(n) for n, _ in BLOK)
    for path in berkas:
        nama = os.path.splitext(os.path.basename(path))[0]
        hasil, catatan = periksa(path)
        hilang = [n for n, ada in hasil.items() if not ada]
        tanda = "LENGKAP" if not hilang else "belum: " + ",".join(hilang)
        if catatan:
            tanda += " (" + "; ".join(catatan) + ")"
        print(f"{nama}  {tanda}")
        (belum if hilang else lengkap).append(nama)

    print()
    print(f"BAB LENGKAP : {len(lengkap)}/{len(berkas)}"
          + (f" -> {' '.join(lengkap)}" if lengkap else ""))
    print(f"BAB BELUM   : {len(belum)}/{len(berkas)}")
    print(f"Blok yang diperiksa ({lebar} huruf terpanjang): "
          + ", ".join(n for n, _ in BLOK))
    if args.ketat and belum:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
