"""Copy shadow.jpg unchanged to entry.png in MAKEFUN_OUTPUT_DIR (default /output)."""

import os
import shutil


def main():
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shadow.jpg")
    if not os.path.isfile(source):
        raise SystemExit("Image missing: place shadow.jpg beside main.py and try again.")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(output_dir, "entry.png"))


if __name__ == "__main__":
    main()
