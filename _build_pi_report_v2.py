"""Generate v2 of the PDF progress report for PI Jesse Kinder.

Changes vs v1 (agreed in review with Jassim):
- 4 pages; figures sized for legibility with self-contained captions.
- Circle-mask mechanism explained; self-imposed ~84 R_sun inner limit stated.
- "Cannot measure L" replaced by measured ~1000x noise-to-signal framing.
- Run 01 -> 02 -> 03 iteration story is the spine of page 2.
- Purity / completeness / match criterion defined in plain language.
- Visual-first is future-tense, owned as a lesson; Henry Throop reinforces it.
- DS9 described as zoom + stretch only.
- Native-FITS-as-source-of-truth principle included (256-value JP2 evidence).
- STEREO appears once, as a light tease, pending a good science frame.
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
OUT = PROJECT / "PUNCH_Progress_Report_Jassim_v2.pdf"

INK = "#1a1a2e"
ACCENT = "#0b5394"
MUTED = "#555555"
RULE = "#c9d3df"
BOXBG = "#eef3f8"

PAGE_W, PAGE_H = 8.5, 11.0
MARGIN = 0.85
LH = 0.19  # body line height (inches)
FS = 8.7   # body font size


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
    """Write pre-wrapped lines starting at top y_in (inches). Returns y after."""
    yy = y_in
    for line in lines:
        if line:
            ax.text(xf(x_in), yf(yy), line, fontsize=fontsize, color=color,
                    va="top", style=style or "normal")
            yy -= lh
        else:
            yy -= 0.55 * lh  # paragraph gap
    return yy


def add_image(ax, path, x_in, y_in, w_in, h_in, caption=None):
    """Place image fitted inside box (inches; y_in = bottom of box)."""
    x, y, w, h = xf(x_in), yf(y_in), xf(w_in), yf(h_in)
    try:
        img = mpimg.imread(str(path))
    except Exception:
        ax.text(x + w / 2, y + h / 2, f"[missing figure]\n{Path(path).name}",
                ha="center", va="center", fontsize=7, color="red")
        return
    ih, iw = img.shape[0], img.shape[1]
    aspect = iw / ih
    box_aspect = w_in / h_in
    if aspect > box_aspect:
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
                fontsize=7.2, color=MUTED, style="italic", wrap=True)


def header(ax, title, page_no):
    if title:
        ax.text(xf(MARGIN), yf(PAGE_H - 0.62), title, fontsize=13,
                fontweight="bold", color=ACCENT, va="center")
        ax.plot([xf(MARGIN), 1 - xf(MARGIN)], [yf(PAGE_H - 0.78)] * 2,
                color=RULE, lw=1)
    ax.text(1 - xf(MARGIN), yf(0.45), f"{page_no}", ha="right",
            fontsize=8, color=MUTED)
    ax.text(xf(MARGIN), yf(0.45),
            "PUNCH Coronagraph — Progress Report · Jassim Hussain",
            ha="left", fontsize=7, color=MUTED)


def section(ax, y_in, text, fontsize=11.5):
    ax.text(xf(MARGIN), yf(y_in), text, fontsize=fontsize, fontweight="bold",
            color=ACCENT, va="top")
    return y_in - 0.32


with PdfPages(OUT) as pdf:
    # ========================= PAGE 1 =========================
    fig, ax = new_page()

    band_h = 2.15
    ax.add_patch(plt.Rectangle((0, yf(PAGE_H - band_h)), 1, yf(band_h),
                               color=ACCENT, zorder=0))
    ax.text(xf(MARGIN), yf(PAGE_H - 0.85),
            "Adapting the MEE Pipeline to PUNCH Coronagraph Data",
            fontsize=16.5, fontweight="bold", color="white", va="center")
    ax.text(xf(MARGIN), yf(PAGE_H - 1.32),
            "Centroid detection, Gaia validation, and what the noise floor taught us",
            fontsize=10.5, color="#d6e4f0", va="center")
    ax.text(xf(MARGIN), yf(PAGE_H - 1.78),
            "Prepared by Jassim Hussain   |   PI: Prof. Jesse Kinder   |   July 2026",
            fontsize=9, color="#eaf1f8", va="center")

    summ = [
        "Over the past few weeks I adapted our MEE2024 Tab 1 centroid pipeline to PUNCH Level-3 white-light",
        "coronagraph images. PUNCH turned out to be different enough from eclipse data that I went through three",
        "full pipeline iterations before getting a clean result — the corona itself generates thousands of false",
        "detections, so I ultimately masked the inner field and validated everything that remained against the Gaia",
        "star catalog using PUNCH's mission pointing solution.",
        "",
        "The pipeline works: of 4,343 detected centroids in the final run, 86% correspond to real catalog stars.",
        "But the same analysis quantified a hard limitation — at PUNCH's plate scale (~81\u2033/pixel), the gravitational",
        "deflection signal for even our closest detectable star is roughly 1,000x below our measured position noise.",
        "Moving closer to the Sun doesn't fix this: at PUNCH's resolution, no observable radius puts the signal",
        "above the noise.",
        "",
        "The value of this exercise is that the machinery — centroid finding, catalog matching, and the deflection",
        "sensitivity check — is now built and validated, and the numbers tell us exactly what kind of instrument it",
        "needs next: a finer plate scale that reaches closer to the Sun. For future runs I also plan a visual-first",
        "step (confirming stars by eye before trusting automated matches), a check I skipped on this first pass.",
    ]
    box_top = PAGE_H - band_h - 0.30
    n_text = sum(1 for line in summ if line)
    n_blank = len(summ) - n_text
    box_h = 0.62 + n_text * LH + n_blank * 0.55 * LH + 0.12
    box_bot = box_top - box_h
    ax.add_patch(plt.Rectangle((xf(MARGIN), yf(box_bot)), 1 - 2 * xf(MARGIN),
                               yf(box_h), color=BOXBG, ec=RULE, lw=1))
    ax.text(xf(MARGIN + 0.2), yf(box_top - 0.26), "Executive Summary",
            fontsize=11, fontweight="bold", color=ACCENT, va="top")
    para(ax, MARGIN + 0.2, box_top - 0.60, summ)

    yy = section(ax, box_bot - 0.28, "1.  Data & Setup")
    data_rows = [
        ("Instrument:", "PUNCH (Polarimeter to Unify the Corona and Heliosphere), Level-3 white light."),
        ("Frame:", "2026-02-19 00:16 UTC, 4096 x 4096 pixels, Sun centered at pixel (2048, 2048)."),
        ("Plate scale:", "~81 arcsec/pixel — about 44x coarser than our eclipse data (~1.85\u2033/px); 1 R\u2609 \u2248 12 px."),
        ("The challenge:", "the corona fills the inner ~20% of the frame with bright, lumpy structure that the"),
        ("", "centroid finder happily mistakes for stars."),
    ]
    for lead, txt in data_rows:
        if lead:
            ax.text(xf(MARGIN + 0.05), yf(yy), lead, fontsize=FS,
                    fontweight="bold", color=INK, va="top")
        ax.text(xf(MARGIN + 1.15), yf(yy), txt, fontsize=FS, color=INK, va="top")
        yy -= 0.215

    fig1_top = yy - 0.12
    add_image(ax, PROJECT / "PUNCH_L3_CAM_20260219.png",
              MARGIN, 0.95, PAGE_W - 2 * MARGIN, fig1_top - 0.95,
              caption="Figure 1. The 2026-02-19 PUNCH white-light frame. The Sun (black disk) is surrounded by the bright corona;\n"
                      "real stars are faint points in the outer field. Everything inside the corona is a minefield for automated star detection.")
    header(ax, "", 1)
    pdf.savefig(fig)
    plt.close(fig)

    # ========================= PAGE 2 =========================
    fig, ax = new_page()
    header(ax, "2.  What I Did — Three Iterations to a Clean Detection", 2)

    # ---- run table ----
    tbl_top = PAGE_H - 1.15
    rows = [
        ["Run", "Threshold", "Corona handling", "Centroids", "Outcome"],
        ["01", "\u03c3 = 6", "none (MEE's blob mask never fires on PUNCH)", "9,255", "mostly corona junk"],
        ["02", "\u03c3 = 10", "none", "4,824", "still corona-dominated"],
        ["03", "\u03c3 = 10", "circle mask, r < 1000 px", "4,343", "clean — used for analysis"],
    ]
    col_x = [MARGIN + 0.05, MARGIN + 0.55, MARGIN + 1.45, MARGIN + 4.35, MARGIN + 5.15]
    rh = 0.26
    for r, row in enumerate(rows):
        ytop = tbl_top - r * rh
        if r == 0:
            ax.add_patch(plt.Rectangle((xf(MARGIN), yf(ytop - rh + 0.05)),
                                       1 - 2 * xf(MARGIN), yf(rh),
                                       color=ACCENT, zorder=0))
        elif r % 2 == 0:
            ax.add_patch(plt.Rectangle((xf(MARGIN), yf(ytop - rh + 0.05)),
                                       1 - 2 * xf(MARGIN), yf(rh),
                                       color="#f4f7fa", zorder=0))
        for c, cell in enumerate(row):
            bold = (r == 0) or (r == 3 and c == 2)
            ax.text(xf(col_x[c]), yf(ytop - 0.055), cell, fontsize=8.3,
                    va="top", color="white" if r == 0 else INK,
                    fontweight="bold" if bold else "normal")

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

    yy = section(ax, yy - 0.18, "2.1  Validating against Gaia")
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
            ax.text(xf(MARGIN + 0.05), yf(yy), "\u2022", fontsize=FS, color=ACCENT, va="top")
        ax.text(xf(MARGIN + 0.22), yf(yy), txt, fontsize=FS, color=INK, va="top")
        yy -= LH

    add_image(ax, PROJECT / "Coronagraph Runs/punch_tab1_run03/gaia_match_overlay.png",
              MARGIN, 1.15, PAGE_W - 2 * MARGIN, yy - 0.20 - 1.15,
              caption="Figure 2. Run 03 validation. Left: detected centroids (cyan) on the masked PUNCH frame. Right: the Gaia truth set —\n"
                      "green points are catalog stars recovered by the pipeline. The empty central region is the r < 1000 px corona mask.")
    pdf.savefig(fig)
    plt.close(fig)

    # ========================= PAGE 3 =========================
    fig, ax = new_page()
    header(ax, "3.  The Limiting Result — Deflection Signal vs. Noise Floor", 3)

    # key numbers block
    kb_top = PAGE_H - 1.2
    kb_h = 1.42
    ax.add_patch(plt.Rectangle((xf(MARGIN), yf(kb_top - kb_h)),
                               1 - 2 * xf(MARGIN), yf(kb_h),
                               color=BOXBG, ec=RULE, lw=1))
    kv = [
        ("Closest detectable star:", "83.7 solar radii from Sun center (set by the corona mask)"),
        ("Predicted Einstein deflection there:", "0.021 arcsec  \u2248  0.0003 pixels"),
        ("Measured position noise:", "22.6 arcsec  \u2248  0.28 pixels  (median centroid-to-Gaia residual)"),
        ("The gap:", "signal is ~1,000x below the noise"),
    ]
    yy = kb_top - 0.22
    for lead, txt in kv:
        ax.text(xf(MARGIN + 0.2), yf(yy), lead, fontsize=9.2, fontweight="bold",
                color=INK, va="top")
        ax.text(xf(MARGIN + 3.05), yf(yy), txt, fontsize=9.2, color=INK, va="top")
        yy -= 0.29

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
    yy = para(ax, MARGIN, kb_top - kb_h - 0.28, p)

    fig3_top = yy - 0.15
    add_image(ax, PROJECT / "Coronagraph Runs/punch_tab1_run03/deflection_sensitivity_scatter.png",
              MARGIN, fig3_top - 2.15, PAGE_W - 2 * MARGIN, 2.15,
              caption="Figure 3. Measured star offsets vs. distance from the Sun (left: total offset, right: radial component). The red curve\n"
                      "is the predicted Einstein deflection (1.75\u2033/r) — three orders of magnitude below the measurement noise at every\n"
                      "distance PUNCH can see. The dashed gray line is the ~23\u2033 noise floor.")

    # supplementary: preprocessed preview to show the mask visually
    add_image(ax, PROJECT / "Coronagraph Runs/punch_tab1_run03/preprocessed_preview.png",
              MARGIN, 1.35, PAGE_W - 2 * MARGIN, fig3_top - 2.15 - 0.75 - 1.35,
              caption="Figure 4. The corona mask that made run 03 work. Left: original frame. Right: the pre-processed input actually fed\n"
                      "to the centroid finder — everything inside r < 1000 px (dashed circle) is flattened to a single sky value.")
    pdf.savefig(fig)
    plt.close(fig)

    # ========================= PAGE 4 =========================
    fig, ax = new_page()
    header(ax, "4.  Refined Approach & Next Steps", 4)

    yy = section(ax, PAGE_H - 1.05, "4.1  A visual-first check")
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

    fig5_h = 3.35
    fig5_bot = yy - 0.12 - fig5_h
    add_image(ax, PROJECT / "Coronagraph Runs/punch_top20/PUNCH_top20_comparison_20260703_211737.png",
              MARGIN, fig5_bot, PAGE_W - 2 * MARGIN, fig5_h,
              caption="Figure 5. Top-20 brightest detections (orange circles) vs. top-20 predicted Gaia stars (cyan squares). Where a circle\n"
                      "has no square, the \"star\" is corona. The closest genuine match, at roughly the 3 o'clock position, lies at ~98 solar radii.")

    yy = section(ax, fig5_bot - 0.42, "4.2  A working principle I've adopted")
    p = [
        "For anything astrometric, I now treat the native mission FITS as the only source of truth. Display products",
        "(JP2s, PNGs) are stretched, 8-bit, and lossy-compressed — I verified that a JP2 re-wrapped as FITS carries",
        "only 256 distinct pixel values versus thousands in the real data — so they cannot be used for sub-pixel",
        "position work, no matter the file extension.",
    ]
    yy = para(ax, MARGIN, yy, p)

    # next steps box
    steps = [
        ["Apply the visual-first workflow to establish a trusted star list per frame."],
        ["Repeat the brightest-N analysis across multiple PUNCH dates: same stars, many epochs — this validates",
         "the method and pins down our real error budget (even though PUNCH itself cannot yield L)."],
        ["In parallel, I'm looking for a suitable dataset from a finer-scale coronagraph (the STEREO instruments,",
         "at ~15\u2033/px and reaching within a few solar radii of the limb, are the leading candidates). If I can source",
         "a good science-grade frame, that's where this pipeline gets pointed next."],
    ]
    n_lines = sum(len(s) for s in steps)
    nb_h = 0.55 + n_lines * 0.205 + len(steps) * 0.06 + 0.10
    nb_top = yy - 0.15
    ax.add_patch(plt.Rectangle((xf(MARGIN), yf(nb_top - nb_h)),
                               1 - 2 * xf(MARGIN), yf(nb_h),
                               color=BOXBG, ec=RULE, lw=1))
    ax.text(xf(MARGIN + 0.2), yf(nb_top - 0.24), "Next steps",
            fontsize=10.5, fontweight="bold", color=ACCENT, va="top")
    yy = nb_top - 0.58
    for lines in steps:
        ax.text(xf(MARGIN + 0.22), yf(yy), "\u2022", fontsize=9, color=ACCENT, va="top")
        for i, line in enumerate(lines):
            ax.text(xf(MARGIN + 0.38), yf(yy), line, fontsize=8.5, color=INK, va="top")
            yy -= 0.205
        yy -= 0.06

    pdf.savefig(fig)
    plt.close(fig)

    d = pdf.infodict()
    d["Title"] = "PUNCH Coronagraph Progress Report (v2)"
    d["Author"] = "Jassim Hussain"
    d["Subject"] = "Progress update for PI Jesse Kinder"

print(f"WROTE {OUT} ({OUT.stat().st_size/1024:.0f} KB)")
