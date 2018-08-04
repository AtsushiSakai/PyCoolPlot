"""

Sample code for PyCoolPlot

author: Atsushi Sakai (@Atsushi_twi)

"""
from pycoolplot import pycoolplot


# Horizontal bar plot
data = [1000, 2000, 10000]
index = ["A", "B", "C"]
pycoolplot.horizontal_bar(index, data)

# Horizontal rate bar plot
data = [1000, 2000, 10000]
index = ["A", "B", "C"]
pycoolplot.horizontal_bar(index, data, rate_graph=True)


# Line graph
data2 = [[970, 1010, 1015, 1008],
         [975, 1020, 1002, 1035],
         [975, 985, 995, 999]]
index2 = ['Toyota', 'VW', 'GM']
columns = [2013, 2014, 2015, 2016]
ylabel = "Number"
xlabel = "Year"
pycoolplot.line_graph(data2, index2, columns, xlabel,
                      ylabel, xtick=1, ytick=25)

# Line graph with focusing a line
data2 = [[970, 1010, 1015, 1008],
         [975, 1020, 1002, 1035],
         [975, 985, 995, 999]]
index2 = ['Toyota', 'VW', 'GM']
columns = [2013, 2014, 2015, 2016]
ylabel = "Number"
xlabel = "Year"
focus_id = 1  # the index of focusing line, in this case Toyota=0, VW=1, GM=2
pycoolplot.line_graph(data2, index2, columns, xlabel,
                      ylabel, xtick=1, ytick=25, focus_id=focus_id)

# Time series vertical bar plot
data = pycoolplot.np.linspace(450, 990, 12) + \
    pycoolplot.np.random.randint(-50, 50, 12)
time_index = pycoolplot.pd.date_range('2017/5', periods=12, freq='MS')
pycoolplot.time_vertical_bar(data, time_index, xlabel="time", ylabel="MAU")


pycoolplot.plt.show()
