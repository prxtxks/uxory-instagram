import sys, pathlib, asyncio
from playwright.async_api import async_playwright
HERE = pathlib.Path(__file__).parent
OUT = HERE / "out"; PNG = HERE / "png"; PNG.mkdir(exist_ok=True)

async def main(names):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for n in names:
            await pg.goto((OUT / f"{n}.html").as_uri())
            await pg.evaluate("document.fonts.ready")
            fam = await pg.evaluate("[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight)")
            issue = [] if any('DM Sans' in f for f in fam) else ["ISSUE: DM Sans not loaded"]
            # nothing under 26px outside mock screens / phone
            small = await pg.evaluate("""[...document.querySelectorAll('body *')].filter(e=>{const t=[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim());return t&&parseFloat(getComputedStyle(e).fontSize)<26&&!e.closest('.screen,.mock')}).map(e=>e.className+':'+getComputedStyle(e).fontSize)""")
            if small: issue.append("ISSUE small text: " + ",".join(small))
            await pg.screenshot(path=str(PNG / f"{n}.png"))
            print(n, "ok" if not issue else " ".join(issue))
        await b.close()

names = sys.argv[1:] or sorted(p.stem for p in OUT.glob("*.html"))
asyncio.run(main(names))
