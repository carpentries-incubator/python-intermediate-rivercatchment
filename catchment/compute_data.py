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

    daily_std_list = []
    for dataset in data:
        daily_std = dataset.groupby(dataset.index.date).std()
        daily_std_list.append(daily_std)
    
    daily_standard_deviation = pd.concat(daily_std_list)

    graph_data = {
        'daily standard deviation': daily_standard_deviation
    }

    views.visualize(graph_data)
