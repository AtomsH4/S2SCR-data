# S2SCR data

Reference images, calibration inputs, and LR-HSI/HR-MSI observation pairs for
hyperspectral–multispectral image fusion.

## Data files

The package contains six scene/setting combinations and two calibration
inputs. Reference images are included in the observation files.

| Scene | Setting | Reference HSI | LR-HSI | HR-MSI |
| --- | --- | --- | --- | --- |
| Pavia University | simx4 | 320×320×89 | 80×80×89 | 320×320×4 |
| Chikusei | simx4 | 432×432×89 | 108×108×89 | 432×432×4 |
| Washington DC Mall | simx4 | 288×288×89 | 72×72×89 | 288×288×4 |
| Pavia University | simx8 | 320×320×89 | 40×40×89 | 320×320×4 |
| Chikusei | simx8 | 384×384×89 | 48×48×89 | 384×384×4 |
| Washington DC Mall | simx8 | 256×256×89 | 32×32×89 | 256×256×4 |

- `release/observations/simx4/` and `simx8/`: losslessly zipped MAT files
  containing `gt`, `hrhsi`, `lrhsi`, `hrmsi`, `psf`, and `srf`; `gt` equals `hrhsi`.
- `release/calibration/`: `simx4.mat` and `simx8.mat`.
- `release/manifest.json`: file paths, array shapes, types, and hashes.
- `release/protocol.json`: preprocessing and observation construction.
- `release/sources.json`: original data sources and attribution.

Image arrays use HWC layout and float32. Fusion inputs are `lrhsi` and
`hrmsi`; the reference is `hrhsi`.

## Download and verify

```sh
git clone https://github.com/AtomsH4/S2SCR-data.git
cd S2SCR-data
python3 verify_public_integrity.py
```

All files use ordinary Git storage. ZIP files preserve the original MAT files;
their uncompressed hashes are included in the manifest.

## Load data

Install NumPy and SciPy with `python3 -m pip install -r requirements.txt`.

```python
from io import BytesIO
from zipfile import ZipFile
from scipy.io import loadmat

with ZipFile("release/observations/simx4/paviau.mat.zip") as archive:
    case = loadmat(BytesIO(archive.read("paviau_simx4.mat")))
print(case["hrhsi"].shape, case["lrhsi"].shape, case["hrmsi"].shape)
```

## Sources and reuse

Original providers are [NUD_PAF](https://github.com/jeline0110/NUD_PAF),
[University of Tokyo](https://naotoyokoya.com/Download.html),
[Purdue University](https://engineering.purdue.edu/~biehl/MultiSpec/hyperspectral.html), and
[Copernicus SentiWiki](https://sentiwiki.copernicus.eu/web/s2-documents).
Exact source links and processing details are in `release/sources.json`.

The authors gratefully acknowledge Space Application Laboratory, Department of
Advanced Interdisciplinary Studies, the University of Tokyo for providing the
hyperspectral data. For Chikusei, cite N. Yokoya and A. Iwasaki, technical report
SAL-2016-05-27 (May 2016).

Third-party data retain the original providers' terms; see `TERMS.md`.
`LICENSE` applies to the repository's original documentation and integrity helper.
