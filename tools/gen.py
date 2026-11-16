"""Uxory Instagram generator (rebuilt 16 Nov 2026, v2 after tests B/C).
Templates: lock-screen festive (X), carousel 11 (K). python3 gen.py -> out/*.html ; render.py -> png/.
"""
import pathlib

HERE = pathlib.Path(__file__).parent
OUT = HERE / "out"; OUT.mkdir(exist_ok=True)
REPO = pathlib.Path("/home/claude/uxory-instagram")
LOGO_DARK = (REPO / "brand/logos/uxory-on-dark.svg").read_text()
FONTS = HERE / "node_modules/@fontsource"

T = {
    "canvas": "#151515", "panel": "#1C1C1C", "card": "#232323", "ink": "#EDF0F5",
    "body": "rgba(237,240,245,.7)", "muted": "rgba(237,240,245,.6)", "line": "rgba(237,240,245,.1)",
    "tag": "rgba(237,240,245,.14)", "btn": "#EDF0F5", "btn-ink": "#151515",
    "web-fill": "#6BB1FF", "web-panel-to": "#3D7FE6", "accent-ink-light": "#1E5EA7",
    "web-50": "#232E3A", "web-100": "#344960", "web-200": "#406184", "web-ink": "#84C1FF",
    "rank-fill": "#FFD39D", "rank-panel-to": "#F2A85E", "rank-50": "#3A332B", "rank-100": "#605343",
}
ACC = {"co": dict(handle="uxory.co"), "in": dict(handle="uxory.in")}

CSS = f"""
@font-face{{font-family:'DM Sans';font-weight:400;src:url('file://{FONTS}/dm-sans/files/dm-sans-latin-400-normal.woff2') format('woff2')}}
@font-face{{font-family:'DM Sans';font-weight:500;src:url('file://{FONTS}/dm-sans/files/dm-sans-latin-500-normal.woff2') format('woff2')}}
@font-face{{font-family:'DM Sans';font-weight:600;src:url('file://{FONTS}/dm-sans/files/dm-sans-latin-600-normal.woff2') format('woff2')}}
@font-face{{font-family:'DM Mono';font-weight:400;src:url('file://{FONTS}/dm-mono/files/dm-mono-latin-400-normal.woff2') format('woff2')}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:{T['canvas']};font-family:'DM Sans',sans-serif;color:{T['ink']};-webkit-font-smoothing:antialiased}}
.post{{position:relative;width:1080px;height:1350px;padding:80px;overflow:hidden}}
.logo{{position:absolute;top:80px;right:80px;width:190px;height:auto}}
.logo svg{{width:190px;height:auto;display:block}}
.pill{{display:inline-flex;align-items:center;height:56px;padding:0 26px;border-radius:999px;background:{T['tag']};font-size:26px;font-weight:500;color:{T['ink']};line-height:1}}
.eyebrow{{font-size:28px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;line-height:1.2;color:{T['ink']}}}
.footer{{position:absolute;left:80px;bottom:80px;font-size:28px;line-height:1.35;color:{T['muted']}}}
.handle{{position:absolute;right:80px;bottom:80px;font-size:28px;line-height:1.35;color:{T['muted']}}}
.grad-blue{{background:linear-gradient(135deg,{T['web-fill']},{T['web-panel-to']});-webkit-background-clip:text;background-clip:text;color:transparent}}
.grad-amber{{background:linear-gradient(135deg,{T['rank-fill']},{T['rank-panel-to']});-webkit-background-clip:text;background-clip:text;color:transparent}}
.glow{{position:absolute;border-radius:50%;filter:blur(140px);pointer-events:none}}
"""

def page(body, extra_css=""):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}{extra_css}</style></head><body>{body}</body></html>"

