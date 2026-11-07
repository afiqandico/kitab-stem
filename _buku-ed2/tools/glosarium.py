#!/usr/bin/env python3
"""Second-edition book glossary: one entry for every `\\kamus` term in the chapters.

The glossary used to hold 86 selected entries, while 32 chapters used 161 different
terms in the `\\kamus` boxes. This script stores the definitions of all those terms
and rewrites them into `main.tex` in alphabetical order, so that:

  * every technical term the book uses has a definition in one place, and
  * the alphabetical order is produced by machine, not typed by hand.

Usage:
    python3 tools/glosarium.py tulis     # rewrite the main.tex glossary block
    python3 tools/glosarium.py cek       # report \\kamus terms that are missing
    python3 tools/glosarium.py daftar    # print the entries stored here

The same gate lives in `build_ed2.py check` (marker `glosarium-kurang=N`), so
forgetting to add an entry turns `make check` red instead of being just a note.
"""
from __future__ import annotations

import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(HERE, "main.tex")
AWAL = "\\chapter{Glosarium}"
AKHIR = "% ---------------------------- lampiran C"

def arg(teks: str, i: int) -> tuple[str, int]:
    """Read one braced argument starting at `teks[i]` (must be '{'), aware of nested braces.

    The regex `\\{[^{}]*\\}` is not enough: many analogies contain `$...^{7}$`, so terms
    are silently missed. This function counts brace depth, so `$2^{7}$` stays whole.
    """
    if i >= len(teks) or teks[i] != "{":
        return "", i
    d, j = 0, i
    while j < len(teks):
        if teks[j] == "{":
            d += 1
        elif teks[j] == "}":
            d -= 1
            if d == 0:
                return teks[i + 1:j], j + 1
        j += 1
    return "", i


def normal(s: str) -> str:
    """Comparison form: no surrounding spaces, no curly braces, lowercase."""
    return re.sub(r"\s+", " ", s.strip().strip("{}")).lower()


