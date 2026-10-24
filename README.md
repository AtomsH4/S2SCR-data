# S2SCR data

Reference images, calibration inputs, and LR-HSI/HR-MSI observation pairs for
hyperspectral–multispectral image fusion.

## Data files

The package contains nine scene/setting combinations and three calibration
inputs. Reference images are included in the observation files.

| Scene | Setting | Reference HSI | LR-HSI | HR-MSI |
| --- | --- | --- | --- | --- |
| Pavia University | simx4 | 320×320×89 | 80×80×89 | 320×320×4 |
| Chikusei | simx4 | 432×432×89 | 108×108×89 | 432×432×4 |
| Washington DC Mall | simx4 | 288×288×89 | 72×72×89 | 288×288×4 |
| Pavia University | simx8 | 320×320×89 | 40×40×89 | 320×320×4 |
| Chikusei | simx8 | 384×384×89 | 48×48×89 | 384×384×4 |
| Washington DC Mall | simx8 | 256×256×89 | 32×32×89 | 256×256×4 |
| Pavia University | wv2 | 320×320×8 | 80×80×8 | 320×320×3 |
| Chikusei | wv2 | 432×432×8 | 108×108×8 | 432×432×3 |
| Washington DC Mall | wv2 | 288×288×8 | 72×72×8 | 288×288×3 |

- `release/observations/simx4/` and `simx8/`: losslessly zipped MAT files
  containing `gt`, `hrhsi`, `lrhsi`, `hrmsi`, `psf`, and `srf`; `gt` equals `hrhsi`.
- `release/observations/wv2/`: NPZ files containing `hrhsi`, `lrhsi`,
  `hrmsi`, `lr2hsi`, and `lrmsi`.
- `release/calibration/`: `simx4.mat`, `simx8.mat`, and `wv2.mat`.
- `release/manifest.json`: file paths, array shapes, types, and hashes.
- `release/protocol.json`: preprocessing and observation construction.
- `release/sources.json`: original data sources and attribution.

Image arrays use HWC layout and float32, except the WV2 calibration `lrhsi`,
which is uint16. Fusion inputs are `lrhsi` and `hrmsi`; the reference is
`hrhsi`. The WV2 calibration `hrmsi` contains a PAN image divided by 2047
and copied into three identical channels.

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
import numpy as np

with ZipFile("release/observations/simx4/paviau.mat.zip") as archive:
    case = loadmat(BytesIO(archive.read("paviau_simx4.mat")))
print(case["hrhsi"].shape, case["lrhsi"].shape, case["hrmsi"].shape)

with np.load("release/observations/wv2/paviau.npz", allow_pickle=False) as case:
    print(case["hrhsi"].shape, case["lrhsi"].shape, case["hrmsi"].shape)
```

## Sources and reuse

Original providers are [NUD_PAF](https://github.com/jeline0110/NUD_PAF),
[University of Tokyo](https://naotoyokoya.com/Download.html),
[Purdue University](https://engineering.purdue.edu/~biehl/MultiSpec/hyperspectral.html),
[PanCollection](https://github.com/liangjiandeng/PanCollection), and
[Copernicus SentiWiki](https://sentiwiki.copernicus.eu/web/s2-documents).
Exact source links and processing details are in `release/sources.json`.

The authors gratefully acknowledge Space Application Laboratory, Department of
Advanced Interdisciplinary Studies, the University of Tokyo for providing the
hyperspectral data. For Chikusei, cite N. Yokoya and A. Iwasaki, technical report
SAL-2016-05-27 (May 2016).

Third-party data retain the original providers' terms; see `TERMS.md`.
`LICENSE` applies to the repository's original documentation and integrity helper.
