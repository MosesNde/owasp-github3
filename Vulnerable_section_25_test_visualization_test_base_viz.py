 import pyabc
 import tempfile
import pytest
 import os
 import numpy as np
 import pandas as pd
 import matplotlib.pyplot as plt
 
 
# create and run some model
 
 
 def model(p):
 
 
 p_true = {'p0': 3, 'p1': 4}
observation = {'ss0': p_true['p0'], 'ss1': p_true['p1']}
 limits = {'p0': (0, 5), 'p1': (1, 8)}
prior = pyabc.Distribution(**{
    key: pyabc.RV('uniform', limits[key][0], limits[key][1] - limits[key][0])
    for key in p_true.keys()})

db_path = "sqlite:///" \
    + os.path.join(tempfile.gettempdir(), "test_visualize.db")

 
distance = pyabc.PNormDistance(p=2)
n_history = 2
sampler = pyabc.sampler.MulticoreEvalParallelSampler(n_procs=2)
 
for _ in range(n_history):
    abc = pyabc.ABCSMC(model, prior, distance, 20, sampler=sampler)
    abc.new(db_path, observation)
    abc.run(minimum_epsilon=.1, max_nr_populations=3)


histories = []
labels = []
for j in range(n_history):
    history = pyabc.History(db_path)
    history.id = j + 1
    histories.append(history)
    labels.append("Some run " + str(j))
 
 
 def test_epsilons():
 def test_acceptance_rates_trajectory():
     """Test `pypesto.visualization.plot_acceptance_rates_trajectory`"""
     pyabc.visualization.plot_acceptance_rates_trajectory(
        histories, labels, yscale='log', rotation=76)
     _, ax = plt.subplots()
     pyabc.visualization.plot_acceptance_rates_trajectory(
        histories, labels, yscale='log10', rotation=76, size=(10, 5), ax=ax,
         normalize_by_ess=True)
     pyabc.visualization.plot_acceptance_rates_trajectory(
        histories, labels, yscale='log10', rotation=76, size=(10, 5), ax=ax,
         normalize_by_ess=False)
     plt.close()
 
     pyabc.visualization.plot_kde_matrix(df, w)
 
     # also use the highlevel interfaces
    pyabc.visualization.plot_kde_1d_highlevel(history, x='p0', size=(4, 5),
                                              refval=p_true)
    pyabc.visualization.plot_kde_2d_highlevel(history, x='p0', y='p1',
                                              size=(7, 5),
                                              refval=p_true)
    pyabc.visualization.plot_kde_matrix_highlevel(history, height=27.43,
                                                  refval=p_true)
     plt.close()
 
 