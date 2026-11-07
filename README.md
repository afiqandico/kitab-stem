# Why Machines Can Be Wrong / Kenapa Mesin Bisa Salah?

A tiered textbook — from linear algebra to *machine learning* security — in **two
parallel editions**: Indonesian and English. Every chapter carries tiered reader
paths (child, undergraduate, lecturer, researcher), worked examples whose numbers
come from actual executions, exercises, and answer keys.

**Author:** Afiq Andico Pangimpian
**Edition:** First, 2026 · **32 chapters**, 6 parts, 304 exercises, 304 keys
**License:** text CC BY 4.0 · code MIT · **Book pages:** 643 (ID) / 638 (EN)

| File | Content |
|---|---|
| `Kitab-STEM-Kenapa-Mesin-Bisa-Salah.pdf` | Indonesian edition, 643 pages, 3.54 MB |
| `Kitab-STEM-Why-Machines-Can-Be-Wrong.pdf` | English edition, 638 pages, 3.80 MB |
| `_buku-ed2/` | LaTeX source of the Indonesian edition + quality gates + verification tools |
| `_buku-en/` | LaTeX source of the English edition + translation-parity gates |

## Book contents

Six parts, 32 chapters: **(I)** mathematical foundations — linear algebra, real
analysis, probability, optimisation; **(II)** machine learning — generalisation,
honest evaluation; **(III)** formal methods with Lean 4; **(IV)** adversarial
machine learning and its defences; **(V)** attack surfaces, NIDS, post-quantum
cryptography; **(VI)** differential privacy and the mathematical foundations of
QML.

## Rebuilding

Prerequisites: TeX Live (pdflatex, makeindex), Python 3 with `numpy`, `scipy`,
`sympy`; Lean 4 (optional, only for the chapter 28 checker).

```bash
make check   # quality gate: 32 chapters, body words, glossary, exercise<->key mapping
make test    # skeleton tests (36 checks) + sandbox compilation
make pdf     # build the Indonesian PDF
cd _buku-en && python3 tools/cek-en.py --pdf   # build + English PDF gate
```

Builds are **reproducible**: two consecutive builds produce an identical sha256.

| Artifact | sha256 |
|---|---|
| Indonesian edition | `d66d9c2f30704c30df98d0e666acc2f14f8be00988fcb102cc966fca6de614e9` |
| English edition | `64e0e90f06a8aa6dac840800a619a89d073b60ccb41824821c4d2da272172f9c` |

## Verification you can run yourself

Every number in the answer keys is re-checked with real computation, and the
checkers ship in the repo — these are not claims:

```bash
cd _buku-ed2
python3 tools/cek-cacah-kunci.py      # 304 exercises <-> 304 keys, 1:1 across 32 chapters
python3 tools/cek-kunci-01-05.py      # key numbers, chapters 1-5
python3 tools/verify-kunci-06-15.py   # 37 checks (6.5, 9.9, 12.2, 13.7, 14.5)
python3 tools/verify-kunci-16-23.py   # 36 checks (18.8, 18.10, 19.10, 20.4, 20.7)
python3 tools/verify-kunci-21-25.py   # 38 checks (21.5, 21.9, 22.10, 25.5, 25.9)
python3 tools/verify-kunci-26-32.py   # 20 checks, runs Lean in tools/lean-28/
cd ../_buku-en
python3 tools/cek-en.py               # parity of both editions, 32 chapters
python3 tools/cek-belakang.py         # 13 back-matter sections
```

The key audit ran in six waves guided by `_buku-ed2/AUDIT-KUNCI.md` and found
**23 defective key items** (14 in chapters 6–25, 9 in chapters 26–32), plus one
exercise (21.5) and one chapter-text number (chapter 29); all were fixed in both
editions.

## Known limitations (stated, not hidden)

- **30.5** asks for three numbers on a two-layer model whose width is not given
  in the exercise; the key only provides a qualitative estimate.
- **29.4**: the 95.48 percent figure is valid for one random draw (`rng(1)`/`rng(2)`;
  `rng(0)` gives 95.64).
- The chapter 29 `lab` block ships only the attack library, without the training
  driver, so tables 29.5/29.9 cannot be reproduced from the repo without writing
  a driver.
- ID↔EN parity proves the translation is faithful to its source, **not** that the
  source is correct; content correctness is guarded by the key audit above.
- This repo contains **original writing and code**, not the copyrighted source
  books used as writing references.

## Citation

See `CITATION.cff`. Short form:

> Pangimpian, A. A. (2026). *Kenapa Mesin Bisa Salah? Dari Aljabar Linear sampai
> Keamanan Machine Learning* (First Edition, v1.0.0). CC BY 4.0.

## License

- **Book text** (both editions, including the PDFs): [CC BY 4.0](LICENSE) — free
  to use, share, and adapt with attribution.
- **Code** (build scripts, gates, checkers under `tools/`): [MIT](LICENSE-CODE).
