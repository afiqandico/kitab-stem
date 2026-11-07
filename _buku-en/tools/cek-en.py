#!/usr/bin/env python3
"""Gerbang edisi Inggris: paritas struktur + paritas kata + sisa bahasa Indonesia.

Pakai:
    python3 tools/cek-en.py [chNN ...]     # tanpa argumen = semua bab yang ada
    python3 tools/cek-en.py --pdf          # rakit main-en.tex lalu periksa log

Yang diperiksa per bab (dibandingkan dengan ../_buku-ed2/chNN.tex):
  1. jumlah \\section, \\tingkat, \\kamus, \\index, \\label, \\begin{...} per lingkungan;
  2. himpunan kunci \\label identik dengan sumber;
  3. semua \\ref di berkas EN punya \\label di berkas EN;
  4. rasio jumlah kata 0,85-1,35 terhadap sumber;
  5. sisa kata Indonesia di bawah 0,5% kata (daftar kata fungsi, bukan nama istilah);
  6. urutan lingkungan sama dengan sumber (dibandingkan sebagai daftar nama).
Keluar 1 bila ada bab bermasalah.
"""
from __future__ import annotations

import collections
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EN = os.path.dirname(HERE)
ID = os.path.join(os.path.dirname(EN), "_buku-ed2")

IDWORD = ("yang dan dengan adalah untuk dari tidak pada ini itu juga karena sehingga dalam "
          "akan bisa dapat kita harus satu dua tiga tetapi namun sebagai oleh lebih sudah "
          "belum hanya antara serta bila jika maka agar tanpa melalui terhadap").split()


def baca(p: str) -> str:
    return open(p, encoding="utf-8").read()


def matematika(t: str) -> collections.Counter:
    """Multiset potongan matematika, spasi dibuang, isi \\text{} dinormalisasi.

    Spasi dibuang karena baris sumber dan terjemahan dipatahkan di tempat berbeda;
    isi \\text{} dinormalisasi karena prosa di dalam matematika memang diterjemahkan.
    """
    t = re.sub(r"\\begin\{(verbatim|lstlisting)\}.*?\\end\{\1\}", " ", t, flags=re.S)
    t = re.sub(r"(?<!\\)%.*", " ", t)
    # "\\[3pt]" adalah pindah baris di dalam sel TikZ, bukan pembuka matematika
    # display; tanpa lookbehind keduanya tertukar dan seluruh isi simpul ikut
    # menjadi satu potongan.
    xs = re.findall(r"\$[^$]+\$|(?<!\\)\\\[.*?(?<!\\)\\\]", t, flags=re.S)
    # ",{}" dan "." sama-sama penanda desimal: edisi Indonesia memakai koma,
    # edisi Inggris memakai titik, jadi keduanya disamakan sebelum dibandingkan.
    def norm(x: str) -> str:
        # koma desimal Indonesia selalu berarti desimal kecuali saat memisah
        # ribuan (tiga digit mengikuti); keduanya disamakan ke titik dulu.
        x = re.sub(r"(\d)\{,\}", r"\1.", x)
        # Pemisah ribuan (1.073.741.824 / 1{,}073{,}741{,}824) dibuang simetris
        # di kedua edisi: konvensinya memang berbeda, yang harus sama adalah angkanya.
        for _ in range(8):
            baru = re.sub(r"(?<=\d)[.,](?=\d{3}(?!\d))", "", x)
            if baru == x:
                break
            x = baru
        return re.sub(r"\\text\{[^{}]*\}", r"\\text{}", re.sub(r"\s+", "", x))
    return collections.Counter(norm(x) for x in xs)


def kata(t: str) -> int:
    t = re.sub(r"\\begin\{(verbatim|lstlisting)\}.*?\\end\{\1\}", " ", t, flags=re.S)
    t = re.sub(r"(?<!\\)%.*", " ", t)
    t = re.sub(r"\\[a-zA-Z]+\*?", " ", t)
    t = re.sub(r"[{}$&_^~\\]", " ", t)
    return len([w for w in re.split(r"\s+", t) if re.search(r"[A-Za-z0-9]", w)])


def entitas(t: str) -> dict:
    return {
        "section": len(re.findall(r"\\section\*?(\[[^\]]*\])?\{", t)),
        "chapter": len(re.findall(r"\\chapter\*?(\[[^\]]*\])?\{", t)),
        "tingkat": len(re.findall(r"\\tingkat\{", t)),
        "kamus": len(re.findall(r"\\kamus(?=\{)", t)),
        "index": len(re.findall(r"\\index\{", t)),
        "label": len(re.findall(r"\\label\{", t)),
        "lingkungan": re.findall(r"\\begin\{([^}]+)\}", t),
    }


STOPWORD = {"the", "and", "of", "a", "an", "to", "in", "for", "on", "with", "from"}


def judul_bab(t: str) -> str:
    """Ambil argumen wajib \\chapter{...} (kurung kurawal bersarang dihitung)."""
    m = re.search(r"\\chapter\*?(?:\[[^\]]*\])?\{", t)
    if not m:
        return ""
    i, d = m.end() - 1, 0
    for j in range(i, len(t)):
        if t[j] == "{":
            d += 1
        elif t[j] == "}":
            d -= 1
            if d == 0:
                return t[i + 1:j]
    return ""


