# Panduan menulis bab — Edisi Pertama
## *Kenapa Mesin Bisa Salah? Dari Aljabar Linear sampai Keamanan Machine Learning*

Buku ajar berbahasa Indonesia, **6 bagian, 32 bab**, dibangun dengan pdfLaTeX.
Kamu menulis **satu bab** sebagai berkas `.tex` berisi badan bab saja (tanpa preamble).

Buku ini harus bisa dibaca **empat lapis pembaca sekaligus**: anak SD/SMP yang penasaran,
mahasiswa S1, dosen yang mengajar, dan peneliti yang mencari batas pengetahuan.
Mereka tidak membaca buku yang berbeda; mereka membaca bab yang sama lewat jalur berbeda.
Karena itu setiap bab **wajib** memuat kotak lapisan di bawah ini.

## Aturan mutlak

1. Keluaran: satu berkas, path persis yang diberikan (`_buku-ed2/chNN.tex`). Tidak ada
   berkas lain yang boleh kamu buat di `_buku-ed2/` selain di direktori uji `_wrap/chNN/`.
2. **Tanpa** `\documentclass`, `\usepackage`, `\begin{document}`, `\cite`, `\footnote`,
   dan tanpa float `table`. Bab dimasukkan lewat `\input{}` ke `main.tex`.
   **Gambar diperbolehkan** hanya sebagai `figure` berisi TikZ/pgfplots (tanpa berkas
   gambar luar), wajib punya `\caption{}` dan `\label{fig:...}`, dan wajib dirujuk di
   teks dengan `\ref{fig:...}` pada berkas yang sama. Maksimal **3 gambar** per bab,
   lebar tidak melebihi `\linewidth`, dan gambar harus menjelaskan gagasan yang sudah
   disebut di teks, bukan menggantikannya. `\label`/`\ref` untuk gambar saja;
   `\eqref` dan `\pageref` tetap dilarang.
3. Tanpa Unicode di luar mode matematika (jangan tulis ε, ≈, ⇒, ×, √, α sebagai teks).
   Di dalam `$...$` pakai `\varepsilon`, `\approx`, `\Rightarrow`, `\times`,
   `\sqrt{2}`, `\alpha`, `\mathbb{R}`, `\mathbf{x}`, `\nabla`, `\sum`, `\int`,
   `\mathcal{O}`, `\mathbb{E}`.
4. Lingkungan yang tersedia: `definisi`, `teorema`, `lemma`, `akibat`, `proposisi`,
   `contoh`, `latihan`, `catatan`, `ringkasan`, `lab`, `untukanak`, `untukdosen`,
   `untukpeneliti`, `itemize`, `enumerate`, `description`, `equation`, `align`,
   `tabular`, `quote`, `verbatim`. Perintah tambahan: `\kertas{...}`, `\peta{...}`,
   `\kamus{istilah}{padanan Inggris}{analogi}`, `\tingkat{dasar|menengah|lanjut}`.
   Jangan mendefinisikan lingkungan atau perintah baru, jangan memuat paket apa pun.
5. **Angka wajib hasil eksekusi nyata.** Setiap angka numerik yang bukan definisi
   harus berasal dari (a) teori yang kamu turunkan, (b) hitungan tangan yang kamu
   kerjakan dan verifikasi dengan Python/numpy/scipy, atau (c) hasil yang eksplisit
   tercetak pada sumber yang kamu baca. Kalau ragu, hitung lagi. Jangan mengarang.
6. Rujuk kitab sumber dengan **nama bab/bagian**, bukan nomor halaman (penomoran
   berbeda antar edisi). Rujuk bab lain buku ini dengan "lihat Bab 9", bukan `\ref`.
7. Bahasa Indonesia baku, sapaan **"kita"** (bukan "aku"/"kamu"). Dilarang membuka
   dengan kalimat kosong seperti "Pada bab ini kita akan membahas...". Mulai dari
   satu masalah konkret.
