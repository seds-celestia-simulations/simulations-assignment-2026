# Rigid Balls, Round Walls

Week 1 — SEDS Celestia Simulations induction. Build a 2D rigid-ball simulator in
Python with Pygame: equal-radius, equal-mass balls falling under gravity inside a
circular arena. Full spec in `week1.pdf`.

## Submission

1. Write the brief in the README file of your repository: answers to Question 1 and Question 2
   (mandatory), plus what you make of your own results like where it broke, what
   surprised you. Half a page is plenty.
2. Push source code + this README to a public GitHub repo.
3. Link the repo in the Google Form. Due EOD 7th June 2026.

**Honest notes on incomplete work score above finished work you cannot explain.**

## Setup (uv)

[uv](https://docs.astral.sh/uv/) handles Python and the dependencies. Install it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then from this directory:

```bash
uv init                # only if pyproject.toml does not exist yet
uv add pygame
uv run main.py
```

`uv run` creates the virtual environment and installs pygame on first use — no
manual `venv` activation needed. To drop into a shell with it anyway:

```bash
uv sync
source .venv/bin/activate
```

One-off run without touching the project files:

```bash
uv run --with pygame main.py
```

## Brief

*(answers go here)*
