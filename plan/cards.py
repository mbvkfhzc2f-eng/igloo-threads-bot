# -*- coding: utf-8 -*-
"""igloo bilgi kartlarını (1080×1350) HTML'den JPEG'e çizer. Liste sığmazsa yazı boyutunu küçültür."""
import html
import json
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

OUT = Path('/home/claude/igloo-threads-bot/img')
CARDS = json.load(open('/home/claude/igloo/cards.json', encoding='utf-8'))

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;background:#F1F5FB;color:#13213C;font-family:'Inter',sans-serif;position:relative;overflow:hidden}
.d1{position:absolute;width:620px;height:620px;border-radius:50%;background:#DDE9F7;right:-230px;top:-250px}
.d2{position:absolute;width:300px;height:300px;border-radius:50%;border:30px solid #D3E3F5;left:-150px;bottom:120px}
.wrap{position:absolute;left:86px;right:86px;top:84px;bottom:76px;display:flex;flex-direction:column}
.pill{align-self:flex-start;background:#13213C;color:#fff;font:600 26px 'Inter';padding:12px 24px;border-radius:999px}
h1{font:700 64px/1.07 'Inter Display','Inter';letter-spacing:-1.2px;margin:30px 0 8px;max-width:860px}
.sub{font:500 28px 'Inter';color:#4E6283}
.list{flex:1;display:flex;flex-direction:column;justify-content:center;gap:var(--gap);margin:30px 0 26px;min-height:0}
.item{display:flex;gap:22px;align-items:center;background:#fff;border:2px solid #E0E9F5;border-radius:22px;padding:var(--pad) 26px}
.num{flex:0 0 50px;height:50px;border-radius:50%;background:#13213C;color:#fff;font:700 24px 'Inter';display:flex;align-items:center;justify-content:center}
.txt{font-size:var(--fs);line-height:1.28;font-weight:500}
.term{font-weight:700;display:block}
.def{font-weight:400;color:#34496D;display:block;margin-top:2px}
.foot{display:flex;justify-content:space-between;align-items:flex-end;border-top:2px solid #D7E3F2;padding-top:22px}
.wm{font:700 40px 'Inter Display','Inter';letter-spacing:-0.6px}
.url{font:500 26px 'Inter';color:#4E6283}
"""


def page(card):
    items = []
    for i, (a, b) in enumerate(card['items'], 1):
        if b:
            body = f'<span class="term">{html.escape(a)}</span><span class="def">{html.escape(b)}</span>'
        else:
            body = html.escape(a)
        items.append(f'<div class="item"><div class="num">{i}</div><div class="txt">{body}</div></div>')
    sub = f'<div class="sub">{html.escape(card["sub"])}</div>' if card.get('sub') else '<div class="sub">Kaydedin, lazım olunca açın</div>'
    return (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="d1"></div><div class="d2"></div><div class="wrap"><div class="pill">{html.escape(card["label"])}</div>'
            f'<h1>{html.escape(card["title"])}</h1>{sub}<div class="list" id="L">{"".join(items)}</div>'
            f'<div class="foot"><div class="wm">igloo collective</div><div class="url">igloocollective.com</div></div></div>'
            f'</body></html>')


with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
    for card in CARDS:
        pg.set_content(page(card))
        pg.evaluate('document.fonts.ready')
        fit = None
        for fs in range(34, 21, -1):
            pad = max(14, round(fs * 0.62))
            gap = max(10, round(fs * 0.5))
            pg.evaluate(f"document.body.style.setProperty('--fs','{fs}px');document.body.style.setProperty('--pad','{pad}px');"
                        f"document.body.style.setProperty('--gap','{gap}px')")
            over = pg.evaluate("(()=>{const L=document.getElementById('L');return L.scrollHeight>L.clientHeight+1})()")
            if not over:
                fit = fs
                break
        if fit is None:
            print('SIĞMADI:', card['file'], file=sys.stderr)
        png = OUT / (card['file'].rsplit('.', 1)[0] + '.png')
        pg.screenshot(path=str(png), full_page=False)
        Image.open(png).convert('RGB').save(OUT / card['file'], 'JPEG', quality=90, optimize=True)
        png.unlink()
        print(card['file'], 'yazı', fit, 'px')
    b.close()
