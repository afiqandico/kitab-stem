#!/usr/bin/env python3
"""Gerbang paritas materi belakang edisi Inggris (depan, lampiran A-D, kolofon, rujukan).

Materi belakang tidak berbentuk bab, jadi tidak bisa dipakai `cek-en.py`: isinya tabel
notasi, daftar istilah, kunci jawaban, dan daftar rujukan. Yang dijaga tetap sama:
matematika, angka, jumlah butir, dan label harus identik dengan sumbernya; prosa harus
sudah berbahasa Inggris.

Pemakaian:
    python3 tools/cek-belakang.py            # semua bagian yang sudah ada
    python3 tools/cek-belakang.py lampB      # satu bagian
    python3 tools/cek-belakang.py --daftar   # daftar bagian + status

Sumber: belakang/_sumber/<nama>.tex ; sasaran: belakang/<nama>-en.tex
"""
from __future__ import annotations

import collections
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EN = os.path.dirname(HERE)
SUMBER = os.path.join(EN, "belakang", "_sumber")
SASARAN = os.path.join(EN, "belakang")

# nama: (keterangan, batas kata bawah, batas kata atas)
BAGIAN = {
    "depan-a": ("Kata Pengantar", 0.75, 1.35),
    "depan-b": ("Cara Membaca: Empat Jalur", 0.75, 1.35),
    "depan-c": ("Peta Ketergantungan Bab", 0.75, 1.35),
    "lampA": ("Lampiran A: Tabel Notasi", 0.75, 1.35),
    "lampB": ("Lampiran B: Glosarium", 0.75, 1.45),
    "lampC": ("Lampiran C: Petunjuk dan Kriteria Penilaian", 0.75, 1.35),
    "lampD": ("Lampiran D: Kunci Jawaban (pembuka)", 0.75, 1.45),
    "kunci-01-05": ("Kunci Bab 1-5", 0.70, 1.45),
    "kunci-06-15": ("Kunci Bab 6-15", 0.70, 1.45),
    "kunci-16-23": ("Kunci Bab 16-23", 0.70, 1.45),
    "kunci-24-32": ("Kunci Bab 24-32", 0.70, 1.45),
    "kolofon": ("Kolofon", 0.75, 1.35),
    "rujukan": ("Daftar Rujukan", 0.75, 1.35),
}

# Kata fungsi Indonesia: kalau masih banyak, prosa belum diterjemahkan. Istilah
# Indonesia yang memang dipertahankan (dalam tanda kurung glosarium) dihitung, jadi
# ambangnya relatif dan kelonggarannya disebut di laporan.
KATA_ID = {
    "dan", "yang", "dengan", "untuk", "dari", "pada", "adalah", "tidak", "ini", "itu",
    "atau", "sehingga", "karena", "bila", "jika", "juga", "tetapi", "dalam", "oleh",
    "sebagai", "akan", "dapat", "harus", "kita", "kamu", "sebuah", "setiap", "antara",
    "tanpa", "setelah", "sebelum", "hanya", "lebih", "masih", "sudah", "belum",
    "maka", "agar", "sebab", "ialah", "merupakan", "bagi", "punya", "cara", "bukan",
    "semua", "dua", "tiga", "satu", "empat", "lima", "ada", "di", "ke", "tak", "pun",
    "para", "secara", "telah", "sedang", "serta", "maupun", "namun", "tapi", "saja",
    "lagi", "pula", "sangat", "banyak", "tiap", "kepada", "terhadap", "melalui",
    "hingga", "sampai", "sejak", "ketika", "saat", "demi", "atas", "bawah", "tanpa",
}

MAKRO = ("chapter", "section", "label", "ref", "index", "kamus", "item", "caption",
         "addcontentsline", "markboth", "toprule", "midrule", "bottomrule")


