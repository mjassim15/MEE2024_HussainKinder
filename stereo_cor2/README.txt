STEREO-A SECCHI COR2 — 2014-05-15 07:54 UTC
================================================

Three related files for the SAME observation time as STEREO_SECCHI_starfield.ipynb.

WHICH FILE TO USE?
------------------
| File | What it is | Stars visible? | Best for |
|------|------------|----------------|----------|
| STEREO_COR2_A_20140515_075400_helioviewer.fits | JP2 converted to FITS (Helioviewer) | YES | Matching the notebook, Gaia overlays, quick viewing |
| 20140515_075400_d4c2A.fts | Mission Level-0.5 archive FITS | Only after calibration/stretch | Real astrometry pipeline input (needs SECCHI_PREP-style calibration) |
| STEREO_COR2_A_20140515_075400.jp2 | Helioviewer JPEG2000 (notebook source) | YES | Notebook only; use the .fits export instead |

IMPORTANT
---------
There is NO pre-made public FITS that is byte-for-byte identical to the Helioviewer JP2.
Helioviewer processes the mission L0 file (d4c2A) through calibration + display scaling
before serving JP2. The archive only distributes Level-0.5 FITS via VSO/SSC.

For mission-grade astrometry, scientists run SECCHI_PREP (SolarSoft/IDL) on the L0 file
to produce Level-1 FITS (bias/flat/vignette/distortion corrected). That L1 product is
NOT hosted as a ready download — you generate it locally from the L0 .fts file.

File naming (mission):
  d4c2A = total-brightness "double" image (0° + 90° pol summed onboard)
  n4c2A = single polarization frame in a sequence (seq/ directory)
  d7c2A = polarization-sequence related product

SunPy gallery starfield example intentionally uses Helioviewer JP2 because it is
already display-calibrated. Our helioviewer.fits export preserves that image + WCS.
