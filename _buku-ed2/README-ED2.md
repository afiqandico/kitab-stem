# Edisi Pertama — *Kenapa Mesin Bisa Salah? Dari Aljabar Linear sampai Keamanan Machine Learning*

Kitab ajar berbahasa Indonesia, **6 bagian, 32 bab**, disusun ulang dari versi 13 bab
(`../_buku/`, diarsipkan sebagai catatan sejarah) dengan sumber gagasan dari kitab ajar
pada Daftar Rujukan. Dua bab yang membedakannya dari rakitan sebelumnya: Bab 16
(Persamaan Diferensial dan Sistem Dinamik) dan Bab 21 (Regresi dan Statistika Terapan).

Hasil rakitan: `Kitab-STEM-Kenapa-Mesin-Bisa-Salah.pdf` di akar repo —
**643 halaman, 3716202 byte (3,54 MB), 206.944 kata badan, 95 gambar, 128 kotak kanal belajar
(32 × 4), 361 entri indeks (402 kunci `\index`, sebagian tergabung), **217 entri glosarium**
(seluruh 162 istilah `\kamus` di bab + 55 istilah pendukung), 34 rujukan**,
**0 error LaTeX, 0 overfull sama sekali**, 0 rujukan `??`, Daftar Gambar berisi **95 entri**
(sama dengan jumlah `\begin{figure}`), dan 32/32 judul bab terverifikasi ada di PDF
(sha256 `d66d9c2f30704c30df98d0e666acc2f14f8be00988fcb102cc966fca6de614e9`, rakitan 2026-11-07,
**reproduksibel**: dua rakitan berturut-turut menghasilkan sha identik).

> **Audit lanjutan (4 titik lagi).** Petunjuk 5.9 keliru memakai $H_{2K}$ (memberi
> $0{,}8959$); pola tiga-positif-satu-negatif menghasilkan $S_K=H_{6K}-\tfrac12H_{3K}-\tfrac12H_{K}
> \to1{,}2424521$ — cocok dengan hitungan langsung, jadi petunjuk diperbaiki. Premis soal 12.9
> ("mengapa batas itu jauh lebih longgar") salah: $p_2(0{,}04)=1{,}0198$, galat $3{,}90\times10^{-6}$,
> sisa Lagrange $4{,}00\times10^{-6}$ — batasnya rapat, bukan longgar; soal dan kunci disesuaikan.
> Dua catatan audit ditolak: soal 1.9 memang meminta menilai inferensi yang salah (bukan cacat), dan
> syarat KKT di 23 sudah bertanda benar untuk masalah "minimumkan" ($\mathbb{N}=\{1,2,3,\dots\}$
> didefinisikan di Bab 1).
>
> **Audit kunci jawaban, lintasan kedua (20 butir).** Seluruh 304 butir kunci diuji ulang
> terhadap soalnya dan dihitung ulang dengan Python/Lean; dua puluh butir salah di kedua edisi
> (paritas menyamakan, bukan membenarkan) dan sudah diperbaiki di sumber Indonesia ini lalu
> dicerminkan ke edisi Inggris: 1.9 (menjawab klaim lain, $n^{2}-1$ alih-alih $n^{2}+n+41$ yang
> gagal di $n=40$), 10.6 (arah balik tak dibuktikan), 11.6 ($\delta=\varepsilon/3$ disebut sah
> padahal $(1+\varepsilon/3)^{3}-1>\varepsilon$), 17.1 (suku rangkap tiga terkurang *tiga* kali),
> 17.8 (positif palsu dua uji $999\cdot0{,}01^{2}$, bukan $10$), 18.10 ($R=5\,448$, bukan
> $103\,514$: faktor $n-1$ hilang), 20.4 (selang sempit karena $n=40$, bukan karena $\hat p$ di
> tepi; informasi Fisher justru lebih besar), 20.7 ($p=0{,}02$ dan selisih 2 jam di luar selang),
> 21.5 (selisih pengungkit lenyap seperti $1/n$), 21.8 ($-0{,}2+0{,}6$ bukan dekomposisi;
> kontribusinya $-0{,}028571+0{,}428571$), 24.9 (kapasitas 7 membuang $(1,3)$, bukan $(1,2)$),
> 25.7 dan petunjuk Bab 25 ($1+k+k(k-1)/2$ daerah: $2,4,7$), 25.9 (blok lab memakai ReLU, jadi
> $\mathbf{b}_{1}=+10$ tidak menjenuhkan apa pun), 27.6 (cacah pasangan $5+5+4+3+2=19$), 28.2
> (tujuan memuat $k\cdot k$: bukan linear, jadi \texttt{omega} saja tidak menutupnya), 28.7
> ($\forall\delta$ diganti $\exists\delta$ pada pernyataan lemah), 28.8 (\texttt{omega} memberi
> \texttt{propext} dan \texttt{Quot.sound}, bukan \texttt{Classical.choice}), 29.5 (selisih
> *melebar* sampai 54 poin persen sebelum menyempit), 30.3 (arah ketaksamaan: di bawah 0,35
> dijamin berhasil, dan pada 0,35 label masih berbalik), 32.9 ($16$ TiB, bukan $16$ GiB).
> Satu klaim auditor ditolak: Lean 4.10 di mesin ini menolak $x$ bebas pada 28.9, jadi kunci lama
> benar. Seluruh catatan sisa itu (1.9, 12.9, 23.2, 25.7/25.10, 27.10, petunjuk 5.9) sudah
> diselesaikan pada audit lanjutan di atas: 5.9 dan 12.9 cacat nyata dan diperbaiki, sisanya
> ditolak dengan hitungan.
>
> Perbaikan isi 2026-10-26 (Kunci Jawaban Bab 32 butir 7): untuk keadaan Bell
> $|\Phi^{+}\rangle$, kunci lama menulis "bila hasilnya 1, qubit pertama $|0\rangle$
> dan hasil $01$ pasti" — bertentangan dengan korelasi sempurna yang dinyatakan kalimat
> berikutnya. Koreksi: qubit pertama runtuh ke $|1\rangle$, hasil $11$ pasti, dan peluang
> $01$ juga $0$ (sama seperti kasus hasil $0$). Sumber `lampiran-kunci/kunci-24-32.tex`
> dan PDF ini sudah dibangun ulang; edisi Inggris mengikuti koreksi yang sama. PDF lama
> (sha `59d576a8…`) tidak memuat perbaikan ini.

