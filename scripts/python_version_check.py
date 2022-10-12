#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    PYTHON_MIN_VERSION_MAJOR = 3
    PYTHON_MIN_VERSION_MINOR = 6
    PYTHON_MIN_VERSION = (PYTHON_MIN_VERSION_MAJOR, PYTHON_MIN_VERSION_MINOR)

    if sys.version_info < PYTHON_MIN_VERSION:
        sys.stderr.write(
            f"\n\nPython {PYTHON_MIN_VERSION_MAJOR}.{PYTHON_MIN_VERSION_MINOR} or above is required.\n\n\n"
        )

        exit(1)