# ---------------------------------------------------------------- lock-screen festive template (X)
PHONE_CSS = f"""
.phone{{position:absolute;left:340px;top:400px;width:400px;height:780px;border-radius:62px;background:#0E0E0E;padding:14px;border:2px solid rgba(255,255,255,.14);
  box-shadow:0 4px 5px rgba(0,0,0,.2),0 8px 15px rgba(0,0,0,.2),0 30px 50px rgba(0,0,0,.45)}}
.screen{{position:relative;width:368px;height:748px;border-radius:50px;overflow:hidden;border:2px solid #2A2A2A}}
.screen>svg{{position:absolute;left:0;top:0}}
.island{{position:absolute;left:50%;top:16px;width:104px;height:30px;margin-left:-52px;border-radius:999px;background:#0E0E0E}}
.date{{position:absolute;top:66px;width:100%;text-align:center;font-size:21px;color:rgba(255,255,255,.88)}}
.time{{position:absolute;top:94px;width:100%;text-align:center;font-size:86px;font-weight:500;letter-spacing:-0.01em;color:#FFFFFF;line-height:1}}
.notes{{position:absolute;left:12px;right:12px;top:224px;display:flex;flex-direction:column;gap:10px}}
.note{{display:flex;gap:12px;padding:14px 14px;border-radius:24px;background:rgba(255,255,255,.16);backdrop-filter:blur(20px)}}
.ic{{flex:0 0 44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:21px;font-weight:600;color:#FFFFFF}}
.nt{{flex:1;min-width:0}}
.na{{font-size:15px;letter-spacing:.06em;color:rgba(255,255,255,.75);display:flex;justify-content:space-between}}
.nh{{font-size:19px;font-weight:600;color:#FFFFFF;margin-top:2px;line-height:1.25}}
.nb{{font-size:18px;color:rgba(255,255,255,.88);line-height:1.3}}
.bar{{position:absolute;left:50%;bottom:12px;width:120px;height:5px;margin-left:-60px;border-radius:999px;background:rgba(255,255,255,.9)}}
.h1x{{position:absolute;left:80px;right:80px;top:150px;text-align:center;font-size:92px;font-weight:500;line-height:1.1;letter-spacing:0}}
.pillx{{position:absolute;left:80px;top:80px}}
.ground{{position:absolute;left:290px;top:1150px;width:500px;height:70px;border-radius:50%;background:#000000;opacity:.55;filter:blur(30px)}}
"""

def phone(time, date, notes, screen_bg, in_svg=""):
    rows = ""
    for app, title, body, when, col in notes:
        rows += f"""<div class='note'><div class='ic' style='background:{col}'>{app[0]}</div>
        <div class='nt'><div class='na'>{app}<span>{when}</span></div><div class='nh'>{title}</div><div class='nb'>{body}</div></div></div>"""
    return f"""<div class='phone'><div class='screen' style='background:{screen_bg}'>{in_svg}
      <div class='island'></div><div class='date'>{date}</div><div class='time'>{time}</div>
      <div class='notes'>{rows}</div><div class='bar'></div></div></div>"""

FLAME = f"<linearGradient id='flame' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#FFF1C2'/><stop offset='1' stop-color='{T['rank-panel-to']}'/></linearGradient>"

def diya(x, y, s=1.0):
    return f"""<g transform='translate({x},{y}) scale({s})'>
      <ellipse cx='0' cy='30' rx='40' ry='9' fill='rgba(0,0,0,.4)'/>
      <path d='M-30 10 Q0 34 30 10 Q0 18 -30 10Z' fill='#5A3A1E'/>
      <path d='M-30 10 Q0 2 30 10 Q0 18 -30 10Z' fill='#7A4F27'/>
      <circle cx='0' cy='-16' r='30' fill='{T['rank-fill']}' opacity='.16'/>
      <path d='M0 -34 C8 -24 10 -16 6 -8 C4 -4 -4 -4 -6 -8 C-10 -16 -8 -24 0 -34Z' fill='url(#flame)'/>
    </g>"""

def leaf(x, y, r, s, fill):
    return f"<path transform='translate({x},{y}) rotate({r}) scale({s})' d='M0 -40 C22 -30 30 -8 0 40 C-30 -8 -22 -30 0 -40Z M0 -34 L0 34' fill='{fill}' stroke='rgba(255,255,255,.2)' stroke-width='1.2'/>"

