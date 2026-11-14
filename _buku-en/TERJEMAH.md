# TERJEMAH — aturan edisi bahasa Inggris

Sumber: `../_buku-ed2/chNN.tex`. Sasaran: `chNN.tex` di direktori ini. Satu bab per berkas.
Preamble: `preamble-en.tex` (nama lingkungan sengaja tetap Indonesia agar satu pemeriksa
struktur bisa membandingkan kedua edisi; yang diterjemahkan hanya label yang tercetak).

## Terjemahkan
- Seluruh prosa, judul bagian, isi kotak, keterangan gambar (`\caption`), teks butir latihan,
  analogi, dan teks prosedur di dalam `verbatim` **jika** itu komentar/keluaran berbahasa.
- `\kamus{A}{B}{C}`: **A = istilah Inggris**, **B = istilah Indonesia asli**, C = analogi
  diterjemahkan. Contoh: `\kamus{vertex}{verteks}{the corner of the feasible region...}`.
- `\tingkat{dasar|menengah|lanjut}` → `\tingkat{basic|intermediate|advanced}` (konsisten).
- `\index{...}`: terjemahkan isinya ke Inggris; jumlah kunci harus sama dengan sumber.
- `\peta{...}`: terjemahkan isinya; judul kitab tetap di `\emph{}`, nomor bab/bagian tetap.

## Jangan diubah
- Nama perintah dan lingkungan LaTeX (`\begin{teorema}`, `\section`, `\label`, `\ref`).
- Kunci `\label{...}` dan `\ref{...}` — **persis sama** dengan sumber (dipakai untuk
  membandingkan dua edisi). Jangan menambah atau menghapus label.
- Simbol, angka, dan notasi di dalam `$...$`, `\[...\]`, `equation`, `align`. Satu-satunya
  pengecualian: penulisan pemisah angka (lihat bagian Angka) — angkanya sendiri tetap sama persis.
- **Jangan menyentuh `../_buku-ed2/` sama sekali.** Sumber Indonesia itu sudah final. Kalau
  menurut kamu ada yang salah di sana, tulis di ringkasan, jangan sunting. (Pernah terjadi: satu
  penerjemah mengubah `95\%` menjadi `95 persen` dan membuang `\\[3pt]` di simpul TikZ pada
  `_buku-ed2/ch20.tex`; seluruh suntingan itu dibatalkan.)
- `\begin{verbatim}` dan `\end{verbatim}` harus berdiri di barisnya sendiri (jangan
  digabung dengan `\begin{lab}` di baris yang sama) — 32 bab sumber memakai pola itu dan
  penggabungan membuat LaTeX melaporkan `\begin{lab}` tak pernah ditutup.
- Kode Python/Lean di dalam `verbatim`: logika dan angka **tidak boleh berubah**. Label yang
  dicetak (`print("selisih :", ...)`) boleh diterjemahkan beserta blok keluaran di bawahnya,
  asalkan setiap angka pada keluaran tetap identik dengan sumber — gerbang membandingkan
  angka, bukan teks label.
- Kode TikZ/pgfplots: koordinat, warna, opsi. Hanya teks yang tercetak (`\node{...}`,
  `\caption`, label sumbu `xlabel`/`ylabel`) yang diterjemahkan.

## Angka
- Nilai angka tidak berubah. Koma desimal Indonesia (`3,14`) menjadi titik (`3.14`); pemisah
  ribuan Indonesia (`1.000`) menjadi koma (`1,000`).
- **Di dalam matematika pun begitu.** `$0{,}5$` menjadi `$0.5$` dan `$100.000$` menjadi
  `$100{,}000$`; jangan mengubah digit, orde, atau simbol. Gerbang menyamakan konvensi
  koma/titik sebelum membandingkan, jadi perubahan konvensi tidak bisa dipakai untuk
  menyamarkan perubahan angka.
- **Tanda persen ikut disalin apa adanya.** Kalau sumber menulis `$95\%$`, terjemahan menulis
  `$95\%$`; kalau sumber menulis `$95$ persen`, terjemahan menulis `$95$ percent`. Gerbang
  membandingkan keduanya sebagai matematika yang berbeda, jadi jangan menyeragamkan sendiri.

## Gaya
- Bahasa Inggris Amerika, kalimat aktif, "we" seperti sumber.
- Tidak menambah isi, tidak meringkas, tidak menghapus butir latihan atau kotak.
- Jumlah kata sasaran: 0,85–1,35 × jumlah kata sumber (Inggris biasanya lebih pendek).

## Keluaran
- Berkas diawali `\chapter{...}`, tanpa preamble, tanpa `\begin{document}`.
- Harus dapat dikompilasi dengan `preamble-en.tex` tanpa error dan tanpa overfull > 10 pt.
- Setelah selesai, jalankan: `python3 ../_buku-en/tools/cek-en.py chNN`