def muat_cek_en():
    p = os.path.join(HERE, "cek-en.py")
    spec = importlib.util.spec_from_file_location("ceken", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def baca(p: str) -> str:
    return open(p, encoding="utf-8").read()


def tanpa_komentar(t: str) -> str:
    t = re.sub(r"\\begin\{(verbatim|lstlisting)\}.*?\\end\{\1\}", " ", t, flags=re.S)
    return re.sub(r"(?<!\\)%.*", " ", t)


def angka(t: str) -> collections.Counter:
    """Multiset angka di luar matematika.

    Isi matematika dibuang: angkanya sudah dibandingkan `matematika()` dengan
    normalisasi `{,}` yang benar, dan memindainya lagi di sini memecah "1{,}5625"
    menjadi token "1" + "5625" sehingga laporan gagal padahal angkanya sama.
    Baris \\input{...} juga dibuang: nomor berkas bukan isi naskah.
    """
    t = tanpa_komentar(t)
    t = re.sub(r"\\input\{[^}]*\}", " ", t)
    t = re.sub(r"\$[^$]+\$|(?<!\\)\\\[.*?(?<!\\)\\\]", " ", t, flags=re.S)
    hasil = collections.Counter()
    for tok in re.findall(r"\d+(?:[.,]\d+)*", t):
        # koma = desimal Indonesia bila diikuti 1-2 atau 4+ digit; koma/titik yang
        # diikuti tepat tiga digit adalah pemisah ribuan dan dibuang di kedua edisi.
        tok = re.sub(r"(?<=\d),(?=\d{4,})", ".", tok)
        tok = re.sub(r"(?<=\d),(?=\d{1,2}(?!\d))", ".", tok)
        for _ in range(8):
            baru = re.sub(r"(?<=\d)[.,](?=\d{3}(?!\d))", "", tok)
            if baru == tok:
                break
            tok = baru
        hasil[tok.lstrip("0") or "0"] += 1
    return hasil


def struktur(t: str) -> dict:
    t = tanpa_komentar(t)
    h = {}
    for k in MAKRO:
        h[k] = len(re.findall(r"\\" + k + r"\b", t))
    h["lingkungan"] = re.findall(r"\\begin\{([^}]+)\}", t)
    return h


def residu_id(t: str) -> list[str]:
    """Kata fungsi Indonesia yang masih tertinggal.

    Isi tanda kurung dibuang lebih dulu: glosarium memang menyimpan padanan Indonesia
    di dalam kurung ("... (\\emph{adjoin})"), dan itu bukan prosa yang lupa
    diterjemahkan. Yang dicari hanya kalimat Inggris yang masih memuat kata fungsi
    Indonesia.
    """
    t = tanpa_komentar(t)
    t = re.sub(r"\$[^$]*\$", " ", t, flags=re.S)
    t = re.sub(r"\([^()]*\)", " ", t)
    t = re.sub(r"\\[a-zA-Z]+\*?", " ", t)
    kata = re.findall(r"[A-Za-z]+", t.lower())
    return [w for w in kata if w in KATA_ID]


def cek(nama: str) -> list[str]:
    if nama not in BAGIAN:
        return [f"{nama}: bagian tidak dikenal"]
    ket, lo, hi = BAGIAN[nama]
    p_id = os.path.join(SUMBER, nama + ".tex")
    p_en = os.path.join(SASARAN, nama + "-en.tex")
    if not os.path.exists(p_en):
        return [f"{nama}: belum diterjemahkan ({os.path.basename(p_en)} tidak ada)"]
    ceken = muat_cek_en()
    idn, en = baca(p_id), baca(p_en)
    m: list[str] = []

    # 1. matematika harus sama persis (multiset)
    a, b = ceken.matematika(en), ceken.matematika(idn)
    if a != b:
        hanya_en = list((a - b).items())[:2]
        hanya_id = list((b - a).items())[:2]
        m.append(f"matematika beda: EN-only={hanya_en} ID-only={hanya_id}")

    # 2. angka di luar matematika harus sama
    na, nb = angka(en), angka(idn)
    if na != nb:
        m.append(f"angka beda: EN-only={list((na - nb).items())[:3]} ID-only={list((nb - na).items())[:3]}")

    # 3. struktur: jumlah makro + urutan lingkungan
    sa, sb = struktur(en), struktur(idn)
    for k in MAKRO:
        if sa[k] != sb[k]:
            m.append(f"{k}: EN={sa[k]} ID={sb[k]}")
    if sa["lingkungan"] != sb["lingkungan"]:
        beda = [(i, x, y) for i, (x, y) in enumerate(zip(sa["lingkungan"], sb["lingkungan"])) if x != y]
        m.append(f"urutan lingkungan beda di {beda[:3]} (jumlah {len(sa['lingkungan'])} vs {len(sb['lingkungan'])})")

    # 3b. glosarium harus urut abjad menurut kepala butir INGGRIS (kepala ganda
    # dibolehkan: sumber Indonesia sendiri memuat dua istilah untuk satu konsep,
    # mis. Kovarians/Kovariansi, dan keduanya harus tetap ada).
    if nama == "lampB":
        kepala = re.findall(r"^\s*\\item\[([^\]]*)\]", en, re.M)
        kunci = [re.sub(r"[^a-z0-9 ]", "", k.lower()).strip() for k in kepala]
        if kunci != sorted(kunci):
            rusak = next((i for i in range(len(kunci) - 1) if kunci[i] > kunci[i + 1]), None)
            m.append(f"glosarium tidak urut abjad di butir {rusak}: "
                     f"'{kepala[rusak]}' > '{kepala[rusak + 1]}'")

    # 4. sisa kata fungsi Indonesia
    sisa = residu_id(en)
    nkata = ceken.kata(en)
    # 0,2 persen: satu kalimat Indonesia di tengah berkas panjang sudah ketahuan,
    # sedangkan istilah Indonesia di dalam kurung glosarium tidak dihitung (lihat residu_id).
    batas = max(2, int(0.001 * nkata))
    if len(sisa) > batas:
        m.append(f"sisa kata Indonesia {len(sisa)} > batas {batas}: {collections.Counter(sisa).most_common(6)}")

    # 5. panjang prosa dalam band
    rasio = nkata / max(1, ceken.kata(idn))
    if not (lo <= rasio <= hi):
        m.append(f"rasio kata EN/ID {rasio:.2f} di luar band {lo}-{hi} (EN={nkata}, ID={ceken.kata(idn)})")
    return m


def main(argv: list[str]) -> int:
    if "--daftar" in argv:
        for n, (ket, lo, hi) in BAGIAN.items():
            p = os.path.join(SASARAN, n + "-en.tex")
            print(f"{'ADA ' if os.path.exists(p) else 'KOSONG'} {n:12s} {ket}")
        return 0
    # Salinan sumber harus segar: kalau ../_buku-ed2 berubah dan salinan tidak,
    # gerbang membandingkan terjemahan dengan teks lama dan bisa meloloskan cacat.
    segar = subprocess.run([sys.executable, os.path.join(HERE, "ambil-sumber.py"), "--cek"],
                           capture_output=True, text=True)
    print(segar.stdout.strip())
    if segar.returncode != 0:
        return 1
    target = [a for a in argv[1:] if not a.startswith("-")] or list(BAGIAN)
    gagal = 0
    for n in target:
        m = cek(n)
        if m:
            gagal += 1
            print(f"MASALAH {n}")
            for x in m:
                print("    " + x)
        else:
            print(f"OK    {n}")
    print(f"\n{len(target)} bagian diperiksa, {gagal} bermasalah")
    return 1 if gagal else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
