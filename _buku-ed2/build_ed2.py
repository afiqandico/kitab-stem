#!/usr/bin/env python3
"""Rakit + gerbang mutu naskah buku edisi kedua (6 bagian, 30 bab).

Pemakaian:  python3 build_ed2.py [check|status|pdf]
  check  -> gerbang mutu per bab (kata, section, lapisan pembaca, latihan, indeks, larangan)
  status -> ringkas berkas bab yang ada
  pdf    -> pdflatex + makeindex + pdflatex x2, lalu salin ke akar repo
"""
from __future__ import annotations
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PDF = os.path.join(os.path.dirname(HERE), "pdf", "draf",
                       "Kitab-STEM-Kenapa-Mesin-Bisa-Salah-draf-ed2.pdf")
os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)  # pdf/draf/ ikut dibuat bila belum ada
CH = [f"ch{i:02d}" for i in range(1, 33)]

BANNED = re.compile(r"\\documentclass|\\usepackage|\\begin\{document\}|"
                    r"\\cite\{|\\eqref\{|\\pageref\{|"
                    r"\\begin\{table\}|\\footnote\{")

ALLOWED_ENV = {
    "definisi", "teorema", "lemma", "akibat", "proposisi", "contoh", "latihan",
    "catatan", "ringkasan", "lab", "untukanak", "untukdosen", "untukpeneliti",
    "bacakeras", "tangan", "resep", "tantangan",
    "itemize", "enumerate", "description", "equation", "align", "tabular",
    "quote", "verbatim", "center", "equation*", "align*", "proof",
    "pmatrix", "bmatrix", "vmatrix", "matrix", "smallmatrix", "cases", "array",
    "figure", "tikzpicture", "scope", "axis",
}


def body_text(path: str) -> str:
    s = open(path, encoding="utf-8", errors="replace").read()
    s = re.sub(r"\\begin\{verbatim\}.*?\\end\{verbatim\}", " ",
               s, flags=re.S)                                    # kode tidak dihitung kata
    s = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", " ",
               s, flags=re.S)                    # gambar/TikZ bukan prosa, jangan dihitung
    s = re.sub(r"(?m)%.*$", " ", s)
    s = re.sub(r"\\(chapter|section|subsection|subsubsection|paragraph)"
               r"\*?(\[[^\]]*\])?\{[^}]*\}", " ", s)
    s = re.sub(r"\\(begin|end)\{[^}]*\}", " ", s)
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", s)
    s = re.sub(r"[^A-Za-z0-9\u00C0-\u024F]+", " ", s)
    return " ".join(s.split())


def judul_peta() -> dict[int, str]:
    """Judul bab menurut tabel 'Peta Ketergantungan Bab' di main.tex."""
    try:
        main = open(os.path.join(HERE, "main.tex"), encoding="utf-8").read()
    except OSError:
        return {}
    blok = main[main.find("Peta Ketergantungan Bab"):]
    for batas in ("\\end{tabular}", "\\part{"):
        potong = blok.find(batas)
        if potong > 0:
            blok = blok[:potong]
            break
    return {int(n): re.sub(r"\\emph\{([^}]*)\}", r"\1", j).strip()
            for n, j in re.findall(r"^\s*(\d{1,2})\s*&\s*(.+?)\s*&", blok, re.M)}


def cek_peta() -> list[str]:
    """Judul di tabel peta harus sama dengan \\chapter di naskah."""
    beda = []
    for n, judul in judul_peta().items():
        p = os.path.join(HERE, f"ch{n:02d}.tex")
        if not os.path.exists(p):
            continue
        m = re.search(r"\\chapter(?:\[[^\]]*\])?\{([^}]*)\}",
                      open(p, encoding="utf-8", errors="replace").read())
        asli = m.group(1).strip() if m else "(tanpa chapter)"
        if judul != asli:
            beda.append(f"ch{n:02d}")
    return beda


def cek_glosarium() -> list[str]:
    """Setiap istilah di kotak \\kamus harus punya entri di Lampiran Glosarium.

    Glosarium dulu memuat 86 entri pilihan sementara bab memakai 161 istilah;
    tanpa gerbang ini, istilah baru bisa masuk bab tanpa pernah didefinisikan.
    """
    try:
        main = open(os.path.join(HERE, "main.tex"), encoding="utf-8").read()
    except OSError:
        return []
    awal = main.find("\\chapter{Glosarium}")
    akhir = main.find("% ---------------------------- lampiran C")
    if awal < 0:
        return ["(tanpa lampiran glosarium)"]
    blok = main[awal:akhir if akhir > awal else len(main)]
    entri = {re.sub(r"\s+", " ", l.strip().strip("{}")).lower()
             for l in re.findall(r"\\item\[([^\]]*)\]", blok)}
    kurang = []
    for c in CH:
        p = os.path.join(HERE, c + ".tex")
        if not os.path.exists(p):
            continue
        teks = open(p, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"\\kamus(?=\{)", teks):
            # argumen pertama dibaca sadar-kurawal: banyak istilah diikuti analogi berisi
            # math seperti $2^{7}$, sehingga pola [^{}]* akan melewatkannya tanpa kabar.
            i, d = m.end(), 0
            while i < len(teks):
                if teks[i] == "{":
                    d += 1
                elif teks[i] == "}":
                    d -= 1
                    if d == 0:
                        break
                i += 1
            k = re.sub(r"\s+", " ", teks[m.end() + 1:i].strip()).lower()
            if k and k not in entri and k not in kurang:
                kurang.append(k)
    return kurang