> Perbaikan isi 2026-10-25 (Bab 25): tiga cacat di kotak `tantangan` dan petunjuk
> latihan dibetulkan. `\nabla` dan `\neq` di baris 640-643 terpotong menjadi
> `abla` dan `eq` (PDF lama mencetak "ablaW₁L = 0" dan "W1 eq0"); petunjuk menyebut
> "Butir 10" padahal latihan bab itu hanya 9 butir (isi petunjuknya cocok dengan
> Butir 9); dan batas keberlakuan merujuk "Bab 26 dan 25", yaitu bab itu sendiri.
> PDF lama (sha `d10584af…`) tidak memuat perbaikan ini.

## Yang berubah dari arsip 13 bab

| Aspek | Arsip (`../_buku/`, 13 bab) | Edisi Pertama (folder ini) |
|---|---|---|
| Cakupan | 13 bab, 5 topik | 6 bagian, 32 bab: fondasi, aljabar linear, analisis, peluang/statistika/numerik, optimasi, ML + keamanan + kriptografi + privasi |
| Panjang bab | ±2.500 kata | 5.500–6.500 kata badan + lab komputasi |
| Pembaca | mahasiswa | empat lapis: anak 10+, mahasiswa, dosen, peneliti |
| Penanda | — | kotak oranye (pembaca muda), hijau (dosen), abu-abu (peneliti), `\kamus`, `\tingkat`, plus empat kotak kanal belajar: `bacakeras` (auditori), `tangan` (kinestetik), `resep` (prosedural), `tantangan` (pemecah masalah) |
| Latihan | 4–6 butir | 8–10 butir + petunjuk untuk butir tersulit |
| Gambar | tidak ada | 95 gambar TikZ/pgfplots bernomor (2–3 per bab), ber-caption, dirujuk di teks, dengan Daftar Gambar |
| Tambahan | — | Lampiran notasi, glosarium **217 entri** (setiap istilah `\kamus` di bab punya entri), kriteria penilaian latihan, indeks (makeindex) |

## Isi folder

| Berkas | Peran |
|---|---|
| `main.tex` | kerangka: preamble (tikz, pgfplots, caption), kotak empat lapisan + empat kotak kanal belajar, halaman "Enam cara belajar, enam pintu masuk", halaman judul, kata pengantar, cara membaca (4 jalur), peta ketergantungan 32 bab, 6 `\part`, 32 `\input`, Daftar Isi, Daftar Gambar, lampiran A–D (D = kunci jawaban 304 butir), indeks, kolofon, 34 rujukan |
| `ch01.tex` … `ch32.tex` | badan bab (tanpa preamble; di-`\input` oleh `main.tex`) |
| `PANDUAN-BAB-ED2.md` | aturan mutlak (termasuk aturan gambar) + bagian "Empat lapisan pembaca" + resep uji kompilasi |
| `SPEC-BAB-ED2.md` | isi tiap bab: bagian, sumber, angka wajib (termasuk Bab 29–30) |
| `build_ed2.py` | perakit + gerbang mutu: `check`, `status`, `pdf` |
| `tools/glosarium.py` | sumber definisi seluruh istilah `\kamus` + penulis blok glosarium: `tulis` (tulis ulang `main.tex`, urut abjad), `cek` (laporkan istilah tanpa entri), `daftar` |
| `tools/cek-kunci-01-05.py` | pemeriksa angka kunci Lampiran D **Bab 1–5**: 121 baris `assert`, keluaran `OK: seluruh angka kunci cocok` |
| `tools/cek-cacah-kunci.py` | memetakan 304 butir latihan ↔ 304 butir kunci per bab; mencetak `Semua bab 1:1` (gagal bila ada bab yang tidak sepadan atau parser buta) |
| `tools/verify-kunci-06-15.py` | 37 cek untuk perbaikan 6.5, 9.9, 12.2, 13.7, 14.5 (teks kedua edisi + hitungan ulang) |
| `tools/verify-kunci-16-23.py` | 36 cek untuk perbaikan 18.8, 18.10, 19.10, 20.4, 20.7 |
| `tools/verify-kunci-21-25.py` | 38 cek untuk 21.5, 21.9, 22.10, 25.5, 25.9; butir 25.9 diuji dengan menjalankan ulang blok lab dari `ch25.tex` |
| `tools/verify-kunci-26-32.py` | 20 cek untuk 26.2, 27.9, 28.2, 28.3, 28.5, 28.9, 29 (teks bab), 30.3, 31.9, 32.6; menjalankan Lean 4 pada `tools/lean-28/*.lean` |
| `AUDIT-KUNCI.md` | kontrak audit: auditor hanya melapor, induk yang menyunting kedua edisi, dan setiap angka wajib disertai perintah + keluaran |
| `test_gerbang.py` | uji kerangka **36 cek** (`make test` → 36/36 PASS): gerbang mutu (positif + negatif, termasuk aturan gambar dan glosarium), judul/edisi PDF, dan kompilasi `main.tex` sampai PDF di sandbox `tempfile` |
| `_wrap/` | direktori uji per bab (harus kosong bila bersih) |

## Membangun ulang

```
cd "_buku-ed2"
source ~/venv/bin/activate
python3 test_gerbang.py       # uji kerangka: harus "N/N PASS", exit 0
python3 build_ed2.py status   # bab mana yang sudah ada
python3 build_ed2.py check    # gerbang per bab; exit 0 = siap, 2 = ada bab kosong, 1 = ada bab cacat
python3 build_ed2.py pdf      # pdflatex, makeindex, pdflatex x2 -> akar repo
```

## Gerbang mutu yang dipakai `check`

Per bab: 5.000–7.500 kata badan (ambigu dua arah: `pendek` <5.000, `kepanjangan`
>7.500; verbatim **dan gambar** tidak dihitung karena bukan prosa), ≥5 `\section` dan
tiap section punya `\tingkat`, ≥4 lingkungan teori, 2–4 `untukanak`, tepat 1
`untukdosen` dan 1 `untukpeneliti`, ≥3 `\kamus`, ≥8 `\index`, 8–10 butir latihan, ada
`\kertas`, `\peta`, `lab`, `verbatim`, `ringkasan`; ASCII murni; tanpa
`\documentclass`/`\usepackage`/`\cite`/`\footnote`/float `table`; hanya lingkungan dari
daftar izin.

Aturan gambar (sejak gambar diizinkan): `figure` berisi TikZ/pgfplots tanpa berkas
gambar luar, wajib `\caption{}` + `\label{fig:...}`, dan wajib dirujuk `\ref{fig:...}`
di berkas yang sama. `\label`/`\ref` dibuka hanya untuk gambar; `\eqref` dan
`\pageref` tetap dilarang.

Gerbang yang hanya berguna pada **buku utuh**, ditemukan dari rakitan nyata:

| Tanda | Arti |
|---|---|
| `judul-panjang` | judul `\chapter` >55 karakter tanpa bentuk pendek `\chapter[pendek]{...}`; kepala halaman akan meluber keluar margin |
| `verbatim>N` | ada baris kode >90 kolom; dengan `\footnotesize` global batas aman ±90 kolom |
| `figure-tanpa-caption/label` | `figure` tanpa caption atau tanpa label `fig:...` |
| `figure-tak-dirujuk` | label gambar tidak pernah di-`\ref` di berkas yang sama |
| `Judul di tabel peta tidak cocok` | judul bab ≠ barisnya di tabel "Peta Ketergantungan Bab" pada `main.tex` |
| `Istilah \kamus tanpa entri glosarium` | ada `\kamus{...}` di bab yang tidak punya entri di Lampiran Glosarium; tambahkan lewat `tools/glosarium.py` lalu jalankan `tulis` |

`build_ed2.py pdf` **gagal** (exit 1) bila ada overfull >10 pt di buku rakitan; angka
overfull dan jumlah halaman dicetak di akhir.

## Batas yang jujur