def festive(code, acc, pill, h1a, h1b, grad, scene, time, date, notes, screen_bg, footer, glow, in_svg=""):
    a = ACC[acc]
    body = f"""<div class='post'>
      <div class='glow' style='{glow}'></div>
      <svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;left:0;top:0'><defs>{FLAME}</defs>{scene}</svg>
      <div class='pill pillx'>{pill}</div>
      <div class='logo'>{LOGO_DARK}</div>
      <div class='h1x'>{h1a}<br><span class='{grad}'>{h1b}</span></div>
      <div class='ground'></div>
      {phone(time, date, notes, screen_bg, in_svg)}
      <div class='footer'>{footer}</div><div class='handle'>{a['handle']}</div>
    </div>"""
    (OUT / f"{code}-{acc}.html").write_text(page(body, PHONE_CSS))

UX, FAM, CLI = T['web-panel-to'], T['rank-panel-to'], T['web-200']

def build_festive():
    # X2 Guru Nanak Jayanti (.in, Tue 24 Nov)
    scene = "".join(diya(x, 1172, s) for x, s in [(130,1.5),(255,1.15),(825,1.15),(950,1.5)]) + \
            f"<ellipse cx='540' cy='1250' rx='720' ry='170' fill='{T['rank-panel-to']}' opacity='.10'/>"
    in_svg = f"<svg width='368' height='748' viewBox='0 0 368 748'><defs>{FLAME}</defs><ellipse cx='184' cy='760' rx='300' ry='120' fill='#FFF1C2' opacity='.22'/>" + \
             "".join(diya(x, 640, s) for x, s in [(70,.9),(184,1.1),(298,.9)]) + "</svg>"
    screen = f"linear-gradient(180deg,#1A120A 0%,#3A2410 55%,{T['rank-panel-to']} 100%)"
    festive("X2", "in", "Guru Nanak Jayanti · 24 November", "Honest work,", "done well.", "grad-amber",
            scene, "6:30", "Tuesday 24 November",
            [("UXORY", "Prakash Purab today", "Kirat karo. Office closed, support on call.", "now", UX),
             ("FAMILY", "Papa", "Gurdwara at 9, langar after. Bring the kids.", "7m", FAM),
             ("CLIENT", "New message", "No rush on the estimate. Enjoy the day.", "21m", CLI)],
            screen, "Happy Guru Nanak Jayanti from Pune.", f"left:290px;top:140px;width:500px;height:500px;background:{T['rank-panel-to']};opacity:.22", in_svg)

    # X3 Constitution Day (.in, Thu 26 Nov)
    rings = "".join(f"<circle cx='540' cy='790' r='{r}' fill='none' stroke='{T['web-fill']}' stroke-width='2' opacity='{o}'/>" for r, o in [(440,.18),(530,.13),(620,.09),(710,.06)])
    year = f"<text x='540' y='1120' text-anchor='middle' font-family='DM Sans' font-weight='500' font-size='300' fill='{T['web-fill']}' opacity='.07' letter-spacing='-3'>1949</text>"
    in_svg = f"<svg width='368' height='748' viewBox='0 0 368 748'>" + "".join(f"<circle cx='184' cy='760' r='{r}' fill='none' stroke='#FFFFFF' stroke-width='1.5' opacity='{o}'/>" for r, o in [(90,.35),(150,.25),(210,.17),(270,.1)]) + \
             f"<rect x='44' y='640' width='280' height='52' rx='26' fill='none' stroke='#FFFFFF' stroke-opacity='.35' stroke-width='1.5'/><text x='184' y='672' text-anchor='middle' font-family=\"DM Sans\" font-size='17' letter-spacing='3' fill='#FFFFFF' opacity='.85'>WE, THE PEOPLE OF INDIA</text></svg>"
    screen = f"linear-gradient(180deg,#0B1526 0%,#14305A 55%,{T['web-panel-to']} 100%)"
    festive("X3", "in", "Constitution Day · 26 November", "Good rules make", "good systems.", "grad-blue",
            rings + f"<ellipse cx='540' cy='1250' rx='720' ry='170' fill='{T['web-panel-to']}' opacity='.10'/>", "9:41", "Thursday 26 November",
            [("UXORY", "Constitution Day", "Adopted 26 November 1949. Still the spec we build under.", "now", UX),
             ("CLIENT PORTAL", "Invoice INV-0412 paid", "Thank you. GST invoice attached.", "12m", CLI),
             ("FAMILY", "Mum", "Preamble reading at school, 10:30. Come if you can.", "25m", FAM)],
            screen, "Happy Constitution Day from Pune.", f"left:290px;top:160px;width:500px;height:500px;background:{T['web-panel-to']};opacity:.22", in_svg)

    # X4 Thanksgiving (.co, Thu 26 Nov)
    leaves = "".join(leaf(x, y, r, s, f) for x, y, r, s, f in [
        (120,1080,-25,1.3,"#B8622A"),(230,1150,30,1.0,"#D98A3A"),(70,960,-60,.85,"#8C4A22"),(300,1010,70,.75,"#E0A24E"),
        (960,1080,25,1.3,"#B8622A"),(850,1150,-30,1.0,"#D98A3A"),(1010,960,60,.85,"#8C4A22"),(780,1010,-70,.75,"#E0A24E")])
    in_svg = "<svg width='368' height='748' viewBox='0 0 368 748'>" + "".join(leaf(x, y, r, s, f) for x, y, r, s, f in [
        (60,600,-30,.9,"#B8622A"),(150,660,40,.7,"#D98A3A"),(250,620,-50,.8,"#E0A24E"),(320,690,20,.6,"#8C4A22"),(110,720,80,.6,"#D98A3A")]) + "</svg>"
    scene = leaves + f"<ellipse cx='540' cy='1250' rx='720' ry='170' fill='{T['rank-panel-to']}' opacity='.08'/>"
    screen = f"linear-gradient(180deg,#1A1008 0%,#4A2A10 55%,{T['rank-panel-to']} 100%)"
    festive("X4", "co", "Thanksgiving · November 26", "Thankful for every", "site we got to build.", "grad-amber",
            scene, "8:15", "Thursday, November 26",
            [("UXORY", "Office closed today", "Support stays on. Deploys resume Monday.", "now", UX),
             ("FAMILY", "Mom", "Dinner at 4. You are on pie duty.", "9m", FAM),
             ("CLIENT", "New message", "Site held up through the sale rush. Thank you.", "32m", CLI)],
            screen, "Happy Thanksgiving from Uxory LLC.", f"left:290px;top:140px;width:500px;height:500px;background:{T['rank-panel-to']};opacity:.22", in_svg)

    # X5 Small Business Saturday (.co, Sat 28 Nov)
    def awning(w, y, h, step, op, ox=0):
        s = "".join(f"<rect x='{ox+x}' y='{y}' width='{step}' height='{h}' fill='{T['web-fill'] if i%2==0 else T['web-200']}'/>" for i, x in enumerate(range(0, w, step)))
        c = "".join(f"<circle cx='{ox+x+step/2}' cy='{y+h}' r='{step/2}' fill='{T['web-fill'] if i%2==0 else T['web-200']}'/>" for i, x in enumerate(range(0, w, step)))
        return f"<g opacity='{op}'>{s}{c}</g>"
    scene = awning(1080, 1000, 130, 60, .7) + f"<rect x='0' y='1160' width='1080' height='190' fill='{T['web-50']}' opacity='.7'/>" + \
            f"<rect x='0' y='1130' width='1080' height='40' fill='#000000' opacity='.35'/>"
    in_svg = "<svg width='368' height='748' viewBox='0 0 368 748'>" + \
             f"<rect x='60' y='600' width='248' height='80' rx='16' fill='#FFFFFF' fill-opacity='.1' stroke='#FFFFFF' stroke-opacity='.4' stroke-width='2'/><text x='184' y='648' text-anchor='middle' font-family=\"DM Sans\" font-size='22' font-weight='500' fill='#FFFFFF'>OPEN TODAY 9–6</text></svg>"
    screen = f"linear-gradient(180deg,#0B1526 0%,#17335F 55%,{T['web-panel-to']} 100%)"
    festive("X5", "co", "Small Business Saturday · November 28", "Shop small.", "Build it right.", "grad-blue",
            scene, "9:00", "Saturday, November 28",
            [("UXORY", "Small Business Saturday", "Your site should work as hard as you do today.", "now", UX),
             ("POS", "Card payment received", "$84.00 · Maple Street Books", "3m", CLI),
             ("CUSTOMER", "Dana R.", "Found you on Google. Open till 6 today?", "11m", FAM)],
            screen, "Happy Small Business Saturday.", f"left:290px;top:160px;width:500px;height:500px;background:{T['web-panel-to']};opacity:.22", in_svg)

