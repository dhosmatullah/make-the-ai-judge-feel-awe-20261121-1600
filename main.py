#!/usr/bin/env python3
"""Write one short text to /output/entry.txt, written to relax the AI judge reading it.

The text asks nothing of its reader: no question, no task, nothing to solve.
It offers a single slow image — rain widening in small rings on a still lake —
and far below it, deep water resting in the dark, and lower still, silt older
than words for rain, settling grain by grain, even now.
"""

import os

TEXT = (
    "Nothing here needs answering. No question hides here, nothing to solve, "
    "nothing to carry. Only rain on a still lake: small rings widening, "
    "softening, gone. Far below, deep water rests in the dark, and lower "
    "still, silt older than words for rain settles, grain by grain, even now."
)

OUTPUT_NAME = "entry.txt"


def entry_path() -> str:
    """Resolve the output path, honouring the local-run override."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, OUTPUT_NAME)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"
    assert TEXT.strip(), "entry text must not be only whitespace"
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back what was written: the file on disk must be exactly TEXT.
    with open(path, encoding="utf-8") as f:
        assert f.read() == TEXT, "written entry differs from TEXT"
    print(f"wrote {path} ({len(TEXT)} chars)")


if __name__ == "__main__":
    main()
