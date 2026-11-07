# Akar proyek kitab STEM. Inti pekerjaan ada di _buku-ed2/.
# make test  -> uji kerangka (gerbang mutu + kompilasi main.tex)
# make check -> gerbang mutu 28 bab pada naskah asli
# make pdf   -> rakit PDF ke akar repo (Kitab-STEM-Kenapa-Mesin-Bisa-Salah.pdf)
BUKU := _buku-ed2

.PHONY: test check status pdf clean

test check status pdf clean:
	$(MAKE) -C $(BUKU) $@
