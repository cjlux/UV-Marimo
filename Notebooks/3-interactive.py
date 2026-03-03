import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Interactive widgets (UI elements)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1 - The `Slider` widget
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🌈 Simple usage
    """)
    return


@app.cell
def _(mo):
    s1 = mo.ui.slider(1,10)
    s1    # last line of a cell is always displayed as the "cell visual"
    return (s1,)


@app.cell(hide_code=True)
def _(mo, s1):
    mo.md(f"""
    f-strings are allowed within Makdwon cells $\leadsto$ check the 'f' case bellow the cell code  frame...<br>
    sliber _s1_ value: {s1.value}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ⚠️ `print` statement causes some flashes...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    s2 = mo.ui.slider(1,10)
    s2
    return (s2,)


@app.cell
def _(s2):
    # print(...) displays data using the *console output* (display updates flash a bit)
    print(f"value of the 's1' slider: {s2.value}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🎂 Usage of `mo.hstack(...)` to horizonthaly concatenate objects
    """)
    return


@app.cell
def _(mo):
    slider_mass = mo.ui.slider(start=1, stop=110, label="Mass", value=50)
    return (slider_mass,)


@app.cell
def _(mo, slider_mass):
    mo.hstack([slider_mass, mo.md(f"Mass: {slider_mass.value:3d} kg")], justify='start')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Other -marimo_ layout widhets here: https://docs.marimo.io/api/layouts/
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2 - The `Date` widget
    """)
    return


@app.cell
def _(mo):
    dates = mo.md("{start} → {end}").batch(
        start=mo.ui.date(label="Start Date"),
        end=mo.ui.date(label="End Date")
    )
    dates
    return (dates,)


@app.cell
def _(dates):
    dates.value
    return


@app.cell
def _(dates, mo):
    mo.md(rf"""
    {dates['start']}
    """)
    return


@app.cell
def _(dates):
    {dates['start'].value}
    return


@app.cell
def _(dates):
    print(dates['start'].value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Other marimo input here : https://docs.marimo.io/api/inputs/
    """)
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np

    return (mo,)


if __name__ == "__main__":
    app.run()
