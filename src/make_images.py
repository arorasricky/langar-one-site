#!/usr/bin/env python3
"""Generates the share image and icons into src/static. Needs Playwright and the two font files.
Run once (or when the logo changes): python3 src/make_images.py /path/to/fonts
Font files expected: bricolage-grotesque-latin-800-normal.woff2, figtree-latin-500-normal.woff2"""
import base64, pathlib, sys
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent / "static"
OUT.mkdir(exist_ok=True)
fonts = pathlib.Path(sys.argv[1])


def b64(name):
    return base64.b64encode((fonts / name).read_bytes()).decode()


FACE = f"""@font-face{{font-family:B;font-weight:800;src:url(data:font/woff2;base64,{b64('bricolage-grotesque-latin-800-normal.woff2')})}}
@font-face{{font-family:F;font-weight:500;src:url(data:font/woff2;base64,{b64('figtree-latin-500-normal.woff2')})}}"""
BASKET = '<path d="M17 30a15 15 0 0 1 30 0" fill="none" stroke="#F2A81D" stroke-width="7" stroke-linecap="round"/><path d="M6 30h52l-5 24a5 5 0 0 1-5 4H16a5 5 0 0 1-5-4z" fill="#F3F6F1"/>'

OG = f"""<style>{FACE}body{{margin:0;width:1200px;height:630px;background:#12392B;color:#F3F6F1;display:flex;overflow:hidden}}
.l{{padding:64px 0 64px 72px;width:700px;display:flex;flex-direction:column;justify-content:space-between}}
.b{{display:flex;align-items:center;gap:16px;font:800 40px B;letter-spacing:-.02em}}.b span{{color:#F2A81D}}
h1{{margin:0;font:800 76px/1 B;letter-spacing:-.035em}}p{{margin:0;font:500 28px/1.35 F;color:#D3E0D6}}
.r{{flex:1;display:flex;align-items:flex-end;justify-content:center}}</style>
<div class="l"><div class="b"><svg width="64" height="64" viewBox="0 0 64 64">{BASKET}</svg><div>Langar <span>One</span></div></div>
<h1>Ending Hunger,<br>One Delivery<br>at a Time</h1><p>Free grocery delivery for families in need.<br>A 501(c)(3) charity · langar.one</p></div>
<div class="r"><svg width="430" viewBox="0 0 460 440"><path d="M110 250a120 120 0 0 1 240 0" fill="none" stroke="#F2A81D" stroke-width="46" stroke-linecap="round"/><path d="M20 250h420l-34 190H54z" fill="#F3F6F1"/><path d="M31 313h398" fill="none" stroke="#C9D8CD" stroke-width="4"/><path d="M43 376h374" fill="none" stroke="#C9D8CD" stroke-width="4"/></svg></div>"""


def icon(size):
    return (f'<style>body{{margin:0;width:{size}px;height:{size}px;background:#12392B;display:flex;align-items:center;justify-content:center}}</style>'
            f'<svg width="{int(size * .66)}" viewBox="0 0 64 64">{BASKET}</svg>')


with sync_playwright() as p:
    b = p.chromium.launch()
    for name, html, w, h in [("og.png", OG, 1200, 630), ("logo.png", icon(512), 512, 512), ("apple-touch-icon.png", icon(180), 180, 180)]:
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.set_content(html)
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT / name))
    b.close()
print("wrote", sorted(f.name for f in OUT.iterdir()))
