PY ?= python3

.PHONY: test check status pdf clean

test:            ## uji kerangka: gerbang mutu (positif+negatif) + kompilasi main.tex
	$(PY) test_gerbang.py

check:           ## gerbang mutu per bab pada naskah asli
	$(PY) build_ed2.py check

status:          ## bab mana yang sudah ada
	$(PY) build_ed2.py status

pdf:             ## rakit PDF ke pdf/ (../pdf/Kitab-STEM-Kenapa-Mesin-Bisa-Salah.pdf)
	$(PY) build_ed2.py pdf

clean:           ## buang berkas antara LaTeX, sisakan main.pdf
	rm -f main.aux main.idx main.ind main.ilg main.log main.out main.toc main.ilg
