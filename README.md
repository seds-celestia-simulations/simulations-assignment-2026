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

Follow these in order. Every line in a grey box is typed into a terminal
(Terminal on macOS/Linux, PowerShell on Windows) and run with Enter.

### 1. Make your own copy of this repository

At the top of this page, click **Use this template → Create a new repository**.
Give it a name, set the visibility to **Public**, and create it. GitHub then
takes you to *your* repository — a full copy of this one, under your account.

Do **not** fork this repository, and do **not** clone this one directly. You do
not have permission to push to it, so your work would have nowhere to go.

### 2. Install the tools

**Git** — check whether you already have it:

```bash
git --version
```

If that prints a version number, skip ahead. If it says the command is not
found, install it from [git-scm.com/downloads](https://git-scm.com/downloads).

**uv** — this installs Python and the libraries for you, so you do not need to
install Python separately.

On macOS or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close the terminal and open a new one afterwards, then check it worked:

```bash
uv --version
```

### 3. Clone your repository in your computer

On *your* repository page, click the green **Code** button and copy the HTTPS
URL. It looks like `https://github.com/<your-username>/<your-repo-name>.git`.

Then, in a terminal, paste that URL into this command in place of the example:

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
```

That creates a folder with the same name as your repository. Move into it:

```bash
cd <your-repo-name>
```

### 4. Move into the week's folder

```bash
cd "week 1"
```

The quotes matter — the folder name has a space in it, and without them the
terminal reads it as two separate things.

### 5. Install the libraries and run the simulation

Run these three, one at a time, from inside the `week 1` folder:

```bash
uv init
uv add pygame numpy
uv run main.py
```

The first one sets up the project, the second downloads pygame and numpy, and
the third starts the simulation. This takes a moment the first time.

A window should open showing a circle with a ball inside it. Close the window to
stop the program.

From now on, only the last one is needed:

```bash
uv run main.py
```

### 6. Do the work, then save it back to GitHub

Open `main.py` in any editor and fill in the `TODO` blocks. Whenever you want to
save your progress to GitHub, run these three from inside your repository
folder:

```bash
git add .
git commit -m "describe what you changed"
git push
```

The first `git push` may ask you to sign in to GitHub. Once it finishes, refresh
your repository page in the browser and your changes will be there.

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
