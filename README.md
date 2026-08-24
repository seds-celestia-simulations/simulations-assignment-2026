# Simulations Induction Assignment 2026.

Crew member induction assignment for the Simulations vertical, split across three
weeks of work. Each week lives in its own directory with its own spec PDF, code
template and README brief.

| Week | Topic | Status |
| --- | --- | --- |
| [Week 1](./week%201) | *Rigid Balls, Round Walls* — gravity integration and collision detection for rigid balls bouncing inside a circular boundary, drawn with Pygame. | released |
| Week 2 | TBD | not released |
| Week 3 | TBD | not released |

## Getting started

1. Click **Use this template → Create a new repository** at the top of this page.
   Make it **public** — it is what you will submit. Do not fork, and do not clone
   this repository directly; you cannot push to it.
2. Clone your own copy and set up the environment (see below).
3. Work inside the week's directory. The template files contain `TODO` blocks —
   those are the assignment.

## Setup (uv)

[uv](https://docs.astral.sh/uv/) handles Python and the dependencies. Install it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then, from the week's directory:

```bash
uv init                # only if pyproject.toml does not exist yet
uv add pygame numpy
uv run main.py
```

## What to do each week

1. Read the week's spec PDF. It is the authority on what the simulation has to do.
2. Fill in the `TODO` blocks in that week's code.
3. **Replace that week's `README.md` with your assignment brief**: answers to the
   questions marked in the PDF (mandatory), plus what you make of your own
   results — where it broke, what surprised you, what you could not get working.
   Half a page is plenty.
4. Commit and push to your repository.
5. Link the repository in the Google Form.

Incomplete work submitted with honest notes on where it broke scores above
complete work you cannot explain. Partial submissions are read: genuine effort
and clear thinking count for more than a finished notebook you cannot explain.
