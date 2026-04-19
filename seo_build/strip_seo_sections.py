# -*- coding: utf-8 -*-
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "index.htm",
    ROOT / "official-site.htm",
    ROOT / "zerkalo.htm",
    ROOT / "vhod.htm",
    ROOT / "registraciya.htm",
    ROOT / "bonus.htm",
    ROOT / "skachat.htm",
    ROOT / "otzyvy.htm",
    ROOT / "play.htm",
    ROOT / "ru" / "index.htm",
]

RX = re.compile(
    r'<section class="seo-text"[^>]*>[\s\S]*?</section>\s*\n(?=\s*<footer class="footer">)',
    re.MULTILINE,
)


def main() -> None:
    for path in FILES:
        text = path.read_text(encoding="utf-8")
        new, n = RX.subn("", text, count=1)
        if n:
            path.write_text(new, encoding="utf-8")
            print("stripped", path.name)
        else:
            print("no block", path.name)


if __name__ == "__main__":
    main()
