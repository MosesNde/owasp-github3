 import matplotlib.pyplot as plt
 import matplotlib as mpl
 import matplotlib.axes
 import numpy as np
 from typing import List, Union
 
 from ..storage import History
 def plot_acceptance_rates_trajectory(
         histories: Union[List, History],
         labels: Union[List, str] = None,
        rotation: int = 0,
         title: str = "Acceptance rates",
         yscale: str = 'lin',
         size: tuple = None,
 
     Parameters
     ----------

    histories: Union[List, History]
         The histories to plot from. History ids must be set correctly.
    labels: Union[List ,str], optional
         Labels corresponding to the histories. If None are provided,
         indices are used as labels.
    rotation: int, optional (default = 0)
        Rotation to apply to the plot's x tick labels. For longer labels,
        a tilting of 45 or even 90 can be preferable.
    title: str, optional (default = "Acceptance rates")
         Title for the plot.
    yscale: str, optional (default = 'lin')
         The scale on which to plot the counts. Can be one of 'lin', 'log'
         (basis e) or 'log10'
    size: tuple of float, optional
         The size of the plot in inches.
    ax: matplotlib.axes.Axes, optional
         The axis object to use.
     normalize_by_ess: bool, optional (default = False)
         Indicator to use effective sample size for the acceptance rate in
         place of the population size.
 
     Returns
     -------

     ax: Axis of the generated plot.
     """
     # preprocess input
     fig.tight_layout()
 
     return ax