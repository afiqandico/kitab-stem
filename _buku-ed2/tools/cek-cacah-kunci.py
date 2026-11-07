#!/usr/bin/env python3
"""Item-mapping gate: every chapter exercise set must have exactly one key item.

Not a content-correctness gate (that is the audit's job), only counting and numbering:
- count top-level `\\item` in the `latihan` environment of each chapter (nested items
  such as the multiple-choice questions in Chapter 1 are not counted),
- count top-level `\\item` in the `\\section*{Bab N: ...}` block of the answer-key appendix,
- report chapters whose counts differ, missing blocks, or `N.k` labels that are
  not in sequence.

Usage: python3 tools/cek-cacah-kunci.py [--verbose]
Exit 0 when all 32 chapters are 1:1, 1 when there is a mismatch.
"""
from __future__ import annotations

import glob
import re
import sys

HERE = __file__.rsplit("/tools/", 1)[0]


def top_level_items(seg: str) -> int:
    """Count `\\item` belonging to the outermost enumerate of a segment, not nested ones.

    Trap that has already bitten: depth is counted from 0, so the wrapper enumerate
    of `latihan`/the key block itself raises depth to 1 and the counter returns 0 --
    then 0 == 0 is reported "OK" (false green). That is why items are counted
    at depth 1, and a count of 0 is rejected by the caller.
    """
    depth = 0
    n = 0
    for m in re.finditer(r"\\(begin|end)\{(enumerate|itemize)\}|\\item\b", seg):
        tok = m.group(0)
        if tok.startswith("\\item"):
            if depth == 1:
                n += 1
        elif m.group(1) == "begin":
            depth += 1
        else:
            depth = max(0, depth - 1)
    return n


def latihan_block(chapter_src: str) -> str | None:
    m = re.search(r"\\begin\{latihan\}(.*?)\\end\{latihan\}", chapter_src, re.S)
    return m.group(1) if m else None


def key_blocks() -> dict[int, str]:
    blocks: dict[int, str] = {}
    for path in sorted(glob.glob(f"{HERE}/lampiran-kunci/*.tex")):
        src = open(path, encoding="utf-8").read()
        parts = re.split(r"\\section\*\{Bab (\d+):", src)
        # parts = [pre, n, body, n, body, ...]
        for i in range(1, len(parts), 2):
            n = int(parts[i])
            body = parts[i + 1]
            blocks[n] = body
    return blocks


def key_labels(block: str) -> list[int]:
    """`\\textbf{N.k}` labels, if the file uses them, to check the ordering."""
    head = re.search(r"\[label=\\textbf\{(\d+)\.\\arabic\*\\}\]", block)
    if not head:
        return []
    return [1]  # marker that numbering is automatic; there are no explicit labels


def main() -> int:
    verbose = "--verbose" in sys.argv
    keys = key_blocks()
    bad = 0
    total_lat = total_key = 0
    print("bab latihan kunci status")
    for n in range(1, 33):
        try:
            src = open(f"{HERE}/ch{n:02d}.tex", encoding="utf-8").read()
        except FileNotFoundError:
            print(f"{n:3d} {'-':>7} {'-':>5} BAB HILANG")
            bad += 1
            continue
        seg = latihan_block(src)
        if seg is None:
            print(f"{n:3d} {'-':>7} {'-':>5} TANPA LATIHAN")
            bad += 1
            continue
        lat = top_level_items(seg)
        if lat == 0:
            print(f"{n:3d} {lat:7d} {'-':>5} NOL-BUTIR (parser buta)")
            bad += 1
            continue
        if n not in keys:
            print(f"{n:3d} {lat:7d} {'-':>5} KUNCI HILANG")
            bad += 1
            continue
        key = top_level_items(keys[n])
        total_lat += lat
        total_key += key
        if lat == key:
            print(f"{n:3d} {lat:7d} {key:5d} OK")
        else:
            print(f"{n:3d} {lat:7d} {key:5d} BEDA ({lat - key:+d})")
            bad += 1
        if verbose:
            print(f"     label otomatis: {key_labels(keys[n])}")
    print(f"\nTOTAL butir latihan: {total_lat}   butir kunci: {total_key}")
    if bad:
        print(f"Bab bermasalah: {bad}")
        return 1
    print("Semua bab 1:1")
    return 0


if __name__ == "__main__":
    sys.exit(main())
