import html
# ================= DATA (edit here, then run: python generate.py) =================
NAME, SUB = "Forthem0339", "2D Illustrator, Animator, Generalist"
ABOUT = ["Hi everyone! I use this account to post my fun projects.",
         "I'm a Japanese Literature student with experience in",
         "many different things. I enjoy drawing, animation, 3D,",
         "and video editing, and right now I'm focusing on",
         "becoming a data analyst without any coding background."]
SKILLS = [("2D illustration, Graphic Design", 60, ["csp", "ps"]), ("2D Animation", 46, ["csp"]),
          ("Video editing, mograph", 40, ["ae", "cap", "dv"]), ("IT Support", 17, []),
          ("Data Analyst", 5, ["sql"])]
LANGS = [("INDONESIAN", "id", 5, "NATIVE"), ("JAPANESE", "jp", 2, "INTERMEDIATE"), ("ENGLISH", "en", 3, "INTERMEDIATE")]
LEARN = ["DATA ANALYST", "IT SUPPORT", "ANIMATION"]
SQL_TOOLS = ["MySQL | SQLite | PostgreSQL", "SQL Server | DBeaver | DataGrip", "MySQL Workbench | DuckDB"]
PROGRESS = 5  # WORKING PROGRESS bar, 0-100
TASKS = [("SQL", "doing"), ("EXCEL", "todo"), ("PANDAS", "todo"), ("PYTHON", "todo"), ("TABLEAU", "todo"), ("POWER BI", "todo")]  # todo=red, doing=blue, done=green
RECENT = [("23 - SEP - 2026", "PROJECT WRITING APP")] * 2
NOTICE = ("23 - SEP - 2026", "CURRENTLY STUDYING TO PASS JLPT N3")
# ==================================================================================
OR, BL, TX, MU = "#d9692a", "#1e9be0", "#e9ecf5", "#8a8fa5"
ST = {"todo": "#ef3b2d", "doing": "#22a6f0", "done": "#22c55e"}
o = []
def a(s): o.append(s)
def T(x, y, t, s=11, f=TX, w=400, an="start"):
    a(f'<text x="{x}" y="{y}" font-size="{s}" fill="{f}" font-weight="{w}" text-anchor="{an}">{html.escape(t)}</text>')
def L(x1, y1, x2, y2, c=TX, w=1, d=""):
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"' + (f' stroke-dasharray="{d}"' if d else "") + '/>')
def R(x, y, w, h, f="none", s="none", sw=1, rx=0):
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}" stroke="{s}" stroke-width="{sw}"/>')
def P(pts, f="none", s="none", sw=1):
    a(f'<path d="{pts}" fill="{f}" stroke="{s}" stroke-width="{sw}"/>')
def icon(k, x, y, s=18):
    if k == "csp":
        R(x, y, s, s, "#e6e6e6", rx=5); P(f"M{x+13} {y+5} a5.5 5.5 0 1 0 0 8", s="#333", sw=1.8)
    elif k == "ps":
        R(x, y, s, s, "#001e36", "#31a8ff", 1, 3); T(x+s/2, y+13, "Ps", 10, "#31a8ff", 700, "middle")
    elif k == "ae":
        R(x, y, s, s, "#00005b", "#9999ff", 1, 3); T(x+s/2, y+13, "Ae", 10, "#9999ff", 700, "middle")
    elif k == "cap":
        R(x, y, s, s, "#f2f2f2", rx=5); P(f"M{x+4} {y+5} L{x+14} {y+13} M{x+4} {y+13} L{x+14} {y+5}", s="#111", sw=2.2)
    elif k == "dv":
        R(x, y, s, s, "#1b1f2a", "#555", 1, 5)
        for cx, cy, c in ((x+9, y+6, "#e8544a"), (x+5.5, y+12, "#3fbf6b"), (x+12.5, y+12, "#4a8cf0")):
            a(f'<circle cx="{cx}" cy="{cy}" r="3.4" fill="{c}" opacity=".9"/>')
    elif k == "sql":
        a(f'<ellipse cx="{x+9}" cy="{y+4}" rx="8" ry="3.5" fill="#3b8fd9"/><path d="M{x+1} {y+4} v11 a8 3.5 0 0 0 16 0 v-11" fill="#2a6fb5"/>')
        T(x+24, y+14, "SQL", 12, "#3d6a99", 700)
def flag(k, x, y):
    if k == "jp":
        R(x, y, 36, 24, "#f4f4f4"); a(f'<circle cx="{x+18}" cy="{y+12}" r="7" fill="#d7263d"/>')
    elif k == "id":
        R(x, y, 36, 12, "#e0202e"); R(x, y+12, 36, 12, "#f4f4f4")
    else:
        a(f'<svg x="{x}" y="{y}" width="36" height="24" viewBox="0 0 36 24"><rect width="36" height="24" fill="#1c3a8a"/>'
          '<path d="M0 0L36 24M36 0L0 24" stroke="#fff" stroke-width="5"/><path d="M0 0L36 24M36 0L0 24" stroke="#d7263d" stroke-width="2"/>'
          '<path d="M18 0V24M0 12H36" stroke="#fff" stroke-width="8"/><path d="M18 0V24M0 12H36" stroke="#d7263d" stroke-width="4.5"/></svg>')
