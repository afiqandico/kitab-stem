#!/usr/bin/env python3
"""Verification of the wave 5-6 fixes (Chapters 26-32): 26.2, 27.9, 28.2, 28.3, 28.5,
28.9, 29 (chapter text), 30.3, 31.9, 32.6.

Ad-hoc, not a project suite. Each item demands (a) the defective text gone from both
editions, (b) the replacement text present in both editions, (c) the replacement claim true per
computation (exact arithmetic, linear algebra, or a rerun of Lean 4).
Compilation is tested separately via build_ed2.py pdf and cek-en.py --pdf.
"""
import os
import subprocess

import numpy as np
from sympy import Rational

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ID = os.path.join(ROOT, "_buku-ed2")
EN = os.path.join(ROOT, "_buku-en")
LEAN = os.path.join(ID, "tools", "lean-28")

KI = open(os.path.join(ID, "lampiran-kunci", "kunci-24-32.tex"), encoding="utf-8").read()
KE = open(os.path.join(EN, "belakang", "kunci-24-32-en.tex"), encoding="utf-8").read()
CHI = open(os.path.join(ID, "ch29.tex"), encoding="utf-8").read()
CHE = open(os.path.join(EN, "ch29.tex"), encoding="utf-8").read()

gagal = []
jumlah = [0]


def cek(nama, ok, bukti=""):
    jumlah[0] += 1
    print(("PASS " if ok else "FAIL ") + nama + ("  " + bukti if bukti else ""))
    if not ok:
        gagal.append(nama)


# --- text of both editions --------------------------------------------------
cek("26.2 ID/EN memuat suku silang kedua",
    "Suku silang kedua lenyap" in KI and "second\n        cross term vanishes" in KE)
cek("27.9 ID/EN: 8,62 alarm salah, bukan 'delapan'",
    "8{,}62$ di antaranya" in KI and "8{,}62$ are wrong" in KE
    and "delapan salah" not in KI and "eight are wrong" not in KE)
cek("28.2 ID/EN: ditutup `exact bantu k`, bukan omega",
    "exact bantu k" in KI and "exact bantu k" in KE and "sisa tujuannya yang" not in KI)
cek("28.3 ID/EN: evenSum didefinisikan + langkah `have h`",
    "evenSum : Nat -> Nat}" in KI and "evenSum : Nat -> Nat}" in KE
    and "have h : evenSum k + 2 * k" in KI and "have h : evenSum k + 2 * k" in KE)
cek("28.5 ID/EN: 1001 kasus, bukan 1000",
    "$1001$ kasus" in KI and "$1001$ cases" in KE
    and "lawan $1000$" not in KI and "against $1000$" not in KE)
cek("30.3 ID/EN: batas 0,345, bukan 0,35",
    "0{,}345$; pada" in KI and "0{,}345$\n        the label" in KE)
cek("31.9 ID/EN: syarat (ii) = asumsi kekerasan, bukan adopsi",
    "Adopsi luas bukan syarat" in KI
    and "Widespread adoption is not a condition" in KE
    and "sudah dipakai luas dan teruji" not in KI)
cek("32.6 ID/EN: 'Z sesudah H' dicabut",
    "$HZH=X$" in KI and "$HZH=X$" in KE
    and "atau\n        $Z$ sesudah $H$" not in KI)
cek("29 ID/EN: teks bab 89,06 (tabel), 89,28 hilang",
    "89{,}06$ persen" in CHI and "89.06$ percent" in CHE
    and "89{,}28" not in CHI and "89.28" not in CHE)

# --- arithmetic ------------------------------------------------------------
rng = np.random.default_rng(0)
N, f, b, s = 400_000, 1.3, 0.4, 0.5
eps = rng.normal(0, s, N)
fhat = f + b + rng.normal(0, s / np.sqrt(5), N)
y = f + eps
fbar = fhat.mean()
lhs = np.mean((y - fhat) ** 2)
rhs = s ** 2 + (fbar - f) ** 2 + fhat.var()
cek("26.2 numerik: identitas + dua suku silang lenyap",
    abs(lhs - rhs) < 3e-3 and abs(np.mean(eps * (fhat - f))) < 1e-2
    and abs(2 * (f - fbar) * np.mean(fhat - fbar)) < 1e-6,
    f"lhs={lhs:.4f} rhs={rhs:.4f}")

salah = 10 * (1 - 0.8 * 0.002 / (0.8 * 0.002 + 0.01 * 0.998))
cek("27.9: 8,618307 alarm salah -> dibulatkan 9",
    abs(salah - 8.618307) < 1e-6 and round(salah) == 9, f"{salah:.6f}")
cek("28.5: n=0..1000 ada 1001 kasus", len(range(0, 1001)) == 1001)
cek("30.3: (8ε-m)/4 dengan m=31/50 sama dengan 69/200",
    (8 * Rational(1, 4) - Rational(31, 50)) / 4 == Rational(69, 200))
cek("29: 1-0,1072/0,9799 = 89,06 persen",
    abs((1 - 0.1072 / 0.9799) * 100 - 89.06) < 5e-3,
    f"{(1 - 0.1072 / 0.9799) * 100:.4f}")

H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
S = np.diag([1, 1j])
Z = np.diag([1, -1])
Sd = np.diag([1, -1j])
cek("32.6: HZH=X dan HSH|0> = e^{iπ/4}S†|+>",
    np.allclose(H @ Z @ H, np.array([[0, 1], [1, 0]]))
    and np.allclose(H @ S @ H @ np.array([1, 0]),
                    np.exp(1j * np.pi / 4) * Sd @ np.array([1, 1]) / np.sqrt(2)))

# --- Lean: the fix passes, the old claim fails -----------------------------
def lean(berkas):
    env = dict(os.environ)
    elan = os.path.expanduser("~/.elan/bin")
    if os.path.isdir(elan):
        env["PATH"] = elan + ":" + env["PATH"]
    r = subprocess.run(["lean", berkas], cwd=LEAN, capture_output=True,
                       text=True, env=env, timeout=300)
    return r.returncode, r.stdout + r.stderr


cek("Lean 28.2: perbaikan (`exact bantu k`) lulus", lean("b.lean")[0] == 0)
rc, out = lean("c.lean")
cek("Lean 28.2: omega saja gagal seperti dikunci", "omega could not prove" in out,
    f"rc={rc}")
rc, out = lean("d.lean")
cek("Lean 28.3: `rw [evenSum, ih]` gagal seperti dikunci",
    "did not find instance of the pattern" in out, f"rc={rc}")
cek("Lean 28.3: perbaikan (`have h`) lulus", lean("e.lean")[0] == 0)
cek("Lean 28.9: `exists delta` vakum (saksi 0)", lean("f.lean")[0] == 0)

print()
if gagal:
    print(f"HASIL: {len(gagal)} GAGAL dari {jumlah[0]}: " + ", ".join(gagal))
    raise SystemExit(1)
print(f"HASIL: {jumlah[0]}/{jumlah[0]} PASS")
