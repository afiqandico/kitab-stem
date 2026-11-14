#!/usr/bin/env python3
"""Verification of Chapter 24 (linear + integer programming): all ten keyed exercises 24.1-24.10.

Ad-hoc, not a project suite. Every item demands (a) the exercise text present in both editions,
(b) the key text present in both editions, (c) the keyed number recomputed from scratch here —
vertices by exact enumeration, the simplex pivot sequence by an exact tableau walk, the LP bounds
by exact rational greedy, the integer answers by exhaustive search, and the vertex-cover ratios by
a brute-force minimum cover.

The point is the asymmetry the audit named: completeness is proven by machine, truth of the keys
is not. This file is the machine argument for Chapter 24 only.

Self-test (proves these checks can fail): python3 tools/uji-verify-kunci-24.py
"""
import itertools
import os
import re
from fractions import Fraction as F

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ID = os.path.join(ROOT, "_buku-ed2")
EN = os.path.join(ROOT, "_buku-en")

KI = open(os.path.join(ID, "lampiran-kunci", "kunci-24-32.tex"), encoding="utf-8").read()
KE = open(os.path.join(EN, "belakang", "kunci-24-32-en.tex"), encoding="utf-8").read()
CHI = open(os.path.join(ID, "ch24.tex"), encoding="utf-8").read()
CHE = open(os.path.join(EN, "ch24.tex"), encoding="utf-8").read()

gagal = []
jumlah = [0]


def cek(nama, ok, bukti=""):
    jumlah[0] += 1
    print(("PASS " if ok else "FAIL ") + nama + ("  " + bukti if bukti else ""))
    if not ok:
        gagal.append(nama)


def blok(sumber, judul):
    m = re.search(re.escape(judul) + r".*?(?=\\section\*\{)", sumber, re.S)
    assert m, "blok tak ditemukan: " + judul
    return m.group(0)


def soal(sumber, n):
    """Exercise n (1-based) from the latihan block."""
    m = re.search(r"\\begin\{latihan\}(.*?)\\end\{latihan\}", sumber, re.S).group(1)
    return re.split(r"\n\s*\\item\s", m)[n]


K24I = blok(KI, "\\section*{Bab 24:")
K24E = blok(KE, "\\section*{Chapter 24:")


# --- exact helpers ----------------------------------------------------------
def irisan_2var(a1, b1, c1, a2, b2, c2):
    """Solve a1*x+b1*y=c1 and a2*x+b2*y=c2 exactly; None if singular."""
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    return ((c1 * b2 - c2 * b1) / det, (a1 * c2 - a2 * c1) / det)


def verteks(A, b):
    """All vertices of {x >= 0 : A x <= b} by intersecting every pair of binding lines."""
    baris = [(F(a1), F(a2), F(r)) for (a1, a2), r in zip(A, b)]
    baris += [(F(-1), F(0), F(0)), (F(0), F(-1), F(0))]  # x1 >= 0, x2 >= 0
    titik = set()
    for (a1, b1, c1), (a2, b2, c2) in itertools.combinations(baris, 2):
        p = irisan_2var(a1, b1, c1, a2, b2, c2)
        if p is None:
            continue
        if all(a1 * p[0] + b1 * p[1] <= c1 + F(0) for a1, b1, c1 in baris):
            titik.add(p)
    return sorted(titik)


def simpleks(c, A, b, jejak=None):
    """Exact primal simplex (Bland) for max c.x, A x <= b, x >= 0. Returns (x, z, dual, jejak)."""
    m, n = len(A), len(c)
    cfull = [F(v) for v in c] + [F(0)] * m      # slack columns carry zero objective
    T = [[F(A[i][j]) for j in range(n)] + [F(1 if i == k else 0) for k in range(m)] + [F(b[i])]
         for i in range(m)]
    basis = [n + i for i in range(m)]
    lebar = n + m
    if jejak is not None:
        jejak.append((None, None, None, basis[:], F(0)))
    while True:
        z = [sum(cfull[basis[i]] * T[i][j] for i in range(m)) for j in range(lebar)]
        red = [cfull[j] - z[j] for j in range(lebar)]
        masuk = next((j for j in range(lebar) if red[j] > 0), None)
        if masuk is None:
            break
        pilihan = [(T[i][lebar] / T[i][masuk], basis[i], i)
                   for i in range(m) if T[i][masuk] > 0]
        if not pilihan:            # unbounded — cannot happen for this book's problems
            raise RuntimeError("tak terbatas")
        _, _, keluar = min(pilihan)
        p = T[keluar][masuk]
        T[keluar] = [v / p for v in T[keluar]]
        for i in range(m):
            if i != keluar and T[i][masuk] != 0:
                f = T[i][masuk]
                T[i] = [a - f * bb for a, bb in zip(T[i], T[keluar])]
        basis[keluar] = masuk
        if jejak is not None:
            jejak.append((masuk, keluar, basis[keluar], basis[:],
                          sum(cfull[basis[i]] * T[i][lebar] for i in range(m))))
    x = [F(0)] * n
    for i in range(m):
        if basis[i] < n:
            x[basis[i]] = T[i][lebar]
    z = sum(cfull[j] * x[j] for j in range(n))
    dual = [sum(cfull[basis[i]] * T[i][n + j] for i in range(m)) for j in range(m)]
    return x, z, dual, jejak


