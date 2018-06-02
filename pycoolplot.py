"""
Cool plot library for Python

author: Atsushi Sakai (@Atsushi_twi)

Inspired: Qiita https://qiita.com/skotaro/items/cdb0732ad1ad2a4b6236

"""

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator
from cycler import cycler


def horizontal_bar(index, data, color="C0"):
    """
    Beautiful bar chart

    usage:
    data = [1000, 2000, 10000]
    index = ["A", "B", "C"]
    horizontal_bar(index, data)
    plt.show()

    """
    combatpower = pd.DataFrame(data,
                               index=index,
                               columns=['data'])

    fig, ax = plt.subplots()
    combatpower.plot.barh(legend=False, ax=ax, width=0.8, color=color)
    ax.invert_yaxis()
    plt.gca().invert_yaxis()
    [spine.set_visible(False) for spine in ax.spines.values()]
    plt.grid(False)
    ax.tick_params(bottom=False, left=False, labelbottom=False)
    ax.tick_params(axis='y', labelsize='x-large')
    vmax = combatpower['data'].max()
    for i, value in enumerate(combatpower['data']):
        ax.text(value + vmax * 0.02, i,
                f'{value:,}', fontsize='x-large', color=color)


def line_graph(data, index, columns, xlabel, ylabel,
               xtick=None, ytick=None, focus_id=None, focus_color='limegreen'):
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

    c = plt.get_cmap('Set1').colors
    plt.rcParams['axes.prop_cycle'] = cycler(color=c)
    fig, ax = plt.subplots()
    if focus_id is None:
        carsales.T.plot(ax=ax, linewidth=4, legend=False)
    else:
        carsales.T.plot(ax=ax, linewidth=4, legend=False, color="lightgray")
        ax.lines[focus_id].set_color(focus_color)
    year = carsales.columns.values
    ax.set(xlabel=xlabel, ylabel=ylabel, xlim=(year.min(), year.max()))
    ax.yaxis.label.set_color('gray')
    # adjust tick
    if xtick is not None:
        ax.xaxis.set_major_locator(MultipleLocator(xtick))
    if ytick is not None:
        ax.yaxis.set_major_locator(MultipleLocator(ytick))

    ax.grid(axis='x')

    ax.tick_params(bottom=False, left=False)
    ax.tick_params(axis='y', colors='gray')
    ax.tick_params(axis='x', colors='dimgray')
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_color('dimgray')
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


def main():
    print(__file__ + " start!!")
    print("matplolib version:", matplotlib._version.get_versions()['version'])

    #  data = [1000, 2000, 10000]
    #  index = ["A", "B", "C"]
    #  horizontal_bar(index, data)

    #  data = [[970, 1010, 1015, 1008],
    #  [975, 1020, 1002, 1035],
    #  [975, 985, 995, 999]]
    #  index = ['Toyota', 'VW', 'GM']
    #  columns = [2013, 2014, 2015, 2016]
    #  ylabel = "Number"
    #  xlabel = "Year"
    #  line_graph(data, index, columns, xlabel,
    #  ylabel, xtick=1, ytick=25, focus_id=None)

    plt.show()


if __name__ == '__main__':
    main()