def slant_bar(x, y, w, h, v, grad):
    pts = f"{x+8},{y} {x+w},{y} {x+w-8},{y+h} {x},{y+h}"
    a(f'<clipPath id="c{y}"><polygon points="{pts}"/></clipPath>')
    a(f'<rect x="{x}" y="{y}" width="{w*v/100:.1f}" height="{h}" fill="url(#{grad})" clip-path="url(#c{y})"/>')
    a(f'<polygon points="{pts}" fill="none" stroke="#9aa0b5" stroke-width=".8"/>')

a('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1010 910" width="1010" height="910" font-family="\'Segoe UI\',Arial,Helvetica,sans-serif">')
a('<defs><linearGradient id="wg"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity=".05"/></linearGradient>'
  '<linearGradient id="gg"><stop offset="0" stop-color="#0fa14a"/><stop offset=".55" stop-color="#0b7d78"/><stop offset="1" stop-color="#0d2c4a"/></linearGradient>'
  + "".join(f'<radialGradient id="r{i}"><stop offset="0" stop-color="{c}" stop-opacity="{o_}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>'
            for i, (c, o_) in enumerate((("#6d3aa8", .45), ("#1f7a6f", .3), ("#c0492b", .4), ("#2a3f9a", .35)))) + '</defs>')