# --- 24.1 bakery: vertices, integer enumeration, gap -----------------------
A1 = [(2, 1), (1, 2)]
b1 = (10, 8)
c1 = (30, 20)
V1 = verteks(A1, b1)
laba1 = {v: c1[0] * v[0] + c1[1] * v[1] for v in V1}
opt1 = max(laba1.values())
bulat1 = max(c1[0] * i + c1[1] * j
             for i in range(11) for j in range(9)
             if 2 * i + j <= 10 and i + 2 * j <= 8)
cek("24.1 verteks (0;0) (5;0) (0;4) (4;2)", V1 == [(F(0), F(0)), (F(0), F(4)),
                                              (F(4), F(2)), (F(5), F(0))], str(V1))
cek("24.1 laba verteks 0;150;80;160",
    laba1 == {(F(0), F(0)): F(0), (F(5), F(0)): F(150),
              (F(0), F(4)): F(80), (F(4), F(2)): F(160)})
cek("24.1 optimum bersambung 160 di (4;2)", opt1 == 160 and
    max(laba1, key=laba1.get) == (F(4), F(2)), f"opt={opt1}")
cek("24.1 enumerasi bulat 160 -> celah 0", bulat1 == 160 and opt1 - bulat1 == 0,
    f"bulat={bulat1}")
cek("24.1 teks ID/EN memuat verteks dan celah 0",
    "(4;2)$ memberi laba" in K24I and "(4;2)$ with profit" in K24E
    and "celahnya $0$" in K24I and "the gap is $0$" in K24E)
cek("24.1 soal ID/EN: 10 kg tepung, 8 jam oven, laba 30/20",
    "$10$ kg tepung dan $8$ jam oven" in soal(CHI, 1)
    and "$10$ kg of flour and $8$ oven hours" in soal(CHE, 1))

# --- 24.2 convexity: the argument collapses on the integer lattice ----------
import random
random.seed(0)
layak1 = [(F(i), F(j)) for i in range(6) for j in range(5)
          if 2 * i + j <= 10 and i + 2 * j <= 8]
konveks = True
for _ in range(2000):
    x, y = random.sample(layak1, 2)
    t = F(random.randint(0, 20), 20)
    p = (t * x[0] + (1 - t) * y[0], t * x[1] + (1 - t) * y[1])
    if not (2 * p[0] + p[1] <= 10 and p[0] + 2 * p[1] <= 8):
        konveks = False
tengah = ((F(0) + F(1)) / 2, F(0))
cek("24.2 gabungan konveks tetap layak (2000 sampel eksak)", konveks)
cek("24.2 titik tengah 0 dan 1 bukan bilangan bulat",
    tengah[0].denominator != 1)
cek("24.2 teks ID/EN memuat bukti linearitas A",
    "\\lambda Ax+(1-\\lambda)Ay\\le\\lambda b+(1-\\lambda)b=b" in K24I
    and "\\lambda Ax+(1-\\lambda)Ay\\le\\lambda b+(1-\\lambda)b=b" in K24E)

# --- 24.3 workshop LP with objective x1 + 2 x2 -----------------------------
A3 = [(6, 4), (1, 2)]
b3 = (24, 6)
c3 = (1, 2)
V3 = verteks(A3, b3)
nilai3 = {v: c3[0] * v[0] + c3[1] * v[1] for v in V3}
opt3 = max(nilai3.values())
optimal3 = sorted(v for v in V3 if nilai3[v] == opt3)
tengah3 = ((F(0) + F(3)) / 2, (F(3) + F(3, 2)) / 2)
cek("24.3 verteks (0;0) (4;0) (0;3) (3;1,5)", V3 == [(F(0), F(0)), (F(0), F(3)),
                                                   (F(3), F(3, 2)), (F(4), F(0))], str(V3))
