# S2SCR curated fusion data

Curated reference images, degradation-estimation inputs, and simulated
LR-HSI/HR-MSI observation pairs accompanying S2SCR hyperspectral–multispectral
image fusion. Repository: https://github.com/AtomsH4/S2SCR-data.

## Contents

This repository distributes nine scene/setting combinations and three calibration
inputs. Selected evaluation references are embedded in each observation file;
separate copies of the full-band reference subsets are omitted.

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

- release/observations/simx4/ and simx8/: six losslessly zipped original MAT files,
  with gt, hrhsi, lrhsi, hrmsi, psf, srf and setting metadata. gt equals hrhsi.
- release/observations/wv2/: three NPZ files, with hrhsi, lrhsi, hrmsi, lr2hsi and lrmsi.
- release/calibration/: simx4.mat, simx8.mat and wv2.mat. Controlled calibration
  pairs/operators equal the corresponding Pavia observations/operators.
- release/manifest.json: shapes, array/file hashes and curation status.
- release/protocol.json and release/sources.json: processing details and attribution.
- paper_results.csv: 81 reported method/case results, transcribed at manuscript precision.

Image arrays use HWC layout and float32. The input pair is (lrhsi, hrmsi);
hrhsi is the evaluation reference. The original WV2 calibration lrhsi is uint16.
Its hrmsi is one PAN image divided by 2047 and replicated into three identical
channels.

## Download and verify

```sh
git clone https://github.com/AtomsH4/S2SCR-data.git
cd S2SCR-data
python3 verify_public_integrity.py
```

All data are ordinary Git files; Git LFS is not required. MATLAB containers
larger than GitHub's per-file limit are supplied as lossless ZIP archives.
Their original uncompressed MAT hashes are recorded in release/manifest.json.

To read a controlled case without extracting it to disk:

```python
from io import BytesIO
from zipfile import ZipFile
from scipy.io import loadmat

with ZipFile('release/observations/simx4/paviau.mat.zip') as archive:
    data = loadmat(BytesIO(archive.read('paviau_simx4.mat')))
print(data['hrhsi'].shape, data['lrhsi'].shape, data['hrmsi'].shape)
```

To read a WV2-transferred case:

```python
import numpy as np

with np.load('release/observations/wv2/paviau.npz', allow_pickle=False) as data:
    print(data['hrhsi'].shape, data['lrhsi'].shape, data['hrmsi'].shape)
```

Install NumPy and SciPy using requirements.txt for these examples.

## Original sources and terms

- WV2: [PanCollection](https://github.com/liangjiandeng/PanCollection), full-resolution
  test sample Test(HxWxC)_wv2_data_fr5.mat. Full-array numerical correspondence
  is verified after PAN normalization and channel replication.
- Pavia University processed reference: [NUD_PAF distribution](https://github.com/jeline0110/NUD_PAF/blob/2bbc506a982610c7b071a5c43000b84d6f7c959e/datasets/paviau.mat).
- Chikusei: [University of Tokyo / Naoto Yokoya](https://naotoyokoya.com/Download.html).
- Washington DC Mall: [Purdue University MultiSpec](https://engineering.purdue.edu/~biehl/MultiSpec/hyperspectral.html).
- Sentinel-2A response curves: [Copernicus SentiWiki](https://sentiwiki.copernicus.eu/web/s2-documents), 2024 v4.0.

The authors gratefully acknowledge Space Application Laboratory, Department of
Advanced Interdisciplinary Studies, the University of Tokyo for providing the
hyperspectral data. Cite N. Yokoya and A. Iwasaki, technical report
SAL-2016-05-27 (May 2016), for Chikusei.

See TERMS.md for source-specific attribution and reuse terms. The MIT license
covers the repository's original documentation and integrity-check helper;
third-party imagery and its derived arrays retain the upstream terms.