def header_salah(teks_pdf: str, judul: dict[int, str],
                 lampiran: dict[str, str] | None = None) -> list[tuple[object, str, list[str]]]:
    """Kepala halaman yang kata judulnya tidak ada di judul bab itu.

    Ini penangkal kebocoran yang tidak bisa dilihat LaTeX: kalau satu berkas bab
    menulis \\renewcommand{\\chaptermark}{...}, perintah itu berlaku untuk semua
    bab sesudahnya, sehingga header bab 14-18 bisa berbunyi judul bab 13 tanpa
    satu pun peringatan. Nomor bab pada header tetap menaik, jadi urutan nomor
    saja tidak cukup - teksnya harus dicocokkan dengan judul bab tersebut.
    """
    salah = []
    for label, nomor, teks in re.findall(r"^(CHAPTER|APPENDIX) (\d+|[A-D])\. (.+)$", teks_pdf, re.M):
        if nomor.isdigit():
            if label != "CHAPTER":
                continue
            t, kunci = judul.get(int(nomor), ""), int(nomor)
        else:
            t = (lampiran or {}).get(nomor, "")
            if not t:
                continue
            if label != "APPENDIX":
                # "\chaptermark" memakai \chaptername, bukan \@chapapp: halaman
                # lampiran memakai awalan bab. LaTeX tidak berperingatan soal ini.
                salah.append((nomor, teks.strip(), ["prefix: seharusnya APPENDIX"]))
                continue
            kunci = nomor
        if not t:
            continue
        kata_judul = set(re.findall(r"[a-z]+", t.lower()))
        hilang = [w for w in re.findall(r"[a-z]+", teks.lower())
                  if len(w) > 2 and w not in STOPWORD and w not in kata_judul]
        if hilang:
            salah.append((kunci, teks.strip(), hilang[:2]))
    return salah


def cek_bab(n: str) -> list[str]:
    p_en, p_id = os.path.join(EN, n + ".tex"), os.path.join(ID, n + ".tex")
    masalah: list[str] = []
    if not os.path.exists(p_en):
        return [f"{n}: belum diterjemahkan"]
    if not os.path.exists(p_id):
        return [f"{n}: sumber Indonesia tidak ada"]
    en, idn = baca(p_en), baca(p_id)
    a, b = entitas(en), entitas(idn)
    for k in ("section", "chapter", "tingkat", "kamus", "index", "label"):
        if a[k] != b[k]:
            masalah.append(f"{n}: {k} EN={a[k]} ID={b[k]}")
    if a["lingkungan"] != b["lingkungan"]:
        beda = [(i, x, y) for i, (x, y) in enumerate(zip(a["lingkungan"], b["lingkungan"])) if x != y]
        masalah.append(f"{n}: urutan lingkungan beda di posisi {beda[:3]} (jumlah {len(a['lingkungan'])} vs {len(b['lingkungan'])})")
    lab_en = set(re.findall(r"\\label\{([^}]+)\}", en))
    lab_id = set(re.findall(r"\\label\{([^}]+)\}", idn))
    if lab_en != lab_id:
        masalah.append(f"{n}: label beda: hanya-EN {sorted(lab_en - lab_id)[:3]}, hanya-ID {sorted(lab_id - lab_en)[:3]}")
    ref_en = set(re.findall(r"\\ref\{([^}]+)\}", en))
    yatim = sorted(ref_en - lab_en)
    if yatim:
        masalah.append(f"{n}: \\ref tanpa \\label: {yatim[:3]}")
    ke, ki = kata(en), kata(idn)
    rasio = ke / max(1, ki)
    if not 0.85 <= rasio <= 1.35:
        masalah.append(f"{n}: rasio kata {rasio:.2f} ({ke} vs {ki}) di luar 0,85-1,35")
    m_en, m_id = matematika(en), matematika(idn)
    beda_math = (m_en - m_id) + (m_id - m_en)
    if beda_math:
        contoh = sorted(beda_math)[0][:60]
        masalah.append(f"{n}: matematika beda di {len(beda_math)} potongan (mis. {contoh})")
    if not re.search(r"\\chapter\*?(\[[^\]]*\])?\{", en):
        masalah.append(f"{n}: tidak ada \\chapter{{")
    if "\\begin{document}" in en or "\\documentclass" in en:
        masalah.append(f"{n}: memuat preamble (harus bab saja)")
    teks = re.sub(r"\\[a-zA-Z]+\*?", " ", en)
    teks = re.sub(r"\$[^$]*\$", " ", teks)
    words = re.findall(r"[A-Za-z]+", teks.lower())
    sisa = [w for w in words if w in IDWORD]
    if words and len(sisa) / len(words) > 0.005:
        contoh = ", ".join(sorted(set(sisa))[:8])
        masalah.append(f"{n}: sisa kata Indonesia {len(sisa)}/{len(words)} ({100*len(sisa)/len(words):.2f}%): {contoh}")
    return masalah