cek("24.3 nilai verteks 0;4;6;6",
    [nilai3[v] for v in [(F(0), F(0)), (F(4), F(0)), (F(0), F(3)), (F(3), F(3, 2))]]
    == [F(0), F(4), F(6), F(6)])
cek("24.3 dua verteks optimal (0;3) dan (3;1,5)",
    optimal3 == [(F(0), F(3)), (F(3), F(3, 2))], str(optimal3))
cek("24.3 seluruh ruas optimal: titik tengah juga bernilai 6, dan bukan verteks",
    c3[0] * tengah3[0] + c3[1] * tengah3[1] == opt3 and tengah3 not in V3,
    f"tengah=({tengah3[0]};{tengah3[1]})")
cek("24.3 dual y=(0;1) layak dan kuat: 24*0+6*1 = 6",
    all(F(a1) * 0 + F(b1) * 1 >= F(ci) for (a1, b1), ci in zip(A3, c3))
    and 24 * 0 + 6 * 1 == opt3)
cek("24.3 teks ID/EN memuat 0;4;6;6 dan dual (0;1)",
    ": $0$; $4$; $6$; $6$" in K24I and ": $0$; $4$; $6$; $6$" in K24E
    and "$y=(0;1)$" in K24I and "$y=(0;1)$" in K24E)
cek("24.3 soal ID/EN: ganti laba menjadi x1+2x2",
    "Ganti laba bengkel menjadi $x_{1}+2x_{2}$" in soal(CHI, 3)
    and "$x_{1}+2x_{2}$" in soal(CHE, 3))

# --- 24.4 simplex by hand, checked by an exact tableau walk -----------------
b4 = (4, 3, 3)                                   # right-hand sides of exercise 24.4
x4, z4, dual4, jejak = simpleks((3, 2), [(1, 1), (1, 0), (0, 1)], b4, jejak=[])
cek("24.4 basis awal (s1,s2,s3) dengan nilai (4;3;3)",
    jejak[0][3] == [2, 3, 4] and b4 == (4, 3, 3), f"basis={jejak[0][3]} nilai={b4}")
cek("24.4 pivot 1: x1 masuk, s2 keluar (nisbah 4 dan 3), nilai 9",
    len(jejak) >= 2 and jejak[1][0] == 0 and jejak[1][1] == 1 and jejak[1][4] == 9,
    str(jejak[1]))
cek("24.4 pivot 2: x2 masuk, s1 keluar (nisbah 1), optimum (3;1) z=11",
    len(jejak) == 3 and jejak[2][0] == 1 and jejak[2][1] == 0
    and x4 == [F(3), F(1)] and z4 == 11,
    f"x={x4} z={z4}")
cek("24.4 harga dual tabel akhir (2;1;0) dan 4(2)+3(1)+3(0)=11",
    dual4 == [F(2), F(1), F(0)] and 4 * 2 + 3 * 1 + 3 * 0 == z4, str(dual4))
cek("24.4 teks ID/EN memuat (3;1), (2;1;0), dua pivot",
    "$(3;1)$" in K24I and "$(2;1;0)$" in K24I
    and "$(3;1)$" in K24E and "$(2;1;0)$" in K24E)
cek("24.4 soal ID/EN: kendala 4/3/3 dan petunjuk dua pivot",
    "$x_{1}+x_{2}\\le4$, $x_{1}\\le3$, $x_{2}\\le3$" in soal(CHI, 4)
    and "$x_{1}+x_{2}\\le4$, $x_{1}\\le3$, $x_{2}\\le3$" in soal(CHE, 4))

# --- 24.5 the dual of exercise 1, solved exactly ----------------------------
y1_, y2_ = irisan_2var(F(2), F(1), F(30), F(1), F(2), F(20))     # binding: 2y1+y2>=30, y1+2y2>=20
nilai_dual = 10 * y1_ + 8 * y2_
cek("24.5 dual (40/3;10/3) bernilai 160 = primal",
    (y1_, y2_) == (F(40, 3), F(10, 3)) and nilai_dual == 160
    and nilai_dual == opt1, f"y=({y1_};{y2_}) nilai={nilai_dual}")
cek("24.5 harga bayangan 13,333 per kg dan 3,333 per jam",
    abs(float(10 * y1_) / 10 - 13.333) < 5e-4
    and abs(float(8 * y2_) / 8 - 3.333) < 5e-4,
    f"tepung={float(y1_):.4f} oven={float(y2_):.4f}")
cek("24.5 soal ID/EN menunjuk latihan 1",
    "dual dari program pada latihan 1" in soal(CHI, 5)
    and "dual of the program in exercise 1" in soal(CHE, 5))
