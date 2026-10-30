# mito-seg

[![Tests](https://github.com/martlj/test-1/actions/workflows/tests.yml/badge.svg)](https://github.com/martlj/test-1/actions/workflows/tests.yml)

[Fiji](https://fiji.sc) scripts for segmenting mitochondria in FIB-SEM volumes.

## Installation

<!-- The text between the --8<-- markers also appears on the documentation
site (docs/getting-started.md), so it's written only once. Keep links out of
it: they would break on the site. -->
<!-- --8<-- [start:install] -->
You need [Fiji](https://fiji.sc). The scripts are plain text files in the
`fiji/` folder: download the repository (the green **Code** button on GitHub,
then **Download ZIP**), or clone it with git:

```bash
git clone https://github.com/martlj/test-1.git
```

There's nothing else to install to run the scripts.
<!-- --8<-- [end:install] -->

To work on the code itself, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Quick start

<!-- --8<-- [start:quickstart] -->
Make a small synthetic label volume. This needs Python with `tifffile`
(`python -m pip install tifffile`):

```bash
python examples/make_example_data.py
```

It writes `data/example_labels.tif`: two box-shaped objects with
8 × 8 × 16 nm voxels. Then, in Fiji, open
`fiji/measure_object_volumes.groovy`, click **Run**, and choose
`data/example_labels.tif` and an output folder, e.g. `results/example`. The
script writes:

- `object_volumes.csv`: the volume of each object in nm³;
- `provenance.json`: the parameters, input, ImageJ version and the script's
  checksum.

Object 1 is 8 × 20 × 20 voxels of 1,024 nm³ each, so its volume should be
3,276,800 nm³.
<!-- --8<-- [end:quickstart] -->

## Getting help

Report bugs and ask for features in the
[issue tracker](https://github.com/martlj/test-1/issues). For
general questions, use the [image.sc forum](https://forum.image.sc/).

## Contributing

Contributions are welcome. New to coding or GitHub? Start with
[START_HERE.md](START_HERE.md). The full details are in
[CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

If you use this software, please cite it using [CITATION.cff](CITATION.cff)
(GitHub's **Cite this repository** button).

## Use of AI

<!-- Describe substantive use of generative AI in developing this software,
or delete this section if none. See guidance/ai-use.md. -->

Generative AI coding assistants were used in developing this software. All
changes were reviewed by a maintainer before merging, and are covered by the
automated tests.

## Licence

[BSD-3-Clause](LICENSE).
