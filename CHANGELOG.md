# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased] — second edition

Work in progress, not released. Working files: `_buku-ed2/` (`SPEC-BAB-ED2.md`,
`PANDUAN-BAB-ED2.md`, `AUDIT-KUNCI.md`, `ch06.tex`). No second-edition PDF has been
published, so nothing can be cited as v2 yet.

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

[Unreleased]: https://github.com/afiqandico/kitab-stem/compare/v1.0.2...HEAD
[1.0.2]: https://github.com/afiqandico/kitab-stem/releases/tag/v1.0.2
[1.0.1]: https://github.com/afiqandico/kitab-stem/releases/tag/v1.0.1
[1.0.0]: https://github.com/afiqandico/kitab-stem/releases/tag/v1.0.0
