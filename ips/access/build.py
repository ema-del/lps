"""Build the 3 ActiveCampaign files for /access.

preview.html holds the page; ac-form-57.{html,css,js} is the AC form exactly as
AC exported it (button text aside). The AC Embed block strips <style> and
<script>, so the form CSS goes in the Header, and the Body script inserts the
form into its slot (if the Embed block dropped it) and then starts it.
"""
import json
import re
from pathlib import Path

here = Path(__file__).parent
s = (here / "preview.html").read_text()
form_html = (here / "ac-form-57.html").read_text().strip()
form_css = (here / "ac-form-57.css").read_text().strip()
form_js = (here / "ac-form-57.js").read_text().rstrip()

def between(a, b):
    return s[s.index(a) + len(a):s.index(b)].strip() + "\n"

page_css = between("<!-- HEADER CSS START -->", "<!-- HEADER CSS END -->")
embed = between("<!-- EMBED START -->", "<!-- EMBED END -->")
body = between("<!-- BODY SCRIPT START -->", "<!-- BODY SCRIPT END -->")

embed = embed.replace("<!-- AC FORM -->", form_html)
embed = re.sub(r"[ \t]*<!--.*?-->\n?", "", embed, flags=re.S)  # AC may print comments

# AC's form CSS first, then the page CSS (which restyles the form) so ours wins on ties
header = ("<!-- IPS /access: Page Settings > Custom Code > HEADER -->\n"
          "<style>\n" + form_css + "\n</style>\n" + page_css)

form_boot = """<script>
/* IPS: put the AC form in its slot if the Embed block stripped it, then start it */
(function () {
  var FORM_HTML = %s;
  function start() {
    var slot = document.getElementById('ips-form-slot');
    if (!document.getElementById('_form_57_') && slot) slot.innerHTML = FORM_HTML;
    if (!document.getElementById('_form_57_') || window.__ipsForm57) return;
    window.__ipsForm57 = true;
%s
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
</script>
""" % (json.dumps(form_html), "\n".join("    " + l if l else l for l in form_js.split("\n")))

(here / "1-ac-header-code.html").write_text(header)
(here / "2-ac-embed-block.html").write_text(embed)
(here / "3-ac-body-code.html").write_text("<!-- IPS /access: Page Settings > Custom Code > BODY -->\n" + body + form_boot)
