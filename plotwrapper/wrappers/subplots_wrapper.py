import numpy as np
import matplotlib.pyplot as plt

from .axis_wrapper import AxisWrapper

def subplots(nrows: int = 1, ncols: int = 1):

    fig, axs = plt.subplots(nrows, ncols)
    fig.set_figwidth(ncols * 5)
    fig.set_figheight(nrows* 5)
    fig.subplots_adjust(wspace=0.7)
    
    # assert 2d array of self.axs
    if nrows == 1 and ncols == 1:
        axs = np.array([[axs]])
    elif nrows == 1 or ncols == 1:
        axs = np.reshape(axs, (nrows, ncols))
    else:
        axs = axs

    # conver to wrapper
    for i in range(nrows):
        for j in range(ncols):
            axs[i][j] = AxisWrapper(axs[i][j])

    return fig, axs