def check() -> int:
    bad, hilang, total = 0, 0, 0
    print(f"{'bab':4} {'kata':>5} {'sec':>3} {'teo':>3} {'ank':>3} {'dsn':>3} "
          f"{'pnl':>3} {'kam':>3} {'lat':>3} {'idx':>3}  status")
    for c in CH:
        p = os.path.join(HERE, c + ".tex")
        if not os.path.exists(p):
            print(f"{c:4} {'-':>5} {'-':>3} {'-':>3} {'-':>3} {'-':>3} {'-':>3} "
                  f"{'-':>3} {'-':>3} {'-':>3}  HILANG")
            hilang += 1
            continue
        s = open(p, encoding="utf-8", errors="replace").read()
        w = len(body_text(p).split())
        total += w
        ns = len(re.findall(r"\\section\{", s))
        nt = len(re.findall(r"\\begin\{(?:teorema|lemma|akibat|proposisi|definisi)\}", s))
        nank = len(re.findall(r"\\begin\{untukanak\}", s))
        ndsn = len(re.findall(r"\\begin\{untukdosen\}", s))
        npnl = len(re.findall(r"\\begin\{untukpeneliti\}", s))
        nkam = len(re.findall(r"\\kamus\{", s))
        nbc = len(re.findall(r"\\begin\{bacakeras\}", s))
        ntg = len(re.findall(r"\\begin\{tangan\}", s))
        nrs = len(re.findall(r"\\begin\{resep\}", s))
        ntn = len(re.findall(r"\\begin\{tantangan\}", s))
        nfig = len(re.findall(r"\\begin\{figure\}", s))
        nidx = len(re.findall(r"\\index\{", s))
        ntk = len(re.findall(r"\\tingkat\{", s))
        lat = re.search(r"\\begin\{latihan\}(.*?)\\end\{latihan\}", s, re.S)
        nlat = len(re.findall(r"\\item", lat.group(1))) if lat else 0
        flags = []
        if w < 5000:
            flags.append("pendek")
        if w > 7500:
            flags.append("kepanjangan")
        if ns < 5:
            flags.append("section<5")
        if nt < 4:
            flags.append("teori<4")
        if ntk < max(ns - 2, 1):
            flags.append("tingkat<section")
        if not 2 <= nank <= 4:
            flags.append(f"untukanak={nank}")
        if ndsn != 1:
            flags.append(f"untukdosen={ndsn}")
        if npnl != 1:
            flags.append(f"untukpeneliti={npnl}")
        if nkam < 3:
            flags.append(f"kamus<3")
        if nidx < 8:
            flags.append(f"index<8")
        if nlat < 8:
            flags.append(f"latihan={nlat}")
        for nama, n in (("bacakeras", nbc), ("tangan", ntg), ("resep", nrs),
                        ("tantangan", ntn)):
            if n != 1:
                flags.append(f"{nama}={n}")
        if not 2 <= nfig <= 3:
            flags.append(f"gambar={nfig}")
        for nama, need in (("kertas", "\\kertas{"), ("peta", "\\peta{"),
                           ("lab", "\\begin{lab}"), ("verbatim", "\\begin{verbatim}"),
                           ("ringkasan", "\\begin{ringkasan}"),
                           ("untukanak", "\\begin{untukanak}"),
                           ("chapter", "\\chapter")):
            if need not in s:
                flags.append("tanpa " + nama)
        if BANNED.search(s):
            flags.append("pelanggaran aturan")
        nonascii = {ch for ch in s if ord(ch) > 127}
        if nonascii:
            flags.append("unicode:" + "".join(sorted(nonascii))[:8])
        mch = re.search(r"\\chapter(\[[^\]]*\])?\{([^}]*)\}", s)
        if mch and len(mch.group(2)) > 55 and mch.group(1) is None:
            flags.append("judul-panjang")
        kode = re.findall(r"\\begin\{verbatim\}(.*?)\\end\{verbatim\}", s, re.S)
        lebar = max((len(ln) for b in kode for ln in b.splitlines()), default=0)
        if lebar > 90:
            flags.append(f"verbatim>{lebar}")
        for fig in re.findall(r"\\begin\{figure\}(.*?)\\end\{figure\}", s, re.S):
            if "\\caption{" not in fig or not re.search(r"\\label\{fig:", fig):
                flags.append("figure-tanpa-caption/label")
                break
        for lab in re.findall(r"\\label\{(fig:[^}]*)\}", s):
            if f"\\ref{{{lab}}}" not in s:
                flags.append("figure-tak-dirujuk")
                break
        envs = set(re.findall(r"\\begin\{([^}]*)\}", s))
        extra = envs - ALLOWED_ENV
        if extra:
            flags.append("env:" + ",".join(sorted(extra))[:40])
        if flags:
            bad += 1
        print(f"{c:4} {w:5d} {ns:3d} {nt:3d} {nank:3d} {ndsn:3d} {npnl:3d} "
              f"{nkam:3d} {nlat:3d} {nidx:3d}  {'OK' if not flags else ', '.join(flags)}")
    beda = cek_peta()
    kurang = cek_glosarium()
    print(f"\nTOTAL kata badan: {total}  (target {len(CH)} x 5.500-6.500 = "
          f"{len(CH)*5500:,}-{len(CH)*6500:,})".replace(",", "."))
    print(f"Judul di tabel peta tidak cocok: {len(beda)}" + (f" -> {' '.join(beda)}" if beda else ""))
    print(f"Istilah \\kamus tanpa entri glosarium: {len(kurang)}"
          + (f" -> {' '.join(kurang[:6])}" if kurang else ""))
    print(f"Bab belum ditulis: {hilang}   Bab ada tapi bermasalah: {bad}")
    return 1 if (bad or beda or kurang) else (2 if hilang else 0)


