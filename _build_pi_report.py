"""Generate a concise 3-page PDF progress report for PI Jesse Kinder.

First-person voice (Jassim). Henry Throop framed as a helpful mid-project
collaborator, not as someone redirecting the work.
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
OUT = PROJECT / "PUNCH_Progress_Report_Jassim.pdf"

# ---- colors / style ----
INK = "#1a1a2e"
ACCENT = "#0b5394"
MUTED = "#555555"
RULE = "#c9d3df"
BOXBG = "#eef3f8"

PAGE_W, PAGE_H = 8.5, 11.0
MARGIN = 0.85


def new_page(pdf):
    fig = plt.figure(figsize=(PAGE_W, PAGE_H))
    fig.patch.set_facecolor("white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return fig, ax


def x_frac(inch):
    return inch / PAGE_W


def y_frac(inch):
    return inch / PAGE_H


def add_image(ax, path, x, y, w, h, caption=None):
    """x,y,w,h in figure fraction (0-1). y is bottom of image box."""
    try:
        img = mpimg.imread(str(path))
    except Exception as e:
        ax.text(x + w / 2, y + h / 2, f"[missing figure]\n{Path(path).name}",
                ha="center", va="center", fontsize=7, color="red")
        return
    ih, iw = img.shape[0], img.shape[1]
    aspect = iw / ih
    box_aspect = (w * PAGE_W) / (h * PAGE_H)
    if aspect > box_aspect:
        draw_w = w
        draw_h = w * PAGE_W / aspect / PAGE_H
    else:
        draw_h = h
        draw_w = h * PAGE_H * aspect / PAGE_W
    cx = x + (w - draw_w) / 2
    cy = y + (h - draw_h) / 2
    iax = ax.figure.add_axes([cx, cy, draw_w, draw_h])
    iax.imshow(img)
    iax.axis("off")
    for s in iax.spines.values():
        s.set_visible(True)
        s.set_edgecolor(RULE)
    if caption:
        ax.text(x + w / 2, y - 0.012, caption, ha="center", va="top",
                fontsize=6.7, color=MUTED, style="italic", wrap=True)


def header(ax, title, page_no):
    ax.text(x_frac(MARGIN), y_frac(PAGE_H - 0.62), title, fontsize=13,
            fontweight="bold", color=ACCENT, va="center")
    ax.plot([x_frac(MARGIN), 1 - x_frac(MARGIN)],
            [y_frac(PAGE_H - 0.78)] * 2, color=RULE, lw=1)
    ax.text(1 - x_frac(MARGIN), y_frac(0.45), f"{page_no}", ha="right",
            fontsize=8, color=MUTED)
    ax.text(x_frac(MARGIN), y_frac(0.45),
            "PUNCH Coronagraph — Progress Report · Jassim Hussain",
            ha="left", fontsize=7, color=MUTED)


def bullet(ax, x, y, text, fontsize=8.6, dy=0.0, color=INK, bold_lead=None):
    ax.text(x, y, "•", fontsize=fontsize, color=ACCENT, va="top")
    if bold_lead:
        ax.text(x + 0.018, y, bold_lead, fontsize=fontsize, color=INK,
                va="top", fontweight="bold")
    ax.text(x + 0.018, y, text, fontsize=fontsize, color=color, va="top")


with PdfPages(OUT) as pdf:
    # ================= PAGE 1 =================
    fig, ax = new_page(pdf)

    # Title band
    ax.add_patch(plt.Rectangle((0, y_frac(PAGE_H - 2.35)), 1, y_frac(2.35),
                               color=ACCENT, zorder=0))
    ax.text(x_frac(MARGIN), y_frac(PAGE_H - 1.0),
            "Adapting the MEE Pipeline to PUNCH Coronagraph Data",
            fontsize=17, fontweight="bold", color="white", va="center")
    ax.text(x_frac(MARGIN), y_frac(PAGE_H - 1.5),
            "Centroid validation, Gaia matching, and a refined measurement strategy",
            fontsize=10.5, color="#d6e4f0", va="center")
    ax.text(x_frac(MARGIN), y_frac(PAGE_H - 2.0),
            "Prepared by Jassim Hussain   |   PI: Prof. Jesse Kinder   |   July 2026",
            fontsize=9, color="#eaf1f8", va="center")

    # Executive summary box
    box_y = y_frac(PAGE_H - 5.5)
    box_h = y_frac(2.95)
    ax.add_patch(plt.Rectangle((x_frac(MARGIN), box_y), 1 - 2 * x_frac(MARGIN),
                               box_h, color=BOXBG, ec=RULE, lw=1))
    ax.text(x_frac(MARGIN + 0.2), box_y + box_h - y_frac(0.32),
            "Executive Summary", fontsize=11, fontweight="bold", color=ACCENT, va="top")
    summ = [
        "I adapted the MEE2024 Tab 1 centroid pipeline to PUNCH Level-3 white-light images and built a",
        "Gaia-based validation workflow using PUNCH's mission WCS (the built-in plate solve does not",
        "converge on coronagraph data).",
        "",
        "Centroid detection and Gaia matching work well (86–88% purity). However, the stars I can reliably",
        "detect sit far from the Sun (nearest confirmed match ~84 solar radii), where the gravitational",
        "deflection signal is ~1000x below our position noise. A measurement of the Einstein coefficient L",
        "is therefore not achievable with this data as-is.",
        "",
        "I am now pivoting to a visual-first strategy: confirm stars by eye (DS9) before trusting automated",
        "matches, which improves reliability and sets up a cleaner multi-image test of the method.",
    ]
    yy = box_y + box_h - y_frac(0.7)
    for line in summ:
        ax.text(x_frac(MARGIN + 0.2), yy, line, fontsize=8.7, color=INK, va="top")
        yy -= y_frac(0.19)

    # Data section + figure
    ax.text(x_frac(MARGIN), y_frac(PAGE_H - 5.9), "1.  Data & Setup",
            fontsize=12, fontweight="bold", color=ACCENT, va="center")
    data_lines = [
        ("Instrument:", "PUNCH (Polarimeter to Unify the Corona and Heliosphere), Level-3 white light."),
        ("Frame:", "2026-02-19 00:16 UTC, 4096x4096, Sun centered at pixel (2048, 2048)."),
        ("Plate scale:", "~81 arcsec/pixel — about 44x coarser than MEE eclipse data (~1.85 arcsec/px)."),
        ("Implication:", "Each pixel covers a large patch of sky; faint/close stars blur and the corona"),
        ("", "dominates, producing many false centroids that must be filtered."),
    ]
    yy = y_frac(PAGE_H - 6.25)
    for lead, txt in data_lines:
        if lead:
            ax.text(x_frac(MARGIN + 0.05), yy, lead, fontsize=8.7,
                    fontweight="bold", color=INK, va="top")
            ax.text(x_frac(MARGIN + 0.95), yy, txt, fontsize=8.7, color=INK, va="top")
        else:
            ax.text(x_frac(MARGIN + 0.95), yy, txt, fontsize=8.7, color=INK, va="top")
        yy -= y_frac(0.225)

    add_image(ax, PROJECT / "PUNCH_L3_CAM_20260219.png",
              x_frac(MARGIN), y_frac(0.75), 1 - 2 * x_frac(MARGIN), y_frac(2.9),
              caption="Figure 1. PUNCH L3 white-light frame (2026-02-19). Stars appear as faint points across a corona-dominated field.")
    header(ax, "", 1)
    pdf.savefig(fig)
    plt.close(fig)

    # ================= PAGE 2 =================
    fig, ax = new_page(pdf)
    header(ax, "2.  What I Did — and the Limiting Result", 2)

    ax.text(x_frac(MARGIN), y_frac(PAGE_H - 1.05),
            "2.1  Centroid finding + Gaia validation", fontsize=11,
            fontweight="bold", color=INK, va="center")
    intro = [
        "I ran Tab 1 to detect centroids, then projected the Gaia catalog onto the image through PUNCH's",
        "WCS and matched detections to catalog stars. Two representative runs:",
    ]
    yy = y_frac(PAGE_H - 1.4)
    for line in intro:
        ax.text(x_frac(MARGIN), yy, line, fontsize=8.7, color=INK, va="top")
        yy -= y_frac(0.2)

    # metrics table
    tbl_y = y_frac(PAGE_H - 2.15)
    rows = [
        ["Run", "Centroids", "Matched", "Purity", "Completeness"],
        ["Full field (corona-masked)", "4,343", "3,749", "86.3%", "44.8%"],
        ["Top-50 brightest (G<4)", "50", "44", "88.0%", "45.4%"],
    ]
    col_x = [MARGIN + 0.05, MARGIN + 2.55, MARGIN + 3.75, MARGIN + 4.85, MARGIN + 5.75]
    rh = 0.26
    for r, row in enumerate(rows):
        yrow = tbl_y - y_frac(r * rh)
        if r == 0:
            ax.add_patch(plt.Rectangle((x_frac(MARGIN), yrow - y_frac(rh) + y_frac(0.05)),
                                       1 - 2 * x_frac(MARGIN), y_frac(rh),
                                       color=ACCENT, zorder=0))
        for c, cell in enumerate(row):
            ax.text(x_frac(col_x[c]), yrow - y_frac(0.06), cell, fontsize=8.4,
                    va="top", color="white" if r == 0 else INK,
                    fontweight="bold" if r == 0 else "normal")
    ax.text(x_frac(MARGIN), tbl_y - y_frac(3 * rh + 0.05),
            "Takeaway: the detector reliably finds real stars (high purity); "
            "roughly half the catalog stars in-field are recovered.",
            fontsize=8.2, color=MUTED, style="italic", va="top")

    # Section 2.2 limiting result
    ax.text(x_frac(MARGIN), y_frac(PAGE_H - 3.55),
            "2.2  The limiting result: deflection vs. noise", fontsize=11,
            fontweight="bold", color=INK, va="center")
    lim = [
        ("Closest confirmed star:", "~84 solar radii from Sun center."),
        ("Predicted deflection there:", "~0.021 arcsec  (~0.0003 pixels)."),
        ("Measured position noise:", "~23 arcsec  (~0.28 pixels)."),
        ("Signal-to-noise:", "~0.001  — the signal is ~1000x below the noise floor."),
    ]
    yy = y_frac(PAGE_H - 3.9)
    for lead, txt in lim:
        ax.text(x_frac(MARGIN + 0.05), yy, lead, fontsize=8.7, fontweight="bold",
                color=INK, va="top")
        ax.text(x_frac(MARGIN + 2.35), yy, txt, fontsize=8.7, color=INK, va="top")
        yy -= y_frac(0.225)
    ax.text(x_frac(MARGIN + 0.05), yy - y_frac(0.05),
            "This is a physics + resolution limit, not a tuning problem: the detectable stars are simply "
            "too far\nfrom the Sun, and the plate scale is too coarse, for the bending to register.",
            fontsize=8.2, color=MUTED, style="italic", va="top")

    # two figures side by side
    fw = (1 - 2 * x_frac(MARGIN) - x_frac(0.3)) / 2
    add_image(ax, PROJECT / "Coronagraph Runs/punch_tab1_run03/gaia_match_overlay.png",
              x_frac(MARGIN), y_frac(0.75), fw, y_frac(3.2),
              caption="Figure 2. Gaia stars projected onto centroids (full-field run).")
    add_image(ax, PROJECT / "Coronagraph Runs/punch_tab1_run03/deflection_sensitivity_scatter.png",
              x_frac(MARGIN) + fw + x_frac(0.3), y_frac(0.75), fw, y_frac(3.2),
              caption="Figure 3. Measured offsets vs. tiny predicted deflection — noise dominates.")
    pdf.savefig(fig)
    plt.close(fig)

    # ================= PAGE 3 =================
    fig, ax = new_page(pdf)
    header(ax, "3.  Refined Approach & Next Steps", 3)

    ax.text(x_frac(MARGIN), y_frac(PAGE_H - 1.05),
            "3.1  Visual-first validation", fontsize=11, fontweight="bold",
            color=INK, va="center")
    v = [
        "Rather than trusting the brightest detections outright (some are corona features, not stars), I",
        "moved to a visual-first workflow: examine the frame in DS9, confirm which point sources are",
        "genuinely star-like, and only then match those to Gaia. A helpful conversation with Henry Throop",
        "(NASA) reinforced this direction — he suggested confirming stars by eye before trusting automated",
        "matches, which I have folded into the process.",
        "",
        "I built a Top-20 comparison (20 brightest observed centroids vs. 20 brightest predicted Gaia",
        "stars) for direct visual inspection. It confirms the geometry issue: several very bright centroids",
        "near the Sun do NOT correspond to Gaia stars (they are corona structure), while the nearest",
        "visually-confirmed matches lie at ~98–160 solar radii.",
    ]
    yy = y_frac(PAGE_H - 1.4)
    for line in v:
        ax.text(x_frac(MARGIN), yy, line, fontsize=8.7, color=INK, va="top")
        yy -= y_frac(0.205)

    add_image(ax, PROJECT / "Coronagraph Runs/punch_top20/PUNCH_top20_comparison_20260703_211737.png",
              x_frac(MARGIN), y_frac(4.35), 1 - 2 * x_frac(MARGIN), y_frac(2.95),
              caption="Figure 4. Top-20 observed centroids vs. Top-20 predicted Gaia stars (visual inspection, no blind auto-match).")

    ax.text(x_frac(MARGIN), y_frac(3.95),
            "3.2  A multi-image idea (and an honest caveat)", fontsize=11,
            fontweight="bold", color=INK, va="center")
    m = [
        "Extending this across several PUNCH dates would let me track the same Gaia-confirmed stars and",
        "test whether offsets follow the expected 1/R law. Averaging N epochs reduces random error as ~1/sqrt(N).",
        "Caveat: with the current ~1000x signal-to-noise gap, this characterizes our error budget and validates",
        "the method — it will not by itself yield a real L measurement until stars can be detected much closer",
        "to the Sun (e.g., finer plate scale such as STEREO COR1, or eclipse data).",
    ]
    yy = y_frac(3.6)
    for line in m:
        ax.text(x_frac(MARGIN), yy, line, fontsize=8.5, color=INK, va="top")
        yy -= y_frac(0.2)

    # Next steps box
    nb_y = y_frac(0.7)
    nb_h = y_frac(1.55)
    ax.add_patch(plt.Rectangle((x_frac(MARGIN), nb_y), 1 - 2 * x_frac(MARGIN),
                               nb_h, color=BOXBG, ec=RULE, lw=1))
    ax.text(x_frac(MARGIN + 0.2), nb_y + nb_h - y_frac(0.3), "Next steps",
            fontsize=10.5, fontweight="bold", color=ACCENT, va="top")
    steps = [
        "DS9 visual inspection of PUNCH frames to establish a trusted star list.",
        "Targeted Gaia matching on visually-confirmed stars (not blind brightest-N).",
        "Extend Top-20 / Gaia overlay to multiple dates; measure offset scatter vs. solar radius.",
        "Evaluate finer-scale references (STEREO COR1) to test the workflow where stars sit closer in.",
    ]
    yy = nb_y + nb_h - y_frac(0.62)
    for s in steps:
        ax.text(x_frac(MARGIN + 0.22), yy, "•", fontsize=9, color=ACCENT, va="top")
        ax.text(x_frac(MARGIN + 0.36), yy, s, fontsize=8.5, color=INK, va="top")
        yy -= y_frac(0.24)

    pdf.savefig(fig)
    plt.close(fig)

    d = pdf.infodict()
    d["Title"] = "PUNCH Coronagraph Progress Report"
    d["Author"] = "Jassim Hussain"
    d["Subject"] = "Progress update for PI Jesse Kinder"

print(f"WROTE {OUT} ({OUT.stat().st_size/1024:.0f} KB)")
