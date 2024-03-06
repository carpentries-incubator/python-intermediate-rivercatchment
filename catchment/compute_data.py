"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views


def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    works out the mean for each day, and then graphs the standard deviation
    of these means.
    """
    data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError('No CSV files found in the data directory')
    data = map(models.read_variable_from_csv, data_file_paths)


    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = pd.concat(means_by_day, axis=1)

    daily_standard_deviation = pd.DataFrame(means_by_day_matrix.std(axis=1), columns=['std'])

    graph_data = {
        'daily standard deviation': daily_standard_deviation
    }

    views.visualize(graph_data)
