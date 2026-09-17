"""Through-bag sleeve cartridge figure. Schematic, not to scale; layer thicknesses exaggerated."""
import math, os

W, H = 1200, 1560
OUT = os.path.dirname(os.path.abspath(__file__))

DIRTY = "#f9d9c9"; CLEAN = "#d6eddd"; SLEEVE = "#7fb2e0"; SLEEVE_LINE = "#2f6ea8"
SPACER = "#a97c45"; WALL = "#a3a3a3"; WALL_LINE = "#555"; BAG_LINE = "#2b2b2b"
BAND = "#1f1f1f"; CAP = "#6b6b6b"; TXT = "#222"
A_DIRTY = "#b5523b"; A_CLEAN = "#2e7d4f"; A_BAD = "#e8590c"; A_GREY = "#444"
FONT = 'font-family="Segoe UI, Arial, sans-serif"'


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=14, anchor="start", weight="normal", fill=TXT, style="normal"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}" font-style="{style}" fill="{fill}" {FONT}>{esc(s)}</text>')


def mtext(x, y, lines, size=14, anchor="start", weight="normal", fill=TXT, lh=None):
    lh = lh or size * 1.25
    return "".join(text(x, y + i * lh, s, size, anchor, weight, fill) for i, s in enumerate(lines))


def leader(x0, y0, x1, y1):
    return (f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#444" stroke-width="1"/>'
            f'<circle cx="{x0:.1f}" cy="{y0:.1f}" r="2.6" fill="#444"/>')


def rect(x, y, w, h, fill, stroke="none", sw=1, rx=0):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def poly(pts, fill, stroke="none", sw=1):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'


def pline(pts, stroke, sw=1.2, fill="none", dash=None):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} stroke-linejoin="round"/>'


def path(d, fill="none", stroke="none", sw=1, dash=None, extra=""):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{ds} {extra}/>'


MARKERS = {A_DIRTY: "mD", A_CLEAN: "mC", A_BAD: "mB", A_GREY: "mG"}


def defs():
    s = ["<defs>"]
    for col, mid in MARKERS.items():
        s.append(f'<marker id="{mid}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" '
                 f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>')
    s.append("</defs>")
    return "".join(s)


def arrow(x0, y0, x1, y1, col, sw=2.6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{col}" stroke-width="{sw}"{d} '
            f'marker-end="url(#{MARKERS[col]})"/>')


def arrow_path(pts, col, sw=2.4, dash=None):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<polyline points="{p}" fill="none" stroke="{col}" stroke-width="{sw}"{d} stroke-linejoin="round" '
            f'marker-end="url(#{MARKERS[col]})"/>')


def zigzag(x0, x1, ya, yb, tooth=9, col=SPACER, sw=1.4):
    pts, x, up = [], x0, True
    while x <= x1 + 0.01:
        pts.append((x, ya if up else yb)); x += tooth / 2; up = not up
    return pline(pts, col, sw)


def pt(cx, cy, r, a):
    t = math.radians(a)
    return cx + r * math.cos(t), cy - r * math.sin(t)


def sector(cx, cy, r0, r1, a0, a1, fill, stroke="none", sw=1, steps=None):
    steps = steps or max(8, int(abs(a1 - a0) / 3))
    outer = [pt(cx, cy, r1, a0 + (a1 - a0) * i / steps) for i in range(steps + 1)]
    inner = [pt(cx, cy, r0, a1 - (a1 - a0) * i / steps) for i in range(steps + 1)]
    return poly(outer + inner, fill, stroke, sw)


def zigzag_ring(cx, cy, r0, r1, n, col=SPACER, sw=1.3):
    pts = [pt(cx, cy, r1 if i % 2 else r0, 360 * i / (2 * n)) for i in range(2 * n + 1)]
    return pline(pts, col, sw)


def heading(x, y, s):
    return text(x, y, s, 18, weight="bold")


