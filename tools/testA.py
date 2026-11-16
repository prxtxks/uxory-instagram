import re, pathlib, json
OUT=pathlib.Path('out'); fails=[]
BANNED=['!','comment ','dm you','whatsapp','+91','exclusive','blow your mind']
for f in sorted(OUT.glob('*.html')):
    s=f.read_text(); acc=f.stem.split('-')[-1]
    body=re.sub(r'<style>.*?</style>','',s,flags=re.S); body=re.sub(r'<svg.*?</svg>','',body,flags=re.S)
    text=re.sub(r'<[^>]+>',' ',body); text=re.sub(r'&#8209;','-',text)
    # hashless hex
    for m in re.findall(r'(?:fill|stroke|background|color)\s*[:=]\s*[\'"]?\s*([0-9A-Fa-f]{6})\b',s):
        fails.append((f.name,'hashless hex',m))
    # fonts
    if re.search(r"font-family:\s*'(?!DM Sans|DM Mono)",s): fails.append((f.name,'font',''))
    # banned
    low=text.lower()
    for b in BANNED:
        if b in low: fails.append((f.name,'banned',b))
    if re.search(r'[\U0001F300-\U0001FAFF☀-➿]',text): fails.append((f.name,'emoji',''))
    # phone-like numbers
    if re.search(r'\b\d{3}[\s.-]\d{3}[\s.-]\d{4}\b|\+\d{2}\s?\d{5}',text): fails.append((f.name,'phone',''))
    # account
    if acc=='co' and re.search(r'\b(colour|enquir|Pune|₹|uxory\.in)\b',text): fails.append((f.name,'locale .co',''))
    if acc=='in' and re.search(r'\b(color\b|inquir|uxory\.co\b|\$)',text): fails.append((f.name,'locale .in',''))
    if f"{'uxory.co' if acc=='co' else 'uxory.in'}" not in text: fails.append((f.name,'footer handle',''))
    if 'width:190px' not in s: fails.append((f.name,'logo 190',''))
    if 'padding:80px' not in s: fails.append((f.name,'padding 80',''))
    if 'linear-gradient' not in s: fails.append((f.name,'no gradient',''))
    if not re.search(r"class='(mock|phone)'",s): fails.append((f.name,'no asset',''))
print(json.dumps(fails,indent=0) if fails else 'TEST A PASS', len(list(OUT.glob('*.html'))),'files')
