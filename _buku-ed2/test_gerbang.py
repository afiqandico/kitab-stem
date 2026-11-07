#!/usr/bin/env python3
"""Second-edition skeleton test: quality gates + main.tex compilation.

Tests `build_ed2.py` with a `tempfile` sandbox, not the real manuscript:
positive control (28 test chapters pass), negative control per gate, then
compilation of `main.tex` (pdflatex + makeindex) all the way to PDF.

Usage:  python3 test_gerbang.py      -> exit 0 when every check passes
"""
from __future__ import annotations
import os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

# A TEXINPUTS exported in the shell can pull files from the repo into the sandbox:
# the "sandbox" test then silently tests the real book, and the overfull gate becomes invalid.
# Every test subprocess runs without that variable.
ENV = {k: v for k, v in os.environ.items() if k != "TEXINPUTS"}
FILL = ("Kita menuliskan prosa uji yang cukup panjang agar penghitung kata badan "
        "mencapai ambang gerbang mutu dan tidak dianggap pendek oleh pemeriksa. ") * 260
IDX = "".join(r"\index{istilah%d}" % i for i in range(8))

FIG = r"""Lihat Gambar~\ref{fig:uji-a} dan Gambar~\ref{fig:uji-b}.
\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.5]
  \draw[->] (-2.4,0)--(2.4,0);
  \draw[->] (0,-1.4)--(0,1.4);
  \draw[thick,accent] (0,0) circle (1);
\end{tikzpicture}
\caption{Uji gambar pertama: lingkaran satuan.}
\label{fig:uji-a}
\end{figure}
\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.5]
  \draw[fill=teal!20] (0,0) rectangle (2,1);
\end{tikzpicture}
\caption{Uji gambar kedua: kotak satuan.}
\label{fig:uji-b}
\end{figure}"""
STUB = r"""\chapter{Bab Uji %(n)d}
%(fill)s
\begin{untukanak}Analogi benda sehari-hari tanpa notasi.\end{untukanak}
\begin{untukanak}Analogi kedua untuk pembaca muda.\end{untukanak}
\section{Satu}\tingkat{dasar}
\begin{definisi}Uji definisi.\end{definisi}
\begin{teorema}Uji teorema.\end{teorema}
\begin{proof}Bukti singkat.\end{proof}
\begin{equation}
\begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix}
\end{equation}
\begin{lemma}Uji lemma.\end{lemma}
\begin{proposisi}Uji proposisi.\end{proposisi}%(idx)s
\kamus{Basis}{basis}{analogi}\kamus{Deret}{series}{analogi}\kamus{Supremum}{supremum}{analogi}
\section{Dua}\tingkat{menengah}
\begin{contoh}Uji contoh.\end{contoh}
\begin{bacakeras}Bacakan naskah pendek ini. dua, tiga.\end{bacakeras}
\begin{tangan}Ambil lima kartu, susun jadi baris.\end{tangan}
\begin{resep}\begin{enumerate}\item Satu\item Dua\item Tiga\end{enumerate}\end{resep}
\begin{tantangan}Buktikan atau bantah klaim ini; petunjuk bertingkat.\end{tantangan}
%(fig)s
\section{Contoh hitung}\tingkat{menengah}
\kertas{Kerjakan di kertas.}
\section{Lab komputasi}\tingkat{lanjut}
\begin{lab}
\begin{verbatim}
print(1+1)
\end{verbatim}
\end{lab}
\begin{untukdosen}Urutan mengajar dan miskonsepsi.\end{untukdosen}
\section{Tiga}\tingkat{dasar}
\section{Ringkasan}
\begin{ringkasan}Empat butir ringkas.\end{ringkasan}
\section{Latihan}
\begin{latihan}
\begin{enumerate}
\item Satu\item Dua\item Tiga\item Empat\item Lima\item Enam\item Tujuh\item Delapan
\end{enumerate}
\end{latihan}
\begin{untukpeneliti}Batas klaim dan pertanyaan terbuka.\end{untukpeneliti}
\peta{Bab 1 pada kitab uji.}
""" % {"n": 0, "fill": FILL, "idx": IDX, "fig": FIG}


sys.path.insert(0, HERE)
import build_ed2  # noqa: E402


def judul_peta() -> dict[int, str]:
    """Chapter titles according to the map table in main.tex — one source: build_ed2."""
    return build_ed2.judul_peta()


JUDUL = judul_peta()


def stub(n: int) -> str:
    judul = JUDUL.get(n, f"Bab Uji {n}")
    chap = (f"\\chapter[Ringkas {n}]{{{judul}}}" if len(judul) > 55
            else f"\\chapter{{{judul}}}")
    s = STUB.replace("\\chapter{Bab Uji 0}", chap)
    # figure labels must be unique across chapters: pdf() rejects duplicate labels in the build,
    # and the sandbox copies 32 chapters, so the chapter-number suffix is mandatory.
    for lab in ("fig:uji-a", "fig:uji-b"):
        s = s.replace("{" + lab + "}", "{" + lab + f"-{n:02d}" + "}")
    return s