def panel_a():
    s = [heading(20, 104, "A. Side section of one cartridge")]
    yc = 400
    # plenum (dirty air inside the bag), drawn first and covered by the tube
    s.append(path("M360,294 C430,160 770,160 836,294 L836,506 C770,640 430,640 360,506 Z", fill=DIRTY))
    # clean air inside the tube and in the spacer / window gaps
    s.append(rect(250, 305, 696, 190, CLEAN))
    s.append(poly([(380, 305), (398, 291), (798, 291), (816, 305)], CLEAN))
    s.append(poly([(380, 495), (398, 509), (798, 509), (816, 495)], CLEAN))
    # tube wall with windows over the active length
    wins = [(406, 450), (474, 518), (542, 586), (610, 654), (678, 722), (746, 790)]
    edges = [250] + [v for w in wins for v in w] + [946]
    for i in range(0, len(edges), 2):
        x0, x1 = edges[i], edges[i + 1]
        for y in (305, 486):
            s.append(rect(x0, y, x1 - x0, 9, WALL, WALL_LINE, 1))
    # spacer
    s.append(zigzag(398, 798, 292, 304))
    s.append(zigzag(398, 798, 508, 496))
    # sleeve (top and bottom): lies on the wall at the margins, on the spacer over the windows
    top = [(310, 295), (380, 295), (398, 281), (798, 281), (816, 295), (886, 295),
           (886, 305), (816, 305), (798, 291), (398, 291), (380, 305), (310, 305)]
    s.append(poly(top, SLEEVE, SLEEVE_LINE, 1.3))
    s.append(poly([(x, 2 * yc - y) for x, y in top], SLEEVE, SLEEVE_LINE, 1.3))
    # cap at the left end
    s.append(rect(238, 298, 12, 204, CAP, "#333", 1))
    # bag film: balloon plus gathered tails under the bands
    s.append(path("M360,294 C430,160 770,160 836,294", stroke=BAG_LINE, sw=2.4))
    s.append(path("M360,506 C430,640 770,640 836,506", stroke=BAG_LINE, sw=2.4))
    for y in (293, 507):
        s.append(pline([(322, y), (328, y - 3), (334, y), (340, y - 3), (346, y)], BAG_LINE, 2))
        s.append(pline([(850, y), (856, y - 3), (862, y), (868, y - 3), (874, y)], BAG_LINE, 2))
    # bands on the sleeve margins
    for x in (344, 836):
        s.append(rect(x, 280, 16, 15, BAND, rx=2))
        s.append(rect(x, 505, 16, 15, BAND, rx=2))
    # fan duct into the top of the bag
    s.append(rect(580, 112, 40, 86, "#e3e3e3", "#555", 1.4))
    for y in range(122, 196, 10):
        s.append(f'<line x1="580" y1="{y}" x2="620" y2="{y}" stroke="#999" stroke-width="1"/>')
    s.append(rect(572, 188, 56, 7, "#777", rx=1))
    s.append(arrow(600, 118, 600, 230, A_DIRTY, 3))
    # dirty air pushed through the sleeve
    for x, y0 in ((450, 244), (500, 228), (700, 228), (750, 244)):
        s.append(arrow(x, y0, x, 276, A_DIRTY))
    for x in (450, 525, 600, 675, 750):
        s.append(arrow(x, 574 if x in (450, 750) else 588, x, 524, A_DIRTY))
    # filtered air through the windows and along the tube
    for x in (428, 564, 700):
        s.append(arrow(x, 318, x, 348, A_CLEAN, 2.2))
        s.append(arrow(x, 482, x, 452, A_CLEAN, 2.2))
    for x0 in (440, 560, 680, 800):
        s.append(arrow(x0, 420, x0 + 95, 420, A_CLEAN, 2.6))
    s.append(arrow(905, 420, 1110, 420, A_CLEAN, 3.2))
    # zone labels
    s.append(text(600, 262, "dirty air at fan pressure", 14, "middle", "bold", A_DIRTY))
    s.append(text(600, 386, "filtered air, lower pressure", 14, "middle", "bold", A_CLEAN))
    s.append(text(1010, 250, "open air", 14, "start", "bold", "#666"))
    s.append(text(30, 640, "open air", 14, "start", "bold", "#666"))
    # section marker B and detail marker C
    s.append(f'<line x1="720" y1="186" x2="720" y2="622" stroke="#333" stroke-width="1.3" stroke-dasharray="7 5"/>')
    s.append(text(720, 180, "B", 16, "middle", "bold"))
    s.append(text(720, 640, "B", 16, "middle", "bold"))
    s.append(f'<circle cx="352" cy="292" r="34" fill="none" stroke="#333" stroke-width="1.3" stroke-dasharray="5 4"/>')
    s.append(text(322, 250, "C", 16, "middle", "bold"))
    # labels with leaders
    s.append(leader(311, 297, 176, 206))
    s.append(mtext(24, 196, ["Sleeve's cut edge,", "outside the bag"]))
    s.append(leader(346, 285, 205, 292))
    s.append(mtext(24, 276, ["Band clamps the", "gathered bag onto", "the sleeve margin"]))
    s.append(leader(239, 440, 140, 452))
    s.append(mtext(24, 448, ["Cap, outside", "the bag"]))
    s.append(leader(456, 283, 456, 138))
    s.append(text(270, 132, "Mask sleeve: masks wrapped round the tube"))
    s.append(leader(621, 160, 640, 152))
    s.append(mtext(644, 148, ["Fan duct taped into a", "hole in the bag"]))
    s.append(leader(806, 262, 872, 214))
    s.append(text(876, 212, "Bin bag, bottom cut open"))
    s.append(leader(300, 496, 300, 654))
    s.append(text(300, 670, "Tube: cut bottle or rolled card", 14, "middle"))
    s.append(leader(440, 503, 440, 678))
    s.append(text(440, 694, "Corrugated-card spacer", 14, "middle"))
    s.append(leader(631, 492, 631, 654))
    s.append(text(631, 670, "Windows cut in the tube", 14, "middle"))
    s.append(leader(844, 518, 844, 678))
    s.append(text(844, 694, "Band on the sleeve margin", 14, "middle"))
    s.append(mtext(960, 448, ["Outlet: to the next", "stage's bag, or the hood"]))
    return "\n".join(s)


