"""Build the 3 ActiveCampaign files for /access.

The opt-in form is JotForm 262984250929368, loaded by the Body script into the
card on the page and (as its own copy) into the video pop-up.
"""
import json
import re
from pathlib import Path

here = Path(__file__).parent
s = (here / "preview.html").read_text()

def between(a, b):
    return s[s.index(a) + len(a):s.index(b)].strip() + "\n"

page_css = between("<!-- HEADER CSS START -->", "<!-- HEADER CSS END -->")
embed = between("<!-- EMBED START -->", "<!-- EMBED END -->")
embed = re.sub(r"[ \t]*<!--.*?-->\n?", "", embed, flags=re.S)  # AC may print comments

# the pop-up styles also ship inside the Body script (see buildPopup in preview.html)
modal_css = page_css[page_css.index("  /* ---------- FORM POP-UP"):page_css.index("  /* ---------- JOTFORM opt-in")]
body = between("<!-- BODY SCRIPT START -->", "<!-- BODY SCRIPT END -->")
assert "'/*MODAL_CSS*/'" in body
body = body.replace("'/*MODAL_CSS*/'", json.dumps(modal_css))

(here / "1-ac-header-code.html").write_text("<!-- IPS /access: Page Settings > Custom Code > HEADER -->\n" + page_css)
(here / "2-ac-embed-block.html").write_text(embed)
(here / "3-ac-body-code.html").write_text("<!-- IPS /access: Page Settings > Custom Code > BODY -->\n" + body)
