"""Split preview.html into the 3 files pasted into ActiveCampaign."""
import re
from pathlib import Path

here = Path(__file__).parent
s = (here / "preview.html").read_text()

def between(a, b):
    return s[s.index(a) + len(a):s.index(b)].strip() + "\n"

css = between("<!-- HEADER CSS START -->", "<!-- HEADER CSS END -->")
embed = between("<!-- EMBED START -->", "<!-- EMBED END -->")
embed = re.sub(r"[ \t]*<!--.*?-->\n?", "", embed, flags=re.S)  # AC may print comments
body = between("<!-- BODY SCRIPT START -->", "<!-- BODY SCRIPT END -->")

(here / "1-ac-header-code.html").write_text("<!-- IPS /check-this-out: Page Settings > Custom Code > HEADER -->\n" + css)
(here / "2-ac-embed-block.html").write_text(embed)
(here / "3-ac-body-code.html").write_text("<!-- IPS /check-this-out: Page Settings > Custom Code > BODY -->\n" + body)
