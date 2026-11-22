#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261122 bounty,
"Sum up 22 November's world news in one image".

The artwork -- one front page covering Sunday 22 November 2026,
35 stories across 6 regions -- is stored in this repository as
entry.png. (Its bytes are a JPEG; the gate identifies the format
from the file's magic bytes, so the .png name is fine.) All this
program does is deliver that artwork, untouched, to
/output/entry.png on every run.

Nothing here needs the network, and only the standard library is
used, so the output bytes never vary between runs.
"""

import os
import sys


def main() -> int:
    # Read and write in binary so no newline or encoding translation
    # can creep in: the judged bytes are the stored bytes.
    # The judged file is exactly the stored bytes: entry.png is a
    # JPEG by magic bytes, and the .png name is what the rules ask
    # for, so copy it verbatim and never re-encode it.
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.png"), "rb") as fh:
        payload = fh.read()
    if not payload:
        raise SystemExit("entry.png is empty; refusing to write a blank entry")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as fh:
        fh.write(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