def main(argv: list[str]) -> int:
    if "--pdf" in argv:
        env_pdf = dict(os.environ, SOURCE_DATE_EPOCH="1792857600", FORCE_SOURCE_DATE="1")
        def latex() -> subprocess.CompletedProcess:
            return subprocess.run(["pdflatex", "-interaction=nonstopmode", "main-en.tex"],
                                  cwd=EN, capture_output=True, text=True, env=env_pdf)
        r = latex()
        # Indeks harus benar-benar dibuat: tanpa makeindex, \printindex mencetak halaman
        # kosong dan tidak ada satu pun peringatan LaTeX. Dulu itu lolos tanpa terlihat.
        idx = os.path.join(EN, "main-en.idx")
        if os.path.exists(idx) and "\\indexentry" in baca(idx):
            subprocess.run(["makeindex", "-q", "main-en.idx"], cwd=EN, capture_output=True, text=True)
            r = latex()
        r = latex()
        log = os.path.join(EN, "main-en.log")
        isi = baca(log) if os.path.exists(log) else ""
        over = re.findall(r"Overfull \\hbox \(([\d.]+)pt", isi)
        besar = [o for o in over if float(o) > 10]
        ganda = re.findall(r"Label `([^']*)' multiply defined", isi)
        err = re.findall(r"^! .*$", isi, re.M)
        # Mark header tidak boleh bocor antar-bab. \chaptermark yang didefinisikan
        # ulang di dalam satu berkas bab berlaku global, sehingga header bab-bab
        # sesudahnya bisa memakai judul bab sebelumnya tanpa satu pun peringatan
        # LaTeX. Kepala halaman yang sehat selalu menaik nomornya.
        pdf = os.path.join(EN, "main-en.pdf")
        # pdftotext menempelkan \f di depan baris pertama tiap halaman, sehingga
        # regex ber-anchor ^ tidak melihat kepala halaman sama sekali - gerbang
        # pernah melaporkan "bocor-header=0" hanya karena buta, bukan karena bersih.
        teks_pdf = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True
                                 ).stdout.replace("\f", "\n")
        isi_main = baca(os.path.join(EN, "main-en.tex"))
        judul = {}
        for nm in re.findall(r"\\input\{(ch\d\d)\}", isi_main):
            p = os.path.join(EN, nm + ".tex")
            if os.path.exists(p):
                judul[int(nm[2:])] = judul_bab(baca(p))
        # Lampiran diperiksa dengan aturan yang sama: kepala halaman harus
        # "APPENDIX A. <judul lampiran>", bukan "CHAPTER A. ...".
        lampiran = {}
        for nm in re.findall(r"\\input\{belakang/(lamp[A-D])-en\}", isi_main):
            p_l = os.path.join(EN, "belakang", nm + "-en.tex")
            if os.path.exists(p_l):
                lampiran[nm[-1]] = judul_bab(baca(p_l))
        bocor = header_salah(teks_pdf, judul, lampiran)
        # Rujukan yang tidak terselesaikan tercetak '??' tanpa menggagalkan pdflatex.
        tanya = len(re.findall(r"\?\?", teks_pdf))
        # Indeks kosong juga tidak berperingatan: yang diperiksa jumlah baris indeks nyata.
        ind = os.path.join(EN, "main-en.ind")
        entri_ind = 0
        if os.path.exists(ind):
            entri_ind = len(re.findall(r"\\item ", baca(ind)))
        jumlah_header = len(re.findall(r"^(?:CHAPTER|APPENDIX) (?:\d+|[A-D])\. ", teks_pdf, re.M))
        # Penjaga: buku 636 halaman tanpa satu pun kepala halaman berarti regex
        # (atau pemakaian fancyhdr) rusak, bukan bukunya bersih.
        if jumlah_header < 400:
            err = err + [f"hanya {jumlah_header} kepala halaman terbaca"]
        ok = (r.returncode == 0 and not err and not ganda and not besar and not bocor
              and tanya == 0 and entri_ind > 0)
        print(f"{'OK' if ok else 'GAGAL'} rakitan EN: rc={r.returncode} error={len(err)} "
              f"label-ganda={len(ganda)} overfull>10pt={len(besar)} bocor-header={len(bocor)} "
              f"'??'={tanya} entri-indeks={entri_ind} header={jumlah_header}")
        if bocor:
            n, teks, hilang = bocor[0]
            print(f"   mark header keliru di {n}: '{teks[:50]}' (kata bukan dari judul: {hilang})")
        if not ok:
            print((" | ".join(err[:3]) or "")[:400])
        return 0 if ok else 1

    bab = argv or sorted(f[:-4] for f in os.listdir(EN)
                         if re.fullmatch(r"ch\d\d\.tex", f))
    if not bab:
        print("belum ada bab Inggris")
        return 1
    semua: list[str] = []
    for n in bab:
        m = cek_bab(n)
        print(f"{'OK   ' if not m else 'MASALAH'} {n}")
        for x in m:
            print("   ", x)
        semua += m
    print(f"\n{len(bab)} bab diperiksa, {len(semua)} masalah")
    return 1 if semua else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