def panel_b():
    cx, cy = 175, 945
    s = [heading(20, 745, "B. Cross-section at B–B")]
    s.append(f'<circle cx="{cx}" cy="{cy}" r="140" fill="{DIRTY}" stroke="{BAG_LINE}" stroke-width="2.4"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="92" fill="{CLEAN}"/>')
    ribs = [(23, 67), (115.8, 133.8), (182.6, 200.6), (249.4, 267.4), (316.2, 334.2)]
    for a0, a1 in ribs:
        s.append(sector(cx, cy, 74, 82, a0, a1, WALL, WALL_LINE, 1))
    s.append(zigzag_ring(cx, cy, 83, 91, 64))

    def rin(a):
        if a < 380: return 92
        if a < 388: return 92 + 8 * (a - 380) / 8
        return 100
    angs = [28 + i for i in range(0, 395)]
    outer = [pt(cx, cy, rin(a) + 8, a) for a in angs]
    inner = [pt(cx, cy, rin(a), a) for a in reversed(angs)]
    s.append(poly(outer + inner, SLEEVE, SLEEVE_LINE, 1.2))
    for a in (120, 180, 240, 300, 350):
        x0, y0 = pt(cx, cy, 134, a); x1, y1 = pt(cx, cy, 106, a)
        s.append(arrow(x0, y0, x1, y1, A_DIRTY, 2.4))
    s.append(text(cx, cy + 5, "filtered air", 12, "middle", "bold", A_CLEAN))
    s.append(text(cx, cy + 122, "dirty air", 12, "middle", "bold", A_DIRTY))
    s.append(text(28, 790, "open air", 13, "start", "bold", "#666"))
    lx, ly = pt(cx, cy, 100, 45)
    s.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="22" fill="none" stroke="#333" stroke-width="1.3" stroke-dasharray="5 4"/>')
    s.append(f'<line x1="{lx + 18:.1f}" y1="{ly - 12:.1f}" x2="370" y2="846" stroke="#333" stroke-width="1.1" stroke-dasharray="5 4"/>')
    # lap detail inset
    s.append(rect(370, 760, 220, 300, "white", "#333", 1.3))
    s.append(rect(372, 790, 216, 168, DIRTY))
    s.append(text(380, 781, "Lap detail", 13, weight="bold"))
    s.append(mtext(380, 808, ["Plenum pressure presses the", "outer flap onto the inner one"], 12))
    for x in (440, 520):
        s.append(f'<line x1="{x}" y1="865" x2="{x}" y2="{932 if x == 440 else 944}" stroke="#555" stroke-width="1" stroke-dasharray="3 3"/>')
    s.append('<line x1="440" y1="872" x2="520" y2="872" stroke="#333" stroke-width="1.2"/>')
    s.append(text(480, 862, "overlap 3 cm or more", 12, "middle"))
    for x in (462, 498):
        s.append(arrow(x, 884, x, 930, A_DIRTY, 2.4))
    s.append(rect(372, 958, 216, 22, CLEAN))
    s.append(zigzag(372, 588, 960, 978))
    s.append(poly([(372, 946), (520, 946), (520, 958), (372, 958)], SLEEVE, SLEEVE_LINE, 1.2))
    s.append(poly([(520, 958), (540, 958), (522, 946)], CLEAN))
    s.append(poly([(440, 934), (522, 934), (540, 946), (588, 946), (588, 958), (540, 958), (522, 946), (440, 946)],
                  SLEEVE, SLEEVE_LINE, 1.2))
    s.append(rect(372, 980, 216, 14, WALL, WALL_LINE, 1))
    s.append(text(480, 991, "solid rib under the lap", 10, "middle", "bold", "white"))
    s.append(rect(372, 994, 216, 64, CLEAN))
    s.append(arrow_path([(422, 920), (440, 946), (519, 946), (531, 972)], A_BAD, 2.8, "5 3"))
    s.append(mtext(380, 1020, ["The only dirty-to-clean path:", "along the overlap"], 12, weight="bold", fill=A_BAD))
    return "\n".join(s)


