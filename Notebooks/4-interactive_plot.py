import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Examples of marimo UI widgets (inputs, layouts...)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1 - Play with *checkbutton*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Minimalist plot
    """)
    return


@app.cell
def _(mo):
    grid   = mo.ui.checkbox(label="Show grid")
    legend = mo.ui.checkbox(label="Show legend")
    return grid, legend


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `plt.show()` displays the graph in console output:
    """)
    return


@app.cell(hide_code=True)
def _(grid, legend):
    grid, legend
    return


@app.cell(hide_code=True)
def _(grid, legend, np, plt):
    plt.figure(figsize=(3,2))
    _x = np.arange(0,6,0.1)
    plt.plot(_x, np.sin(_x), label="sine")
    plt.grid(grid.value)
    plt.title('plt.show() rendering')
    if legend.value: plt.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _(grid, legend, np, plt):
    plt.figure(figsize=(3,2))
    _x = np.arange(0,6,0.1)
    plt.plot(_x, np.sin(_x), label="sine")
    plt.grid(grid.value)
    plt.title('plt.gca() rendering')
    if legend.value: plt.legend()
    #plt.show()
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Better plot
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tips:
    - use `mo.vstack` as last line to display the UI elements `grid`, `legend` and the plot in the __cell output__ (above the cell)
    -  use matplotlib OO style for smoother display
    """)
    return


@app.cell(hide_code=True)
def _(grid, legend, mo, np, plt):
    _fig, _ax = plt.subplots(1, 1, figsize=(11, 3))
    _x = np.arange(0, 6, 0.1)
    _ax.plot(_x, np.sin(_x), label="sine")
    _ax.grid(grid.value)
    _ax.set_xlabel('Time [s]')
    if legend.value: _ax.legend()

    mo.vstack([grid, legend, _fig])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2 - Sliders for dynamically interacting with the drawing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Naive way
    """)
    return


@app.cell
def _(mo):
    freq  = mo.ui.slider(1,  10, 1, label='freq. (Hz)', show_value=True)
    phase = mo.ui.slider(0, 180, 1, label=r'phase (°)', show_value=True)
    tmax  = mo.ui.slider(1,  10, 1, label=r'$t_{max}$ (sec)', show_value=True)
    return freq, phase, tmax


@app.cell
def _(freq, mo, np, phase, plt, tmax):
    _t   = np.arange(0, tmax.value, 0.01)
    _f   = freq.value
    _phi = phase.value

    fig, ax = plt.subplots(1,1, figsize=(10,3))
    ax.plot(_t, np.sin(2*np.pi*_f*_t + _phi), label=fr"$\sin(2 \pi {_f} t + {np.degrees(_phi):.1f}°)$")
    fig.suptitle('Sine plot')
    fig.tight_layout()
    ax.set_xlabel('time [s]')
    ax.grid(which='major', color='xkcd:cool grey',  linestyle='-',  alpha=0.7)
    ax.grid(which='minor', color='xkcd:light grey', linestyle='--', alpha=0.5)
    ax.legend(loc='upper right')
    mo.vstack([mo.hstack([freq, phase, tmax], justify='start'), fig])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Marimo style
    """)
    return


@app.cell
def _(mo):
    f2 = mo.ui.slider(1,  10, 1, label='freq. (Hz)', show_value=True)
    p2 = mo.ui.slider(0, 180, 1, label=r'phase (°)', show_value=True)
    t2 = mo.ui.slider(1,  10, 1, label=r'$t_{max}$ (sec)', show_value=True)
    return f2, p2, t2


@app.cell(hide_code=True)
def _(mo, np, plt):
    def plot_sine_with_slider(freq, phase, tmax):
        t = np.arange(0, tmax.value, 0.005)
        f = freq.value
        phi = np.radians(phase.value)

        fig, ax = plt.subplots(1,1, figsize=(10,3))
        ax.plot(t, np.sin(2*np.pi*f*t + phi))
        fig.suptitle(fr"Plot of function $\sin(2 \pi\,{f}\,t + {phi:.2f}°)$")
        fig.tight_layout()
        ax.set_xlabel('time [s]')
        ax.grid(which='major', color='xkcd:cool grey',  linestyle='-',  alpha=0.7)
        ax.grid(which='minor', color='xkcd:light grey', linestyle='--', alpha=0.5)
        return mo.vstack([mo.hstack([freq, phase, tmax], justify='start'), fig])    

    return (plot_sine_with_slider,)


@app.cell
def _(f2, p2, plot_sine_with_slider, t2):
    plot_sine_with_slider(f2, p2, t2)
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, np, plt


if __name__ == "__main__":
    app.run()
