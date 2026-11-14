"""Renumber 30 -> 32 bab: sisipkan Bab 16 (ODE) dan Bab 21 (Regresi).

Pemetaan lama->baru:
  1-15 tetap; 16->17 ... 19->20; 20->22; 21->23 ... 30->32
Dijalankan menurun supaya tidak ada tabrakan nomor.
"""
import os
import re

ED2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = {}
for old in range(16, 31):
    MAP[old] = old + 1 if old <= 19 else (22 if old == 20 else old + 2)

# 1. ganti nama berkas menurun
for old in sorted(MAP, reverse=True):
    src = os.path.join(ED2, "ch%02d.tex" % old)
    dst = os.path.join(ED2, "ch%02d.tex" % MAP[old])
    if os.path.exists(src):
        os.rename(src, dst)
print("berkas di-rename:", len(MAP))

# 2. ganti rujukan 'Bab N' / 'Bab~N' di semua berkas (menurun)
POLA = re.compile(r"(Bab\s*~?\s*)(\d{1,2})\b")
laporan = {}
for nama in sorted(os.listdir(ED2)):
    if not re.match(r"ch\d{2}\.tex$", nama) and nama != "main.tex":
        continue
    path = os.path.join(ED2, nama)
    teks = open(path, encoding="utf-8").read()
    n = [0]

    def ganti(m):
        num = int(m.group(2))
        if num in MAP:
            n[0] += 1
            return "%s%d" % (m.group(1), MAP[num])
        return m.group(0)

    baru = POLA.sub(ganti, teks)
    if n[0]:
        open(path, "w", encoding="utf-8").write(baru)
        laporan[nama] = n[0]
print("rujukan 'Bab N' diubah:", sum(laporan.values()), "di", len(laporan), "berkas")
for k in sorted(laporan):
    print("  %s %d" % (k, laporan[k]))
