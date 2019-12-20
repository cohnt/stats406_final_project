Stats 406 (Introduction to Statistical Computing) final research project

In order to run a python script `scripts/script.py`, run the command `python2 -m scripts/script` from within the python directory.

Some relevant scripts:

* `num_landfall.py` counts how many hurricanes made landfall in a given dataset
* `only_early_test.py` learns a model from a training dataset, and then computes a test dataset.
* `similar_hurricanes.py` plots out similar hurricanes according to the similarity metric.
* `simulation_proportion_landfall.py` compares how the different ways of adding noise affect the number of landfalls.
* `noise_test_script.py` plots out the effects of the different ways of adding noise.
* `what_dimension_best.py` learns a model for each dimension in a range, and graphs the accuracy of each one by dimension.

To separate out the datasets further, you can use the shell scripts in the `data` folder.

* `./get_year.sh [year]` will create a new data file containing just information for that year.
* `./get_years.sh [start] [end]` will create a new data file containing information from the start year *through* the end year.

Some essential python packages:

* `numpy`
* `sklearn`
* `matplotlib.pyplot`
* `mpl_toolkits.basemap`
* `statsmodels`