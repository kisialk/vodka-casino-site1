# -*- coding: utf-8 -*-
"""Merge SEO fragment parts and inject before <footer class="footer">."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]


def word_count_ru(html: str) -> int:
    return len(re.findall(r"[А-Яа-яЁёA-Za-z0-9]+(?:-[А-Яа-яЁёA-Za-z0-9]+)?", html))


def inject(htm_name: str, slug: str) -> None:
    base = ROOT / "seo_build" / slug
    parts = sorted(base.glob("part*.html"))
    if not parts:
        raise SystemExit(f"No parts for {slug}")
    block = "".join(p.read_text(encoding="utf-8") for p in parts)
    if not block.strip().startswith("<section"):
        raise SystemExit(f"Bad block start {slug}")
    path = ROOT / htm_name
    text = path.read_text(encoding="utf-8")
    needle = '  <footer class="footer">'
    if needle not in text:
        raise SystemExit(f"Footer needle missing: {htm_name}")
    if 'class="seo-text"' in text:
        print("skip (already)", htm_name)
        return
    n = word_count_ru(block)
    print(htm_name, "words ~", n)
    if n < 1180:
        print("  WARNING: below ~1200 words")
    if n > 1880:
        print("  WARNING: above ~1800 words")
    text = text.replace(needle, block.rstrip() + "\n" + needle, 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    mapping = [
        ("index.htm", "index"),
        ("official-site.htm", "official-site"),
        ("zerkalo.htm", "zerkalo"),
        ("vhod.htm", "vhod"),
        ("registraciya.htm", "registraciya"),
        ("bonus.htm", "bonus"),
        ("skachat.htm", "skachat"),
        ("otzyvy.htm", "otzyvy"),
        ("play.htm", "play"),
        ("ru/index.htm", "ru_index"),
    ]
    for htm, slug in mapping:
        inject(htm, slug)


if __name__ == "__main__":
    main()
