# Roadmap

What's left to do, most important first. Finished work moves to
[CHANGELOG.md](CHANGELOG.md). Link each item to its issue.

## Next

- [ ] Write the first mitochondria segmentation script in `fiji/`, with
      tests on a small synthetic volume.
- [ ] Record the typical size of the FIB-SEM volumes and where they're
      stored, in `AGENTS.md` → *About this project*.
- [ ] Add the rule protecting `main` (`.github/rulesets/main.json`), once
      this setup is merged.

## Later

- [ ] Publish the documentation site on GitHub Pages.
- [ ] First release (`v0.1.0`) archived on Zenodo.
- [ ] Run the Fiji script tests in CI (e.g. a job that downloads Fiji):
      GitHub Actions skips them today, so they only run locally.
- [ ] Review the docs tooling: Material for MkDocs reaches end of life in
      May 2027; its successor is [Zensical](https://zensical.org/).

## Open questions

- Which segmentation method to use (e.g. thresholding, a trained classifier
  such as Labkit or Weka, or a deep-learning model). Decided by Martin Jones;
  record the choice in [docs/decisions.md](docs/decisions.md).