# ---------------------------------------------------------------- carousel template 11 (K)
CAR_CSS = f"""
.k-eyebrow{{position:absolute;left:80px;top:88px}}
.k-h1{{position:absolute;left:80px;right:80px;top:184px;font-size:92px;font-weight:500;line-height:1.08;letter-spacing:0}}
.k-h2{{position:absolute;left:80px;right:80px;top:320px;font-size:72px;font-weight:500;line-height:1.1;letter-spacing:0}}
.k-lead{{position:absolute;left:80px;right:80px;font-size:32px;line-height:1.45;color:{T['body']}}}
.num{{position:absolute;left:80px;top:184px;width:104px;height:104px;border-radius:28px;display:flex;align-items:center;justify-content:center;
     font-size:48px;font-weight:500;color:#FFFFFF;background:linear-gradient(135deg,{T['web-fill']},{T['web-panel-to']} 60%,{T['accent-ink-light']});box-shadow:0 4px 5px rgba(0,0,0,.3)}}
.of{{position:absolute;left:208px;top:218px;font-size:28px;color:{T['muted']}}}
.mock{{position:absolute;left:80px;right:80px;top:580px;height:600px;border-radius:40px;background:{T['panel']};border:2px solid {T['line']};overflow:hidden;box-shadow:0 4px 5px rgba(0,0,0,.2),0 8px 15px rgba(0,0,0,.2),0 30px 50px rgba(0,0,0,.45)}}
.chrome{{height:60px;display:flex;align-items:center;gap:12px;padding:0 28px;border-bottom:2px solid {T['line']};font-size:18px;color:{T['muted']}}}
.chrome i{{width:14px;height:14px;border-radius:50%;background:{T['tag']}}}
.chrome b{{margin-left:16px;height:30px;width:380px;border-radius:999px;background:{T['tag']};font-weight:400;display:flex;align-items:center;padding-left:16px}}
.pg{{position:relative;padding:28px 44px 0}}
.nav{{display:flex;gap:30px;align-items:center;font-size:19px;color:{T['body']};margin-bottom:26px}}
.nav .lg{{font-size:24px;font-weight:600;color:{T['ink']};letter-spacing:.04em;margin-right:auto}}
.nav .cta{{height:40px;padding:0 20px;border-radius:999px;background:{T['ink']};color:{T['btn-ink']};display:flex;align-items:center;font-weight:500}}
.hl{{font-size:44px;font-weight:500;line-height:1.12;color:{T['ink']};letter-spacing:0}}
.sub{{margin-top:12px;font-size:20px;color:{T['body']};line-height:1.4}}
.tiles{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:26px}}
.tile{{height:200px;border-radius:22px;background:linear-gradient(135deg,{T['web-200']},{T['web-50']});position:relative;border:2px solid {T['line']};overflow:hidden;padding:18px}}
.tile .art{{position:absolute;right:-20px;top:-20px;width:120px;height:120px;border-radius:50%;background:{T['web-fill']};opacity:.35}}
.tile .art2{{position:absolute;right:30px;top:60px;width:70px;height:70px;border-radius:18px;background:{T['web-fill']};opacity:.5}}
.tile .t1{{position:absolute;left:18px;bottom:40px;font-size:21px;font-weight:500;color:{T['ink']}}}
.tile .t2{{position:absolute;left:18px;bottom:16px;font-size:16px;color:{T['body']}}}
.lbl{{position:absolute;font-family:'DM Mono',monospace;font-size:17px;color:{T['web-ink']};background:rgba(107,177,255,.14);padding:4px 10px;border-radius:8px}}
.fold{{position:absolute;left:0;right:0;border-top:2px dashed rgba(107,177,255,.6)}}
.cta-pill{{display:inline-flex;align-items:center;height:84px;padding:0 44px;border-radius:999px;background:linear-gradient(135deg,{T['web-fill']},{T['web-panel-to']});color:#FFFFFF;font-size:32px;font-weight:500}}
.cursor{{position:absolute;width:30px;height:38px}}
"""

