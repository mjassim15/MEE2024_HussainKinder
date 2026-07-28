"""v3 of the PI progress report — new visual identity.

Design: deep-space navy + solar amber, serif display headings, stat cards,
left-bar executive summary. Content per v2 review, plus:
- No "over the past few weeks" opening.
- Next steps #2 reframed: multi-epoch analysis is a method rehearsal on PUNCH,
  payoff is on a finer-scale instrument (PUNCH confirmed unable to reach L).
"""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path.cwd() / ".mplconfig"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.image as mpimg

PROJECT = Path("/Users/jassim/Desktop/MEE 2024 Coronagraph/MEE2024_HussainKinder")
OUT = PROJECT / "PUNCH_Progress_Report_Jassim_v3.pdf"

# ---- palette ----
NAVY = "#101828"        # deep space
NAVY2 = "#1c2942"       # slightly lighter navy (panels on dark)
AMBER = "#e8791d"       # solar accent
AMBER_SOFT = "#f4b26a"  # lighter amber for dark backgrounds
INK = "#232733"
MUTED = "#6b7280"
PAPER = "#faf6f0"       # warm light card background
RULE = "#e4dcd0"

SERIF = "DejaVu Serif"
SANS = "DejaVu Sans"

PAGE_W, PAGE_H = 8.5, 11.0
MARGIN = 0.85
LH = 0.19
FS = 8.7


