"""
Cool plot library for Python

author: Atsushi Sakai (@Atsushi_twi)

"""

import matplotlib
import matplotlib.pyplot as plt
#  import numpy as np
import pandas as pd


def vertical_bar(index, data):
    combatpower = pd.DataFrame(data,
                               index=index,
                               columns=['data'])

    fig, ax = plt.subplots(figsize=(6, 3))
    combatpower.plot.barh(legend=False, ax=ax, width=0.8)
    ax.invert_yaxis()
    plt.gca().invert_yaxis()
    [spine.set_visible(False) for spine in ax.spines.values()]
    plt.grid(False)
    ax.tick_params(bottom=False, left=False, labelbottom=False)
    ax.tick_params(axis='y', labelsize='x-large')
    vmax = combatpower['data'].max()
    for i, value in enumerate(combatpower['data']):
        ax.text(value + vmax * 0.02, i,
                f'{value:,}', fontsize='x-large', color='C0')


def main():
    print(__file__ + " start!!")
    print(matplotlib._version.get_versions()['version'])

    data = [1000, 2000, 10000]
    index = ["A", "B", "C"]
    vertical_bar(index, data)
    plt.show()


if __name__ == '__main__':
    main()
