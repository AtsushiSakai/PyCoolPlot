# PyCoolPlot

A cool plot module for Python

# What is this?

This is a plotting module for Python.

It only uses matplotlib.

Ref:

- [データ視覚化のデザイン \#1｜Go Ando / THE GUILD｜note](https://note.mu/goando/n/neb6ea35f1da3)

- [「データ視覚化のデザイン \#1」をmatplotlibで実装する \- Qiita](https://qiita.com/skotaro/items/cdb0732ad1ad2a4b6236)

# Requirements

- Python 3.6.x

- matplotlib 2.x.x

# Download

1. Install Python 3.6.x.

2. Clone or download as zip this repository. 

3. import pycoolplot.py

# How to use

## Horizontal bar plot

You can plot a beautiful horizontal bar plot like:

    data = [1000, 2000, 10000]
    index = ["A", "B", "C"]
    pycoolplot.horizontal_bar(index, data)
    pycoolplot.plt.show()

You will see:

![1](https://github.com/AtsushiSakai/PyCoolPlot/raw/master/imgs/1.png)

If you want a rate bar plot, you can set rate\_graph is True like:

    data = [1000, 2000, 10000]
    index = ["A", "B", "C"]
    pycoolplot.horizontal_bar(index, data, rate_graph=True)
    pycoolplot.plt.show()


You will see:

![2](https://github.com/AtsushiSakai/PyCoolPlot/raw/master/imgs/2.png)

## Line graph

You can plot a beautiful line graph like:

    data2 = [[970, 1010, 1015, 1008],
             [975, 1020, 1002, 1035],
             [975, 985, 995, 999]]
    index2 = ['Toyota', 'VW', 'GM']
    columns = [2013, 2014, 2015, 2016]
    ylabel = "Number"
    xlabel = "Year"
    pycoolplot.line_graph(data2, index2, columns, xlabel,
                          ylabel, xtick=1, ytick=25)
    pycoolplot.plt.show()

You can get:

![3](https://github.com/AtsushiSakai/PyCoolPlot/raw/master/imgs/3.png)

If you want to focus a line, you can set focus\_id_

![4](https://github.com/AtsushiSakai/PyCoolPlot/raw/master/imgs/4.png)

## Time bar chart
![5](https://github.com/AtsushiSakai/PyCoolPlot/raw/master/imgs/5.png)

# License 

MIT

# Author

- [Atsushi Sakai](https://github.com/AtsushiSakai/) ([@Atsushi_twi](https://twitter.com/Atsushi_twi))




