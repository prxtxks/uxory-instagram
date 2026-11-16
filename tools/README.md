# tools

Generator for the Instagram templates (rebuilt 16 Nov 2026 after the scratchpad was wiped).

- `gen.py` writes `out/*.html` for the lock-screen festive template (X) and carousel template 11 (K). Tokens are inlined from the brand system's tokens.json (dark theme).
- `render.py [CODE ...]` renders `out/*.html` to `png/` with Playwright at 1080×1350 and reports ISSUE lines (fonts not loaded, text under 26px outside a mock/phone screen).
- `testA.py` is the rule script (fonts, hashless hex, banned words, emoji, phone numbers, locale per account, footer handle, logo 190px, 80px padding, gradient present, asset present).

Setup: `npm i @fontsource/dm-sans @fontsource/dm-mono` next to the scripts (fonts are loaded from node_modules), Playwright with Chromium, Pillow.