def new_page():
    fig = plt.figure(figsize=(PAGE_W, PAGE_H))
    fig.patch.set_facecolor("white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def xf(inch):
    return inch / PAGE_W


def yf(inch):
    return inch / PAGE_H


def para(ax, x_in, y_in, lines, fontsize=FS, lh=LH, color=INK, style=None):
    yy = y_in
    for line in lines:
        if line:
            ax.text(xf(x_in), yf(yy), line, fontsize=fontsize, color=color,
                    va="top", style=style or "normal", family=SANS)
            yy -= lh
        else:
            yy -= 0.55 * lh
    return yy


def add_image(ax, path, x_in, y_in, w_in, h_in, caption=None):
    x, y, w, h = xf(x_in), yf(y_in), xf(w_in), yf(h_in)
    try:
        img = mpimg.imread(str(path))
    except Exception:
        ax.text(x + w / 2, y + h / 2, f"[missing figure]\n{Path(path).name}",
                ha="center", va="center", fontsize=7, color="red")
        return
    ih, iw = img.shape[0], img.shape[1]
    aspect = iw / ih
    if aspect > w_in / h_in:
        dw_in, dh_in = w_in, w_in / aspect
    else:
        dh_in, dw_in = h_in, h_in * aspect
    cx = x + (w - xf(dw_in)) / 2
    cy = y + (h - yf(dh_in)) / 2
    iax = ax.figure.add_axes([cx, cy, xf(dw_in), yf(dh_in)])
    iax.imshow(img)
    iax.axis("off")
    for s in iax.spines.values():
        s.set_visible(True)
        s.set_edgecolor(RULE)
    if caption:
        ax.text(x + w / 2, y - yf(0.10), caption, ha="center", va="top",
                fontsize=7.2, color=MUTED, style="italic", family=SANS)


def page_header(ax, number, title, page_no):
    """Amber number block + serif title + thin rule."""
    top = PAGE_H - 0.55
    sq = 0.30
    ax.add_patch(plt.Rectangle((xf(MARGIN), yf(top - sq)), xf(sq), yf(sq),
                               color=AMBER, zorder=1))
    ax.text(xf(MARGIN + sq / 2), yf(top - sq / 2), number, ha="center",
            va="center", fontsize=12, fontweight="bold", color="white",
            family=SERIF, zorder=2)
    ax.text(xf(MARGIN + sq + 0.18), yf(top - sq / 2), title, va="center",
            fontsize=13.5, fontweight="bold", color=NAVY, family=SERIF)
    ax.plot([xf(MARGIN), 1 - xf(MARGIN)], [yf(top - sq - 0.14)] * 2,
            color=RULE, lw=1.2)
    footer(ax, page_no)
    return top - sq - 0.42


def footer(ax, page_no):
    ax.text(xf(MARGIN), yf(0.45),
            "PUNCH Coronagraph — Progress Report · Jassim Hussain",
            fontsize=7, color=MUTED, family=SANS)
    ax.add_patch(plt.Rectangle((1 - xf(MARGIN + 0.22), yf(0.36)),
                               xf(0.22), yf(0.22), color=AMBER))
    ax.text(1 - xf(MARGIN + 0.11), yf(0.47), str(page_no), ha="center",
            va="center", fontsize=8, color="white", fontweight="bold",
            family=SANS)


def subsection(ax, y_in, text):
    ax.text(xf(MARGIN), yf(y_in), text, fontsize=11, fontweight="bold",
            color=NAVY, family=SERIF, va="top")
    ax.plot([xf(MARGIN), xf(MARGIN + 0.42)], [yf(y_in - 0.26)] * 2,
            color=AMBER, lw=2)
    return y_in - 0.44


with PdfPages(OUT) as pdf:
    # ========================= PAGE 1 =========================
    fig, ax = new_page()

    band_h = 2.85
    ax.add_patch(plt.Rectangle((0, yf(PAGE_H - band_h)), 1, yf(band_h),
                               color=NAVY, zorder=0))
    ax.add_patch(plt.Rectangle((0, yf(PAGE_H - band_h)), 1, yf(0.055),
                               color=AMBER, zorder=1))
    ax.text(xf(MARGIN), yf(PAGE_H - 0.62),
            "P R O G R E S S   R E P O R T   ·   J U L Y   2 0 2 6",
            fontsize=8, color=AMBER_SOFT, family=SANS, va="center")
    ax.text(xf(MARGIN), yf(PAGE_H - 1.08),
            "Adapting the MEE Pipeline to",
            fontsize=19, fontweight="bold", color="white", family=SERIF,
            va="center")
    ax.text(xf(MARGIN), yf(PAGE_H - 1.48),
            "PUNCH Coronagraph Data",
            fontsize=19, fontweight="bold", color="white", family=SERIF,
            va="center")
    ax.text(xf(MARGIN), yf(PAGE_H - 1.96),
            "Centroid detection, Gaia validation, and what the noise floor taught us",
            fontsize=10.5, color="#c8d2e4", family=SANS, va="center")
    ax.text(xf(MARGIN), yf(PAGE_H - 2.42),
            "Jassim Hussain    ·    PI: Prof. Jesse Kinder",
            fontsize=9.5, color=AMBER_SOFT, family=SANS, va="center")

    # ---- executive summary with amber left bar ----
    es_top = PAGE_H - band_h - 0.42
    ax.text(xf(MARGIN + 0.25), yf(es_top), "Executive Summary", fontsize=12,
            fontweight="bold", color=NAVY, family=SERIF, va="top")
    summ = [
        "I adapted our MEE2024 Tab 1 centroid pipeline to PUNCH Level-3 white-light coronagraph images.",
        "PUNCH is different enough from eclipse data that it took three full pipeline iterations to get a clean",
        "result — the corona generates thousands of false detections, so I masked the inner field and validated",
        "everything that remained against the Gaia star catalog using PUNCH's mission pointing solution.",
        "",
        "The pipeline works: of 4,343 detected centroids in the final run, 86% correspond to real catalog stars.",
        "The same analysis also quantified a hard limitation — at PUNCH's plate scale (~81\u2033/pixel), the",
        "gravitational deflection signal for even our closest detectable star is roughly 1,000x below our",
        "measured position noise, and moving closer to the Sun cannot fix it.",
        "",
        "The real value is the machinery: centroid finding, catalog matching, and the deflection sensitivity",
        "check are now built and validated, and the numbers tell us exactly what instrument they need next —",
        "a finer plate scale that reaches closer to the Sun. For future runs I also plan a visual-first step",
        "(confirming stars by eye before trusting automated matches), a check I skipped on this first pass.",
    ]
    es_text_top = es_top - 0.34
    es_bot = para(ax, MARGIN + 0.25, es_text_top, summ)
    ax.add_patch(plt.Rectangle((xf(MARGIN), yf(es_bot + 0.06)), xf(0.05),
                               yf(es_top + 0.05 - es_bot - 0.06), color=AMBER))

    # ---- data & setup ----
    yy = subsection(ax, es_bot - 0.30, "1.  Data & Setup")
    data_rows = [
        ("INSTRUMENT", "PUNCH (Polarimeter to Unify the Corona and Heliosphere), Level-3 white light."),
        ("FRAME", "2026-02-19 00:16 UTC, 4096 x 4096 pixels, Sun centered at pixel (2048, 2048)."),
        ("PLATE SCALE", "~81 arcsec/pixel — about 44x coarser than our eclipse data (~1.85\u2033/px); 1 R\u2609 \u2248 12 px."),
        ("THE CHALLENGE", "the corona fills the inner ~20% of the frame with bright, lumpy structure that the"),
        ("", "centroid finder happily mistakes for stars."),
    ]
    for lead, txt in data_rows:
        if lead:
            ax.text(xf(MARGIN + 0.05), yf(yy + 0.012), lead, fontsize=7.0,
                    fontweight="bold", color=AMBER, family=SANS, va="top")
        ax.text(xf(MARGIN + 1.35), yf(yy), txt, fontsize=FS, color=INK,
                family=SANS, va="top")
        yy -= 0.215

    fig1_top = yy - 0.12
    add_image(ax, PROJECT / "PUNCH_L3_CAM_20260219.png",
              MARGIN, 0.95, PAGE_W - 2 * MARGIN, fig1_top - 0.95,
              caption="Figure 1. The 2026-02-19 PUNCH white-light frame. The Sun (black disk) is surrounded by the bright corona;\n"
                      "real stars are faint points in the outer field. Everything inside the corona is a minefield for automated star detection.")
    footer(ax, 1)
    pdf.savefig(fig)
    plt.close(fig)

    # ========================= PAGE 2 =========================
    fig, ax = new_page()
    top = page_header(ax, "2", "What I Did — Three Iterations to a Clean Detection", 2)

    # ---- run table, navy header, amber accent on run 03 ----
    tbl_top = top - 0.05
    rows = [
        ["RUN", "THRESHOLD", "CORONA HANDLING", "CENTROIDS", "OUTCOME"],
        ["01", "\u03c3 = 6", "none (MEE's blob mask never fires on PUNCH)", "9,255", "mostly corona junk"],
        ["02", "\u03c3 = 10", "none", "4,824", "still corona-dominated"],
        ["03", "\u03c3 = 10", "circle mask, r < 1000 px", "4,343", "clean — used for analysis"],
    ]
    col_x = [MARGIN + 0.08, MARGIN + 0.58, MARGIN + 1.48, MARGIN + 4.38, MARGIN + 5.18]
    rh = 0.27
    for r, row in enumerate(rows):
        ytop = tbl_top - r * rh
        if r == 0:
            ax.add_patch(plt.Rectangle((xf(MARGIN), yf(ytop - rh + 0.05)),
                                       1 - 2 * xf(MARGIN), yf(rh), color=NAVY))
        elif r == 3:
            ax.add_patch(plt.Rectangle((xf(MARGIN), yf(ytop - rh + 0.05)),
                                       1 - 2 * xf(MARGIN), yf(rh), color=PAPER))
            ax.add_patch(plt.Rectangle((xf(MARGIN), yf(ytop - rh + 0.05)),
                                       xf(0.045), yf(rh), color=AMBER))
        for c, cell in enumerate(row):
            hdr = r == 0
            bold = hdr or (r == 3 and c in (0, 2))
            ax.text(xf(col_x[c]), yf(ytop - 0.06), cell,
                    fontsize=7.2 if hdr else 8.3, va="top",
                    color="white" if hdr else INK,
                    fontweight="bold" if bold else "normal", family=SANS)

    p1 = [
        "MEE's built-in saturation mask assumes an over-exposed Sun; PUNCH's Sun is a dark hole, so that mask",
        "never activated. For run 03 I wrote my own pre-processing step: every pixel within 1,000 px of Sun-center",
        "is replaced with a single flat sky value (the median of a thin ring just outside the mask), blanking 18.7%",
        "of the image. This removes the corona's false bumps before the centroid finder ever sees them.",
    ]
    yy = para(ax, MARGIN, tbl_top - 4 * rh - 0.18, p1)

    note = [
        "One important consequence: at 12 px per solar radius, a 1,000 px mask means the nearest star we can",
        "possibly detect sits at ~83 solar radii. That inner limit in everything below is self-imposed by the",
        "mask — not a physical property of the data.",
    ]
    yy = para(ax, MARGIN, yy - 0.10, note, style="italic", color=MUTED)

    yy = subsection(ax, yy - 0.16, "2.1  Validating against Gaia")
    p2 = [
        "A detected centroid counts as a match if it lands within 2 pixels of where the Gaia catalog says a star",
        "should be (projected through PUNCH's pointing solution). Two numbers summarize the result:",
    ]
    yy = para(ax, MARGIN, yy, p2)
    defs = [
        (True, "Purity = 86.3% — of the 4,343 things I flagged, 3,749 are real stars. The detector rarely cries wolf."),
        (True, "Completeness = 44.8% — of the 8,560 catalog stars bright enough to be in the usable field, I"),
        (False, "recovered about 45%. The fainter half stay below PUNCH's noise."),
    ]
    yy -= 0.04
    for has_bullet, txt in defs:
        if has_bullet:
            ax.text(xf(MARGIN + 0.05), yf(yy), "\u25aa", fontsize=FS,
                    color=AMBER, va="top", family=SANS)
        ax.text(xf(MARGIN + 0.24), yf(yy), txt, fontsize=FS, color=INK,
                va="top", family=SANS)
        yy -= LH

    add_image(ax, PROJECT / "Coronagraph Runs/punch_tab1_run03/gaia_match_overlay.png",
              MARGIN, 1.15, PAGE_W - 2 * MARGIN, yy - 0.20 - 1.15,
              caption="Figure 2. Run 03 validation. Left: detected centroids (cyan) on the masked PUNCH frame. Right: the Gaia truth set —\n"
                      "green points are catalog stars recovered by the pipeline. The empty central region is the r < 1000 px corona mask.")
    pdf.savefig(fig)
    plt.close(fig)

    # ========================= PAGE 3 =========================
    fig, ax = new_page()
    top = page_header(ax, "3", "The Limiting Result — Deflection Signal vs. Noise Floor", 3)

    # ---- four stat cards ----
    cards = [
        ("83.7 R\u2299", "closest detectable star", "(set by the corona mask)"),
        ("0.021\u2033", "predicted deflection there", "\u2248 0.0003 pixels"),
        ("22.6\u2033", "measured position noise", "\u2248 0.28 pixels"),
        ("~1,000x", "signal below the noise", "at every visible radius"),
    ]
    gap = 0.18
    cw = (PAGE_W - 2 * MARGIN - 3 * gap) / 4
    ch = 1.12
    card_top = top - 0.02
    for i, (big, label, sub) in enumerate(cards):
        cx0 = MARGIN + i * (cw + gap)
        ax.add_patch(plt.Rectangle((xf(cx0), yf(card_top - ch)), xf(cw), yf(ch),
                                   color=PAPER, ec=RULE, lw=1))
        ax.add_patch(plt.Rectangle((xf(cx0), yf(card_top - 0.05)), xf(cw),
                                   yf(0.05), color=AMBER))
        ax.text(xf(cx0 + cw / 2), yf(card_top - 0.42), big, ha="center",
                fontsize=14.5, fontweight="bold", color=NAVY, family=SERIF,
                va="center")
        ax.text(xf(cx0 + cw / 2), yf(card_top - 0.72), label, ha="center",
                fontsize=7.2, color=INK, family=SANS, va="center")
        ax.text(xf(cx0 + cw / 2), yf(card_top - 0.92), sub, ha="center",
                fontsize=6.8, color=MUTED, family=SANS, va="center",
                style="italic")

    p = [
        "The natural question is whether detecting stars closer to the Sun would close the gap. It would not.",
        "Deflection grows as 1.75\u2033/r, so to lift the signal above even a tenth of a pixel at PUNCH's scale, a star",
        "would need to sit at r < 0.2 solar radii — inside the Sun. The limitation is not where our stars are; it is",
        "that 81\u2033 pixels are too coarse for this measurement at any radius.",
        "",
        "That is a useful thing to know precisely, and it points directly at what would work: the same pipeline",
        "pointed at a coronagraph with a finer plate scale, which can both resolve smaller shifts and see stars",
        "much nearer the limb.",
    ]
    yy = para(ax, MARGIN, card_top - ch - 0.28, p)

    fig3_top = yy - 0.15
    add_image(ax, PROJECT / "Coronagraph Runs/punch_tab1_run03/deflection_sensitivity_scatter.png",
              MARGIN, fig3_top - 2.15, PAGE_W - 2 * MARGIN, 2.15,
              caption="Figure 3. Measured star offsets vs. distance from the Sun (left: total offset, right: radial component). The red curve\n"
                      "is the predicted Einstein deflection (1.75\u2033/r) — three orders of magnitude below the measurement noise at every\n"
                      "distance PUNCH can see. The dashed gray line is the ~23\u2033 noise floor.")

    add_image(ax, PROJECT / "Coronagraph Runs/punch_tab1_run03/preprocessed_preview.png",
              MARGIN, 1.35, PAGE_W - 2 * MARGIN, fig3_top - 2.15 - 0.75 - 1.35,
              caption="Figure 4. The corona mask that made run 03 work. Left: original frame. Right: the pre-processed input actually fed\n"
                      "to the centroid finder — everything inside r < 1000 px (dashed circle) is flattened to a single sky value.")
    pdf.savefig(fig)
    plt.close(fig)

    # ========================= PAGE 4 =========================
    fig, ax = new_page()
    top = page_header(ax, "4", "Refined Approach & Next Steps", 4)

    yy = subsection(ax, top, "4.1  A visual-first check")
    p = [
        "One lesson from the first pass: I trusted the automated brightest-detections list without first confirming",
        "by eye which of them were actually stars. A conversation with Henry Throop (NASA) reinforced a better",
        "habit — inspect the frame visually and confirm star-like sources before matching. (For this I use DS9, a",
        "standard free astronomy viewer for FITS images that lets you zoom and adjust the brightness stretch.)",
        "",
        "As a first application, I built a \"top-20\" comparison: the 20 brightest detected centroids plotted against",
        "the 20 brightest predicted Gaia stars, with no automatic matching — pure visual inspection. It was",
        "immediately informative: several of the brightest detections near the Sun have no catalog counterpart at",
        "all (they are corona structure, not stars), while the nearest visually confirmed real star sits at ~98 solar",
        "radii, with other confirmed matches out to ~160.",
    ]
    yy = para(ax, MARGIN, yy, p)

    fig5_h = 2.90
    fig5_bot = yy - 0.10 - fig5_h
    add_image(ax, PROJECT / "Coronagraph Runs/punch_top20/PUNCH_top20_comparison_20260703_211737.png",
              MARGIN, fig5_bot, PAGE_W - 2 * MARGIN, fig5_h,
              caption="Figure 5. Top-20 brightest detections (orange circles) vs. top-20 predicted Gaia stars (cyan squares). Where a circle\n"
                      "has no square, the \"star\" is corona. The closest genuine match, at roughly the 3 o'clock position, lies at ~98 solar radii.")

    yy = subsection(ax, fig5_bot - 0.38, "4.2  A working principle I've adopted")
    p = [
        "For anything astrometric, I now treat the native mission FITS as the only source of truth. Display products",
        "(JP2s, PNGs) are stretched, 8-bit, and lossy-compressed — I verified that a JP2 re-wrapped as FITS carries",
        "only 256 distinct pixel values versus thousands in the real data — so they cannot be used for sub-pixel",
        "position work, no matter the file extension.",
    ]
    yy = para(ax, MARGIN, yy, p)

    # ---- next steps: navy box, amber heading ----
    steps = [
        ["Apply the visual-first workflow to establish a trusted star list per frame."],
        ["Repeat the brightest-N analysis across many epochs, tracking the same stars frame to frame to pin",
         "down the real error budget. This can run on PUNCH as a method rehearsal, but the payoff comes on a",
         "finer-scale instrument — we've confirmed PUNCH itself cannot reach the signal at any radius."],
        ["Source a science-grade frame from a finer-scale coronagraph (STEREO, at ~15\u2033/px and reaching",
         "within a few solar radii of the limb, is the leading candidate) — that is where this pipeline points next."],
    ]
    n_lines = sum(len(s) for s in steps)
    nb_h = 0.55 + n_lines * 0.205 + len(steps) * 0.06 + 0.10
    nb_top = yy - 0.15
    ax.add_patch(plt.Rectangle((xf(MARGIN), yf(nb_top - nb_h)),
                               1 - 2 * xf(MARGIN), yf(nb_h), color=NAVY))
    ax.add_patch(plt.Rectangle((xf(MARGIN), yf(nb_top - nb_h)),
                               1 - 2 * xf(MARGIN), yf(0.045), color=AMBER))
    ax.text(xf(MARGIN + 0.22), yf(nb_top - 0.26), "Next Steps",
            fontsize=11, fontweight="bold", color=AMBER_SOFT, family=SERIF,
            va="top")
    yy = nb_top - 0.60
    for lines in steps:
        ax.text(xf(MARGIN + 0.24), yf(yy), "\u25aa", fontsize=9, color=AMBER,
                va="top", family=SANS)
        for line in lines:
            ax.text(xf(MARGIN + 0.42), yf(yy), line, fontsize=8.5,
                    color="#e8ecf4", va="top", family=SANS)
            yy -= 0.205
        yy -= 0.06

    pdf.savefig(fig)
    plt.close(fig)

    d = pdf.infodict()
    d["Title"] = "PUNCH Coronagraph Progress Report (v3)"
    d["Author"] = "Jassim Hussain"
    d["Subject"] = "Progress update for PI Jesse Kinder"

print(f"WROTE {OUT} ({OUT.stat().st_size/1024:.0f} KB)")
