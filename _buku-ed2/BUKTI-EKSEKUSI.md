# Bukti eksekusi (lampiran yang belum dipasang di buku)

Berkas kerja. Isinya data nyata dari rakitan 2026-11-12, disiapkan untuk menjawab
pertanyaan penguji: "angka di Lab komputasi ini dari mana, dan bisa diulang di mesin apa?"

## Mesin dan versi yang benar-benar dipakai saat memeriksa ulang

| Alat | Versi terukur | Perintah |
|---|---|---|
| Python | 3.14.9 | `python3 -VV` |
| NumPy | 2.4.3 | `python3 -c "import numpy; print(numpy.__version__)"` |
| SciPy | **tidak terpasang** | `python3 -c "import scipy"` -> ModuleNotFoundError |
| Lean 4 | 4.10.0 (commit c375e19f6b65) | `lean --version` |
| pdfTeX | 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) | `pdflatex --version` |
| Kernel | 7.0.0-42-generic | `uname -r` |
| Tanggal rakitan | 2026-11-12T19:22:40+08:00 | `date -Iseconds` |

## Hasil rakitan dan pemeriksaan

| Pemeriksaan | Hasil |
|---|---|
| PDF Indonesia | 646 halaman, 3,56 MB, 0 overfull > 10pt |
| PDF Inggris | rc=0, 0 error, 0 label ganda, 0 overfull, indeks 352 entri |
| Determinisme | dua rakitan berturut-turut identik, sha256 berawalan `19b819485925e6aa` |
| Gerbang bab | 32 bab OK, 0 bermasalah, 207.743 kata badan |
| Paritas ID-EN | `cek-en.py` -> 32 bab, 0 masalah |
| Blok jembatan pemahaman | `cek-jembatan.py` -> 1/32 lengkap (ch25) |

## Selisih yang harus dinyatakan, bukan disembunyikan

1. **Kolofon menyebut SciPy, mesin ini tidak punya SciPy.** Sepuluh bab memuat kode SciPy
   (`ch06`, `ch07`, `ch09`, `ch10`, `ch13`-`ch16`, `ch18`, `ch19`). Keluaran SciPy di buku
   berasal dari mesin lain dan **belum** diverifikasi ulang di sini. Kalimat yang jujur:
   "Lab NumPy dijalankan ulang pada 2026-11-12; lab SciPy dikutip dari eksekusi sebelumnya
   dan belum diulang."
2. **Versi berbeda dari yang tertulis di Bab 25.** Bab 25 menyebut Python 3.14.4 dan NumPy
   2.5.2; rakitan ulang hari ini memakai 3.14.9 dan 2.4.3. Angka di blok jembatan pemahaman
   (Bab 25) tetap cocok karena operasinya dasar, tetapi versi di teks perlu diselaraskan
   atau diberi catatan.
3. **Lean 4.10.0 cocok** dengan klaim kolofon, dan keluaran Bab 28 diambil dari
   `_buku-ed2/tools/lean-28/*.lean` yang tersimpan.
4. **Tidak ada CI.** Semua gerbang dijalankan manual; tidak ada bukti historis bahwa gerbang
   pernah hijau pada commit lain selain yang diukur hari ini.

## Blok LaTeX siap pakai (bila ingin dijadikan Lampiran C)

```latex
\chapter*{Lampiran C: Bukti eksekusi}
\addcontentsline{toc}{chapter}{Lampiran C: Bukti eksekusi}

Angka di \emph{Lab komputasi} dihasilkan pada mesin dengan Python 3.14.9, NumPy 2.4.3,
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) pada 12 November 2026. Dua rakitan
PDF berturut-turut menghasilkan berkas identik (sha256 berawalan \texttt{19b819485925e6aa}),
sehingga angka di buku dapat diperiksa ulang tanpa bergantung pada nomor halaman.

Lab yang memakai SciPy dikutip dari eksekusi sebelumnya dan belum diulang pada mesin ini;
ketentuan itu dinyatakan agar pembaca tahu bagian mana yang sudah diuji ulang.
```

Catatan: memakai `\chapter*` menambah satu halaman depan daftar isi; nomor halaman bab lain
tidak bergeser bila diletakkan setelah Daftar Rujukan.