def panel_c():
    s = [heading(610, 745, "C. Detail at a band: every edge leaks outward")]
    s.append(rect(640, 992, 530, 94, CLEAN))
    for x0, x1 in ((640, 1040), (1090, 1110), (1160, 1170)):
        s.append(rect(x0, 1000, x1 - x0, 16, WALL, WALL_LINE, 1))
    s.append(path("M880,977 C930,900 1060,820 1170,790 L1170,968 L1005,968 L985,978 L880,978 Z", fill=DIRTY))
    s.append(rect(1005, 982, 165, 18, CLEAN))
    s.append(poly([(985, 992), (1005, 982), (1005, 992)], CLEAN))
    s.append(zigzag(1005, 1170, 984, 998))
    s.append(poly([(700, 978), (985, 978), (1005, 968), (1170, 968), (1170, 982), (1005, 982), (985, 992), (700, 992)],
                  SLEEVE, SLEEVE_LINE, 1.3))
    s.append(path("M880,977 C930,900 1060,820 1170,790", stroke=BAG_LINE, sw=2.4))
    s.append(pline([(812, 975), (819, 971), (826, 975), (833, 971), (840, 975), (850, 975)], BAG_LINE, 2))
    s.append(rect(850, 955, 30, 23, BAND, rx=2))
    for x in (1060, 1130):
        s.append(arrow(x, 912, x, 964, A_DIRTY, 2.6))
    s.append(arrow(1065, 986, 1065, 1036, A_CLEAN, 2.4))
    s.append(arrow(1135, 986, 1135, 1036, A_CLEAN, 2.4))
    s.append(arrow_path([(1000, 990), (985, 996), (704, 996), (676, 982), (656, 964)], A_CLEAN, 2.4, "6 4"))
    s.append(arrow_path([(910, 966), (884, 973), (812, 973), (786, 958), (768, 940)], A_CLEAN, 2.4, "6 4"))
    s.append(text(1090, 896, "fan pressure (highest)", 14, "middle", "bold", A_DIRTY))
    s.append(text(1090, 1066, "filtered air (lower)", 14, "middle", "bold", A_CLEAN))
    s.append(text(650, 792, "open air (lowest)", 14, "start", "bold", "#666"))
    s.append(mtext(650, 830, ["Pressure falls from bag to tube to open air,", "so both leaks here run outward."], 13))
    s.append(mtext(650, 900, ["Leak under the bag gather:", "dirty air escapes to open air"], 13, weight="bold", fill=A_CLEAN))
    s.append(mtext(650, 1042, ["Leak under the sleeve margin:", "filtered air escapes to open air"], 13, weight="bold", fill=A_CLEAN))
    s.append(text(700, 968, "cut edge", 11, "middle", "normal", "#333"))
    return "\n".join(s)


