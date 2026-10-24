"""Verify every packaged file listed in PUBLIC_CHECKSUMS.sha256 (standard library only)."""

import hashlib
from pathlib import Path
import sys


def main():
    root = Path(__file__).resolve().parent
    failed = []
    count = 0
    for line in (root / "PUBLIC_CHECKSUMS.sha256").read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        path = root / relative
        if not path.is_file():
            failed.append("MISSING " + relative)
            continue
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        if digest.hexdigest() != expected:
            failed.append("MISMATCH " + relative)
        count += 1
    for item in failed:
        print(item)
    print(f"Checked {count} files; {len(failed)} errors.")
    return bool(failed)


if __name__ == "__main__":
    sys.exit(main())
