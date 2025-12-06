from ..plots.dimensionality_reduction import DimensionaltyReductionPlots
from ..plots.base import BasePlots

import matplotlib.axes as Axes



class AxisWrapper(BasePlots, DimensionaltyReductionPlots):


    def __init__(self, ax : Axes ):

        self._ax = ax