8. Tidak ada klaim berlebih ("terbukti", "selalu", "pasti") tanpa syarat jelas.
   Bukti yang dilewati harus dinyatakan dilewati dan di mana mencarinya.

## Enam pintu masuk belajar (wajib di setiap bab)

Empat lapisan di bawah melayani beda *kedalaman*; empat kotak berikut melayani beda
*cara belajar*. Setiap bab memuat **tepat satu** dari masing-masing, plus 2-3 gambar.
Gerbang menolak bab yang tidak punya keempatnya (`bacakeras=0`, `tangan=0`, `resep=0`,
`tantangan=0`) dan menolak jumlah gambar selain 2-3 (`gambar=N`).

| Kotak | Untuk tipe | Isi wajib | Panjang |
|---|---|---|---|
| `bacakeras` | auditori | naskah yang **enak dibaca keras**: ritme, pengulangan, dialog dua suara, atau jembatan keledai; tulis kalimat yang bisa diucapkan, bukan rumus bertumpuk; akhiri dengan satu baris yang harus diulang pembaca | 90-200 kata |
| `tangan` | kinestetik | aktivitas dengan benda nyata atau gerakan badan: kartu, koin, kertas lipat, lantai berpetak, tali, jari, jalan mundur; sebut bahan, langkah fisik, dan apa yang harus pembaca **lihat** terjadi | 80-180 kata |
| `resep` | prosedural | kartu langkah bernomor (3-6 langkah) yang cukup dihafal untuk mengerjakan soal apa pun pada topik itu, plus satu peringatan urutan yang tidak boleh ditukar | 60-140 kata |
| `tantangan` | pemecah masalah | satu soal terbuka/teka-teki yang **tidak** rutin, dengan 2 petunjuk bertingkat (petunjuk 1 samar, petunjuk 2 hampir menjawab) dan satu kalimat "kalau mentok, kembali ke bagian X" | 70-160 kata |

Aturan tambahan:
- Keempat kotak **tidak boleh** berisi ulangan kalimat dari badan bab; masing-masing
  harus menambah sudut baru pada gagasan yang sama.
- `bacakeras` dan `tangan` wajib bebas notasi berat; `resep` justru wajib konkret dan
  boleh memuat lambang; `tantangan` harus punya jawaban yang benar-benar ada.
- Gambar dipakai sebagai pintu masuk tipe visual: 2-3 `figure` TikZ/pgfplots per bab,
  caption menyebut angka yang sama dengan teks, selalu dirujuk dari prosa.
- Letakkan keempat kotak dekat bagian yang mereka layani, bukan menumpuk di akhir bab.

## Jembatan pemahaman (wajib, sebelum rumus)

Sebagian pembaca berhenti bukan karena rumusnya sulit, tetapi karena rumusnya datang
terlalu cepat. Bagian ini memaksa urutan yang lebih lambat: **cerita tanpa simbol ->
hitungan di kertas -> simbol sebagai singkatan**. Nomor berikut adalah urutan di berkas,
bukan sekadar daftar isi; pembaca harus bertemu angka sebelum bertemu lambang.

| # | Blok | Bentuk LaTeX | Isi wajib |
|---|---|---|---|
| 1 | bagian | `\section{Jembatan pemahaman: dari cerita ke simbol}` + `\tingkat{dasar}` | satu paragraf yang menjanjikan urutan tadi |
| 2 | analogi | `\subsection{Analogi nyata: ...}` | prosa **tanpa simbol**; boleh menumpang analogi `untukanak` yang sudah ada, tetapi harus menambah satu hal baru (mis. "seberapa besar", bukan mengulang "siapa") |
| 3 | manual | `\subsection{Hitung manual dulu}` + `\begin{contoh}` | 4-6 langkah bernomor dengan angka nyata, tiap langkah bisa diperiksa kalkulator; tutup dengan satu pemeriksaan (beda hingga atau substitusi balik) |
| 4 | kamus | `\subsection{Kamus baca simbol}` + `\begin{description}` | 3-5 simbol; tiap butir: cara baca, arti satu kalimat, dan **nomor langkah** di blok 3 yang menghasilkan angkanya |
| 5 | keamanan | `\subsection{Kenapa ini penting untuk keamanan?}` | satu angka turunan yang dipakai menyerang, satu pemakaian bertahan, kaitkan ke bab serangan (29) bila ada |
| 6 | tangan | `\subsection{Latihan menghitung dengan tangan}` + `\begin{catatan}` + `enumerate` | 3-5 soal yang hanya butuh kalkulator, **jawaban ditulis di dalam kurung** supaya bisa dicocokkan sendiri |
| 7 | kode | `\subsection{Dari kertas ke kode}` + `\begin{lab}` + `\begin{verbatim}` | kode NumPy yang menjalankan langkah blok 3 persis; komentar menyebut nomor langkah; keluaran numerik harus sama dengan angka kertas |

