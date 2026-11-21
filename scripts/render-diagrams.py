#!/usr/bin/env python3
"""Render the Mermaid sources and both responsive image formats used on How it works."""

import os
from pathlib import Path
import subprocess
import tempfile

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
DIAGRAMS = Path("static/images/diagrams")
RENDERER = (
    "ghcr.io/mermaid-js/mermaid-cli/mermaid-cli:11.12.0"
    "@sha256:bad64c9d9ad917c8dfbe9d9e9c162b96f6615ff019b37058638d16eb27ce7783"
)
BACKGROUND = "#0e0e0e"
CANVASES = {
    "from-app-to-package": (1858, 3700),
    "from-package-to-user": (2014, 4200),
}


def main():
    # Stage both diagrams before replacing any published image.
    with tempfile.TemporaryDirectory(dir=ROOT) as work:
        staged = Path(work)
        for name, size in CANVASES.items():
            raw = staged / f"{name}.png"
            subprocess.run(
                [
                    "docker", "run", "--rm", "--network", "none",
                    "--user", f"{os.getuid()}:{os.getgid()}",
                    "-v", f"{ROOT}:/data:ro", "-v", f"{staged}:/out",
                    RENDERER, "-i", str(DIAGRAMS / f"{name}.mmd"),
                    "-o", f"/out/{raw.name}", "-c", "scripts/mermaid-config.json",
                    "-w", "1600", "-s", "2", "-b", BACKGROUND,
                ],
                check=True,
            )
            with Image.open(raw) as image:
                full = ImageOps.pad(image.convert("RGB"), size, Image.Resampling.LANCZOS,
                                    color=BACKGROUND)
            for width in (1120, size[0]):
                height = round(width * size[1] / size[0])
                output = full.resize((width, height), Image.Resampling.LANCZOS)
                output.save(staged / f"{name}-{width}.png", optimize=True)
                output.save(staged / f"{name}-{width}.webp", lossless=True, method=6)

        for asset in staged.glob("*-[0-9]*.*"):
            asset.replace(ROOT / DIAGRAMS / asset.name)


if __name__ == "__main__":
    main()
