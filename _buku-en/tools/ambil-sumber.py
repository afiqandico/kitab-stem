#!/usr/bin/env python3
"""Ambil ulang salinan sumber materi belakang dari edisi Indonesia.

Gerbang `cek-belakang.py` membandingkan terjemahan dengan sumber Indonesia. Salinan
sumber di `belakang/_sumber/` TIDAK boleh basi: kalau `../_buku-ed2/main.tex` berubah
dan salinan tidak, gerbang akan membandingkan terjemahan dengan teks lama dan bisa
meloloskan kesalahan. Karena itu salinan dibuat ulang dari penanda (bukan nomor baris,
yang bergeser setiap suntingan).

    python3 tools/ambil-sumber.py          # tulis ulang belakang/_sumber/
    python3 tools/ambil-sumber.py --cek    # 0 bila salinan masih sama dengan sumber
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EN = os.path.dirname(HERE)
ID = os.path.join(os.path.dirname(EN), "_buku-ed2")
SUMBER = os.path.join(EN, "belakang", "_sumber")

# (nama, penanda awal, penanda akhir) - potongan main.tex edisi Indonesia.
POTONGAN = {
    "depan-a": ("\\chapter*{Kata Pengantar}", "\\chapter*{Cara Membaca: Empat Jalur}"),
    "depan-b": ("\\chapter*{Cara Membaca: Empat Jalur}", "\\chapter*{Peta Ketergantungan Bab}"),
    "depan-c": ("\\chapter*{Peta Ketergantungan Bab}", "\\mainmatter"),
    "lampA": ("\\appendix", "\\chapter{Glosarium}"),
    "lampB": ("\\chapter{Glosarium}", "\\chapter{Petunjuk dan Kriteria Penilaian Latihan}"),
    "lampC": ("\\chapter{Petunjuk dan Kriteria Penilaian Latihan}", "\\chapter{Kunci Jawaban}"),
    "lampD": ("\\chapter{Kunci Jawaban}", "% ---------------------------- indeks"),
    "kolofon": ("\\chapter*{Kolofon}", "\\chapter*{Daftar Rujukan}"),
    "rujukan": ("\\chapter*{Daftar Rujukan}", "\\end{document}"),
}
KUNCI = ("kunci-01-05", "kunci-06-15", "kunci-16-23", "kunci-24-32")


def bersihkan(teks: list[str]) -> str:
    """Buang komentar pemisah dan baris kosong di ujung, seperti versi yang dipakai."""
    while teks and (not teks[-1].strip() or teks[-1].lstrip().startswith("%")):
        teks.pop()
    return "\n".join(teks) + "\n"


def bangun() -> dict[str, str]:
    main = open(os.path.join(ID, "main.tex"), encoding="utf-8").read()
    hasil: dict[str, str] = {}
    for nama, (awal, akhir) in POTONGAN.items():
        i = main.index(awal)
        j = main.index(akhir, i + len(awal))
        baris = main[i:j].split("\n")
        if nama == "lampD":
            # \input diisi main-en.tex dengan berkas Inggris; nomor berkas Indonesia
            # tidak boleh ikut terbaca sebagai isi naskah.
            baris = [b for b in baris if not b.startswith("\\input{")]
        hasil[nama] = bersihkan(baris)
    for nama in KUNCI:
        hasil[nama] = open(os.path.join(ID, "lampiran-kunci", nama + ".tex"), encoding="utf-8").read()
    return hasil


def main(argv: list[str]) -> int:
    baru = bangun()
    if "--cek" in argv:
        beda = []
        for nama, isi in baru.items():
            p = os.path.join(SUMBER, nama + ".tex")
            if not os.path.exists(p) or open(p, encoding="utf-8").read() != isi:
                beda.append(nama)
        print("sumber basi: " + ", ".join(beda) if beda else "sumber segar: salinan cocok dengan edisi Indonesia")
        return 1 if beda else 0
    os.makedirs(SUMBER, exist_ok=True)
    for nama, isi in baru.items():
        open(os.path.join(SUMBER, nama + ".tex"), "w", encoding="utf-8").write(isi)
    print(f"{len(baru)} berkas sumber ditulis ke {os.path.relpath(SUMBER, EN)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
