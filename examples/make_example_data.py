"""Create a small synthetic label volume to try the Fiji scripts on.

Usage:  python examples/make_example_data.py [OUTPUT_FOLDER]

Writes example_labels.tif, by default into data/ (which git ignores). Needs
tifffile:  python -m pip install tifffile

Two box-shaped objects, with typical anisotropic FIB-SEM voxels: 8 nm
in-plane, 16 nm between slices, so one voxel is 1,024 nm³. Object 1 is
8 x 20 x 20 voxels (3,276,800 nm³); object 2 is 12 x 40 x 40 voxels
(19,660,800 nm³). Use these values to check results by hand.
"""

import sys
from pathlib import Path

import numpy as np

VOXEL_SIZE = {"z": 16.0, "y": 8.0, "x": 8.0}  # nanometres


def make_labels() -> np.ndarray:
    labels = np.zeros((32, 128, 128), dtype=np.uint16)
    labels[4:12, 10:30, 10:30] = 1  # 8 x 20 x 20 voxels
    labels[16:28, 60:100, 60:100] = 2  # 12 x 40 x 40 voxels
    return labels


def write_tiff(labels: np.ndarray, path: Path) -> None:
    import tifffile

    # ImageJ-style TIFF, so Fiji reads the voxel size and unit.
    tifffile.imwrite(
        path,
        labels,
        imagej=True,
        resolution=(1 / VOXEL_SIZE["x"], 1 / VOXEL_SIZE["y"]),
        metadata={"spacing": VOXEL_SIZE["z"], "unit": "nm", "axes": "ZYX"},
    )


def main(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    labels = make_labels()
    path = out_dir / "example_labels.tif"
    if path.exists():
        print(f"{path} already exists, leaving it as it is")
        return
    try:
        write_tiff(labels, path)
    except ImportError:
        print("Skipped example_labels.tif: to make it, run  python -m pip install tifffile")
        return
    print(f"Wrote {path}")


if __name__ == "__main__":
    default = Path(__file__).resolve().parent.parent / "data"
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else default)
