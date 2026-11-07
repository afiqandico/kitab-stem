# Spesifikasi 32 bab — Edisi Pertama

> **Catatan penomoran (Oktober 2026).** Berkas ini mula-mula menomori tiga puluh bab.
> Setelah Bab 16 (Persamaan Diferensial dan Sistem Dinamik) dan Bab 21 (Regresi dan
> Statistika Terapan) disisipkan, penomoran bergeser: 1--15 tetap; 16--19 menjadi
> 17--20; 20 menjadi 22; 21--30 menjadi 23--32. Judul bab di bawah tetap sah sebagai
> isi; nomornya mengikuti peta itu. Spesifikasi dua bab baru ada di bagian akhir berkas.

Baca `PANDUAN-BAB-ED2.md` lebih dulu (aturan mutlak **dan bagian "Empat lapisan
pembaca"**). Berkas ini hanya memberi isi.

Pengingat lintas bab (berlaku untuk semua bab di bawah): setiap bab wajib memuat
2-4 kotak `untukanak`, 1 `untukdosen`, 1 `untukpeneliti`, minimal 3 `\kamus`, dan
setiap `\section` diberi `\tingkat{dasar|menengah|lanjut}`. Kotak lapisan tidak
menggantikan prosa utama: isi teorinya tetap lengkap dan formal, sedangkan kotak
adalah pintu masuk dan catatan untuk pembaca lain.

Sumber PDF ada di `/home/afiq/Downloads/kitab STEM/<folder>/`. Baca sepotong dengan
`pdftotext -f N -l M "<berkas>" -` (jangan dump seluruh berkas; batasi 2-4 halaman
per bacaan dan cari dengan `grep -n` pada hasilnya). Python: `source ~/venv/bin/activate`.

Kolom **Basis** menunjuk bab edisi pertama di `../_buku/` yang boleh kamu baca sebagai
bahan awal. Perluas dan perdalam; jangan salin mentah, dan angka lama wajib kamu
verifikasi ulang sendiri.

---

## Bab 1 — Bahasa Matematika dan Seni Membuktikan
Basis: `../_buku/ch01.tex`. Bagian: (1) pernyataan, penghubung logika, tabel
kebenaran, kuantor dan cara menegasikannya; (2) membaca definisi secara harfiah
(definisi sebagai syarat perlu-dan-cukup, contoh penyangkal); (3) empat pola bukti:
langsung, kontraposisi, kontradiksi, konstruktif; (4) induksi matematika dan induksi
kuat; (5) ketika bukti gagal: klaim $n^2+n+41$ prima untuk semua $n \ge 0$ patah di
$n=40$, satu bukti keliru khas dan di mana cacatnya; (6) menulis bukti yang bisa
diperiksa orang lain (struktur kalimat, notasi, apa yang boleh dilewati).
Wajib dihitung: nilai $n^2+n+41$ untuk $n=0..40$ dan faktorisasi di $n=40$; jumlah
$1+3+\dots+(2n-1)$ untuk beberapa $n$; negasi dari dua pernyataan berkuantor.
Sumber: `Analisis Real/Abbott - Understanding analysis.pdf` (bagian awal tentang
himpunan dan bukti), `Metode Formal & Lean 4/mathematics_in_lean.pdf` (pendahuluan).

## Bab 2 — Himpunan, Relasi, Fungsi, dan Kardinalitas
Basis: tidak ada (bab baru). Bagian: (1) himpunan, operasi, hukum De Morgan, kuasa
himpunan; (2) hasilkali kartesius dan relasi; (3) relasi ekuivalensi dan partisi;
(4) fungsi: injektif, surjektif, bijektif, komposisi, invers; (5) himpunan berhingga,
terhitung, dan tak terhitung; diagonal Cantor; (6) ketaksamaan, nilai mutlak, dan
supremum sebagai alat (tanpa membangun $\mathbb{R}$; itu Bab 3).
Wajib dihitung: banyaknya himpunan bagian $2^n$ untuk $n$ kecil dan pemeriksaan
enumerasi dengan Python; pasangan Cantor sebagai bijeksi $\mathbb{N}\times\mathbb{N}
\to \mathbb{N}$ (periksa 10 nilai); enumerasi $\mathbb{Q}$ positif.
Sumber: `Analisis Real/Abbott - Understanding analysis.pdf` (bagian himpunan,
kardinalitas, himpunan tak hingga), `Aljabar Linear/Kenneth M Hoffman, Ray Kunze -
Linear Algebra (2nd Edition)-Prentice Hall (1971).pdf` (bab tentang himpunan dan
fungsi), `Metode Formal & Lean 4/mathematics_in_lean.pdf` (himpunan dan fungsi).

## Bab 3 — Aksioma Bilangan Real dan Supremum
Basis: paruh pertama `../_buku/ch02.tex`. Bagian: (1) aksioma lapangan; (2) aksioma
urutan dan akibatnya; (3) nilai mutlak dan ketaksamaan segitiga; (4) kelengkapan:
batas atas terkecil, sifat supremum, akibat (Archimedes, kerapatan $\mathbb{Q}$);
(5) mengapa $\mathbb{Q}$ belum cukup dan keberadaan $\sqrt{2}$ (bukti + aproksimasi
Newton); (6) interval, titik akumulasi, himpunan terbuka dan tertutup (ringkas,
tanpa topologi penuh).
Wajib dihitung: iterasi Newton untuk $\sqrt{2}$ 5 langkah dengan galat relatif tiap
langkah; barisan aproksimasi rasional dengan galat $<10^{-6}$; verifikasi bahwa
$\{q \in \mathbb{Q}: q^2<2\}$ tidak punya maksimum.
Sumber: `Analisis Real/Rudin Principles of Mathematical Analysis.pdf` (bab sistem
bilangan real), `Analisis Real/Abbott - Understanding analysis.pdf` (bab bilangan
real).

## Bab 4 — Barisan dan Limit
Basis: paruh kedua `../_buku/ch02.tex`. Bagian: (1) definisi $\varepsilon$-$N$ dan
cara memakainya; (2) ketunggalan limit, sifat aljabar limit (bukti); (3) teorema
apit dan uji rasio barisan; (4) barisan monoton dan teorema kekonvergenan monoton;
(5) subbarisan, Bolzano-Weierstrass, barisan Cauchy dan kelengkapan; (6) limit
superior dan inferior.
Wajib dihitung: $N$ eksplisit untuk $(3n+1)/(n+2) \to 3$ pada $\varepsilon=10^{-2}$
dan $10^{-4}$; $(1+1/n)^n$ untuk $n=10,10^2,\dots,10^7$; barisan rekursif
$x_{n+1}=\sqrt{2+x_n}$ (batas dan galat).
Sumber: Rudin (bab barisan dan deret bilangan), Abbott (bab barisan dan deret).

## Bab 5 — Deret Tak Hingga
Basis: tidak ada (bab baru; jangan memakai ulang isi Bab 4 sebagai prosa). Bagian:
(1) deret, jumlah parsial, deret geometri dan teleskopik; (2) uji suku ke-$n$ dan
uji pembanding; (3) uji rasio, uji akar, deret-$p$; (4) deret berganti tanda dan
uji Leibniz dengan batas galat; (5) kekonvergenan mutlak, pengelompokan ulang, dan
teorema susunan ulang Riemann (pernyataan); (6) deret harmonik divergen sangat
lambat: mengapa $H_{10^6}$ masih sekitar 14.
Wajib dihitung: $H_{10^6}$ dengan numpy (dan taksiran $\ln n+\gamma$); galat
pemotongan deret Leibniz untuk $\pi/4$ pada 1000 suku; jumlah $\sum 1/n^2$ numerik
vs $\pi^2/6$; uji rasio pada dua deret yang hasilnya berbeda.
Sumber: Rudin (bab barisan dan deret bilangan), Abbott (bab barisan dan deret).

## Bab 6 — Ruang Vektor dan Subruang
Basis: paruh pertama `../_buku/ch03.tex`. Bagian: (1) aksioma ruang vektor dan
contoh ($\mathbb{R}^n$, ruang matriks, ruang fungsi, ruang polinomial); (2) subruang
dan uji subruang; (3) kombinasi linear dan span; (4) kebebasan linear dan
ketergantungan; (5) basis dan dimensi (teorema pertukaran, bukti); (6) jumlah
langsung dan subruang komplemen.
Wajib dihitung: rank dan basis ruang kolom sebuah matriks $3\times4$ (numpy +
eliminasi manual); pemeriksaan bahwa tiga vektor di $\mathbb{R}^3$ bergantung;
dimensi ruang polinomial derajat $\le 3$.
Sumber: `Aljabar Linear/Book_H_Anton_11_Ed_Linear_Algebra.pdf` (bab ruang vektor
umum), `Aljabar Linear/LADR4e.pdf` (bab ruang vektor dan ruang vektor
berdimensi hingga).

## Bab 7 — Basis, Dimensi, dan Transformasi Linear
Basis: paruh kedua `../_buku/ch03.tex`. Bagian: (1) koordinat terhadap basis dan
matriks transisi; (2) transformasi linear, kernel, jangkauan; (3) matriks
representasi dan kaitan dengan perkalian matriks; (4) rank-nullity dengan bukti;
(5) isomorfisme dan invarian dimensi; (6) transformasi linear pada ruang berdimensi
hingga dinyatakan sebagai matriks (ruang $\mathcal{L}(V,W)$).
Wajib dihitung: matriks $3\times3$ dengan satu baris bergantung: rank, nullity,
basis kernel dan jangkauan langkah demi langkah; verifikasi `numpy.linalg.matrix_rank`
dan `scipy.linalg.null_space`; matriks representasi satu transformasi pada dua basis
berbeda dan pemeriksaan $[T]_{\mathcal{B}'} = P^{-1}[T]_{\mathcal{B}}P$.
Sumber: Anton (bab transformasi linear umum), Axler (bab peta linear), Hoffman-Kunze
(bab transformasi linear).

## Bab 8 — Sistem Persamaan Linear, Determinan, dan Invers
Basis: tidak ada (bab baru). Bagian: (1) bentuk eselon baris dan eliminasi Gauss,
kasus solusi tunggal/banyak/tidak ada; (2) determinan: definisi aksiomatik
(multilinear dan bergantian), sifat, ekspansi kofaktor; (3) aturan Cramer dan
adjoin; (4) invers matriks, matriks elementer, dan syarat invertibilitas yang
setara; (5) biaya komputasi dan bilangan kondisi (jembatan ke Bab 20).
Wajib dihitung: satu sistem $3\times3$ diselesaikan dua cara (eliminasi dan Cramer);
determinan $4\times4$ dengan ekspansi kofaktor vs `numpy.linalg.det`; bilangan
kondisi matriks Hilbert $4\times4$; sistem yang hampir singular (solusi melompat).
Sumber: Anton (bab sistem persamaan linear dan matriks, bab determinan),
Hoffman-Kunze (bab persamaan linear, bab determinan).

## Bab 9 — Nilai Eigen dan Diagonalisasi
Basis: paruh pertama `../_buku/ch04.tex`. Bagian: (1) polinomial karakteristik dan
nilai eigen sebagai akarnya; (2) ruang eigen, multiplisitas aljabar dan geometrik;
(3) syarat diagonalisasi (bukti); (4) matriks serupa dan invarian; (5) contoh
$2\times2$ yang gagal didiagonalkan; (6) penerapan: pangkat matriks, sistem
diferensial linear, rantai Markov singkat.
Wajib dihitung: nilai eigen dan vektor eigen satu matriks $3\times3$ (numpy, dengan
pemeriksaan $A\mathbf{v}=\lambda\mathbf{v}$); $A^{10}$ lewat diagonalisasi vs
perkalian langsung; satu matriks defective dan rank ruang eigennya.
Sumber: Anton (bab nilai eigen), Axler (bab nilai eigen dan vektor eigen, bab
operator pada ruang vektor kompleks), Hoffman-Kunze (bab bentuk kanonik elementer).

## Bab 10 — Ortogonalitas, SVD, dan Kuadrat Terkecil
Basis: paruh kedua `../_buku/ch04.tex`. Bagian: (1) hasilkali dalam, norma,
ketaksamaan Cauchy-Schwarz (bukti); (2) himpunan ortogonal, proyeksi, Gram-Schmidt
dan ketidakstabilan klasiknya; (3) kuadrat terkecil: persamaan normal, tafsir
geometris; (4) dekomposisi nilai singular $A=U\Sigma V^{\top}$ dan kaitannya dengan
nilai eigen $A^{\top}A$; (5) pseudoinverse dan solusi norma minimum; (6) mengapa SVD
lebih aman daripada persamaan normal secara numerik.
Wajib dihitung: proyeksi satu vektor pada subruang berdimensi dua; kuadrat terkecil
matriks $5\times2$ lewat persamaan normal vs `numpy.linalg.lstsq` (selisih galat
dan bilangan kondisi); SVD satu matriks $3\times2$ (nilai singular, rank, rasio
kondisi); Gram-Schmidt manual vs `numpy.linalg.qr` (ortogonalitas $\|Q^{\top}Q-I\|$).
Sumber: Axler (bab ruang hasilkali dalam, bab operator pada ruang hasilkali dalam),
`Introduction to Linear Algebra 6th edition...pdf` (bab ortogonalitas, bab SVD),
Anton (bab ruang hasilkali dalam).

## Bab 11 — Kekontinuan dan Kekontinuan Seragam
Basis: paruh pertama `../_buku/ch05.tex`. Bagian: (1) limit fungsi dan definisi
$\varepsilon$-$\delta$; (2) kekontinuan, sifat aljabar, komposisi; (3) teorema nilai
antara dan teorema nilai ekstrem (bukti ringkas); (4) kekontinuan seragam dan
perbedaannya dengan kekontinuan titik demi titik; (5) $x^2$ tidak seragam di
$\mathbb{R}$ tetapi seragam di $[0,1]$; Lipschitz; (6) fungsi yang kontinu hanya di
satu titik, dan fungsi Dirichlet termodifikasi.
Wajib dihitung: $\delta$ eksplisit untuk $f(x)=x^2$ di $x_0=2$ pada
$\varepsilon=10^{-3}$; pencarian $\delta$ yang gagal seragam pada $x_0$ besar
(tabel numerik); kekontinuan $1/x$ pada $[1,\infty)$ vs $(0,1]$.
Sumber: Rudin (bab kekontinuan), Abbott (bab limit fungsi dan kekontinuan).

## Bab 12 — Turunan: Satu dan Banyak Variabel
Basis: paruh kedua `../_buku/ch05.tex`. Bagian: (1) definisi turunan dan aturan
dasar; (2) aturan rantai dengan bukti; (3) teorema nilai rata-rata dan akibatnya
(monotonisitas, turunan nol, ketaksamaan); (4) polinomial Taylor dengan sisa;
(5) turunan parsial, gradien, Jacobian; diferensiabilitas vs parsial ada (contoh
penyangkal); (6) aturan rantai multivariabel dan matriks Hessian.
Wajib dihitung: beda hingga vs turunan analitik untuk satu fungsi di beberapa $h$;
gradien dan Jacobian satu fungsi $\mathbb{R}^2\to\mathbb{R}^2$ di satu titik;
pemeriksaan aturan rantai multivariabel lewat komposisi numerik; contoh fungsi yang
parsialnya ada di $(0,0)$ tetapi tidak kontinu.
Sumber: Rudin (bab diferensiasi), Abbott (bab turunan),
`Kalkulus Multivariabel/Stewart.pdf` (bab turunan parsial),
`Kalkulus Multivariabel/spivak-calculus-on-manifolds.pdf` (bab diferensiasi).

## Bab 13 — Integral Riemann dan Teorema Dasar Kalkulus
Basis: paruh pertama `../_buku/ch06.tex`. Bagian: (1) partisi, jumlah atas dan
bawah, kriteria keterintegralan; (2) kelas fungsi yang terintegralkan (kontinu,
monoton) dan contoh fungsi tidak terintegralkan; (3) teorema dasar kalkulus bagian
1 dan 2 dengan bukti; (4) substitusi dan integral parsial; (5) teorema nilai rata-rata
untuk integral; (6) integral tak wajar singkat dan kaitannya dengan deret (Bab 5).
Wajib dihitung: jumlah Riemann kiri/kanan/titik tengah untuk $\int_0^1 x^2\,dx$
dengan $n=10,100,1000$ dan laju galatnya ($\mathcal{O}(1/n)$, $\mathcal{O}(1/n^2)$);
perbandingan dengan `scipy.integrate.quad`; satu integral yang nilainya tidak bisa
dihitung dengan antiturunan elementer.
Sumber: Rudin (bab integral Riemann-Stieltjes), Abbott (bab integral Riemann).

## Bab 14 — Deret Fungsi dan Pertukaran Limit
Basis: paruh kedua `../_buku/ch06.tex`. Bagian: (1) kekonvergenan titik demi titik
vs seragam; (2) uji Weierstrass M dan contoh $x^n$ pada $[0,1]$; (3) pertukaran limit
dengan kekontinuan, turunan, dan integral (tiga teorema + sketsa bukti); (4) deret
pangkat, radius konvergensi, turunan dan integral suku demi suku; (5) contoh di mana
pertukaran gagal dan kerugian praktisnya; (6) aproksimasi fungsi dengan deret dan
batas galatnya.
Wajib dihitung: $\sup_{x\in[0,1]} |x^n - 0|$ untuk beberapa $n$; galat aproksimasi
$\exp(x)$ dengan deret Taylor pada $x=1$ untuk suku ke-$N$; radius konvergensi tiga
deret pangkat.
Sumber: Rudin (bab barisan dan deret fungsi), Abbott (bab barisan dan deret fungsi).

## Bab 15 — Integral Lipat, Perubahan Variabel, dan Teorema Lapangan Vektor
Basis: tidak ada (bab baru). Bagian: (1) integral lipat dua dan tiga, teorema
Fubini; (2) perubahan variabel dan determinan Jacobian; koordinat polar, silinder,
bola; (3) integral garis dan medan konservatif; (4) teorema Green, Gauss, dan Stokes
(pernyataan + satu contoh masing-masing); (5) bentuk diferensial sebagai bahasa
umum (perkenalan dengan Spivak, tanpa formalisme penuh); (6) kapan teorema lapangan
vektor gagal (syarat batas dan singularitas).
Wajib dihitung: satu integral lipat di daerah lingkaran dihitung dua cara (Cartesius
vs polar) dan dicek dengan `scipy.integrate.dblquad`; volume bola dengan Jacobian
bola; satu integral garis dihitung langsung vs lewat potensial.
Sumber: `Kalkulus Multivariabel/Stewart.pdf` dan `.../Calculus Early
Transcendentals 9th Edition...pdf` (bab integral lipat, bab kalkulus vektor),
`Kalkulus Multivariabel/acm-full-text.pdf` (Active Calculus: integral lipat dan
kalkulus vektor), `Kalkulus Multivariabel/spivak-calculus-on-manifolds.pdf`
(integrasi pada rantai dan manifold).

## Bab 16 — Peluang dan Peluang Bersyarat
Basis: paruh pertama `../_buku/ch07.tex`. Bagian: (1) aksioma peluang dan akibatnya;
(2) pencacahan dan peluang kombinatorial; (3) peluang bersyarat dan aturan
perkalian; (4) teorema Bayes dengan contoh dua langkah dan tafsir medis; (5)
independensi dan kesalahpahaman "saling lepas"; (6) paradoks yang menuntut hitungan
(masalah ulang tahun, Monty Hall).
Wajib dihitung: peluang Bayes untuk uji diagnostik dengan sensitivitas dan
spesifisitas tertentu; peluang ulang tahun untuk $n=23$ dan $n=50$; simulasi Monty
Hall minimal $10^4$ percobaan dengan numpy.
Sumber: `Probabilitas & Statistika/preview-9780429766749_A36188955.pdf`
(Blitzstein-Hwang: peluang dan pencacahan, peluang bersyarat).

## Bab 17 — Variabel Acak dan Distribusi
Basis: paruh kedua `../_buku/ch07.tex`. Bagian: (1) variabel acak, fungsi massa,
kepadatan, fungsi distribusi kumulatif; (2) harapan, variansi, momen; (3) distribusi
Bernoulli, binomial, geometrik, Poisson; (4) distribusi normal, eksponensial, dan
kaitannya; (5) distribusi bersama, kovarians, korelasi; (6) transformasi variabel
acak dan Jacobian.
Wajib dihitung: turunkan rata-rata dan variansi binomial, lalu cocokkan dengan
Monte Carlo $10^5$; jumlah pmf Poisson untuk beberapa $\lambda$ (harus 1 dalam galat
mesin); transformasi $Y=X^2$ untuk $X$ seragam dan pemeriksaan kepadatan hasil.
Sumber: Blitzstein-Hwang (variabel acak dan distribusinya, harapan),
`Probabilitas & Statistika/2004 - wasserman - all of statistics.pdf` (peluang,
variabel acak, harapan).

## Bab 18 — Hukum Bilangan Besar dan Teorema Limit Pusat
Basis: paruh ketiga `../_buku/ch07.tex`. Bagian: (1) barisan variabel acak dan
konvergensi dalam peluang; (2) hukum bilangan besar lemah (bukti lewat ketaksamaan
Chebyshev) dan hukum kuat (pernyataan); (3) teorema limit pusat dan sketsa bukti
lewat fungsi karakteristik; (4) aproksimasi normal, koreksi kontinuitas; (5) laju
galat Monte Carlo dan mengapa $1/\sqrt{n}$ itu lambat; (6) kapan CLT menyesatkan
(ekor berat, variansi tak hingga).
Wajib dihitung: simulasi LLN untuk rata-rata dadu pada $n=10,10^2,\dots,10^5$;
simulasi CLT untuk rata-rata eksponensial (bandingkan kuantil dengan normal, uji
Kolmogorov-Smirnov lewat scipy); galat baku Monte Carlo empiris vs $1/\sqrt{n}$;
satu contoh distribusi ekor berat (Cauchy) yang melanggar CLT.
Sumber: Blitzstein-Hwang (bagian kekonvergenan), Wasserman (bab konvergensi
variabel acak, bab pertidaksamaan).

## Bab 19 — Estimasi, Interval Kepercayaan, dan Uji Hipotesis
Basis: paruh keempat `../_buku/ch07.tex` + bagian Wilson dan rule of three dari
`../_buku/ch11.tex`. Bagian: (1) estimator, bias, variansi, galat baku; (2) interval
kepercayaan rata-rata (normal dan t); (3) interval kepercayaan proporsi: Wald vs
Wilson, dengan tabel perbandingan; (4) aturan tiga untuk nol kejadian; (5) uji
hipotesis, nilai-p, galat tipe I/II, daya; (6) salah tafsir nilai-p yang paling
umum, dan cara melaporkan hasil dengan benar.
Wajib dihitung: Wilson dan Wald untuk 33/50 dan 53/100 (bandingkan lebar dan
perilaku di dekat 0 dan 1); aturan tiga untuk $n=100$; simulasi daya uji proporsi
untuk satu skenario (numpy) dan bandingkan dengan rumus aproksimasi normal.
Sumber: Wasserman (bab inferensi statistik dan pembelajaran, bab inferensi
parametrik, bab uji hipotesis dan nilai-p), Blitzstein-Hwang (bagian harapan dan
kekonvergenan).

## Bab 20 — Aritmetika Floating-Point dan Analisis Galat
Basis: `../_buku/ch08.tex`. Bagian: (1) format IEEE-754: tanda, eksponen, mantissa,
bias; normal dan subnormal; (2) pembulatan, ULP, epsilon mesin; (3) $0{,}1+0{,}2 \ne
0{,}3$ dan selisih sebenarnya dalam ULP; (4) galat absolut/relatif, bilangan
kondisi, hilangnya digit signifikan; (5) ketidakstabilan algoritma: $(1-\cos x)/x^2$
untuk $x$ kecil, penjumlahan berurutan vs penjumlahan Kahan; (6) pedoman praktis
menulis kode numerik.
Wajib dihitung: bitfield `struct`/`numpy.float32` untuk beberapa bilangan dan
`float.hex()`; ULP dan epsilon mesin; penjumlahan Kahan vs naif untuk $10^6$ suku;
galat relatif $(1-\cos x)/x^2$ pada $x=10^{-1},\dots,10^{-10}$ dan pembanding
deret Taylor.
Sumber: `Numerik/goldberg.pdf`.

## Bab 21 — Optimasi Konveks dan Dualitas
Basis: paruh pertama `../_buku/ch09.tex`. Bagian: (1) himpunan konveks dan
kombinasi konveks; (2) fungsi konveks, uji orde pertama dan kedua (Hessian definit
positif); (3) bentuk baku masalah optimasi dan mengapa konveks berarti optimum
global; (4) Lagrangian, dual Lagrange, dualitas lemah dengan bukti, dualitas kuat
dan syarat Slater (pernyataan); (5) kondisi KKT dan tafsir pengali; (6) contoh
kuadratik kecil diselesaikan lewat KKT.
Wajib dihitung: satu masalah QP dua variabel dengan kendala, diselesaikan lewat KKT
manual lalu `scipy.optimize.minimize` (bandingkan $x^{*}$ dan pengali); uji
konveksitas Hessian satu fungsi dua variabel (nilai eigen); ilustrasi celah dualitas
pada satu masalah nonkonveks kecil.
Sumber: `Optimasi & Neural Networks/bv_cvxbook.pdf` (bab himpunan konveks, bab
fungsi konveks, bab masalah optimasi konveks, bab dualitas).

## Bab 22 — Pemrograman Linear dan Integer
Basis: paruh kedua `../_buku/ch09.tex`. Bagian: (1) bentuk baku LP dan formulasi;
(2) geometri: titik ekstrem dan verteks; (3) metode simpleks: satu tabel
dikerjakan penuh; (4) dualitas LP, complementary slackness, dan tafsir harga bayangan;
(5) relaksasi LP untuk program integer, integrality gap, branch and bound; (6) satu
program integer kecil diselesaikan dengan enumerasi dan dengan `scipy.optimize.milp`.
Wajib dihitung: satu LP dua variabel secara grafik dan dengan `scipy.optimize.linprog`
(nilai optimum dan harga bayangan); dual dan pemeriksaan dualitas kuat secara
numerik; satu IP (knapsack 4 barang) lewat enumerasi vs MILP, plus integrality gap
relaksasinya.
Sumber: `Optimasi & Neural Networks/WSPrinted.pdf` (Bertsimas-Tsitsiklis: formulasi,
geometri, simpleks, dualitas), `Optimasi & Neural Networks/IntegerProgramming-Wolsey.pdf`
(formulasi dan relaksasi).

## Bab 23 — Jaringan Saraf dan Turunan Balik
Basis: `../_buku/ch10.tex`. Bagian: (1) perceptron dan batas linear; (2) MLP,
fungsi aktivasi (ReLU, sigmoid), universal approximation (pernyataan); (3) softmax
dan cross-entropy; (4) turunan balik lengkap untuk jaringan 4 masukan - 2 unit ReLU
- 1 keluaran sigmoid, semua angka eksak; (5) pemeriksaan gradien numerik; (6)
gradien terhadap masukan (jembatan ke Bab 27) dan satu langkah gradient descent.
Wajib dihitung: forward pass eksak dengan bobot yang ditentukan; gradien setiap
bobot manual dan dengan numpy (selisih harus di bawah $10^{-12}$); satu langkah
gradient descent dengan learning rate yang diberikan; gradien terhadap masukan
diverifikasi dengan beda hingga.
Sumber: `Optimasi & Neural Networks/book.pdf` (Nielsen, bab 1-2),
`Optimasi & Neural Networks/Deep+Learning+Ian+Goodfellow.pdf` (bagian deep
feedforward networks).

## Bab 24 — Generalisasi, Regularisasi, dan Pelatihan
Basis: tidak ada (bab baru). Bagian: (1) galat latih vs galat uji; underfitting dan
overfitting; (2) dekomposisi bias-variansi; (3) regularisasi L2, L1, early stopping,
dropout; (4) standardisasi fitur memakai statistik data latih saja (kebocoran data);
(5) penurun gradien: SGD, momentum, Adam — perbedaan pembaruan; (6) jadwal learning
rate, pemilihan hiperparameter, dan protokol validasi yang jujur.
Wajib dihitung: eksperimen numpy kecil (regresi logistik atau MLP satu lapis) pada
data sintetis dengan tiga setelan (tanpa regularisasi, L2, L1) — laporkan galat
latih dan validasi, dan tunjukkan overfitting secara nyata; satu lintasan optimasi
SGD vs Adam (jumlah langkah sampai ambang galat).
Sumber: Goodfellow (bab regularization for deep learning, bab optimization for
training deep models), Nielsen (bab improving the way neural networks learn).

## Bab 25 — Evaluasi Model yang Jujur
Basis: `../_buku/ch11.tex` (kecuali bagian Wilson yang sudah dipakai Bab 19) dan
contoh dari `../note.md` bila relevan. Bagian: (1) matriks konfusi dan metrik turunan
(precision, recall, F1) beserta kapan tiap metrik menyesatkan; (2) kurva ROC dan AUC,
serta ketergantungannya pada prevalensi; (3) ketidakseimbangan kelas dan akurasi yang
menipu; (4) ketidakpastian metrik: interval untuk proporsi (rujuk Bab 19), aturan
tiga, interval untuk selisih dua model; (5) kebocoran data, pemisahan latih/uji,
validasi silang yang benar; (6) checklist pelaporan hasil eksperimen.
Wajib dihitung: matriks konfusi contoh dengan 1000 prediksi (precision/recall/F1
manual vs `sklearn` bila tersedia, kalau tidak numpy); AUC dari data skor kecil
dihitung manual; efek prevalensi pada precision pada recall tetap; contoh kebocoran
data yang menaikkan akurasi uji secara palsu (simulasi kecil).
Sumber: Wasserman (bab model, inferensi statistik dan pembelajaran),
`../note.md` (contoh kerja penulis sendiri, sebutkan batasnya).

## Bab 26 — Metode Formal dengan Lean 4
Basis: `../_buku/ch12.tex`. Bagian: (1) proposisi sebagai tipe, bukti sebagai term;
(2) kuantor dan aturan intro/eliminasi; (3) taktik dasar (`intro`, `exact`, `rw`,
`simp`, `induction`, `linarith`); (4) satu bukti induksi lengkap (jumlah bilangan
ganjil $=n^2$) ditulis bertahap dengan penjelasan tiap taktik; (5) struktur,
typeclass, dan `native_decide`: apa yang benar-benar dijamin, apa yang diasumsikan;
(6) batas formalisasi: spesifikasi salah menghasilkan bukti yang tak berguna;
kaitannya dengan sertifikat dan evaluasi model jujur (Bab 25).
Wajib disebut jujur: Lean **tidak terpasang** di mesin ini, jadi potongan kode tidak
dieksekusi; kode dicocokkan dengan `mathematics_in_lean.pdf` dan `print.pdf` dan
dinyatakan begitu di dalam bab. Angka yang dihitung (mis. jumlah bilangan ganjil
untuk beberapa $n$) tetap diverifikasi Python.
Sumber: `Metode Formal & Lean 4/mathematics_in_lean.pdf`,
`.../matematika-dalam-lean-bahasa-indonesia.pdf`, `.../print.pdf` (Theorem Proving
in Lean 4).

## Bab 27 — Adversarial Machine Learning: Serangan dan Pertahanan
Basis: paruh pertama `../_buku/ch13.tex`. Bagian: (1) definisi ancaman: norma
$L_\infty$, $\varepsilon$, tujuan penyerang; (2) mengapa tanda gradien cukup:
derivasi FGSM dari linearisasi; (3) PGD dan formulasi min-max, adversarial training;
(4) transferabilitas dan serangan black-box; (5) contoh numerik pada model linear
dan MLP kecil (gradien terhadap masukan, perubahan prediksi); (6) biaya komputasi
dan keterbatasan praktis.
Wajib dihitung: FGSM pada model linear dengan bobot tertentu (perubahan keluaran
eksak); PGD beberapa langkah pada MLP kecil: akurasi bersih vs akurasi di bawah
serangan untuk beberapa $\varepsilon$; perbandingan dengan beda hingga gradien.
Sumber: `Adversarial ML/1412.6572v3.pdf` (FGSM),
`Adversarial ML/1706.06083v4.pdf` (PGD, adversarial training).

## Bab 28 — Batas Serangan: Gradien Dikaburkan dan Evasi NIDS
Basis: paruh kedua `../_buku/ch13.tex` + `../note.md`. Bagian: (1) tujuh teknik
mengaburkan gradien dan mengapa evaluasi menjadi menyesatkan; (2) serangan yang
menembusnya: BPDA, EOT, reparameterisasi; (3) bagaimana merancang evaluasi yang
jujur (anggaran adaptif, beberapa seed, laporkan variansi); (4) studi kasus: evasi
terhadap NIDS berbasis ML, mengapa NIDS dinamis lebih tahan; (5) hasil kerja penulis
sendiri dari `note.md` — sebutkan sebagai kerja penulis, sertakan batasnya secara
eksplisit, dan jangan mengklaim lebih dari yang ada di catatan; (6) daftar periksa
untuk klaim "serangan berhasil".
Wajib dihitung: simulasi serangan pada klasifikasi dengan gradien yang sengaja
dikaburkan (mis. kuantisasi keluaran) dan demonstrasi bahwa serangan naif gagal
padahal model tetap rapuh (BPDA sederhana, numpy); metrik keberhasilan dengan
beberapa seed (rata-rata dan simpangan).
Sumber: `Adversarial ML/1802.00420v4.pdf` (obfuscated gradients),
`main/Evasion Adversarial Attacks Remain Impractical Against ML-based Network
Intrusion Detection Systems, Especially Dynamic Ones.pdf`, `../note.md`.

## Bab 29 — Kriptografi: Bilangan Bulat Modular sampai Ancaman Kuantum

Prasyarat: Bab 2, 3, 26. Ditambahkan 2026-10-24 atas keputusan penulis agar judul
"ke Keamanan Machine Learning" tidak berhenti pada serangan adversarial.
Isi: aritmetika modular dan kelas sisa; gcd, Euklid, invers modular; Fermat kecil dan
Euler dengan bukti; grup siklik secukupnya; Diffie-Hellman dengan contoh angka yang
dihitung Python; RSA (mengapa bekerja, mengapa tanpa padding salah); hash dan MAC;
tanda tangan; model keamanan komputasi sebagai asumsi, bukan teorema; Shor dan apa
yang runtuh; kriptografi pasca-kuantum secara konseptual; satu bagian yang
menghubungkan kebocoran lewat keluaran ke pola ancaman Bab 27-28.
Gambar wajib: jam modular dan/atau alur Diffie-Hellman (TikZ, ber-caption, dirujuk).

## Bab 30 — Privasi Diferensial dan Fondasi Matematis QML

Prasyarat: Bab 10, 16, 17. Ditambahkan 2026-10-24 untuk menutup celah "privasi" dan
"kuantum" yang nol kemunculan pada edisi sebelumnya.
Isi: kebocoran data lewat model dan serangan inferensi keanggotaan; definisi
$\varepsilon$-$\delta$ dan alasan memilih jaminan terburuk, bukan rata-rata;
sensitivitas global; mekanisme Laplace dengan bukti jaminan; Gaussian secukupnya;
komposisi dan anggaran privasi; DP-SGD (clipping + noise) serta trade-off
privasi-utilitas; batas klaim DP. Lalu fondasi QML: bilangan kompleks, modulus dan
fase, ruang Hilbert berdimensi hingga, bra-ket, gerbang uniter dan kekekalan norma,
Fourier sebagai perubahan basis, aturan Born, satu sirkuit 1-2 qubit dihitung tangan,
dan ledakan dimensi $2^{n}$ sebagai alasan klaim keunggulan harus dijaga.
Gambar wajib: kurva trade-off dari eksperimen nyata atau diagram fase (TikZ).
Kejujuran: QML belum punya bukti keunggulan praktis yang mapan; sebutkan batasnya.


---

## Bab 16 — Persamaan Diferensial dan Sistem Dinamik

**Berkas:** `ch16.tex` · **Bagian III** · **Prasyarat:** Bab 12, 14, 15
**Pesan utama:** sebuah persamaan diferensial bukan rumus yang harus ditebak, melainkan
janji bahwa keadaan besok ditentukan keadaan hari ini — dan janji itu perlu syarat agar
tidak pecah.

Isi minimum:
1. ODE orde satu: pemisahan variabel, persamaan linear + faktor integrasi, contoh laju
   peluruhan dan pendinginan Newton.
2. Kapan solusi ada dan tunggal: syarat Lipschitz, teorema Picard-Lindelof (pernyataan
   lengkap, bukti sketsa lewat iterasi Picard), contoh $x'=\sqrt{|x|}$ yang gagal tunggal.
3. Sistem otonom dan bidang fase: dua dimensi, trayektori, titik setimbang, linearisasi
   memakai nilai eigen (sambung Bab 9), klasifikasi simpul/pelana/pusat.
4. Osilator harmonik, redaman, pendulum tak linear: mengapa linearisasi hanya berlaku lokal.
5. Metode numerik: Euler (galat lokal orde 2, global orde 1), Runge-Kutta orde 4,
   perbandingan pada satu soal yang solusi eksaknya diketahui; kekakuan secara kualitatif.
6. Kestabilan Lyapunov: definisi, fungsi Lyapunov sederhana, contoh pendulum dengan energi.
7. Satu kotak peneliti: mengapa integrasi numerik jangka panjang bisa memberi jawaban
   yang tampak masuk akal tetapi salah secara kualitatif.

**Gambar (3):** (a) bidang fase pendulum dengan beberapa trayektori; (b) galat Euler vs
RK4 terhadap ukuran langkah pada skala log-log; (c) diagram klasifikasi titik setimbang
berdasarkan tanda dan jenis nilai eigen.

---

## Bab 21 — Regresi dan Statistika Terapan

**Berkas:** `ch21.tex` · **Bagian IV** · **Prasyarat:** Bab 10, 20
**Pesan utama:** regresi adalah proyeksi, dan setiap angka yang keluar darinya hanya
sejujur asumsi yang menyertainya.

Isi minimum:
1. Regresi linear sederhana dan berganda dari kuadrat terkecil; persamaan normal
   $X^{\top}X\hat{\beta}=X^{\top}y$ diturunkan lewat proyeksi ortogonal (Bab 10).
2. Tafsiran koefisien beserta satuannya; apa yang berubah bila satu peubah penjelas
   diskalakan.
3. Asumsi Gauss-Markov dan arti "penaksir tak bias terbaik linear"; kapan asumsi itu
   dilanggar dan apa akibatnya.
4. $R^2$, korelasinya dengan sisa, dan mengapa $R^2$ tinggi bukan bukti model benar.
5. Selang kepercayaan dan uji $t$ untuk koefisien (sambung Bab 20); selang prediksi
   versus selang rata-rata.
6. Diagnostik residu: pola, heteroskedastisitas, pencilan; multikolinearitas dan VIF.
7. Regresi logistik secara ringkas: mengapa OLS tidak dipakai untuk keluaran biner,
   dan bagaimana koefisiennya ditafsirkan lewat rasio odds.
8. Korelasi bukan kausalitas, dengan paradoks Simpson memakai tabel angka yang dihitung
   penuh di dalam bab.
9. Kotak peneliti: pelaporan yang jujur — jumlah pengamatan, pemisahan data, larangan
   memilih model setelah melihat hasil.

**Gambar (2-3):** (a) titik data + garis kuadrat terkecil + residu sebagai segmen tegak;
(b) bidang regresi berganda diproyeksikan sebagai kontur pada dua peubah; (c) paradoks
Simpson: dua tren kelompok yang berlawanan dengan tren gabungan.
