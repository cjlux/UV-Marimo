import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium", layout_file="layouts/1-simple.slides.json")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Simple marimo notebook to show the content of the Python file
    """)
    return


@app.cell
def _(np):
    x = np.arange(1,5)
    return (x,)


@app.cell
def _(x):
    x
    return


@app.cell
def _():
    import numpy as np
    import marimo as mo

    return mo, np


if __name__ == "__main__":
    app.run()
