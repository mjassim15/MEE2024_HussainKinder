
# MEE2024
Modern Eddington Experiment codebase

## Installation

### Windows

The Windows executable (see releases) will run on Windows 10 and 11 computers without having to install Python.

### Mac/Linux

- The recommended way to install MEE2024 is via pip in the terminal. As a pre-requisite, this requires an install of Python 3.9+, with Python added to path (see https://www.python.org/downloads/).

- (Linux only: you may need to install tkinter for python: sudo apt-get install python3-tk)

- Note that a terminal is required both to install and launch the program.

- Then to either install or run, paste the following into a terminal (you may want to save the command to a local re-usable bash file):

```
set -e

APP_NAME="mee2024"
ENV_DIR="$HOME/.mee2024env"
REPO_URL="git+https://github.com/andrew551/MEE2024.git"

echo "Using environment: $ENV_DIR"

if [ ! -d "$ENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$ENV_DIR"
fi

source "$ENV_DIR/bin/activate"

if ! command -v mee2024 >/dev/null 2>&1; then
    echo "Installing / reinstalling MEE2024..."
    pip install --upgrade pip
    pip install --upgrade "$REPO_URL"
fi

echo "Launching MEE2024..."
exec mee2024
```
After installing, you may use this to run MEE2024:
```
source "$HOME/.mee2024env/bin/activate"
mee2024
```


### Installation from Source

- To run (and potentially edit) the Python source code, install the most recent version of Python from python.org (make sure to check the box to add Python to PATH on windows).

- **macOS tip:** Apple’s `/usr/bin/python3` often ships an old **Tk** (FreeSimpleGUI warns about Tk 8.5.x) and some binary wheels can **abort** at startup on newer macOS. For a reliable GUI, use **Python 3.12+** from [python.org](https://www.python.org/downloads/) or install a standalone interpreter with [uv](https://docs.astral.sh/uv/) (`uv python install 3.12`), then recreate `.venv` and reinstall requirements.

- To install requirements: `pip install -r requirements.txt` (inside your virtual environment).

- **Launch the GUI** (from the repository root, after activating `.venv`):

```
./run_gui.sh
```

  Or: `python -m mee2024.main` (do **not** use `python mee2024/main.py`, which breaks package imports).

## Kaggle: PI-aligned Station 1 subset (400 ms run)

The full [Station 1 dataset on Kaggle](https://www.kaggle.com/datasets/kinderphysics/mee-2024-station-1) is very large. To download only the calibration and eclipse 400 ms frames that match the published MEE 2024 layout (one run, not the whole tree), from the repo root (with `.venv` and `~/.kaggle/kaggle.json` set up):

```bash
# Preview file count and total size (no download)
DRY_RUN=1 ./scripts/get_pi_run_400ms.sh

# Download into data/pi_run_400ms/
./scripts/get_pi_run_400ms.sh
```

Kaggle’s CLI unzips each file into a **flat** `data/pi_run_400ms/` folder (only the filename, no subfolders). **After the download finishes**, run:

```bash
./scripts/organize_pi_run_400ms.sh
```

That recreates the intended tree: `calibration/darks/…`, `calibration/flats/…`, `eclipse/science-400ms/…`, and so on, so it lines up with the MEE 2024 layout. Until then, you can still read filenames: the time stamp in the name distinguishes sessions (e.g. `…-0618_5-…` vs `…-0628_3-…`).

A broader helper that can pick “latest” calibration sessions is `scripts/get_station1_400ms.sh`; use `get_pi_run_400ms.sh` when you want the exact run IDs from the project documentation.

## Tips

A small platesolve database is built into the executable (derived from the Tycho catalogue).

An internet connection is required to connect to the Gaia database.

Note that when the program is run for the first time, it may take a few minutes to perform some one-off precomputation.



## **Usage**

Run the Python file / executable obtained following installation.
Select the images to be stacked (the "Light frames").
Dark frame(s) and Flat frame(s) can also be selected, if desired.

It is recommended to choose an _Output folder_ or else the output files will be written to the same folder which contains the image data.

Select "Show graphics" if you want to view the intermediate graphical analysis (optional).
Choose the number of bright stars to be identified in the stacked image (the default of 100 is a reasonable choice).

The output FITS stacked image is by default resized to 16-bit (the same as the input). A second 32-bit floating point (FP) FITS file can also be saved (optional).
The program does its calculations in 32-bit FP to preserve accuracy. The 32-bit FP file will be twice the size of the 16-bit file.

The Dark and Flat stacked images can also be saved (optional); the format is 32-bit FP FITS. These stacks can be used in subsequent processing of Light frames.

"Remove big bright object" is useful when images contain the Sun or Moon. It can be kept enabled for star fields with no Sun or Moon.
The _blob_radius_extra_ parameter determines the extra exclusion zone outside the saturated region. The "extra" distance is measured in pixels.
The _centroid_gap_blob_ parameter determines which centroids outside the extra exclusion zone should be ignored. The "gap" distance is measured in pixels.
The default parameters are (100, 30) but neither is particularly sensitive.
The purpose of this function is to limit the centroid search to areas away from the Moon and the solar corona.

"Sensitive stacking mode" should only be use if images contain the Sun or Moon or are taken on a bright sky (e.g. twilight).
For dark-sky star fields, this mode will take too long and is not recommended.

"Use sensitive mode on stacked result" can be left on for most images which require accurate centroid finding, but the sensitivity parameters should adjusted accordingly.
A lower _sigma_thresh_ will increase the sensitivity (between 4 and 7 are typical values).
A smaller _min_area_ will mean centroids of smaller pixel size will be found (between 1 and 4 are typical values).
A higher _sigma_subtract_ will increase the background cutoff, thereby eliminating more noise and reducing the number of centroids found (between 0 and _sigma_thresh_ -2 are typical values). For good dark-sky images, (5.0, 4, 3.0) are reasonable values.

"Remove centroids near edges" will remove extraneous centroids associated with edge effects near the Moon or the solar corona.
This function can be left on, just like "Remove big bright object", even when processing normal star fields.

The file called _MEE_config.txt_ (saved in your appdata or userdata) stores the program parameters, including the input and output directories.
It is automatically updated each time the program is run, and can also be manually edited for advanced use (all standard parameters can be edited via the GUI).

## STEREO / SECCHI star-field notebook

`STEREO_SECCHI_starfield.ipynb` follows the [SunPy gallery example](https://docs.sunpy.org/en/stable/generated/gallery/units_and_coordinates/STEREO_SECCHI_starfield.html) (Gaia stars on a STEREO COR2 coronagraph image).

```bash
.venv/bin/pip install -r requirements-stereo.txt
brew install openjpeg   # macOS only — needed to read .jp2 from Helioviewer
```

Open the notebook, select the `.venv` kernel, run all cells (internet required).