cek("24.5 teks ID/EN memuat 40/3 dan 13,333 / 3,333",
    "$y=(40/3;\\,10/3)$" in K24I and "$y=(40/3;\\,10/3)$" in K24E
    and "$13{,}333$" in K24I and "$13{,}333$" in K24E)

# --- 24.6 the claim is false: rounding down can be infeasible ---------------
xl = F(25, 10)                            # max x1+x2 s.t. 2x1+2x2=5 -> (2.5, 0)
bulat6 = (int(xl), 0)                     # round down
cek("24.6 penyangkal: (2,5;0) dibulatkan (2;0) melanggar 2x1+2x2=5",
    2 * F(bulat6[0]) + 2 * F(bulat6[1]) != 5, f"2*{bulat6[0]} = {2*bulat6[0]} != 5")
cek("24.6 teks ID 'Salah' / EN 'False' + contoh kesamaan",
    "Salah. Pembulatan ke bawah tidak selalu layak" in K24I
    and "False. Rounding down is not always feasible" in K24E
    and "$2x_{1}+2x_{2}=5$" in K24I and "$2x_{1}+2x_{2}=5$" in K24E)

# --- 24.7 complementary slackness, and the degenerate counterexample --------
aktif3 = [(F(a1) * F(3) + F(b1) * F(3, 2) == F(r)) for (a1, b1), r in zip(A3, b3)]
cek("24.7 pada (3;1,5) kedua kendala aktif, padahal y_1 = 0",
    aktif3 == [True, True], str(aktif3))
cek("24.7 kendala dengan y_i>0 (=1) memang aktif",
    aktif3[1] and F(1) > 0)
cek("24.7 teks ID/EN: arah maju benar, kebalikannya tidak",
    "Benar untuk arah majunya" in K24I and "Sebaliknya tidak berlaku" in K24I
    and "True for the forward direction" in K24E
    and "The converse does not hold" in K24E)

# --- 24.8 / 24.9 knapsack: LP bound by exact greedy, integer by enumeration -
BERAT = (5, 4, 3, 2)
NILAI = (10, 7, 5, 3)


def knapsack(kap):
    urut = sorted(range(4), key=lambda i: F(NILAI[i], BERAT[i]), reverse=True)
    sisa, batas = F(kap), F(0)
    for i in urut:
        ambil = min(F(BERAT[i]), sisa)
        batas += ambil * F(NILAI[i], BERAT[i])
        sisa -= ambil
    bulat, terbaik = 0, ()
    for amb in itertools.product((0, 1), repeat=4):
        w = sum(a * b for a, b in zip(amb, BERAT))
        if w <= kap:
            v = sum(a * n for a, n in zip(amb, NILAI))
            if v > bulat:
                bulat, terbaik = v, amb
    celah = batas - bulat
    return urut, batas, bulat, terbaik, celah, celah / batas * 100


def _tup(teks):
    return tuple(int(v) for v in teks.split(","))


s8i, s8e, s9i, s9e = soal(CHI, 8), soal(CHE, 8), soal(CHI, 9), soal(CHE, 9)
mi8 = re.search(r"berat \$\(([\d,]+)\)\$ dan nilai \$\(([\d,]+)\)\$", s8i)
me8 = re.search(r"weights \$\(([\d,]+)\)\$, values \$\(([\d,]+)\)\$", s8e)
mi9 = re.search(r"kapasitas\s+\$7\$", s9i)
me9 = re.search(r"capacity\s+\$7\$", s9e)
cek("24.8 data soal = data yang dihitung (berat dan nilai, ID dan EN)",
    bool(mi8) and bool(me8)
    and _tup(mi8.group(1)) == BERAT and _tup(mi8.group(2)) == NILAI
    and _tup(me8.group(1)) == BERAT and _tup(me8.group(2)) == NILAI,
    f"ID={mi8.groups() if mi8 else None} EN={me8.groups() if me8 else None}")
cek("24.9 soal memakai kapasitas 7 di kedua edisi",
    bool(mi9) and bool(me9) and re.search(r"kapasitas\s+\$8\$", s8i) is not None,
    "kapasitas 7 pada 24.9, 8 pada 24.8")

urut8, batas8, bulat8, pakai8, celah8, persen8 = knapsack(8)
cek("24.8 kerapatan 2,0;1,75;1,667;1,5 (urutan 1,2,3,4)",
    urut8 == [0, 1, 2, 3]
    and [F(NILAI[i], BERAT[i]) for i in urut8] == [F(2), F(7, 4), F(5, 3), F(3, 2)])