CURSOR = "<svg class='cursor' viewBox='0 0 30 38' style='left:{x}px;top:{y}px'><path d='M2 2 L2 30 L9 23 L14 35 L19 33 L14 21 L24 21 Z' fill='#FFFFFF' stroke='#151515' stroke-width='2'/></svg>"
NAV = "<div class='nav'><span class='lg'>HARBOR</span><span>Work</span><span>Services</span><span>About</span><span class='cta'>Book a call</span></div>"

def tile(name, kind, style=""):
    return f"<div class='tile' style='{style}'><div class='art'></div><div class='art2'></div><div class='t1'>{name}</div><div class='t2'>{kind}</div></div>"
TILES = [("Atlas Dental", "Website · 2026"), ("Pier Coffee", "Online store"), ("Nova Fitness", "Booking app")]

def tiles(styles=("", "", "")):
    return "<div class='tiles'>" + "".join(tile(n, k, s) for (n, k), s in zip(TILES, styles)) + "</div>"

def mock(inner, url="harbor.studio", style=""):
    return f"<div class='mock' style='{style}'><div class='chrome'><i></i><i></i><i></i><b>{url}</b></div><div class='pg'>{inner}</div></div>"

def carousel(acc):
    a = ACC[acc]
    foot = f"<div class='footer'>{a['handle']}</div>"
    logo = f"<div class='logo'>{LOGO_DARK}</div>"
    glow = f"<div class='glow' style='left:560px;top:-200px;width:700px;height:700px;background:{T['web-panel-to']};opacity:.3'></div>"
    slides = []
    cover = NAV + "<div class='hl'>A site that moves when it should.</div><div class='sub'>Custom design, built in weeks, cared for after launch.</div>" + \
            tiles(("height:250px", "height:250px;opacity:.7;transform:translateY(10px)", "height:250px;opacity:.4;transform:translateY(20px)")) + \
            "<div class='lbl' style='right:0;top:150px'>ease-out · 600 ms</div>"
    slides.append(f"""<div class='post'>{glow}<div class='eyebrow k-eyebrow'>Websites · Motion</div>{logo}
      <div class='k-h1'>Five motions that make a site feel <span class='grad-blue'>finished.</span></div>
      <div class='k-lead' style='top:510px'>Small, deliberate movement. None of it decorative. Swipe.</div>{mock(cover)}{foot}</div>""")
    items = [
        ("Headline reveal", "The first line arrives, then the rest. One short animation, under 600 ms, readable the whole time.",
         NAV + f"<div class='hl'>Websites and apps, <span style='opacity:.55'>built to</span> <span style='opacity:.22'>last.</span></div><div class='sub' style='opacity:.22'>Custom design, built in weeks, cared for after launch.</div>" + tiles(("opacity:.15", "opacity:.15", "opacity:.15")) + "<div class='lbl' style='right:0;top:168px'>0 → 600 ms</div>"),
        ("Hover states", "A card lifts 4px and its shadow deepens. The visitor learns what is clickable without a label.",
         NAV + "<div class='hl'>Recent work</div><div class='sub'>Three of this year's launches.</div>" + tiles(("", "transform:translateY(-14px);box-shadow:0 30px 50px rgba(0,0,0,.55);border-color:rgba(107,177,255,.6)", "")) + CURSOR.format(x=560, y=300) + "<div class='lbl' style='left:430px;top:184px'>translateY(−4px)</div>"),
        ("Staggered gallery", "Images enter one after another, 80 ms apart. Each project gets its moment instead of a wall arriving at once.",
         NAV + "<div class='hl'>Selected projects</div><div class='sub'>Work we are allowed to show.</div>" + tiles(("", "opacity:.6;transform:translateY(14px)", "opacity:.25;transform:translateY(28px)")) + "<div class='lbl' style='left:44px;top:470px'>0 ms</div><div class='lbl' style='left:356px;top:470px'>80 ms</div><div class='lbl' style='left:668px;top:470px'>160 ms</div>"),
        ("Scroll reveal", "Sections fade in and rise 24px as they enter the viewport. Once. Never again on the way back up.",
         NAV + "<div class='hl'>What we do</div><div class='sub'>Websites, web apps, mobile apps and AI agents.</div>" + tiles(("height:170px",)*3) + "<div class='fold' style='top:432px'></div><div class='lbl' style='right:0;top:394px'>viewport edge</div><div class='tiles' style='opacity:.3;transform:translateY(24px);margin-top:20px'>" + "".join(tile(n, k, "height:100px") for n, k in [("Websites", "Launch-ready"), ("Web apps", "Portals"), ("AI agents", "Automation")]) + "</div>"),
        ("Page transitions", "Routes cross-fade instead of flashing white. The site feels like one product, not a stack of pages.",
         NAV + "<div style='display:flex;gap:30px;align-items:flex-start'><div style='flex:0 0 36%;opacity:.3'><div class='hl' style='font-size:34px'>About the studio</div><div class='sub' style='font-size:17px'>Twelve people, one office.</div><div class='tiles' style='grid-template-columns:1fr'>" + tile('Atlas Dental','Website · 2026','height:120px') + "</div></div><div style='flex:1'><div class='hl'>Pricing</div><div class='sub'>Scoped in the open before we start.</div><div class='tiles' style='grid-template-columns:1fr 1fr'>" + tile('Websites','From a fixed quote','height:120px') + tile('Web apps','Scoped per sprint','height:120px') + "</div></div></div><div class='lbl' style='left:44px;top:470px'>cross-fade · 300 ms</div>"),
    ]
    for i, (h, b, inner) in enumerate(items, 1):
        slides.append(f"""<div class='post'>{glow}<div class='eyebrow k-eyebrow'>Websites · Motion</div>{logo}
          <div class='num'>{i}</div><div class='of'>of 5</div>
          <div class='k-h2'>{h}</div><div class='k-lead' style='top:430px;right:120px'>{b}</div>{mock(inner)}{foot}</div>""")
    cta_mock = NAV + "<div class='hl'>Your site, moving the way it should.</div><div class='sub'>Scoped on a free call. Built in weeks. Cared for after launch.</div>" + tiles(("height:120px",)*3)
    slides.append(f"""<div class='post'>{glow}<div class='eyebrow k-eyebrow'>Websites · Motion</div>{logo}
      <div class='k-h1' style='top:200px'>We build this into every site we <span class='grad-blue'>ship.</span></div>
      <div class='k-lead' style='top:470px;right:100px'>Custom design, Lighthouse scores in the 90s, and motion that earns its place. Book a free 30&#8209;minute call. Link in bio.</div>
      <div style='position:absolute;left:80px;top:640px'><span class='cta-pill'>Book a free 30&#8209;minute call</span></div>
      {mock(cta_mock, style='top:790px;height:390px')}{foot}</div>""")
    for n, s in enumerate(slides, 1):
        (OUT / f"K1-{n}-{acc}.html").write_text(page(s, CAR_CSS))

if __name__ == "__main__":
    build_festive()
    for acc in ("co", "in"):
        carousel(acc)
    print(len(list(OUT.glob("*.html"))), "html files")