def mini_cart(x0, yc, L=280, fan=False):
    s = []
    b0, b1 = x0 + 60, x0 + L - 60
    mid = (b0 + b1) / 2
    s.append(path(f"M{b0},{yc-26} C{b0+30},{yc-105} {b1-30},{yc-105} {b1},{yc-26} L{b1},{yc+26} "
                  f"C{b1-30},{yc+105} {b0+30},{yc+105} {b0},{yc+26} Z", fill=DIRTY))
    s.append(rect(x0, yc - 18, L, 36, CLEAN, WALL_LINE, 1.4))
    s.append(rect(x0 + 40, yc - 26, L - 80, 8, SLEEVE, SLEEVE_LINE, 1))
    s.append(rect(x0 + 40, yc + 18, L - 80, 8, SLEEVE, SLEEVE_LINE, 1))
    s.append(rect(x0 - 8, yc - 22, 8, 44, CAP))
    s.append(path(f"M{b0},{yc-26} C{b0+30},{yc-105} {b1-30},{yc-105} {b1},{yc-26}", stroke=BAG_LINE, sw=2.2))
    s.append(path(f"M{b0},{yc+26} C{b0+30},{yc+105} {b1-30},{yc+105} {b1},{yc+26}", stroke=BAG_LINE, sw=2.2))
    for x in (b0 - 6, b1 - 4):
        s.append(rect(x, yc - 34, 10, 9, BAND, rx=1))
        s.append(rect(x, yc + 25, 10, 9, BAND, rx=1))
    for x in (mid - 50, mid + 50):
        s.append(arrow(x, yc - 58, x, yc - 30, A_DIRTY, 2.2))
        s.append(arrow(x, yc + 58, x, yc + 30, A_DIRTY, 2.2))
    s.append(arrow(x0 + 70, yc, x0 + L - 30, yc, A_CLEAN, 2.4))
    return "\n".join(s)


def panel_d():
    s = [heading(20, 1150, "D. Stages in series: one bag per cartridge")]
    yc = 1275
    s.append(mini_cart(60, yc))
    s.append(mini_cart(420, yc))
    s.append(rect(228, 1160, 54, 26, "#d9d9d9", "#444", 1.3, rx=3))
    s.append(text(255, 1178, "fan", 13, "middle", "bold"))
    s.append(arrow(255, 1188, 255, 1222, A_DIRTY, 2.6))
    s.append(pline([(340, yc), (365, yc), (365, 1180), (540, 1180), (540, 1206)], "#bdbdbd", 11))
    s.append(arrow_path([(345, yc), (365, yc), (365, 1180), (540, 1180), (540, 1220)], A_CLEAN, 2.2))
    s.append(arrow(700, yc, 750, yc, A_CLEAN, 3))
    s.append(text(756, yc + 5, "to hood", 14, weight="bold"))
    s.append(text(455, 1168, "duct runs through open air", 12, "middle"))
    s.append(text(200, 1378, "stage 1", 15, "middle", "bold"))
    s.append(text(560, 1378, "stage 2", 15, "middle", "bold"))
    s.append(text(60, 1402, "Each bag holds one cartridge and sits in open air. Two cartridges in one bag would run in parallel.", 13))
    return "\n".join(s)