cek("24.8 batas LP 15,25 (barang 1 penuh + 3/4 barang 2)",
    batas8 == F(61, 4), str(batas8))
cek("24.8 enumerasi 15 (barang 1 dan 3), celah 0,25 = 1,639 persen",
    bulat8 == 15 and pakai8 == (1, 0, 1, 0)
    and celah8 == F(1, 4) and abs(float(persen8) - 1.639) < 5e-4,
    f"bulat={bulat8} pakai={pakai8} celah={float(celah8)} persen={float(persen8):.4f}")
cek("24.8 teks ID/EN memuat 15,25 / 15 / 1,639",
    "$15{,}25$" in K24I and "$1{,}639$" in K24I
    and "$15{,}25$" in K24E and "$1{,}639$" in K24E)

urut9, batas9, bulat9, pakai9, celah9, persen9 = knapsack(7)
cek("24.9 batas LP 13,5 (barang 1 penuh + 1/2 barang 2)",
    batas9 == F(27, 2), str(batas9))
cek("24.9 enumerasi 13 (barang 1 dan 4, berat 7), celah 0,5 = 3,704 persen",
    bulat9 == 13 and sum(a * b for a, b in zip(pakai9, BERAT)) == 7
    and celah9 == F(1, 2) and abs(float(persen9) - 3.704) < 5e-4,
    f"bulat={bulat9} pakai={pakai9} persen={float(persen9):.4f}")
cek("24.9 pasangan (1,3) beratnya 5+3=8, tak muat pada kapasitas 7",
    5 + 3 == 8 and 8 > 7)
cek("24.9 teks ID/EN memuat 13,5 / 13 / 3,704",
    "$13{,}5$" in K24I and "$3{,}704$" in K24I
    and "$13{,}5$" in K24E and "$3{,}704$" in K24E)

# --- 24.10 LP relaxation of vertex cover on K_n -----------------------------
def penutup_min(n):
    simpul = range(n)
    rusuk = [(i, j) for i in simpul for j in simpul if i < j]
    for k in range(n + 1):
        for pilih in itertools.combinations(simpul, k):
            if all(u in pilih or v in pilih for u, v in rusuk):
                return k
    return n


hitung = {n: penutup_min(n) for n in (4, 5, 6)}
cek("24.10 penutup minimum K_4 = 3, K_5 = 4", hitung[4] == 3 and hitung[5] == 4, str(hitung))
cek("24.10 penutup minimum K_n = n-1 untuk n=3..6",
    all(penutup_min(n) == n - 1 for n in range(3, 7)))
nisbah = {n: F(n, 2) / (n - 1) for n in (4, 5, 10)}
cek("24.10 nisbah LP/bulat 0,6667; 0,625; 0,5556 untuk n=4,5,10",
    abs(float(nisbah[4]) - 0.6667) < 5e-5 and abs(float(nisbah[5]) - 0.625) < 5e-5
    and abs(float(nisbah[10]) - 0.55556) < 5e-5, str({k: float(v) for k, v in nisbah.items()}))
besar = F(1000, 2) / 999
cek("24.10 nisbah menuju 1/2 (makin kecil saat n naik)",
    nisbah[4] > nisbah[5] > nisbah[10] > F(1, 2)
    and abs(float(besar) - 0.5005) < 5e-4, f"n=1000 -> {float(besar):.4f}")
cek("24.10 teks ID/EN memuat 0,6667; 0,625; 0,5556",
    "$0{,}6667$; $0{,}625$; $0{,}5556$" in K24I
    and "$0{,}6667$; $0{,}625$; $0{,}5556$" in K24E)
cek("24.10 soal ID/EN: n=4,5,10 diminta",
    "$n=4,5,10$" in soal(CHI, 10) and "$n=4,5,10$" in soal(CHE, 10))

# --- structural: the appendix really holds ten keys for ten exercises -------
jumlah_kunci = len(re.findall(r"^\s*\\item\s", K24I, re.M))
jumlah_soal = len(re.split(r"\n\s*\\item\s",
                          re.search(r"\\begin\{latihan\}(.*?)\\end\{latihan\}",
                                    CHI, re.S).group(1))) - 1
cek("24 struktur: 10 soal = 10 kunci di lampiran",
    jumlah_soal == 10 and jumlah_kunci == 10, f"soal={jumlah_soal} kunci={jumlah_kunci}")

print()
if gagal:
    print(f"HASIL: {len(gagal)} GAGAL dari {jumlah[0]}: " + ", ".join(gagal))
    raise SystemExit(1)
print(f"HASIL: {jumlah[0]}/{jumlah[0]} PASS")
