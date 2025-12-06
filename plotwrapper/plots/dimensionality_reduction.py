import sys, functools

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import umap
from sklearn.decomposition import PCA
from sklearn.manifold import MDS, TSNE
from sklearn.preprocessing import LabelEncoder



class DimensionaltyReductionPlots:


    def __init__(self, ax: Axes):
        self._ax = ax


    def _dim_red_plot(self, df: pd.DataFrame, labels: list|pd.DataFrame, method: str, xlabel: str, ylabel: str, title: str = None):

        """
        Reduce dimension from higher space into 2d representation,
        with different techniques. 

        """

        dim_red = None

        if method == "pca":
            dim_red = PCA(n_components=2, random_state=42)
        elif method == "mds":
            dim_red = MDS(n_components=2, random_state=42)
        elif method == "tsne":
            dim_red = TSNE(n_components=2, random_state=42)
        elif method == "umap":
            dim_red = umap.UMAP(n_components=2, random_state=42)
        else:
            print("Wrong method")
            sys.exit(1)
        
        X = dim_red.fit_transform(df)

        #
        # process labels
        #
        colors = [0 for i in range(len(df))]
        if type(labels) != None:
            labels_unique = np.unique(labels.tolist()).tolist()
            le = LabelEncoder()
            colors = le.fit_transform(labels)

        scatter = self._ax.scatter(X[:, 0], X[:, 1], c = colors, s=5.0, alpha=1.0, cmap="tab20") #  "nipy_spectral"
        
        handles, _ = scatter.legend_elements()
       
        self._ax.legend(handles = handles, labels = labels_unique, loc = "upper left", 
                            bbox_to_anchor = (1.0, 1.018), fontsize=8) 

        self._ax.set_xlabel(xlabel)
        self._ax.set_ylabel(ylabel)
        self._ax.set_title(title)
        self._ax.grid(True)

    pca_plot = functools.partialmethod(_dim_red_plot, method="pca", xlabel = "PCA 1", ylabel="PCA 2")
    mds_plot = functools.partialmethod(_dim_red_plot, method="mds", xlabel = "Coords. 1", ylabel="Coords. 2")
    tsne_plot = functools.partialmethod(_dim_red_plot, method="tsne", xlabel = "t-SNE 1", ylabel="t-SNE 2")
    umap_plot = functools.partialmethod(_dim_red_plot, method="umap", xlabel = "UMAP 1", ylabel="UMAP 2")