# ---------------------------------------------------------------- new entries
# Key: the term exactly as it appears in the \kamus box. Value: (label, definition).
# Definitions are rewritten from the term's usage in its source chapter, not
# translated from a dictionary; every number and formula must be right as it stands.
BARU: dict[str, tuple[str, str]] = {
    "adjoin": ("Adjoin",
               "matriks kofaktor yang disusun transpos; dipakai menuliskan invers sebagai satu "
               "rumus, $A^{-1}=\\operatorname{adj}(A)/\\det A$ (\\emph{adjugate})."),
    "adjoint": ("Adjoint",
                "dalam turunan balik, bilangan yang menyatakan seberapa besar kerugian akhir "
                "terpengaruh oleh satu besaran di tengah jaringan; satu adjoint per besaran "
                "(\\emph{adjoint})."),
    "akar primitif": ("Akar primitif",
                      "anggota yang bila dipangkatkan berulang melewati semua anggota grup siklik "
                      "lain sebelum kembali ke satu; pada kriptografi, posisi awal yang mencapai "
                      "seluruh posisi kunci (\\emph{primitive root})."),
    "aksioma kelengkapan": ("Aksioma kelengkapan",
                            "janji bahwa setiap himpunan tak kosong yang terbatas ke atas di "
                            "$\\mathbb{R}$ punya supremum; inilah yang membuat garis bilangan tidak "
                            "berlubang (\\emph{completeness axiom})."),
    "amplitudo": ("Amplitudo",
                  "amplitudo peluang: bilangan kompleks yang modulus kuadratnya memberi peluang; "
                  "berbeda dari peluang karena dua amplitudo dapat saling meniadakan "
                  "(\\emph{probability amplitude})."),
    "anggaran privasi": ("Anggaran privasi",
                         "jumlah $\\varepsilon$ yang boleh dibelanjakan sebuah sistem; setiap kueri "
                         "atau langkah pelatihan mengurangi sisanya (\\emph{privacy budget})."),
    "antiturunan": ("Antiturunan",
                    "fungsi yang turunannya adalah fungsi yang sedang diintegralkan; arah pulang "
                    "dari sebuah turunan (\\emph{antiderivative})."),
    "aturan Born": ("Aturan Born",
                    "aturan yang mengubah amplitudo menjadi peluang dengan mengkuadratkan "
                    "modulusnya (\\emph{Born rule})."),
    "aturan rantai": ("Aturan rantai",
                      "laju perubahan fungsi tersusun sama dengan hasil kali laju pada setiap mata "
                      "rantainya (\\emph{chain rule})."),
    "aturan tiga": ("Aturan tiga",
                    "bila tidak ada kejadian dalam $n$ percobaan, laju kejadiannya masih boleh "
                    "setinggi sekitar $3/n$ pada selang kepercayaan 95 persen (\\emph{rule of three})."),
    "bantalan": ("Bantalan",
                 "isi tambahan pada paket sebelum dikirim agar setiap paket berukuran tetap, "
                 "sehingga ukuran paket tidak lagi membocorkan isinya (\\emph{padding})."),
    "barisan": ("Barisan",
                "deretan bilangan yang diberi nomor urut $a_1,a_2,\\dots$; urutannya bagian dari "
                "definisinya, bukan sesuatu yang ditambahkan kemudian (\\emph{sequence})."),
    "barisan Cauchy": ("Barisan Cauchy",
                       "barisan yang sukunya makin rapat satu sama lain, tanpa perlu menyebut nilai "
                       "yang dituju (\\emph{Cauchy sequence})."),
    "barisan monoton": ("Barisan monoton",
                        "barisan yang hanya naik atau hanya turun, tidak pernah berbalik arah "
                        "(\\emph{monotone sequence})."),
    "bentuk baku": ("Bentuk baku",
                    "penulisan seragam masalah optimasi: satu sasaran, kendala berbentuk tidak "
                    "lebih dari nol, dan peubah tak negatif (\\emph{standard form})."),
    "bijeksi": ("Bijeksi",
                "pemasangan sempurna dua himpunan: injektif dan surjektif sekaligus, tanpa sisa di "
                "kedua sisi (\\emph{bijection})."),
    "bpda": ("BPDA",
             "pengganti gradien pada potongan yang tidak terdiferensiasi dengan gradien fungsi di "
             "titik sesudahnya, dipakai agar serangan tetap dapat dihitung (\\emph{backward pass "
             "differentiable approximation})."),
    "celah integralitas": ("Celah integralitas",
                           "jarak antara nilai terbaik relaksasi LP dan nilai terbaik jawaban bulat; "
                           "ia mengukur seberapa jauh model bersambung menipu "
                           "(\\emph{integrality gap})."),
    "defective": ("Defective",
                  "matriks yang nilai eigennya berulang tetapi ruang eigennya terlalu sempit untuk "
                  "menjadi basis (\\emph{defective})."),
    "deret": ("Deret",
              "penjumlahan suku-suku barisan tanpa henti, yang nilainya dibaca sebagai limit jumlah "
              "parsial (\\emph{series})."),
    "deret harmonik": ("Deret harmonik",
                       "deret $1+1/2+1/3+\\cdots$; sukunya menuju nol tetapi jumlahnya menyimpang "
                       "(\\emph{harmonic series})."),
    "deret pangkat": ("Deret pangkat",
                      "deret berbentuk $\\sum a_n(x-c)^n$; ia berlaku hanya di dalam jari-jari "
                      "konvergensinya (\\emph{power series})."),
    "determinan Jacobian": ("Determinan Jacobian",
                            "faktor skala volume lokal ketika koordinat diganti; nilai mutlaknya "
                            "mengalikan luas atau volume pada integral lipat "
                            "(\\emph{Jacobian determinant})."),
    "diagonalisasi": ("Diagonalisasi",
                      "penggantian basis sampai matriksnya menjadi diagonal, sehingga pekerjaannya "
                      "tinggal perkalian angka (\\emph{diagonalization})."),
    "dimensi": ("Dimensi",
                "banyaknya vektor dalam sebuah basis; angkanya milik ruang, bukan milik satu basis "
                "yang kebetulan dipilih (\\emph{dimension})."),
    "distribusi eksponensial": ("Distribusi eksponensial",
                                "sebaran waktu tunggu pada proses tanpa penuaan, dengan fungsi "
                                "kepadatan $\\lambda e^{-\\lambda t}$ "
                                "(\\emph{exponential distribution})."),
    "distribusi normal": ("Distribusi normal",
                          "sebaran lonceng simetris yang ditentukan sepenuhnya oleh rata-rata dan "
                          "variansinya (\\emph{normal distribution})."),
    "ekor berat": ("Ekor berat",
                   "sebaran yang peluang nilai raksasanya mengecil terlalu lambat, sehingga satu "
                   "pengamatan dapat mengalahkan seluruh sisanya (\\emph{heavy tail})."),
    "eliminasi": ("Eliminasi",
                  "penggantian sebuah sistem dengan sistem yang lebih sederhana tanpa mengubah "
                  "himpunan solusinya (\\emph{elimination})."),
    "entropi silang": ("Entropi silang",
                       "ukuran kejutan $-\\sum_i y_i\\log \\hat{p}_i$; makin yakin model pada "
                       "jawaban yang salah, makin besar dendanya (\\emph{cross-entropy})."),
    "eot": ("EOT",
            "serangan yang memaksimumkan harapan kerugian atas keacakan pertahanan, biasanya dengan "
            "merata-ratakan gradien pada beberapa salinan acak (\\emph{expectation over "
            "transformation})."),
    "epsilon mesin": ("Epsilon mesin",
                      "jarak antara $1$ dan bilangan mesin berikutnya; ukuran satu langkah pada "
                      "skala satu (\\emph{machine epsilon})."),
    "faktor integrasi": ("Faktor integrasi",
                         "pengali yang mengubah ruas kiri persamaan diferensial linear menjadi satu "
                         "turunan hasil kali (\\emph{integrating factor})."),
    "fungsi aktivasi": ("Fungsi aktivasi",
                        "pemetaan tak linear pada keluaran sebuah unit; ia menentukan seberapa besar "
                        "sinyal diteruskan dan bentuk turunannya (\\emph{activation function})."),
    "fungsi distribusi kumulatif": ("Fungsi distribusi kumulatif",
                                    "fungsi $F(x)=P(X\\le x)$; tangga menanjak yang tingginya "
                                    "menyatakan peluang yang sudah terkumpul sampai $x$ "
                                    "(\\emph{cumulative distribution function})."),
    "fungsi konveks": ("Fungsi konveks",
                       "fungsi yang grafiknya selalu di bawah tali penghubung dua titiknya; setiap "
                       "minimum lokalnya adalah minimum global (\\emph{convex function})."),
    "fungsi Lyapunov": ("Fungsi Lyapunov",
                        "fungsi bernilai positif yang menurun sepanjang lintasan sistem; "
                        "keberadaannya membuktikan kestabilan tanpa menyelesaikan persamaannya "
                        "(\\emph{Lyapunov function})."),
    "fungsi phi": ("Fungsi phi",
                   "fungsi $\\varphi(n)$: banyaknya bilangan antara $1$ dan $n$ yang saling prima "
                   "dengan $n$ (\\emph{Euler totient function})."),
    "galat baku": ("Galat baku",
                   "simpangan baku penaksir, bukan simpangan baku data; ia mengukur goyangan satu "
                   "tebakan (\\emph{standard error})."),
    "galat pemotongan": ("Galat pemotongan",
                        "selisih yang muncul karena proses tak hingga diganti potongan berhingga "
                        "(\\emph{truncation error})."),
    "generalisasi": ("Generalisasi",
                     "kemampuan mengerjakan soal yang belum pernah dilihat, bukan soal yang sudah "
                     "dihafal (\\emph{generalization})."),
    "gradien dikaburkan": ("Gradien dikaburkan",
                           "gradien yang diberikan kepada penyerang tidak menunjuk arah yang benar, "
                           "biasanya karena ada potongan tak terdiferensiasi atau acak "
                           "(\\emph{obfuscated gradient})."),
    "harapan": ("Harapan",
                "nilai harapan $\\mathbb{E}[X]$: rata-rata berbobot peluang, titik tumpu sebaran "
                "(\\emph{expectation})."),
    "hasilkali dalam": ("Hasilkali dalam",
                        "pemetaan dua vektor ke satu skalar yang mengukur panjang dan sudut; di "
                        "$\\mathbb{R}^n$ nilainya $\\langle \\mathbf{x},\\mathbf{y}\\rangle="
                        "\\mathbf{x}^{\\top}\\mathbf{y}$ (\\emph{inner product})."),
    "himpunan kuasa": ("Himpunan kuasa",
                       "himpunan semua himpunan bagian, termasuk himpunan kosong dan himpunan itu "
                       "sendiri; kardinalitasnya $2^n$ (\\emph{power set})."),
    "hukum bilangan besar": ("Hukum bilangan besar",
                            "janji bahwa rata-rata banyak pengamatan menempel ke rata-rata "
                            "sebenarnya, dengan peluang meleset yang mengecil "
                            "(\\emph{law of large numbers})."),
    "implikasi": ("Implikasi",
                  "pernyataan berbentuk jika $P$ maka $Q$; ia hanya salah bila $P$ benar dan $Q$ "
                  "salah (\\emph{implication})."),
    "independen": ("Independen",
                   "dua kejadian yang tidak saling memberi kabar, $P(A\\cap B)=P(A)P(B)$; "
                   "mengetahui yang satu tidak mengubah peluang yang lain (\\emph{independent})."),
    "induksi": ("Induksi",
                "pola bukti domino: basis benar, lalu setiap kasus menjatuhkan kasus berikutnya "
                "(\\emph{induction})."),
    "induksi kuat": ("Induksi kuat",
                     "induksi yang boleh memakai seluruh kasus sebelumnya, bukan hanya kasus "
                     "terdekat (\\emph{strong induction})."),
    "integral lipat dua": ("Integral lipat dua",
                           "penjumlahan nilai pada petak-petak kecil sebuah daerah, lalu limitnya "
                           "ketika petak mengecil (\\emph{double integral})."),
    "interval wilson": ("Interval Wilson",
                        "selang kepercayaan proporsi yang dicari dengan membalik uji, sehingga "
                        "tetap masuk akal ketika proporsi mendekati nol atau satu "
                        "(\\emph{Wilson interval})."),
    "inti": ("Inti",
             "lihat kernel: himpunan semua vektor yang dipetakan ke nol oleh transformasi linear "
             "(\\emph{kernel, null space})."),
    "invers modular": ("Invers modular",
                       "bilangan $b$ sehingga $ab\\equiv 1 \\pmod n$; tombol batalkan pada "
                       "aritmetika jam (\\emph{modular inverse})."),
    "isomorfisme": ("Isomorfisme",
                    "pemetaan bijektif yang mempertahankan struktur; dua ruang yang isomorfik tidak "
                    "dapat dibedakan secara aljabar (\\emph{isomorphism})."),
    "jari-jari konvergensi": ("Jari-jari konvergensi",
                              "jarak terjauh dari pusat tempat sebuah deret pangkat masih konvergen "
                              "(\\emph{radius of convergence})."),
    "jumlah atas": ("Jumlah atas",
                    "taksiran integral yang sengaja dibesarkan, memakai nilai terbesar pada tiap "
                    "potongan (\\emph{upper sum})."),
    "jumlah langsung": ("Jumlah langsung",
                        "penjumlahan dua subruang yang hanya bertemu di vektor nol, sehingga setiap "
                        "vektor punya satu cara penulisan (\\emph{direct sum})."),
    "kalibrasi": ("Kalibrasi",
                  "kesesuaian antara angka yang dijanjikan model dan frekuensi kenyataan pada "
                  "kelompok yang dijanjikan sama (\\emph{calibration})."),
    "kelas sisa": ("Kelas sisa",
                   "himpunan bilangan yang memberi sisa sama saat dibagi $n$, seperti pukul tiga "
                   "pagi dan pukul tiga sore (\\emph{residue class})."),
    "keterintegralan": ("Keterintegralan",
                        "sifat fungsi yang jumlah atas dan bawahnya dapat dirapatkan sampai "
                        "selisihnya hilang, disebut keterintegralan Riemann "
                        "(\\emph{Riemann integrability})."),
    "ketunggalan": ("Ketunggalan",
                    "jaminan bahwa satu keadaan awal hanya melahirkan satu lintasan solusi "
                    "(\\emph{uniqueness})."),
    "koefisien determinasi": ("Koefisien determinasi",
                              "bagian variasi yang dijelaskan model, dinyatakan sebagai pecahan "
                              "dari keseluruhan; ditulis $R^2$ "
                              "(\\emph{coefficient of determination})."),
    "kombinasi": ("Kombinasi",
                  "pilihan beberapa anggota tanpa memperhatikan urutannya; banyaknya $\\binom{n}{k}$ "
                  "(\\emph{combination})."),
    "kompak": ("Kompak",
               "himpunan tertutup dan terbatas; setiap barisan di dalamnya punya subbarisan yang "
               "konvergen di dalam himpunan itu (\\emph{compact})."),
    "kontinu": ("Kontinu",
                "fungsi yang grafiknya dapat digambar tanpa mengangkat pena di titik itu, yaitu "
                "$\\lim_{x\\to c}f(x)=f(c)$ (\\emph{continuous})."),
    "konvergensi dalam distribusi": ("Konvergensi dalam distribusi",
                                     "fungsi distribusinya menuju fungsi distribusi batas di setiap "
                                     "titik kontinuitas; yang menyerupai adalah bentuk sebarannya, "
                                     "bukan nilainya (\\emph{convergence in distribution})."),
    "konvergensi dalam peluang": ("Konvergensi dalam peluang",
                                  "$P(|X_n-X|>\\varepsilon)\\to 0$ untuk setiap $\\varepsilon>0$ "
                                  "(\\emph{convergence in probability})."),
    "konvergensi mutlak": ("Konvergensi mutlak",
                           "deret yang tetap konvergen ketika semua sukunya dipaksa menjadi positif "
                           "(\\emph{absolute convergence})."),
    "konvergensi seragam": ("Konvergensi seragam",
                            "lihat kekonvergenan seragam: satu laju untuk seluruh domain, bukan satu "
                            "jadwal per titik (\\emph{uniform convergence})."),
    "koordinat": ("Koordinat",
                  "daftar koefisien yang menyatakan sebuah vektor dalam suatu basis; disebut juga "
                  "vektor koordinat (\\emph{coordinate vector})."),
    "kovarians": ("Kovarians",
                  "lihat kovariansi: ukuran dua besaran bergerak bersama, dihitung dari hasil kali "
                  "simpangan keduanya (\\emph{covariance})."),
    "kuadrat terkecil": ("Kuadrat terkecil",
                         "pemilihan parameter yang meminimumkan jumlah kuadrat sisa ketika tidak ada "
                         "solusi eksak (\\emph{least squares})."),
    "kuantisasi": ("Kuantisasi",
                   "penggantian setiap nilai dengan kelipatan terdekat dari jarak tetap; hasilnya "
                   "fungsi tangga yang turunannya nol hampir di mana-mana (\\emph{quantization})."),
    "kuantor": ("Kuantor",
                "penanda untuk semua ($\\forall$) atau ada ($\\exists$); urutan pemakaiannya "
                "mengubah arti pernyataan (\\emph{quantifier})."),
    "lapangan": ("Lapangan",
                 "himpunan dengan dua operasi yang tertutup, punya identitas dan invers, dan "
                 "memenuhi hukum distributif (\\emph{field})."),
    "lapangan terurut": ("Lapangan terurut",
                         "lapangan yang anggotanya dapat diurutkan dan aturan hitungnya menghormati "
                         "urutan itu (\\emph{ordered field})."),
    "lapisan tersembunyi": ("Lapisan tersembunyi",
                            "lapisan unit yang tidak bersentuhan langsung dengan masukan maupun "
                            "keluaran jaringan (\\emph{hidden layer})."),
    "limit fungsi": ("Limit fungsi",
                     "$f(x)$ dapat dipaksa sedekat apa pun ke $L$ asalkan $x$ cukup dekat ke $c$ "
                     "tetapi tidak sama dengan $c$ (\\emph{functional limit})."),
    "limit superior": ("Limit superior",
                       "nilai terbesar yang masih dikunjungi barisan sesering apa pun di ujungnya, "
                       "ditulis $\\limsup_{n\\to\\infty}a_n$ (\\emph{upper limit})."),
    "matriks elementer": ("Matriks elementer",
                          "matriks identitas yang sudah dikenai satu operasi baris, sehingga menjadi "
                          "catatan operasi itu (\\emph{elementary matrix})."),
    "metode tanda gradien": ("Metode tanda gradien",
                             "serangan satu langkah (FGSM) yang menggeser setiap koordinat sebesar "
                             "anggaran, arahnya mengikuti tanda turunan kerugian "
                             "(\\emph{fast gradient sign method})."),
    "model ancaman": ("Model ancaman",
                      "daftar lengkap kemampuan penyerang: besar gangguannya, apa yang ia ketahui, "
                      "dan apa tujuannya (\\emph{threat model})."),
    "multiplisitas": ("Multiplisitas",
                      "banyaknya kemunculan sebuah nilai eigen sebagai akar polinomial "
                      "karakteristik, yang tidak selalu sama dengan dimensi ruang eigennya "
                      "(\\emph{multiplicity})."),
    "nids": ("NIDS",
             "sistem yang memantau lalu lintas jaringan dan memutuskan apakah suatu aliran paket "
             "merupakan serangan (\\emph{network intrusion detection system})."),
    "nilai mutlak": ("Nilai mutlak",
                     "jarak sebuah bilangan ke nol pada garis bilangan, tanpa memedulikan tandanya "
                     "(\\emph{absolute value})."),
    "orientasi": ("Orientasi",
                  "kesepakatan tentang arah putar mana yang dihitung positif; membaliknya membalik "
                  "tanda integral (\\emph{orientation})."),
    "peluang": ("Peluang",
                "bobot pada setiap kemungkinan, tak negatif dan berjumlah satu "
                "(\\emph{probability})."),
    "pembatalan katastrofik": ("Pembatalan katastrofik",
                               "hilangnya digit berarti ketika dua bilangan hampir sama dikurangkan, "
                               "sehingga yang tersisa hanya galat "
                               "(\\emph{catastrophic cancellation})."),
    "penaksir": ("Penaksir",
                 "aturan yang mengubah sampel menjadi tebakan parameter; tebakan yang dihasilkan "
                 "disebut nilai dugaan (\\emph{estimator})."),
    "penghubung logika": ("Penghubung logika",
                          "operasi yang menggabungkan pernyataan: dan, atau, tidak, jika-maka, "
                          "jika-dan-hanya-jika (\\emph{logical connective})."),
    "persamaan diferensial": ("Persamaan diferensial",
                              "kalimat yang mengikat laju perubahan sebuah besaran dengan besar "
                              "besaran itu sendiri (\\emph{differential equation})."),
    "plateau tandus": ("Plateau tandus",
                       "daerah pada lanskap kerugian sirkuit variasional tempat gradien mengecil "
                       "secara eksponensial terhadap jumlah qubit (\\emph{barren plateau})."),
    "polinomial karakteristik": ("Polinomial karakteristik",
                                 "$\\det(A-\\lambda I)$; akar-akarnya adalah nilai eigen $A$ "
                                 "(\\emph{characteristic polynomial})."),
    "program linear": ("Program linear",
                       "masalah memaksimumkan atau meminimumkan fungsi linear dengan kendala linear "
                       "(\\emph{linear program})."),
    "proposisi": ("Proposisi",
                  "kalimat yang bernilai benar atau salah, bukan pertanyaan atau perintah; dalam "
                  "buku ini juga nama lingkungan teorema (\\emph{proposition})."),
    "proyeksi": ("Proyeksi",
                 "titik pada subruang yang paling dekat dengan sebuah vektor, yaitu bayangan tegak "
                 "lurusnya (\\emph{projection})."),
    "pseudoinvers": ("Pseudoinvers",
                     "invers tergeneralisasi $A^{+}$ yang tetap bekerja ketika sebagian arah sudah "
                     "gepeng: yang dapat dibalik dibalik, yang hilang dibiarkan "
                     "(\\emph{pseudoinverse})."),
    "rank": ("Rank",
             "banyaknya arah bebas yang masih bertahan setelah dipetakan, yaitu "
             "$\\dim\\operatorname{im}T$ (\\emph{rank})."),
    "rasio peluang": ("Rasio peluang",
                      "perbandingan peluang berhasil dan gagal; eksponensial koefisien regresi "
                      "logistik menyatakan berapa kali rasio itu berlipat per satuan "
                      "(\\emph{odds ratio})."),
    "regresi": ("Regresi",
                "menarik fungsi yang paling dekat ke semua titik, bukan fungsi yang melewati "
                "semuanya (\\emph{regression})."),
    "ruang eigen": ("Ruang eigen",
                    "seluruh vektor eigen untuk satu nilai eigen beserta vektor nol; ia sebuah "
                    "subruang (\\emph{eigenspace})."),
    "ruang masalah": ("Ruang masalah",
                      "ruang objek nyata yang boleh diubah penyerang, misalnya paket dan waktu; "
                      "berbeda dari ruang fitur tempat model bekerja (\\emph{problem space})."),
    "ruang vektor": ("Ruang vektor",
                     "himpunan dengan penjumlahan dan perkalian skalar yang tertutup dan memenuhi "
                     "delapan aksioma (\\emph{vector space})."),
    "selang prediksi": ("Selang prediksi",
                        "selang bagi satu pengamatan yang belum terjadi; selalu lebih lebar daripada "
                        "selang bagi rata-rata (\\emph{prediction interval})."),
    "sensitivitas global": ("Sensitivitas global",
                            "pergeseran terbesar jawaban sebuah kueri yang dapat disebabkan satu "
                            "orang pada kasus terburuk (\\emph{global sensitivity})."),
    "serangan adaptif": ("Serangan adaptif",
                         "serangan yang dirancang dengan mengetahui pertahanan yang sedang diuji, "
                         "termasuk mengetahui bahwa gradiennya dimanipulasi "
                         "(\\emph{adaptive attack})."),
    "serupa": ("Serupa",
               "dua matriks yang menyatakan pemetaan linear yang sama dalam dua basis berbeda, "
               "$B=P^{-1}AP$ (\\emph{similar})."),
    "softmax": ("Softmax",
                "pemetaan deretan skor menjadi peluang yang berjumlah satu, "
                "$e^{z_i}/\\sum_j e^{z_j}$ (\\emph{softmax})."),
    "solusi layak basis": ("Solusi layak basis",
                           "titik yang diperoleh dengan menyetel sebagian peubah ke nol lalu "
                           "menyelesaikan sisanya, dan masih memenuhi semua kendala "
                           "(\\emph{basic feasible solution})."),
    "sorry": ("Sorry",
              "penanda Lean~4 bahwa sebuah bukti ditangguhkan; mesin menerimanya tetapi "
              "mencatatnya sebagai aksioma (\\emph{sorry})."),
    "stabil asimtotik": ("Stabil asimtotik",
                         "tetap dekat setelah diganggu, lalu benar-benar kembali ke titik setimbang "
                         "(\\emph{asymptotically stable})."),
    "subbarisan": ("Subbarisan",
                   "barisan yang diperoleh dengan membuang sebagian suku tanpa mengubah urutan "
                   "sisa sukunya (\\emph{subsequence})."),
    "subruang": ("Subruang",
                 "himpunan bagian ruang vektor yang tertutup terhadap penjumlahan dan perkalian "
                 "skalar (\\emph{subspace})."),
    "susunan ulang": ("Susunan ulang",
                      "penukaran urutan suku deret; pada deret yang konvergen mutlak jumlahnya "
                      "tidak berubah, pada deret yang tidak, jumlahnya dapat berubah "
                      "(\\emph{rearrangement})."),
    "syarat perlu": ("Syarat perlu",
                     "syarat yang harus dipenuhi agar pernyataan benar; tanpanya mustahil, tetapi "
                     "memenuhinya belum cukup (\\emph{necessary condition})."),
    "taktik": ("Taktik",
               "perintah langkah demi langkah dalam Lean~4 yang mengubah sasaran pembuktian "
               "(\\emph{tactic})."),
    "tanda tangan digital": ("Tanda tangan digital",
                             "nilai yang hanya dapat dibuat pemegang kunci privat tetapi dapat "
                             "diperiksa siapa pun dengan kunci publik "
                             "(\\emph{digital signature})."),
    "terhitung": ("Terhitung",
                  "himpunan yang anggotanya dapat dinomori tanpa ada yang terlewat; $\\mathbb{Q}$ "
                  "terhitung, $\\mathbb{R}$ tidak (\\emph{countable})."),
    "term bukti": ("Term bukti",
                   "ungkapan yang sekaligus menjadi bukti dan menjadi nilai; memeriksa bukti sama "
                   "dengan memeriksa tipe (\\emph{proof term})."),
    "transferabilitas": ("Transferabilitas",
                         "sifat contoh adversarial yang dibuat untuk satu model tetapi juga menipu "
                         "model lain yang dilatih terpisah (\\emph{transferability})."),
    "turunan": ("Turunan",
                "limit hasil bagi selisih; kemiringan garis singgung sekaligus laju perubahan "
                "sesaat (\\emph{derivative})."),
    "typeclass": ("Typeclass",
                  "daftar kemampuan yang harus dimiliki sebuah tipe agar dapat dipakai di tempat "
                  "tertentu (\\emph{type class})."),
    "uji rasio": ("Uji rasio",
                  "deret konvergen mutlak bila $\\lim|a_{n+1}/a_n|<1$, dan divergen bila limit itu "
                  "lebih besar dari satu (\\emph{ratio test})."),
    "ulp": ("ULP",
            "satuan di tempat terakhir: satu langkah terkecil yang dapat dibedakan mesin pada skala "
            "sebuah bilangan (\\emph{unit in the last place})."),
    "uniter": ("Uniter",
               "matriks yang mempertahankan hasilkali dalam, $U^{*}U=I$; versi kompleks dari "
               "matriks ortogonal (\\emph{unitary})."),
    "validasi silang bersarang": ("Validasi silang bersarang",
                                  "dua lapis lipatan: lapisan luar menilai, lapisan dalam memilih, "
                                  "sehingga pemilihan model tidak membocorkan data uji "
                                  "(\\emph{nested cross-validation})."),
    "variabel kendur": ("Variabel kendur",
                        "peubah tambahan yang mencatat sisa pemakaian, sehingga kendala tidak lebih "
                        "dari berubah menjadi persamaan (\\emph{slack variable})."),
    "varians inflasi": ("Varians inflasi",
                        "seberapa banyak variansi sebuah koefisien digelembungkan oleh penjelas lain "
                        "yang membawa informasi serupa; disingkat VIF "
                        "(\\emph{variance inflation factor})."),
    "sistem floating-point": ("Sistem floating-point",
                              "notasi ilmiah biner dengan jumlah digit tetap; bilangan disimpan "
                              "sebagai tanda, pangkat, dan mantissa, sehingga jarak antar bilangan "
                              "yang dapat diwakili tidak seragam: rapat di dekat nol, renggang di "
                              "ujung atas, dan dua bilangan berbeda dapat jatuh ke tempat yang sama "
                              "(\\emph{floating-point system})."),
    "verteks": ("Verteks",
                "sudut daerah layak, yaitu titik yang tidak pernah menjadi titik tengah antara dua "
                "titik layak lain (\\emph{vertex})."),
}


