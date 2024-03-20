"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views


def analyse_data(data_dir: str, file_id: str = "rain_data_2015*.csv"):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    works out the mean for each day, and then graphs the standard deviation
    of these means.
    """
    data_file_paths = get_filenames_from_dir(data_dir, file_id)
    data = load_catchment_data(data_file_paths)
    return compute_standard_deviaiton_by_day(data)


def get_filenames_from_dir(data_dir: str, file_id: str) -> list:
    """Get filenames from directory that match a pattern"""
    data_file_paths = glob.glob(os.path.join(data_dir, file_id))
    if len(data_file_paths) == 0:
        raise ValueError(f'No files found in the data directory: {data_dir}, matching: {file_id}')
    return data_file_paths


def load_catchment_data(data_file_paths: list):
    """Load data files into list"""
    return map(models.read_variable_from_csv, data_file_paths)


def compute_standard_deviaiton_by_day(data: list[pd.DataFrame]) -> pd.DataFrame:
    """Compute the standard deviation of a list of dataframes
    indexed with daily date values."""
    daily_std_list = map(models.daily_std, data)
    daily_standard_deviation = pd.concat(daily_std_list)
    return daily_standard_deviation