Kerangka minimal (salin apa adanya, ganti isinya):

```latex
\section{Jembatan pemahaman: dari cerita ke simbol}
\tingkat{dasar}

\subsection{Analogi nyata: ...}
\subsection{Hitung manual dulu}
\begin{contoh} ... \begin{enumerate} \item ... \end{enumerate} \end{contoh}
\subsection{Kamus baca simbol}
\begin{description} \item[$\partial L/\partial w$] dibaca ... \end{description}
\subsection{Kenapa ini penting untuk keamanan?}
\subsection{Latihan menghitung dengan tangan}
\begin{catatan} \begin{enumerate} \item ... (jawaban) \end{enumerate} \end{catatan}
\subsection{Dari kertas ke kode}
\begin{lab} \begin{verbatim} ... \end{verbatim} \end{lab}
```

Jebakan yang sudah menimpa:

- **Jangan memakai `\begin{latihan}` untuk blok 6.** Gerbang menghitung `\item` hanya pada
  blok `latihan` **pertama** di berkas; blok baru yang ditaruh di depan akan membuat
  `latihan=4` dan gerbang menolak bab. Pakai `catatan`.
- **Blok ini tidak boleh menambah kotak `bacakeras`/`tangan`/`resep`/`tantangan`.** Keempat
  kotak itu dijatah tepat satu per bab; blok jembatan memakai prosa, `contoh`,
  `description`, `catatan`, dan `lab`.
- **`\section` baru wajib diikuti `\tingkat{...}`**, sebab gerbang menuntut
  `tingkat >= section - 2`.
- **Anggaran kata.** Blok ini memakan 500-650 kata, sedangkan gerbang keras menolak bab
  di atas 7.500 kata. Bab yang sudah 6.400 kata hampir tidak punya ruang: potong prosa
  lama yang mengulang hal sama, jangan menaikkan ambang gerbang tanpa keputusan redaksi.
- **Kode di `verbatim`**: ASCII saja, maksimal 90 kolom per baris (gerbang menolak
  `verbatim>90`), dan angka yang dicetak harus sama dengan angka di blok 3 — kalau berbeda,
  yang salah bukan kodenya melainkan langkah kertasnya.
- **Edisi Inggris wajib menyusul.** `_buku-en/tools/cek-en.py` memeriksa paritas; bab yang
  punya blok ini di edisi Indonesia tetapi belum di edisi Inggris akan tampak sebagai
  selisih struktur, bukan sebagai terjemahan yang tertinggal.

Periksa cakupan dengan `python3 tools/cek-jembatan.py` dan pakai `--ketat` di gerbang rilis
(keluar 1 bila ada bab yang belum lengkap).

## Empat lapisan pembaca (wajib di setiap bab)

Pembaca berbeda butuh pintu masuk berbeda. Empat kotak ini adalah pintu masuknya;
jangan dicampur ke prosa utama supaya pembaca bisa melompatinya.

| Kotak | Untuk siapa | Isi wajib | Panjang |
|---|---|---|---|
| `untukanak` | pembaca 10-14 tahun, tanpa latar matematika | satu analogi benda sehari-hari, **tanpa notasi matematis** (angka sederhana boleh), satu pertanyaan yang membuat penasaran, dan satu kalimat "di bab ini kita akan tahu mengapa" | 120-250 kata |
| `untukdosen` | dosen/pengajar | urutan mengajar yang disarankan, 2 miskonsepsi khas mahasiswa, satu aktivitas papan tulis atau kelas, tanda bahwa mahasiswa siap lanjut | 120-250 kata |
| `untukpeneliti` | peneliti/pembaca lanjut | apa yang benar-benar terbukti vs yang hanya dipopulerkan, sumber primer (nama karya + bagian), pertanyaan terbuka, dan batas keberlakuan hasil | 120-250 kata |
| `\kamus{...}{...}{...}` | semua lapis | istilah baru + padanan Inggris + analogi satu kalimat; wajib dipakai pada 3-5 istilah kunci tiap bab | 1-2 kalimat |

**Setiap istilah `\kamus` wajib punya entri glosarium.** Setelah menambah istilah di bab,
tambahkan pula pasangan (label, definisi) di `tools/glosarium.py` lalu jalankan
`python3 tools/glosarium.py tulis` — blok Lampiran Glosarium di `main.tex` ditulis ulang
dalam urutan abjad, jadi jangan menyunting blok itu dengan tangan. `python3 build_ed2.py
check` menandai `Istilah \kamus tanpa entri glosarium: N` bila ada yang terlewat, dan
`test_gerbang.py` memuat kontrol negatifnya.

Aturan tambahan:
- `untukanak` **tidak boleh** memakai simbol matematika. Kalau perlu, tulis "akar dua"
  bukan `$\sqrt{2}$`. Ini kotak untuk rasa penasaran, bukan untuk definisi.
- Setiap `\section` diawali baris `\tingkat{dasar}`, `\tingkat{menengah}`, atau
  `\tingkat{lanjut}` supaya pembaca tahu bagian mana yang boleh dilewati pada
  pembacaan pertama.
- Setiap teorema/definisi penting didahului satu kalimat biasa yang menjelaskan
  artinya dalam bahasa sehari-hari sebelum pernyataan formalnya.
- Kalimat pendek. Satu gagasan per kalimat. Hindari tanda kurung bersarang.
- Istilah asing ditulis miring dan diberi padanan Indonesia pada kemunculan pertama.
- Judul bab maksimal 55 karakter. Kalau lebih panjang, beri bentuk pendek untuk
  kepala halaman: `\chapter[Bentuk Pendek]{Judul Panjang yang Sebenarnya}`.
  Tanpa bentuk pendek, kepala halaman meluber keluar margin di buku utuh —
  cacat ini **tidak** muncul saat bab dikompilasi sendirian.
- Judul bab harus sama persis dengan barisnya di tabel "Peta Ketergantungan Bab"
  pada `main.tex`. Gerbang memeriksa keduanya; kalau berbeda, perbaiki tabelnya
  (naskah bab adalah acuan), bukan judul bab.

## Struktur wajib satu bab (target 5.500-6.500 kata badan)

```
\chapter{Judul Persis Seperti di Tugas}

[2-3 paragraf: satu masalah konkret + mengapa alat bab sebelumnya belum cukup]

\begin{untukanak} ... \end{untukanak}

\section{...}
\tingkat{dasar}
[prosa + definisi/teorema + bukti]

\section{...}
\tingkat{menengah}
...
\section{...}
\tingkat{lanjut}
...

\section{Contoh hitung}
\tingkat{menengah}
[angka eksak, langkah antara ditulis, satu kotak \kertas{...}]

\section{Lab komputasi}
\tingkat{lanjut}
\begin{lab}
\begin{verbatim}
kode Python yang benar-benar dijalankan
\end{verbatim}
\end{lab}
[keluaran nyata apa adanya, lalu tafsirannya]

\begin{untukdosen} ... \end{untukdosen}

\section{Ringkasan}
\begin{ringkasan} ... \end{ringkasan}   % 4-6 butir, padat

\section{Latihan}
\begin{latihan}
\begin{enumerate}
  ... 8-10 butir ...
\end{enumerate}
\end{latihan}

\begin{untukpeneliti} ... \end{untukpeneliti}

\peta{Bab ... pada [kitab] ...}
```

Syarat kuantitatif yang diperiksa gerbang mutu:
- 5.000-7.500 kata badan (target 5.500-6.500). Kurang dari 5.000 ditolak.
- minimal 5 `\section`, minimal 4 lingkungan teori (`definisi`/`teorema`/`lemma`/
  `akibat`/`proposisi`), setiap `\section` teori dan contoh diberi `\tingkat{...}`
  (boleh dilewati hanya untuk `Ringkasan` dan `Latihan`).
- 2-4 kotak `untukanak`, tepat 1 `untukdosen`, tepat 1 `untukpeneliti`,
  minimal 3 `\kamus{...}{...}{...}`.
- minimal 1 `\kertas`, 1 `\peta`, 1 `\begin{lab}`, 1 `\begin{verbatim}`,
  1 `\begin{ringkasan}`.
- 8-10 butir latihan; wajib ada (a) satu butir "nilai klaim ini: benar, salah, atau
  belum cukup bukti", (b) minimal dua butir bukti, (c) minimal dua butir hitung yang
  bisa diperiksa dengan Python. Sertakan petunjuk singkat untuk 3 butir tersulit.
- minimal 8 `\index{istilah}` (huruf kecil, ASCII, satu atau dua kata; jangan
  mengindeks kata umum seperti "bilangan" — indeks harus berguna).

## Mutu yang dinilai

- Setiap definisi dipakai di bab itu. Definisi dari bab sebelumnya dirujuk, bukan diulang.
- Teorema disertai bukti lengkap, atau pernyataan jujur bahwa bukti dilewati
  beserta lokasi pembuktiannya. Bukti setengah jadi lebih buruk daripada mengaku.
- Contoh hitung: angka eksak, langkah antara ditulis, hasil akhir bisa dicek ulang
  pembaca. Verifikasi dengan Python sebelum menulis hasilnya.
- Lab komputasi: kode yang benar-benar kamu jalankan, keluaran apa adanya
  (boleh dipotong dengan "..." bila panjang, tetapi angka yang ditampilkan harus asli).
- Latihan benar-benar bisa dikerjakan dari isi bab, bukan dari luar bab.
- Nada: menjelaskan, tidak menggurui; tidak memakai "jelas sekali" atau "mudah".

## Cara uji kompilasi (wajib, sebelum menyatakan selesai)

```bash
cd _buku-ed2/_wrap/chNN   # dari akar repo; direktori milikmu
cp ../../chNN.tex .
cat > w.tex <<'EOF'
\documentclass[11pt,a4paper]{book}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{makeidx}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\usepackage[a4paper,margin=2.5cm]{geometry}
\theoremstyle{definition}\newtheorem{definisi}{Definisi}[chapter]
\theoremstyle{plain}\newtheorem{teorema}{Teorema}[chapter]
\newtheorem{lemma}[teorema]{Lemma}
\newtheorem{akibat}[teorema]{Akibat}
\newtheorem{proposisi}[teorema]{Proposisi}
\theoremstyle{remark}\newtheorem{contoh}{Contoh}[chapter]
\newtheorem{latihan}{Latihan}[chapter]
\newtheorem{catatan}{Catatan}[chapter]
\newtheorem*{ringkasan}{Ringkasan}
\newenvironment{lab}{\par\medskip\noindent\textbf{Lab komputasi}\par\nopagebreak}{\par\medskip}
\newtcolorbox{untukanak}{colback=orange!6,colframe=orange!65!black,
  title={\small\bfseries Untuk pembaca muda (10 tahun ke atas)},
  fonttitle=\bfseries,breakable,left=6pt,right=6pt,top=4pt,bottom=4pt}
\newtcolorbox{untukdosen}{colback=teal!5,colframe=teal!55!black,
  title={\small\bfseries Catatan untuk dosen},
  fonttitle=\bfseries,breakable,left=6pt,right=6pt,top=4pt,bottom=4pt}
\newtcolorbox{untukpeneliti}{colback=black!4,colframe=black!55,
  title={\small\bfseries Untuk peneliti: batas dan lanjutan},
  fonttitle=\bfseries,breakable,left=6pt,right=6pt,top=4pt,bottom=4pt}
\newcommand{\kamus}[3]{\par\smallskip\noindent\colorbox{blue!5}{\parbox{\dimexpr\linewidth-2\fboxsep}{\small\textbf{#1} (\emph{#2}) --- #3}}\par\smallskip}
\newcommand{\tingkat}[1]{\par\noindent{\footnotesize\scshape Tingkat: #1}\par\smallskip}
\newcommand{\kertas}[1]{\par\medskip\noindent\fbox{\parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule}{\small #1}}\par\medskip}
\newcommand{\peta}[1]{\par\medskip\noindent{\small\itshape Peta ke kitab sumber: #1}\par\medskip}
\makeindex
\begin{document}
\input{chNN.tex}
\printindex
\end{document}
EOF
pdflatex -interaction=nonstopmode -halt-on-error w.tex
makeindex w.idx >/dev/null 2>&1
pdflatex -interaction=nonstopmode -halt-on-error w.tex
```

Ganti `chNN` dengan nomor babmu. **Wajib**: pdflatex selesai tanpa `!` error dan tanpa
overfull box di atas 10pt. Perbaiki sampai bersih, lalu hapus berkas bantu
(`w.aux`, `w.log`, `w.idx`, `w.ilg`, `w.ind`, `w.toc`, `w.out`, `w.pdf`, `w.tex`,
salinan `chNN.tex`) — direktori `_wrap/chNN/` harus kosong saat kamu selesai.

## Isi seluruh buku (konteks; jangan menulis bab lain)

**Bagian I — Fondasi: Bahasa, Himpunan, dan Bilangan**
1. Bahasa Matematika dan Seni Membuktikan
2. Himpunan, Relasi, Fungsi, dan Kardinalitas
3. Aksioma Bilangan Real dan Supremum
4. Barisan dan Limit
5. Deret Tak Hingga

**Bagian II — Aljabar Linear**
6. Ruang Vektor dan Subruang
7. Basis, Dimensi, dan Transformasi Linear
8. Sistem Persamaan Linear, Determinan, dan Invers
9. Nilai Eigen dan Diagonalisasi
10. Ortogonalitas, SVD, dan Kuadrat Terkecil

**Bagian III — Analisis dan Kalkulus**
11. Kekontinuan dan Kekontinuan Seragam
12. Turunan: Satu dan Banyak Variabel
13. Integral Riemann dan Teorema Dasar Kalkulus
14. Deret Fungsi dan Pertukaran Limit
15. Integral Lipat, Perubahan Variabel, dan Teorema Lapangan Vektor

**Bagian IV — Peluang, Statistika, dan Aritmetika Komputer**
16. Peluang dan Peluang Bersyarat
17. Variabel Acak dan Distribusi
18. Hukum Bilangan Besar dan Teorema Limit Pusat
19. Estimasi, Interval Kepercayaan, dan Uji Hipotesis
20. Aritmetika Floating-Point dan Analisis Galat

**Bagian V — Optimasi**
21. Optimasi Konveks dan Dualitas
22. Pemrograman Linear dan Integer

**Bagian VI — Pembelajaran Mesin dan Keamanan**
23. Jaringan Saraf dan Turunan Balik
24. Generalisasi, Regularisasi, dan Pelatihan
25. Evaluasi Model yang Jujur
26. Metode Formal dengan Lean 4
27. Adversarial Machine Learning: Serangan dan Pertahanan
28. Batas Serangan: Gradien Dikaburkan dan Evasi NIDS
