"""
Cool plot library for Python

author: Atsushi Sakai (@Atsushi_twi)

Inspired:
- https://note.mu/goando/n/neb6ea35f1da3
- Qiita https://qiita.com/skotaro/items/cdb0732ad1ad2a4b6236

"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator
import matplotlib.dates as mdates


def horizontal_bar(index, data, color="C0", xlabel="", rate_graph=False):
    """
    Beautiful bar chart

    usage:
    data = [1000, 2000, 10000]
    index = ["A", "B", "C"]
    horizontal_bar(index, data)
    plt.show()

    """

    if rate_graph:
        data = [round(d / sum(data) * 100.0, 1) for d in data]

    combatpower = pd.DataFrame(data,
                               index=index,
                               columns=['data'])

    fig, ax = plt.subplots()
    plt.gca().invert_yaxis()
    ax.invert_yaxis()
    [spine.set_visible(False) for spine in ax.spines.values()]
    ax.tick_params(bottom=False, left=False, labelbottom=False)
    ax.tick_params(axis='y', labelsize='x-large')
    vmax = combatpower['data'].max()
    low_contrast(xlabel, "", ax)
    combatpower.plot.barh(legend=False, ax=ax, width=0.8, color=color)
    for i, value in enumerate(combatpower['data']):
        if rate_graph:
            ax.text(value + vmax * 0.02, i,
                    f'{value:,}%', fontsize='x-large', color=color)
        else:
            ax.text(value + vmax * 0.02, i,
                    f'{value:,}', fontsize='x-large', color=color)

    plt.grid(False)


def line_graph(data, index, columns, xlabel, ylabel,
               xtick=None, ytick=None, focus_id=None,
               focus_color='limegreen'):
    """
    Beautiful line graph

    usage:
    data = [[970, 1010, 1015, 1008],
            [975, 1020, 1002, 1035],
            [975, 985, 995, 999]]
    index = ['Toyota', 'VW', 'GM']
    columns = [2013, 2014, 2015, 2016]
    ylabel = "Number"
    xlabel = "Year"
    line_graph(data, index, columns, xlabel,
               ylabel, xtick=1, ytick=25, focus_id=None)
    plt.show()

    """
    carsales = pd.DataFrame(data,
                            index=index,
                            columns=columns)

    fig, ax = plt.subplots()
    if focus_id is None:
        carsales.T.plot(ax=ax, linewidth=4, legend=False)
    else:
        carsales.T.plot(ax=ax, linewidth=4, legend=False, color="lightgray")
        ax.lines[focus_id].set_color(focus_color)
    year = carsales.columns.values
    ax.set(xlabel=xlabel, ylabel=ylabel, xlim=(year.min(), year.max()))
    # adjust tick
    if xtick is not None:
        ax.xaxis.set_major_locator(MultipleLocator(xtick))
    if ytick is not None:
        ax.yaxis.set_major_locator(MultipleLocator(ytick))

    ax.grid(axis='x')

    ax.tick_params(bottom=False, left=False)

    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)

    low_contrast(xlabel, ylabel, ax)

    for i, name in enumerate(carsales.index.values):
        if focus_id is None:
            c, f = f'C{i}', 'large'
        else:
            if i == focus_id:
                c, f = focus_color, 'x-large'
            else:
                c, f = 'gray', 'large'

        ax.text(year.max() + 0.03, ax.lines[i].get_data()[1][-1], name,
                color=c, fontsize=f, va='center')


def time_vertical_bar(data, time_index,
                      xtick=None, ytick=None, xlabel="", ylabel=""):
    """
    Beautiful time vertical bar

    usage:
    data = np.linspace(450, 990, 12) + np.random.randint(-50, 50, 12)
    time_index = pd.date_range('2017/5', periods=12, freq='MS')
    time_vertical_bar(data, time_index, xlabel="time", ylabel="MAU")
    plt.show()

    """

    df = pd.Series(data, index=time_index, name=ylabel)

    fig, ax = plt.subplots()
    plt.grid(False)

    ax.bar(df.index, df, width=20,
           color='coral', zorder=2, align='center')
    if xtick is not None:
        ax.xaxis.set_major_locator(MultipleLocator(xtick))
    if ytick is not None:
        ax.yaxis.set_major_locator(MultipleLocator(ytick))

    ax.tick_params(bottom=False, left=False)

    ax.grid(axis='y')
    low_contrast(xlabel, ylabel, ax)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%-m'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    fig.canvas.draw()
    for key, gr in df.groupby(df.index.year):
        i = np.where(df.index == gr.index[0])[0][0]
        pos = ax.get_xmajorticklabels()[i].get_position()
        ax.annotate(f'         {key}', xy=(pos[0] - 15, 0), xycoords='data',
                    xytext=(0, -30), textcoords='offset points', color='dimgray',
                    ha='center', va='bottom',
                    arrowprops={'arrowstyle': '-', 'color': 'dimgray'})


def low_contrast(xlabel, ylabel, ax):
    ax.set_ylabel(ylabel, color='gray')
    ax.set_xlabel(xlabel, color='gray')
    ax.tick_params(axis='x', colors='gray')
    ax.tick_params(axis='y', colors='gray')
    ax.spines['left'].set_color('dimgray')
    ax.spines['right'].set_color('dimgray')
    ax.spines['top'].set_color('dimgray')
    ax.spines['bottom'].set_color('dimgray')


def main():
    print(__file__ + " start!!")
    print("matplolib version:", matplotlib._version.get_versions()['version'])

    data = [1000, 2000, 10000]
    index = ["A", "B", "C"]
    horizontal_bar(index, data, rate_graph=False)

    data2 = [[970, 1010, 1015, 1008],
             [975, 1020, 1002, 1035],
             [975, 985, 995, 999]]
    index2 = ['Toyota', 'VW', 'GM']
    columns = [2013, 2014, 2015, 2016]
    ylabel = "Number"
    xlabel = "Year"
    line_graph(data2, index2, columns, xlabel,
               ylabel, xtick=1, ytick=25, focus_id=None)

    data = np.linspace(450, 990, 12) + np.random.randint(-50, 50, 12)
    time_index = pd.date_range('2017/5', periods=12, freq='MS')
    time_vertical_bar(data, time_index, xlabel="time", ylabel="MAU")

    plt.show()


if __name__ == '__main__':
    main()
