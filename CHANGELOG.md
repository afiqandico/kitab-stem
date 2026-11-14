# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.0.0] — 2026-11-14

Second edition, Indonesian and English editions rebuilt from source. This is the first
citable v2 artifact; v1.0.0 remains available from its own release.

### Added

- `Kitab-STEM-Kenapa-Mesin-Bisa-Salah.pdf` — Indonesian edition, **646 pages**,
  3,727,813 bytes, sha256 `19b819485925e6aaf672a9bd8e88be5b3757781f2ec5d744cba0cb3f7d80e236`.
- `Kitab-STEM-Why-Machines-Can-Be-Wrong.pdf` — English edition, **640 pages**,
  3,814,507 bytes, sha256 `356febf8d63e2afbb1208e8c89eee39fe6fcdb0b8439c5342c8809cc21ff0259`.
- 32 chapters per language (v1 had 13). Exercise-key coverage checker reports 304 exercise
  items and 304 keyed items, 1:1 in every chapter.
- `_buku-ed2/` and `_buku-en/` sources now carry their checkers and audit notes, so the
  published PDFs can be rebuilt from this repository alone.

### Changed

- `CITATION.cff` version 2.0.0, released 2026-11-14.

### Fixed

- The English build depended on leftover auxiliary files. Building on top of a stale
  `main-en.aux/.toc/.ind` produced a PDF with a different sha256 while every gate still
  reported zero problems. `_buku-en/tools/cek-en.py --pdf` now deletes those files before
  the first pass. Two consecutive builds, and a build from a separate checkout, now agree
  byte for byte.

### Reproducibility

- Both editions build deterministically (`SOURCE_DATE_EPOCH=1792857600`,
  `FORCE_SOURCE_DATE=1`). Verified by rebuilding from a second copy of the published
  sources: identical sha256 for both PDFs.


## [1.0.2] — 2026-11-13

### Fixed

- **English edition: blank "Contents" page.** The front matter typeset
  `\tableofcontents` twice — once in `_buku-en/main-en.tex` (line 32) and once again at
  the end of `_buku-en/belakang/depan-c-en.tex`. The second copy produced one page headed
  "Contents" with no entries at all (page 16 of the previous 638-page PDF). The block was
  removed and replaced by `\addcontentsline{toc}{chapter}{List of Figures}`, so the list of
  figures is now listed in the table of contents as well.
- `Kitab-STEM-Why-Machines-Can-Be-Wrong.pdf` rebuilt: **638 → 640 pages**, no blank page,
  0 duplicate labels, 0 leaked headers, 352 index entries.

The Indonesian edition (`Kitab-STEM-Kenapa-Mesin-Bisa-Salah.pdf`, 643 pages) is unaffected:
its source typesets the table of contents once, and pages 1–20 contain no blank page.

## [1.0.1] — 2026-11-07

### Fixed

- Build-script path fix. The published PDFs are identical to v1.0.0.

## [1.0.0] — 2026-11-07

First release, two languages; text under CC BY 4.0 and code under MIT.

### Added

- `Kitab-STEM-Kenapa-Mesin-Bisa-Salah.pdf` (3.72 MB) — Indonesian edition.
- `Kitab-STEM-Why-Machines-Can-Be-Wrong.pdf` (3.80 MB) — English edition.
- `CITATION.cff` (CFF 1.2.0) with licence `CC-BY-4.0` and `language: id`.
- `Makefile` that builds the PDFs from the LaTeX sources in `_buku/` and `_buku-en/`.

[2.0.0]: https://github.com/afiqandico/kitab-stem/releases/tag/v2.0.0
[Unreleased]: https://github.com/afiqandico/kitab-stem/compare/v2.0.0...HEAD
[1.0.2]: https://github.com/afiqandico/kitab-stem/releases/tag/v1.0.2
[1.0.1]: https://github.com/afiqandico/kitab-stem/releases/tag/v1.0.1
[1.0.0]: https://github.com/afiqandico/kitab-stem/releases/tag/v1.0.0
