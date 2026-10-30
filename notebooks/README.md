# Notebooks

Jupyter notebooks for **this project's own analysis**: exploring your data,
trying parameters, and making figures, e.g. from the tables the Fiji
scripts write. There are none yet.

## Run them

```bash
python -m pip install -e ".[notebooks]"
jupyter lab
```

## Good habits

- **Parameters at the top.** Put paths and settings in the first code cell,
  so it's clear what to change, and never hard-code paths to your own
  computer further down.
- **Run top to bottom before committing:** *Kernel → Restart Kernel and Run
  All Cells*. A notebook that only works when cells are run in a particular
  order can't be reproduced.
- **Outputs aren't saved in git.** Plots and tables in notebooks can be large
  and may show unpublished data, so a pre-commit hook (nbstripout) removes
  them when you commit, and a test checks none slip through. Save figures you
  want to keep to `results/`.
- **Move reusable steps into a Fiji script.** Once a step is used in more
  than one notebook, or other people will run it, make it a script in
  `fiji/` with a test.
- **Record decisions.** If a notebook leads you to choose a threshold or
  method, add it to [`docs/decisions.md`](../docs/decisions.md).
- **No data in notebooks:** read it from `data/` or your institute's storage.