def status() -> int:
    ada = [c for c in CH if os.path.exists(os.path.join(HERE, c + ".tex"))]
    print(f"bab ada: {len(ada)}/{len(CH)} -> {' '.join(ada) if ada else '(belum ada)'}")
    return 0


def pdf() -> int:
    # Reproducible: pdfTeX menulis tanggal & /ID dari jam sekarang, sehingga dua
    # rakitan dari sumber yang sama menghasilkan sha256 berbeda. SOURCE_DATE_EPOCH
    # (tanggal rilis buku) + FORCE_SOURCE_DATE memaku keduanya.
    env = dict(os.environ, SOURCE_DATE_EPOCH="1792857600", FORCE_SOURCE_DATE="1")

    def run(cmd):
        return subprocess.run(cmd, cwd=HERE, capture_output=True, text=True, env=env)

    for i in (1, 2):
        r = run(["pdflatex", "-interaction=nonstopmode", "main.tex"])
        if r.returncode != 0:
            log = open(os.path.join(HERE, "main.log"), encoding="utf-8", errors="replace").read()
            errs = [l for l in log.splitlines() if l.startswith("!")]
            print(f"GAGAL pdflatex lintasan {i}:")
            print("\n".join(errs[:30]) or log[-2500:])
            return 1
    if os.path.exists(os.path.join(HERE, "main.idx")):
        run(["makeindex", "main.idx"])
    for _ in range(2):
        r = run(["pdflatex", "-interaction=nonstopmode", "main.tex"])
        if r.returncode != 0:
            log = open(os.path.join(HERE, "main.log"), encoding="utf-8", errors="replace").read()
            print("GAGAL pdflatex akhir:", log[-2500:])
            return 1
    log = open(os.path.join(HERE, "main.log"), encoding="utf-8", errors="replace").read()
    ganda = re.findall(r"Label `([^']*)' multiply defined", log)
    if ganda:
        print("GAGAL: label ganda di buku rakitan: " + ", ".join(sorted(set(ganda))))
        return 1
    over = re.findall(r"Overfull \\hbox \((\d+\.\d+)pt", log)
    big = [o for o in over if float(o) > 10]
    src = os.path.join(HERE, "main.pdf")
    info = subprocess.run(["pdfinfo", src], capture_output=True, text=True).stdout
    pages = re.search(r"^Pages:\s+(\d+)", info, re.M)
    bookmarks = subprocess.run(["python3", "-c",
        "import re,sys;d=open(sys.argv[1],'rb').read();"
        "print(len(re.findall(rb'/Title',d)))", src], capture_output=True, text=True).stdout.strip()
    subprocess.run(["cp", src, OUT_PDF], check=True)
    print(f"OK  {OUT_PDF}")
    print(f"halaman={pages.group(1) if pages else '?'}  "
          f"ukuran={os.path.getsize(OUT_PDF)/2**20:.2f} MB  "
          f"bookmark~{bookmarks}  overfull>10pt={len(big)}")
    return 1 if big else 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    sys.exit({"check": check, "status": status, "pdf": pdf}[mode]())