def panel_dont():
    s = [rect(820, 1132, 360, 278, "#fff7f3", A_BAD, 1.4, rx=4)]
    s.append(text(836, 1156, "Don't", 17, weight="bold", fill=A_BAD))
    # sleeve edge inside the bag
    yc = 1222
    s.append(path(f"M858,{yc} C876,{yc-62} 1022,{yc-62} 1040,{yc} C1022,{yc+62} 876,{yc+62} 858,{yc} Z",
                  fill=DIRTY, stroke=BAG_LINE, sw=2))
    s.append(rect(842, yc - 10, 214, 20, CLEAN, WALL_LINE, 1.2))
    s.append(rect(900, yc - 16, 112, 6, SLEEVE, SLEEVE_LINE, 1))
    s.append(rect(900, yc + 10, 112, 6, SLEEVE, SLEEVE_LINE, 1))
    for x in (862, 1030):
        s.append(rect(x, yc - 18, 7, 36, BAND, rx=1))
    s.append(arrow_path([(888, yc - 26), (897, yc - 12), (925, yc - 12), (934, yc - 2)], A_BAD, 2.2, "4 3"))
    s.append(mtext(1066, yc - 26, ["Sleeve edge inside", "the bag: dirty", "air runs under", "the margin"], 12))
    # bag inside a bag
    yc = 1340
    s.append(f'<ellipse cx="940" cy="{yc}" rx="98" ry="48" fill="{DIRTY}" stroke="{BAG_LINE}" stroke-width="2"/>')
    s.append(f'<ellipse cx="940" cy="{yc}" rx="56" ry="26" fill="#fdeee6" stroke="{BAG_LINE}" stroke-width="1.6"/>')
    s.append(rect(904, yc - 6, 72, 12, CLEAN, WALL_LINE, 1))
    s.append(mtext(1066, yc - 18, ["Bag inside a bag:", "the inner bag's", "joints sit in", "dirty air"], 12))
    for x0, y0 in ((830, 1196), (830, 1318)):
        s.append(f'<path d="M{x0},{y0} l14,14 M{x0+14},{y0} l-14,14" stroke="{A_BAD}" stroke-width="3" stroke-linecap="round"/>')
    return "\n".join(s)


def legend():
    s = [heading(20, 1450, "Key")]
    y = 1476
    items = [(20, DIRTY, "dirty air in the bag"), (205, CLEAN, "filtered air"), (340, SLEEVE, "mask sleeve"),
             (480, WALL, "tube wall")]
    for x, col, lab in items:
        s.append(rect(x, y - 13, 24, 16, col, "#555", 1))
        s.append(text(x + 32, y, lab, 13))
    s.append(zigzag(610, 634, y - 12, y + 2))
    s.append(text(642, y, "spacer", 13))
    s.append(rect(740, y - 13, 12, 16, BAND, rx=1))
    s.append(text(760, y, "band", 13))
    s.append(f'<line x1="850" y1="{y-5}" x2="876" y2="{y-5}" stroke="{BAG_LINE}" stroke-width="2.4"/>')
    s.append(text(884, y, "bag film", 13))
    y = 1512
    for x, col, dash, lab in ((20, A_DIRTY, None, "air pushed through the masks"), (300, A_CLEAN, None, "filtered air"),
                              (470, A_CLEAN, "6 4", "leak that runs outward: harmless"),
                              (780, A_BAD, "5 3", "leak into the clean side: critical")):
        s.append(arrow(x, y - 5, x + 36, y - 5, col, 2.4, dash))
        s.append(text(x + 44, y, lab, 13))
    s.append(text(20, 1544, "Schematic, not to scale: layer thicknesses are exaggerated.", 12, fill="#666", style="italic"))
    return "\n".join(s)


def build():
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
             defs(), rect(0, 0, W, H, "white"),
             text(20, 40, "Through-bag sleeve cartridge", 26, weight="bold"),
             text(20, 68, "One mask stage. Every mask edge, band and tube end sits outside the bag, "
                          "so any leak there runs outward.", 15, fill="#444")]
    for y in (716, 1118, 1422):
        parts.append(f'<line x1="20" y1="{y}" x2="{W-20}" y2="{y}" stroke="#ddd" stroke-width="1"/>')
    parts += [panel_a(), panel_b(), panel_c(), panel_d(), panel_dont(), legend(), "</svg>"]
    out = os.path.join(OUT, "through_bag_cartridge.svg")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print("wrote", out)


build()
