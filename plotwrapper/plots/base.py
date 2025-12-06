from matplotlib.axes import Axes
from ..boilerplate.remover import BoilerplateRemover


class BasePlots:

    def __init__(self, ax: Axes):
        self._ax = ax

    def bar(self, xlabel = None, ylabel = None, title = None, 
            xlim = None, ylim = None, **kwargs):
        
        self._ax.bar(
            edgecolor = "black",
            **kwargs
        )
        BoilerplateRemover.reduce_boilerplate(
            self._ax, 
            title, 
            xlabel, 
            ylabel, 
            xlim, 
            ylim, 
            **kwargs
        )
        
    def hist(self, xlabel = None, ylabel = None, title = None, 
             xlim = None, ylim = None, **kwargs):

        self._ax.hist(
            ec = "black", 
            density = True, 
            **kwargs
        )
        BoilerplateRemover.reduce_boilerplate(
            self._ax, 
            title, 
            xlabel, 
            ylabel, 
            xlim, 
            ylim, 
            **kwargs
        )
        
    def plot(self, x = None, y = None, xlabel = None, ylabel = None, 
             title = None, xlim = None, ylim = None, **kwargs):

        if x != None and y != None:
            self._ax.plot(x, y, **kwargs)

        elif y != None:
            self._ax.plot(y, **kwargs)

        BoilerplateRemover.reduce_boilerplate(
            self._ax, 
            title, 
            xlabel, 
            ylabel, 
            xlim, 
            ylim, 
            **kwargs
        )

    def scatter(self, xlabel = None, ylabel = None, title = None, 
                xlim = None, ylim = None, **kwargs):
        
        self._ax.scatter(
            **kwargs
        )
        BoilerplateRemover.reduce_boilerplate(
            self._ax, 
            title, 
            xlabel, 
            ylabel, 
            xlim, 
            ylim, 
            **kwargs
        )