R(0, 0, 1010, 910, "#0a0e19")
for i, (cx, cy, rx, ry) in enumerate(((230, 70, 300, 120), (330, 470, 220, 260), (980, 50, 220, 130), (60, 260, 160, 200))):
    a(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="url(#r{i})"/>')
R(36, 36, 5, 846, TX)
# ---- profile header
for p in ("73,39 88,39 92,45 77,45", "95,39 110,39 114,45 99,45", "117,39 185,39 185,45 121,45"): a(f'<polygon points="{p}" fill="#fff"/>')
P("M185 40 H260 L268 45 H315 L340 72 V108", s=TX)
L(109, 108, 442, 108, TX, 1, "19 6 27 14 268")
a(f'<polygon points="352,60 361,60 375,74 366,74" fill="#fff"/><polygon points="365,60 374,60 388,74 379,74" fill="#fff"/>')
T(392, 70, "PROFILE", 11.5, OR); L(392, 76, 444, 76, OR)
for l in ((425, 45, 441, 37), (430, 58, 462, 36), (445, 66, 462, 50)): L(*l, TX, 1)
a(f'<circle cx="60" cy="67" r="14" fill="#e4691f"/>')
T(75, 79, NAME, 26, "#fff", 700); T(75, 97, SUB, 11, TX)
R(76, 125, 31, 10, OR)
L(86, 149, 86, 260, OR); T(86, 163, "About me", 13, "#fff", 700)
for i, t in enumerate(ABOUT): T(86, 181 + 17.4 * i, t, 11.3, "#cfd4e6")
R(60, 310, 49, 11, OR); T(84.5, 318.3, "social media", 6.5, "#111", 400, "middle")
L(123, 302, 123, 328); R(137, 304, 22, 22, "none", "#fff", 2, 6); a('<circle cx="148" cy="315" r="5" fill="none" stroke="#fff" stroke-width="2"/><circle cx="154" cy="309" r="1.3" fill="#fff"/>')
for l in ((362, 285, 400, 320), (372, 285, 412, 322), (410, 300, 440, 320)): L(*l, "#c8cce0", 1)
L(54, 343, 455, 343, "#6b7086")
# ---- skill set
R(164, 376, 46, 3, "#fff"); L(210, 375, 222, 364); L(267, 375, 380, 375, "#c8cce0"); R(333, 377, 47, 3, "#fff"); L(326, 380, 335, 369)
T(270, 382, "SKILL SET", 10, "#fff", 500, "middle")
YS = [(412, 430), (461, 478), (515, 532), (565, 582), (613, 633)]
for (lab, v, ics), (ty, by) in zip(SKILLS, YS):
    T(74, ty, lab, 11.5, TX); L(54, by - 5, 54, by + 20, "#6b7086")
    x = 74 + len(lab) * 5.75 + 6
    if ics: L(x, ty - 10, x, ty + 8); x += 9
    for k in ics:
        icon(k, x, ty - 12); x += 44 if k == "sql" else 24
    R(72, by, 361, 10, "none", "#8a8fa5", .8); R(72, by, 361 * v / 100, 10, "url(#wg)")
    T(440, by + 9, str(v), 12, BL)
R(382, 664, 53, 3, "#fff")
# ---- language
T(250, 700, "LANGUAGE", 12, "#fff", 500, "middle")
for cx in (190, 310): a(f'<polygon points="{cx-12},691 {cx+2},691 {cx-5},699" fill="none" stroke="{TX}"/><polygon points="{cx+4},699 {cx+14},699 {cx+9},691" fill="{TX}"/>')
L(193, 717, 303, 717)
for (nm, fl, lv, txt), bx in zip(LANGS, (54, 191, 325)):
    R(bx, 723, 122, 68, "none", "#c8cce0", 1)
    T(bx + 61, 737, nm, 7.5, "#fff", 700, "middle"); flag(fl, bx + 43, 744)
    for i in range(5):
        x0 = bx + 10 + i * 20.5
        a(f'<polygon points="{x0+4},771 {x0+20},771 {x0+16},777 {x0},777" fill="{"#fff" if i < lv else "none"}" stroke="#aab" stroke-width=".6"/>')
    T(bx + 61, 787, f"LEVEL - {txt}", 6.5, MU, 400, "middle")
a(f'<circle cx="58" cy="818" r="3.5" fill="{OR}"/>'); T(67, 822, "now learning", 12.5, TX); L(60, 835, 445, 835, OR)
for t, x, uw in zip(LEARN, (58, 171, 268), (53, 29, 33)):
    T(x, 858, t, 11, TX); L(x + 16, 871, x + 16 + uw, 871, BL, 1.6)
# ---- main task
T(511, 70, "MAIN TASK / CURRENTLY WORKING ON", 13, "#fff", 600); L(773, 65, 890, 65)
for p in ("900,59 915,59 921,72 906,72", "922,59 937,59 943,72 928,72", "944,59 965,59 965,72 950,72"): a(f'<polygon points="{p}" fill="#fff"/>')
P("M502 86 H935 L966 113 V505 H752 L745 497 H512 L502 487 Z", s="#c8cce0")
R(510, 93, 10, 10, "none", "#fff"); R(529, 93, 10, 10, "#fff"); R(538, 98, 10, 10, OR)
T(518, 125, "SKILL", 8.5, MU); T(517, 148, "DATA ANALYST", 18, "#fff", 700); L(517, 156, 707, 156, "#c8cce0")
L(520, 165, 520, 268); L(533, 176, 533, 255)
a(f'<text x="533" y="185" font-size="14" fill="{TX}">STUDYING <tspan font-weight="700">SQL</tspan></text>'); T(534, 197, "SKILL SET SQL", 8.5, MU)
for i, t in enumerate(SQL_TOOLS): T(540, 215 + 16 * i, t, 11.5, TX)
R(764, 103, 145, 13, OR); T(836, 113, "SQL TRACKER PROGRESS", 10.5, "#fff", 600, "middle"); L(766, 118, 872, 118, OR)
R(763, 125, 176, 160, "none", "#6b7086", .8)
L(776, 278, 927, 278, "#c8cce0"); L(927, 142, 927, 278, "#c8cce0")
for x, y in ((832, 198), (855, 176), (869, 188), (886, 178), (905, 200), (927, 142)): L(x, y, x, 278, "#9aa0b5", .6)
P("M776 268 L790 262 L800 266 L810 258 L831 250 L850 220 L869 230 L886 205 L915 236 L927 222", s="#fff", sw=1.3)
T(520, 289, "WORKING PROGRESS", 8.5, MU); slant_bar(518, 294, 422, 16, PROGRESS, "gg")
# ---- list task
P("M697 333 H518 V487 H945 V333 H775", s="#c8cce0")
T(736, 338, "LIST TASK", 12.5, "#fff", 700, "middle"); L(678, 343, 690, 333); L(781, 333, 793, 343); L(620, 343, 678, 343, "#9aa0b5", .6); L(795, 343, 850, 343, "#9aa0b5", .6)
for (t, s), cx in zip(TASKS, (550, 600, 656, 728, 794, 870)):
    T(cx, 376, t, 11.5, TX, 400, "middle"); w = 8 + len(t) * 2.5
    L(cx - w / 2 + 4, 385, cx + w / 2 - 4, 385, ST[s], 1.6)
# ---- bottom
for x0, title, entries in ((511, "LAST UPDATE REPOSITORY", RECENT), (746, "NOTICE", [NOTICE])):
    L(x0, 553, x0 + 8, 546); L(x0 + 4, 555, x0 + 12, 548); T(x0 + 17, 568, title, 11, TX)
    L(x0 + 5, 579, x0 + 196, 579, "#c8cce0")
    for i, (d, t) in enumerate(entries):
        y = 597 + 46 * i; L(x0 + 8, y - 4, x0 + 8, y + 22)
        T(x0 + 16, y + 3, d, 9.5, TX)
        T(x0 + 16, y + 18, t, 10 if title[0] == "L" else 8.3, "#fff", 700 if title[0] == "L" else 400)
a('</svg>')
open("profile.svg", "w", encoding="utf-8").write("\n".join(o))
print("profile.svg created")