# ------------------------------------------------------------------ engine
def baca_entri() -> dict[str, tuple[str, str]]:
    """Entries already in main.tex: {normal key: (label, definition)}."""
    teks = open(MAIN, encoding="utf-8").read()
    awal = teks.find(AWAL)
    akhir = teks.find(AKHIR)
    blok = teks[awal:akhir]
    isi = blok[blok.find("\\begin{description}"):blok.rfind("\\end{description}")]
    hasil = {}
    potong = re.split(r"\n(?=  \\item\[)", isi)
    for p in potong:
        m = re.match(r"\s*\\item\[([^\]]*)\]\s*(.*)", p, re.S)
        if not m:
            continue
        label = m.group(1).strip()
        badan = " ".join(m.group(2).split())
        hasil[normal(label)] = (label, badan)
    return hasil


def daftar_kamus() -> dict[str, str]:
    """{normal term: file name} for every \\kamus in the chapters."""
    out = {}
    for p in sorted(glob.glob(os.path.join(HERE, "ch*.tex"))):
        teks = open(p, encoding="utf-8").read()
        for m in re.finditer(r"\\kamus(?=\{)", teks):
            istilah, _ = arg(teks, m.end())
            if istilah.strip():
                out.setdefault(normal(istilah), os.path.basename(p))
    return out


