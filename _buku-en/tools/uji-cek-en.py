#!/usr/bin/env python3
"""Verifikasi ad-hoc (bukan suite kanonik) untuk _buku-en/tools/cek-en.py + preamble-en.tex.

Yang dibuktikan:
  A. gate menerima bab Inggris yang setia struktur (exit 0);
  B. gate menangkap empat kerusakan nyata: section hilang, label berubah,
     prosa tak diterjemahkan, dan bab yang diringkas;
  C. preamble-en.tex benar-benar dapat dikompilasi (cek-en.py --pdf) memakai
     lingkungan kotak, \\kamus, \\tingkat, lab/verbatim, latihan, dan TikZ.

Jalankan: python3 tools/uji-cek-en.py   (dari _buku-en/, ~20 detik, butuh pdflatex)
"""
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(TOOLS, "cek-en.py")
PRE = os.path.join(os.path.dirname(TOOLS), "preamble-en.tex")
gagal = []

ID_SRC = r"""\chapter{Kenapa Mesin Bisa Salah}
\peta{Bab 1 pada \emph{Understanding Analysis} (Abbott), Bagian 1.1.}
\section{Satu}\tingkat{dasar}
\begin{untukanak}Analogi sederhana tentang kisi dan garis lurus yang tidak berubah bentuk ketika dipetakan oleh fungsi linear apa pun yang dapat dibalik.\end{untukanak}
\begin{teorema}Setiap bilangan genap ditambah dua tetap bilangan genap, dan klaim ini berlaku untuk semua bilangan bulat tanpa kecuali.\end{teorema}
\kamus{verteks}{vertex}{sudut daerah layak, yaitu titik yang tidak pernah menjadi titik tengah antara dua titik layak lain.}
Di dalam kotak itu berlaku $a^2+b^2=c^2$ dan batasnya $|x|<\delta$ dengan peran $\text{tetap}$.
\index{verteks}
\begin{figure}[htbp]\centering
\begin{tikzpicture}\draw (0,0) rectangle (1,1);\end{tikzpicture}
\caption{Kisi uji untuk memeriksa pemetaan linear.}\label{fig:kisi}
\end{figure}
Gambar~\ref{fig:kisi} menunjukkan kisi itu dan menjelaskan mengapa potongan garis lurus tetap lurus setelah dipetakan oleh fungsi linear yang sama, sehingga kisi tetap kisi dan sel tetap sel.\index{kisi}
\section{Dua}\tingkat{lanjut}
\begin{latihan}\begin{enumerate}\item Hitung jumlah seluruh sel pada kisi berukuran tiga kali empat.\item Buktikan bahwa jumlah itu tidak berubah setelah dipetakan.\end{enumerate}\end{latihan}
\begin{lab}
\begin{verbatim}
print(1+1)
\end{verbatim}
\end{lab}
"""

EN_SRC = r"""\chapter{Why Machines Can Be Wrong}
\peta{Chapter 1 of \emph{Understanding Analysis} (Abbott), Section 1.1.}
\section{One}\tingkat{basic}
\begin{untukanak}A simple analogy about a grid and straight lines that keep their shape when mapped by any invertible linear function at all.\end{untukanak}
\begin{teorema}Every even number plus two is still an even number, and this claim holds for all integers without exception.\end{teorema}
\kamus{vertex}{verteks}{a corner of the feasible region, that is, a point that is never the midpoint between two other feasible points.}
Inside that box, $a^2+b^2=c^2$ holds and the bound is $|x|<\delta$ with role $\text{fixed}$.
\index{vertex}
\begin{figure}[htbp]\centering
\begin{tikzpicture}\draw (0,0) rectangle (1,1);\end{tikzpicture}
\caption{Test grid used to check a linear map.}\label{fig:kisi}
\end{figure}
Figure~\ref{fig:kisi} shows that grid and explains why a piece of a straight line stays straight after it is mapped by the same linear function, so the grid stays a grid and a cell stays a cell.\index{grid}
\section{Two}\tingkat{advanced}
\begin{latihan}\begin{enumerate}\item Count every cell of a grid that is three cells wide and four cells tall.\item Prove that the count does not change after the map is applied.\end{enumerate}\end{latihan}
\begin{lab}
\begin{verbatim}
print(1+1)
\end{verbatim}
\end{lab}
"""

MAIN = r"""\input{preamble-en.tex}
\begin{document}
\frontmatter
\tableofcontents
\mainmatter
\input{ch01}
\backmatter
\printindex
\end{document}
"""


def cek(nama, lulus, detail=""):
    print(("PASS " if lulus else "FAIL ") + nama + ("" if lulus else f"  <- {detail}"))
    if not lulus:
        gagal.append(nama)