CHECKS: list[tuple[str, bool, str]] = []


def ok(nama: str, lulus: bool, detail: str = "") -> None:
    CHECKS.append((nama, bool(lulus), detail))


def check_gerbang(d: str) -> tuple[int, str]:
    r = subprocess.run([sys.executable, "build_ed2.py", "check"], cwd=d,
                       capture_output=True, text=True, env=ENV)
    return r.returncode, r.stdout + r.stderr


def main() -> int:
    tmp = tempfile.mkdtemp(prefix="hermes-verify-ed2-frame-")
    try:
        d = os.path.join(tmp, "buku")
        os.makedirs(d)
        shutil.copy(os.path.join(HERE, "build_ed2.py"), d)
        shutil.copy(os.path.join(HERE, "main.tex"), d)
        # the answer-key appendix is copied too: main.tex \input's those files, and the sandbox
        # must test the real build, not a version without appendix D
        kunci = os.path.join(HERE, "lampiran-kunci")
        if os.path.isdir(kunci):
            shutil.copytree(kunci, os.path.join(d, "lampiran-kunci"))
        for n in range(1, len(build_ed2.CH) + 1):
            open(os.path.join(d, f"ch{n:02d}.tex"), "w").write(stub(n))

        rc, out = check_gerbang(d)
        ok("positif: exit 0", rc == 0, out.splitlines()[-1])
        ok("positif: tanpa bab bermasalah", "Bab ada tapi bermasalah: 0" in out, out[-160:].replace("\n", " | "))
        ok(f"positif: {len(build_ed2.CH)} baris OK", out.count("  OK") >= len(build_ed2.CH), str(out.count("  OK")))

        def negatif(bab: str, ubah, penanda: str) -> None:
            p = os.path.join(d, bab)
            asli = stub(int(bab[2:4]))
            open(p, "w").write(ubah(asli))
            rc, out = check_gerbang(d)
            ok(f"negatif: {penanda}", rc == 1 and penanda in out, out.splitlines()[-1])
            open(p, "w").write(asli)

        negatif("ch01.tex", lambda s: s.replace(r"\begin{untukdosen}", r"\begin{catatan}", 1), "untukdosen=0")
        negatif("ch02.tex", lambda s: s.replace(r"\begin{untukpeneliti}", r"\begin{catatan}", 1), "untukpeneliti=0")
        negatif("ch03.tex", lambda s: s.replace(r"\section{Tiga}\tingkat{dasar}", r"\cite{uji}", 1), "pelanggaran aturan")
        negatif("ch04.tex", lambda s: s.replace(r"\tingkat{dasar}", "", 1), "tingkat<section")
        negatif("ch05.tex", lambda s: s.replace(r"\section{", r"\subsection{"), "section<5")
        negatif("ch06.tex", lambda s: s.replace("Analogi benda sehari-hari", "Analogi \u03b5", 1), "unicode:")
        negatif("ch07.tex", lambda s: s.replace(FILL, "Pendek. ", 1), "pendek")
        negatif("ch08.tex", lambda s: s.replace(IDX, "", 1), "index<8")
        negatif("ch09.tex", lambda s: s.replace(r"\begin{verbatim}", r"\begin{quote}")
                                          .replace(r"\end{verbatim}", r"\end{quote}"), "tanpa verbatim")
        negatif("ch10.tex", lambda s: s.replace(r"\kamus{Basis}{basis}{analogi}", ""), "kamus<3")
        negatif("ch11.tex", lambda s: s.replace(r"\begin{proof}", r"\begin{longtable}", 1), "env:longtable")
        negatif("ch12.tex", lambda s: s.replace(FILL, FILL * 2, 1), "kepanjangan")
        negatif("ch13.tex", lambda s: s.replace(JUDUL[13], "Judul Yang Tidak Sama", 1),
                "tidak cocok: 1 -> ch13")
        negatif("ch15.tex", lambda s: re.sub(r"\\chapter\[[^\]]*\]", r"\\chapter", s, count=1),
                "judul-panjang")
        negatif("ch14.tex", lambda s: s.replace("print(1+1)", "x = " + "'a'" * 60, 1),
                "verbatim>184")
        gambar = (r"\begin{figure}[htbp]\caption{Uji}\label{fig:uji}"
                  "\n" r"\begin{tikzpicture}\draw (0,0)--(1,1);\end{tikzpicture}"
                  "\n" r"\end{figure}")
        negatif("ch16.tex", lambda s: s.replace(r"\kertas{", r"\begin{figure}[htbp]"
                "\n" r"\begin{tikzpicture}\draw (0,0)--(1,1);\end{tikzpicture}"
                "\n" r"\end{figure}" "\n" r"\kertas{", 1), "figure-tanpa-caption/label")
        negatif("ch17.tex", lambda s: s.replace(r"\kertas{", gambar + "\n" + r"\kertas{", 1),
                "figure-tak-dirujuk")
        FIG2 = (r"Lihat Gambar~\ref{fig:uji-c} dan Gambar~\ref{fig:uji-d}." "\n"
                r"\begin{figure}[htbp]\caption{Ketiga}\label{fig:uji-c}"
                "\n" r"\begin{tikzpicture}\draw (0,0)--(1,1);\end{tikzpicture}"
                "\n" r"\end{figure}" "\n"
                r"\begin{figure}[htbp]\caption{Keempat}\label{fig:uji-d}"
                "\n" r"\begin{tikzpicture}\draw (0,0)--(2,1);\end{tikzpicture}"
                "\n" r"\end{figure}")
        negatif("ch18.tex", lambda s: s.replace(r"\begin{bacakeras}", r"\begin{catatan}", 1),
                "bacakeras=0")
        negatif("ch19.tex", lambda s: s.replace(r"\begin{tangan}", r"\begin{catatan}", 1),
                "tangan=0")
        negatif("ch20.tex", lambda s: s.replace(r"\begin{resep}", r"\begin{catatan}", 1),
                "resep=0")
        negatif("ch21.tex", lambda s: s.replace(r"\begin{tantangan}", r"\begin{catatan}", 1),
                "tantangan=0")
        negatif("ch22.tex", lambda s: re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", "", s,
                                             count=1, flags=re.S), "gambar=1")
        negatif("ch23.tex", lambda s: s.replace(r"\kertas{", FIG2 + "\n" + r"\kertas{", 1),
                "gambar=4")
        # a \kamus term with no glossary entry must turn the check red
        negatif("ch24.tex", lambda s: s.replace(r"\kamus{Basis}", r"\kamus{Istilahbaru}", 1),
                "tanpa entri glosarium: 1")

        rc, out = check_gerbang(d)
        ok("pulih: exit 0 setelah semua mutasi", rc == 0, out.splitlines()[-1])

        # the sandbox must start from zero: log/aux left by another run can make this
        # run's pagination and overfull report untrustworthy
        for sisa in ("main.log", "main.aux", "main.toc", "main.lof", "main.idx", "main.ind"):
            if os.path.exists(os.path.join(d, sisa)):
                os.remove(os.path.join(d, sisa))
        for _ in range(2):
            subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=d,
                           capture_output=True, text=True, env=ENV)
        if os.path.exists(os.path.join(d, "main.idx")):
            subprocess.run(["makeindex", "main.idx"], cwd=d, capture_output=True, env=ENV)
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=d,
                           capture_output=True, text=True, env=ENV)
        baris = open(os.path.join(d, "main.log"), errors="replace").read().splitlines()
        log = "\n".join(baris)
        errs = [l for l in baris if l.startswith("!")]
        # include the line after 'Overfull' so a failure names the offending text
        gemuk = []
        for i, l in enumerate(baris):
            m_ov = re.search(r"Overfull \\hbox \(([\d.]+)pt", l)
            if m_ov and float(m_ov.group(1)) > 5:
                ekor = baris[i + 1].strip()[:70] if i + 1 < len(baris) else ""
                gemuk.append((float(m_ov.group(1)), ekor))
        info = subprocess.run(["pdfinfo", os.path.join(d, "main.pdf")],
                              capture_output=True, text=True).stdout
        m = re.search(r"^Pages:\s+(\d+)", info, re.M)
        judul = re.search(r"^Title:\s+(.+)$", info, re.M)
        ok("pdflatex exit 0", r.returncode == 0, str(errs[:2]))
        ok("tanpa error '!'", not errs, str(errs[:2]))
        ok("overfull <= 5pt", not gemuk, str(gemuk[:4]))
        ok("halaman > 40", bool(m) and int(m.group(1)) > 40, m.group(1) if m else "?")
        ok("judul PDF memuat 'Edisi Pertama'", bool(judul) and "Edisi Pertama" in judul.group(1),
           judul.group(1) if judul else "")
        ok("indeks terbentuk", os.path.exists(os.path.join(d, "main.ind")), "main.ind tidak ada")

        out_pdf = os.path.join(tmp, "out.pdf")
        kode = (f"import sys, build_ed2 as b; b.HERE={d!r}; "
                f"b.OUT_PDF={out_pdf!r}; sys.exit(b.pdf())")
        r = subprocess.run([sys.executable, "-c", kode], cwd=d, capture_output=True, text=True)
        ukuran = os.path.getsize(out_pdf) if os.path.exists(out_pdf) else 0
        ok("pdf(): exit 0", r.returncode == 0, (r.stdout + r.stderr)[-200:])
        ok("pdf(): berkas > 100 KB", ukuran > 100_000, str(ukuran))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    lulus = sum(1 for _, c, _ in CHECKS if c)
    print(f"{lulus}/{len(CHECKS)} PASS  (uji kerangka, sandbox {os.path.basename(tmp)} dibersihkan)")
    for nama, c, det in CHECKS:
        print(("PASS " if c else "FAIL ") + nama + ("" if c else f"  <- {det}"))
    return 0 if lulus == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
