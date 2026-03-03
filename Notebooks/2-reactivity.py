import marimo

__generated_with = "0.20.2"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Marimo is REACTIVE
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1 - Hide / show cell code 🔨
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can __hide__ or __show__ the code (Python, MarkDow, SQL...) of a cell with the shortcut __`CTRL+H`__<br>
    By default MarkDon cells code is hidden.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2 - __Cell outputs__ _versus_ __console outputs__ ⚠️
    """)
    return


@app.cell(hide_code=True)
def _(mo, text_cell_outputs, text_console_outputs):
    mo.accordion(
        {
            "__Cell outputs__": mo.md(text_cell_outputs),
            "__Console outputs__": mo.md(text_console_outputs),
        }
    )
    return


@app.cell(hide_code=True)
def _():
    text_cell_outputs = '''
    - Every cell can have a __visual output__ called a __cell output__ given by its __last line__.
    - When _editing_, cell outputs are displayed __above cells__.
    - When _running_ a notebook as an __application__, its UI is an arrangement of its cells outputs.<br>
    You can also create outputs programmatically, using `mo.output.replace()` and `mo.output.append()`.'''

    text_console_outputs="""
    - Text written to _stdout/stderr_, including `print` statements and logs
    - Shows up in a __console output area bellow the cell__.
    - By default, these console outputs don't appear when running a marimo notebook as an application.<br> 
    If you do want them to appear in apps, marimo provides utility functions for capturing console outputs and redirecting them to cell outputs.
    """
    return text_cell_outputs, text_console_outputs


@app.cell
def _():
    print('Console output (made by print)')
    'Cell output (last line)'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3 - Reactivity 😇
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\leadsto$ when you modify an object definition, all the cells (Python, Markdown...) using this object are _automatically_ run:
    """)
    return


@app.cell
def _():
    angle = 90              # degrees
    return (angle,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The next cell uses $angle$ in a f_string:
    """)
    return


@app.cell
def _(angle):
    print(f'value of the angle is: {angle}° (by print)')
    f'value of the angle is: {angle}° (last line)'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next cell uses $angle$ to define $y$:
    """)
    return


@app.cell
def _(angle, np):
    y = np.cos(np.radians(angle))
    print(f'{float(y):.3f}')
    return (y,)


@app.cell(hide_code=True)
def _(angle, mo, y):
    mo.md(rf"""
    You can even use _f_strings_ inside a mardown cell like this one: rounded value of cos({angle}°) $\leadsto$ {y:.3f}
    """)
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np

    return mo, np


if __name__ == "__main__":
    app.run()
