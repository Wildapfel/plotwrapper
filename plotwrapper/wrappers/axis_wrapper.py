from ..data_viz.dim_red import DimensionaltyReductionPlots

# from matplotlib.axes import Axes
# from matplotlib.figure import Figure

import matplotlib.pyplot as plt


class AxisWrapper(DimensionaltyReductionPlots):


    def __init__(self, ax : plt.Axes ):

        self._ax = ax


    def plot(self):
        plot = self._ax.plot([1,2,3])
        

    def foo():
        print("hello")