#!/usr/bin/env python3
"""Verifikasi ad-hoc (bukan suite kanonik) untuk tools/verify-kunci-24.py.

Yang dibuktikan:
  A. pengecek menerima pohon nyata: rc=0, 48/48 PASS;
  B. pengecek menangkap nomor kunci yang salah: satu mutasi di lampiran kunci
     menghasilkan TEPAT satu FAIL, di butir 24.8;
  C. pengecek menangkap data soal yang berubah: satu mutasi berat knapsack di
     ch24.tex menghasilkan TEPAT satu FAIL, di cek data soal (tupel ID dan EN
     tercetak), bukan di cek angka;
  D. sandbox pulih: setelah salinan dipulihkan, kembali 48/48.

Alasan uji negatif ini ada: PASS di skrip pengecek hanya bermakna kalau
pemeriksanya memang bisa gagal. Tanpa B dan C, "48/48" tidak membedakan
"semua cocok" dari "tidak ada yang diperiksa".

Jalankan: python3 tools/uji-verify-kunci-24.py   (dari _buku-ed2/, ~5 detik)
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BUKU = os.path.dirname(os.path.dirname(HERE))
ID = os.path.join(BUKU, "_buku-ed2")
EN = os.path.join(BUKU, "_buku-en")
SCRIPT = os.path.join(HERE, "verify-kunci-24.py")

MASUKAN = {
    "_buku-ed2/ch24.tex": os.path.join(ID, "ch24.tex"),
    "_buku-en/ch24.tex": os.path.join(EN, "ch24.tex"),
    "_buku-ed2/lampiran-kunci/kunci-24-32.tex":
        os.path.join(ID, "lampiran-kunci", "kunci-24-32.tex"),
    "_buku-en/belakang/kunci-24-32-en.tex":
        os.path.join(EN, "belakang", "kunci-24-32-en.tex"),
}
gagal = []


def cek(nama, syarat, bukti=""):
    print(("PASS " if syarat else "FAIL ") + nama + ("  " + bukti if bukti else ""))
    if not syarat:
        gagal.append(nama)


def jalankan(akar):
    r = subprocess.run([sys.executable, os.path.join(akar, "_buku-ed2", "tools",
                                                     "verify-kunci-24.py")],
                       capture_output=True, text=True)
    baris = r.stdout.splitlines()
    return (r.returncode,
            sum(b.startswith("PASS") for b in baris),
            [b for b in baris if b.startswith("FAIL")])


def tanam(akar, rel, lama, baru):
    p = os.path.join(akar, rel)
    s = open(p, encoding="utf-8").read()
    assert lama in s, f"mutasi tak menempel: {lama!r} tidak ada di {rel}"
    open(p, "w", encoding="utf-8").write(s.replace(lama, baru, 1))


def pulihkan(akar):
    for rel, src in MASUKAN.items():
        shutil.copy2(src, os.path.join(akar, rel))


akar = tempfile.mkdtemp(prefix="uji-kunci24-")
try:
    for rel in MASUKAN:
        os.makedirs(os.path.join(akar, os.path.dirname(rel)), exist_ok=True)
    for rel, src in MASUKAN.items():
        shutil.copy2(src, os.path.join(akar, rel))
    os.makedirs(os.path.join(akar, "_buku-ed2", "tools"), exist_ok=True)
    shutil.copy2(SCRIPT, os.path.join(akar, "_buku-ed2", "tools", "verify-kunci-24.py"))
    # pengecek membaca keempat berkas lewat akar repo: akar diturunkan dari
    # lokasinya sendiri, jadi salinan di sandbox memakai berkas sandbox.

    rc, n, gagal_cek = jalankan(akar)                                    # A
    cek("A pohon nyata: rc=0, 48/48", rc == 0 and n == 48 and not gagal_cek,
        f"rc={rc} pass={n} fail={gagal_cek}")

    tanam(akar, "_buku-ed2/lampiran-kunci/kunci-24-32.tex", "15{,}25", "15{,}35")
    rc, n, gagal_cek = jalankan(akar)                                    # B
    cek("B nomor kunci salah: tepat 1 FAIL di 24.8",
        rc == 1 and len(gagal_cek) == 1 and "24.8 teks" in gagal_cek[0],
        str(gagal_cek))

    pulihkan(akar)
    tanam(akar, "_buku-ed2/ch24.tex", "berat $(5,4,3,2)$", "berat $(6,4,3,2)$")
    rc, n, gagal_cek = jalankan(akar)                                    # C
    cek("C data soal berubah: tepat 1 FAIL di cek data soal",
        rc == 1 and len(gagal_cek) == 1 and "data soal" in gagal_cek[0],
        str(gagal_cek))

    pulihkan(akar)
    rc, n, gagal_cek = jalankan(akar)                                    # D
    cek("D sandbox pulih: 48/48 lagi", rc == 0 and n == 48 and not gagal_cek,
        f"rc={rc} pass={n}")
finally:
    shutil.rmtree(akar, ignore_errors=True)

print()
if gagal:
    print(f"HASIL: {len(gagal)} GAGAL dari 4 cek: " + ", ".join(gagal))
    raise SystemExit(1)
print("HASIL: 4/4 PASS (ad-hoc, bukan suite kanonik)")