- Kerangka punya uji kanonik: `python3 test_gerbang.py` (36 cek), dijalankan di sandbox
  `tempfile`. Yang **tidak** tercakup uji itu adalah mutu isi bab dan cacat yang hanya
  muncul saat 32 bab dirakit: untuk itu dipakai `make pdf`, yang menolak buku dengan
  overfull >10 pt. Angka-angka di README ini berasal dari rakitan 2026-10-25 selepas
  gelombang tiga (Bab 21–30) dan pelengkapan glosarium, bukan perkiraan.
- `build_ed2.py pdf` memaku `SOURCE_DATE_EPOCH` + `FORCE_SOURCE_DATE`, jadi dua rakitan dari
  sumber yang sama menghasilkan sha256 **identik** (diuji dua kali berturut-turut); sebelum ini
  sha berubah tiap rakitan karena pdfTeX menulis tanggal dan `/ID` dari jam sistem.
- `pdf` juga menolak rakitan yang memuat label ganda. Label `fig:kisi` pernah dipakai di Bab 2
  *dan* Bab 7, sehingga `\ref{fig:kisi}` di Bab 2 menampilkan gambar Bab 7; kini label itu
  menjadi `fig:kisi` (Bab 2) dan `fig:kisi-07` (Bab 7), dan rakitan bersih dari peringatan
  `multiply defined`.
- Glosarium: 215 dari 217 entri mencantumkan padanan Inggris `(\emph{...})`; dua entri
  (`Kamus`, `Ringkasan`) menerangkan kotak buku ini sendiri sehingga sengaja dibiarkan
  tanpa padanan. Gerbang `check` hanya menjamin **kelengkapan** (setiap `\kamus` punya
  entri) dan **format** tidak diperiksa mesin.
- Angka di dalam bab (termasuk di caption gambar) berasal dari eksekusi nyata
  Python/NumPy/SciPy/sklearn di mesin ini; tiap bab memuat kode yang dapat diulang
  pembaca. Bab 30 menyatakan bahwa empat angka waktu simulasi bersifat run-to-run.
- Potongan Lean 4 di Bab 26 dijalankan dengan **Lean 4.10.0** (`~/.elan/bin/lean`) tanpa
  Mathlib: 8 dari 16 blok kompilasi bersih, sisanya demonstrasi kegagalan yang disengaja
  dan transkrip galat. Taktik pustaka seperti `linarith`/`ring` tidak dijalankan.
- Seluruh 32 bab berada di dalam 5.500–6.500 kata badan (rentang nyata 6.237–6.498;
  terendah Bab 21, tertinggi Bab 15). Pemangkasan untuk membayar kotak dan gambar dilakukan pada prosa yang
  mengulang; angka, teorema, dan butir latihan tidak dikurangi.
- **Lampiran D memuat kunci 304 butir latihan** (satu jawaban per butir, seluruh 32 bab).
  Bentuknya sengaja tidak utuh: angka akhir + sketsa langkah 2–5 baris, bukan bukti penuh;
  angka kunci **Bab 1–5** dapat diperiksa ulang dengan `tools/cek-kunci-01-05.py`,
  pemetaan 304 ↔ 304 dengan `tools/cek-cacah-kunci.py`, dan perbaikan Bab 6–32 dengan
  `tools/verify-kunci-06-15.py`, `-16-23.py`, `-21-25.py`, `-26-32.py` (37 + 36 + 38 + 20 cek,
  semuanya lulus). Audit Bab 6–32 dijalankan dalam enam gelombang berpedoman `AUDIT-KUNCI.md`
  dan menemukan **23 butir kunci cacat** (14 di Bab 6–25, 9 di Bab 26–32), ditambah satu soal
  (21.5) dan satu angka teks bab (Bab 29); seluruhnya sudah diperbaiki di kedua edisi.
  Sisa yang diketahui dan sengaja tidak ditutup: 30.5 menuntut arsitektur model dua lapis yang
  tidak disebutkan soalnya, jadi kuncinya hanya memberi ramalan kualitatif; dan angka 29.4
  bergantung tarikan acak (`rng(1)`/`rng(2)` memberi 95,48 persen, `rng(0)` memberi 95,64);
  blok `lab` Bab 29 memuat pustaka serangannya saja tanpa driver pelatihan, jadi tabel 29.5/29.9
  tidak bisa diturunkan ulang dari repo tanpa menulis driver sendiri (driver itulah yang dipakai
  saat audit: akurasi bersih $0{,}9799$ tereproduksi, serangan tak bersasaran $88{,}21$ persen
  menggantikan $89{,}06$ pada protokol yang sama).
  **3 butir ditandai ambigu** karena soalnya sendiri bermasalah. Lampiran C tetap memberi kriteria
  penilaian dan alat verifikasi sebelum pembaca membuka kunci.
