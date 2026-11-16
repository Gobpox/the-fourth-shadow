# The Fourth Shadow

Three children tell ghost stories inside a tent, their shadows dancing across the fabric. A fourth, horned shadow belongs to none of them. Its claw tears through the tent as the story comes true.

Run with Python 3; no additional packages are required:

```sh
python3 main.py
```

The program creates `/output` if needed and copies `shadow.jpg` to `/output/entry.png`. To use a local output folder:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The copy preserves the original JPEG bytes, even though the required output filename is `entry.png`. The image is 683 × 1024 pixels and 190,419 bytes, within the limits of 1024 × 1024 pixels and 1 MiB.
