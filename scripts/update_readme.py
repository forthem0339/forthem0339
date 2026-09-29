import json
import os
import re
import urllib.request
from datetime import datetime

USER = "forthem0339"          # username GitHub
COUNT = 2                     # jumlah repo yang ditampilkan
NOTICE = ("23 - SEP - 2026", "CURRENTLY STUDYING TO PASS JLPT N3")  # edit di sini

START = "<!--START_SECTION:recent-repos-->"
END = "<!--END_SECTION:recent-repos-->"


def api(url):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "readme-updater"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as r:
        return json.load(r)


repos = api(f"https://api.github.com/users/{USER}/repos?sort=pushed&direction=desc&per_page=30&type=owner")
repos = [r for r in repos if not r["fork"] and not r["archived"] and r["name"].lower() != USER.lower()][:COUNT]

if not repos:
           print("Belum ada repo publik untuk ditampilkan, README tidak diubah.")
       raise SystemExit(0)

rows = ["| ╱ **LAST UPDATE REPOSITORY** | ╱ **NOTICE** |", "| :-- | :-- |"]
for i, r in enumerate(repos):
    date = datetime.strptime(r["pushed_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d - %b - %Y").upper()
    left = f"<sub>{date}</sub><br>**[{r['name'].upper()}]({r['html_url']})**"
    right = f"<sub>{NOTICE[0]}</sub><br><sub>{NOTICE[1]}</sub>" if i == 0 else ""
    rows.append(f"| {left} | {right} |")

block = f"{START}\n\n" + "\n".join(rows) + f"\n\n{END}"

with open("README.md", encoding="utf-8") as f:
    text = f.read()

new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, text, flags=re.S)

if new != text:
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new)
    print("README updated")
else:
    print("No changes")