def gabung() -> dict[str, tuple[str, str]]:
    entri = baca_entri()
    for kunci, (label, badan) in BARU.items():
        entri.setdefault(normal(kunci), (label, badan))
    # BARU keys are \kamus terms, old entry keys are labels; the two can
    # meet at one label (e.g. the term "sistem floating-point" -> the same label),
    # so drop duplicates by label and keep the definition from main.tex.
    unik: dict[str, tuple[str, str]] = {}
    for label, badan in entri.values():
        unik.setdefault(label.casefold(), (label, badan))
    return {k: v for k, v in unik.items()}


def tulis() -> int:
    teks = open(MAIN, encoding="utf-8").read()
    awal = teks.find(AWAL)
    akhir = teks.find(AKHIR)
    if awal < 0 or akhir < 0:
        print("GAGAL: blok glosarium tidak ditemukan di main.tex")
        return 1
    entri = gabung()
    urut = sorted(entri.values(), key=lambda e: (e[0].casefold(), e[0]))
    baris = ["\\begin{description}[style=nextline,itemsep=0.35em]"]
    baris += ["  \\item[%s] %s" % (label, badan) for label, badan in urut]
    baris.append("\\end{description}")
    blok = "\n".join(baris) + "\n\n"
    kepala = teks[awal:]
    mulai = kepala.find("\\begin{description}")
    selesai = kepala.find("\\end{description}") + len("\\end{description}")
    baru = teks[:awal + mulai] + blok + teks[awal + selesai:].lstrip("\n")
    if baru != teks:
        open(MAIN, "w", encoding="utf-8").write(baru)
    print(f"glosarium: {len(entri)} entri ditulis ke main.tex")
    return 0


def cek() -> int:
    entri = baca_entri()
    kamus = daftar_kamus()
    kurang = sorted(k for k in kamus if k not in entri)
    print(f"istilah \\kamus: {len(kamus)}   entri glosarium: {len(entri)}   "
          f"belum ada: {len(kurang)}")
    for k in kurang:
        print(f"  {k}  ({kamus[k]})")
    return 1 if kurang else 0


def daftar() -> int:
    for kunci, (label, badan) in sorted(BARU.items()):
        print(f"{kunci:32s} -> {label}")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "cek"
    sys.exit({"tulis": tulis, "cek": cek, "daftar": daftar}[mode]())