tmp = tempfile.mkdtemp(prefix="hermes-verify-en-", dir=os.environ.get("TMPDIR", "/tmp"))
try:
    id_d = os.path.join(tmp, "_buku-ed2")
    en_d = os.path.join(tmp, "_buku-en")
    os.makedirs(os.path.join(en_d, "tools"))
    os.makedirs(id_d)
    shutil.copy(SCRIPT, os.path.join(en_d, "tools", "cek-en.py"))
    shutil.copy(PRE, os.path.join(en_d, "preamble-en.tex"))
    open(os.path.join(id_d, "ch01.tex"), "w", encoding="utf-8").write(ID_SRC)
    en_ch = os.path.join(en_d, "ch01.tex")
    open(en_ch, "w", encoding="utf-8").write(EN_SRC)
    open(os.path.join(en_d, "main-en.tex"), "w", encoding="utf-8").write(MAIN)

    def gate(*args):
        r = subprocess.run([sys.executable, os.path.join(en_d, "tools", "cek-en.py"), *args],
                           capture_output=True, text=True, cwd=en_d)
        return r.returncode, r.stdout + r.stderr

    # A. bab setia struktur
    rc, out = gate("ch01")
    cek("A1 bab setia -> exit 0", rc == 0, out.strip()[-200:])
    cek("A2 keluaran memuat 'OK ch01'", re.search(r"^OK\s+ch01$", out, re.M) is not None, out.strip()[-120:])

    def rusak(nama, ubah, penanda):
        isi = ubah(EN_SRC)
        open(en_ch, "w", encoding="utf-8").write(isi)
        rc, out = gate("ch01")
        cek(nama, rc == 1 and penanda in out, out.strip()[-160:])

    rusak("B1 section hilang ditangkap",
          lambda s: s.replace(r"\section{Two}", "", 1), "section EN=1 ID=2")
    rusak("B2 label berubah ditangkap",
          lambda s: s.replace("fig:kisi", "fig:kisi-baru").replace(r"\label{fig:kisi-baru}", r"\label{fig:kisi-baru}", 1),
          "label beda")
    rusak("B3 prosa tak diterjemahkan ditangkap",
          lambda s: re.sub(r"(Figure~\\ref\{fig:kisi\} shows).*?(cell\.)",
                           r"\1 kisi itu dan menjelaskan mengapa potongan garis lurus tetap lurus setelah "
                           r"dipetakan oleh fungsi linear yang sama sehingga kisi tetap kisi dan sel tetap sel\2", s, flags=re.S),
          "sisa kata Indonesia")
    def ringkas(s: str) -> str:
        s = re.sub(r"(analogy about a grid).*?(linear function at all\.)", r"\1.\2", s, flags=re.S)
        s = re.sub(r"(still an even number,).*?(without exception\.)", r"\1 indeed.\2", s, flags=re.S)
        s = re.sub(r"(shows that grid).*?(cell stays a cell\.)", r"\1.\2", s, flags=re.S)
        return re.sub(r"(vertex}{verteks}{).*?(feasible points\.)", r"\1a corner.\2", s, flags=re.S)

    rusak("B5 matematika diubah ditangkap",
          lambda s: s.replace("a^2+b^2=c^2", "a^2+b^2=c^3", 1), "matematika beda")
    rusak("B4 bab diringkas ditangkap", ringkas, "rasio kata")

    # C. preamble + rakitan benar-benar dikompilasi
    open(en_ch, "w", encoding="utf-8").write(EN_SRC)
    rc, out = gate("--pdf")
    cek("C1 preamble kompilasi + rakitan bersih", rc == 0 and "OK rakitan EN" in out, out.strip()[-200:])
    cek("C2 PDF contoh tercipta", os.path.exists(os.path.join(en_d, "main-en.pdf")))

    # E. penangkal header bocor: \chaptermark yang ditulis di dalam satu berkas bab
    # berlaku global, jadi teks header harus dicocokkan dengan judul babnya.
    spec = importlib.util.spec_from_file_location("gerbang", os.path.join(en_d, "tools", "cek-en.py"))
    gerbang = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gerbang)
    judul = {5: "Infinite Series", 6: "Vector Spaces and Subspaces"}
    bocor = gerbang.header_salah("CHAPTER 5. RIEMANN INTEGRALS\nCHAPTER 6. VECTOR SPACES AND SUBSPACES\n", judul)
    cek("E1 header bocor dari bab lain ditangkap", len(bocor) == 1 and bocor[0][0] == 5, bocor)
    bersih = gerbang.header_salah("CHAPTER 5. INFINITE SERIES\nCHAPTER 6. VECTOR SPACES AND SUBSPACES\n", judul)
    cek("E2 header yang benar tidak dituduh", bersih == [], bersih)
    pendek = gerbang.header_salah("CHAPTER 5. INFINITE SERIES\n", {5: "Infinite Series and Convergence Tests"})
    cek("E3 header yang dipendekkan tetap sah", pendek == [], pendek)

    # F. dua jebakan pembaca LaTeX yang pernah membuat gerbang salah menuduh:
    # "%" yang di-escape bukan komentar, dan "[3pt]" setelah "\\" hanya pindah baris.
    m1 = gerbang.matematika("awal $95\\%$ lalu $x^2$")
    cek("F1 persen ter-escape tidak memotong sisa baris", m1.get("$x^2$") == 1 and m1.get("$95\\%$") == 1, dict(m1))
    m2 = gerbang.matematika("\\node{a\\\\[3pt] b $y^2$};")
    cek("F2 baris TikZ bukan pembuka matematika display",
        m2.get("$y^2$") == 1 and not any("3pt" in k for k in m2), dict(m2))
    k1 = gerbang.kata("satu dua $x$ % komentar tiga")
    cek("F3 komentar tetap dibuang saat menghitung kata", k1 == 3, k1)
finally:
    shutil.rmtree(tmp, ignore_errors=True)
    cek("D1 sandbox dibersihkan", not os.path.exists(tmp))

print("\nsemua cek ad-hoc lulus" if not gagal else f"\n{len(gagal)} gagal: {gagal}")
sys.exit(1 if gagal else 0)
