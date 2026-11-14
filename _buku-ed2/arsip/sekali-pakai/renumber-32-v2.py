"""Renumber 30 -> 32 bab dengan aturan ketat.

Aturan:
  A. Paragraf sitasi (`\\peta{...}` atau "Sumber primer") -> nomor TIDAK diubah,
     kecuali nomor yang langsung diikuti "buku ini" (itu rujukan internal).
  B. Penanda pembuka "\\peta{Bab N pada" selalu diganti ke nomor bab berkas itu.
  C. Paragraf prosa biasa -> semua nomor setelah "Bab" (termasuk rentang) dipetakan.
  D. Rentang di dalam sitasi dilaporkan untuk diperiksa manual.

Pemetaan: 1-15 tetap; 16->17, 17->18, 18->19, 19->20, 20->22, 21->23, ..., 30->32.
"""
import os
import re
import sys

ED2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = {}
for old in range(16, 31):
    MAP[old] = old + 1 if old <= 19 else (22 if old == 20 else old + 2)

BERKAS = re.compile(r"^ch(\d{2})\.tex$")


def petakan(nomor):
    return MAP.get(nomor, nomor)


def ganti_paragraf(p, sitasi):
    pola = re.compile(r"(Bab)(\s*~?\s*)(\d{1,2})((?:\s*(?:--|\u2013|-)\s*\d{1,2})?)")

    def satu(m):
        spasi, angka, ekor = m.group(2), int(m.group(3)), m.group(4)
        sesudah = p[m.end():m.end() + 12]
        internal = "buku ini" in sesudah
        if sitasi and not internal:
            return m.group(0)
        if ekor:
            ekor = re.sub(r"(\s*(?:--|\u2013|-)\s*)(\d{1,2})",
                          lambda mm: mm.group(1) + str(petakan(int(mm.group(2)))), ekor)
        return "Bab%s%d%s" % (spasi, petakan(angka), ekor)

    return pola.sub(satu, p)


def proses(nama, teks):
    nomor_bab = int(BERKAS.match(nama).group(1))
    keluaran = []
    for potong in re.split(r"(\n\s*\n)", teks):
        if not potong.strip():
            keluaran.append(potong)
            continue
        sitasi = ("\\peta{" in potong) or ("Sumber primer" in potong)
        baru = ganti_paragraf(potong, sitasi)
        baru = re.sub(r"(\\peta\{Bab)(\s*~?\s*)(\d{1,2})",
                      lambda m: "%s %d" % (m.group(1), nomor_bab), baru, count=1)
        keluaran.append(baru)
    return "".join(keluaran)


def main():
    ubah = {}
    for nama in sorted(os.listdir(ED2)):
        if not BERKAS.match(nama):
            continue
        path = os.path.join(ED2, nama)
        teks = open(path, encoding="utf-8").read()
        baru = proses(nama, teks)
        if baru != teks:
            beda = sum(1 for a, b in zip(teks.splitlines(), baru.splitlines()) if a != b)
            open(path, "w", encoding="utf-8").write(baru)
            ubah[nama] = beda
    print("berkas diubah:", len(ubah), "| baris berubah:", sum(ubah.values()))
    print(", ".join("%s:%d" % (k[2:4], v) for k, v in sorted(ubah.items())))

    print("\nrentang 'Bab N--M' di paragraf sitasi (periksa manual):")
    for nama in sorted(os.listdir(ED2)):
        if not BERKAS.match(nama):
            continue
        teks = open(os.path.join(ED2, nama), encoding="utf-8").read()
        for p in re.split(r"\n\s*\n", teks):
            if not (("\\peta{" in p) or ("Sumber primer" in p)):
                continue
            for m in re.finditer(r"Bab\s*~?\s*(\d{1,2})\s*(?:--|\u2013|-)\s*(\d{1,2})", p):
                a, b = int(m.group(1)), int(m.group(2))
                if a >= 16 or b >= 16:
                    print("  %s  Bab %d--%d" % (nama, a, b))


if __name__ == "__main__":
    sys.exit(main())
