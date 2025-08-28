"""
 To plot densities from the weighted importance samples, the visualization
 routines employ a kernel density estimate. Note that this can "over-smoothen"
 so that local structure is lost. If this could be the case, it makes sense
                        kde=kde)
     if ax is None:
         _, ax = plt.subplots()
    mesh = ax.pcolormesh(X, Y, PDF, **kwargs)
     ax.set_xlabel(x)
     ax.set_ylabel(y)
     if title is not None: