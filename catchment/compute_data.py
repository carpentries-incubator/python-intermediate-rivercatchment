"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views


class CSVDataSource:
    """Class for handling CSV data sources"""
    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir

    def load_catchment_data(self):
        """Load data files into list"""
        data_file_paths = glob.glob(os.path.join(self.data_dir, "rain_data_2015*.csv"))
        if len(data_file_paths) == 0:
            raise ValueError(
                f'No files found in the data directory: {self.data_dir}')
        return list(map(models.read_variable_from_csv, data_file_paths))


class JSONDataSource:
    """Class for handling JSON data sources"""
    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir

    def load_catchment_data(self):
        """Load data files into list"""
        data_file_paths = glob.glob(os.path.join(self.data_dir, "rain_data_2015*.json"))
        if len(data_file_paths) == 0:
            raise ValueError(
                f'No files found in the data directory: {self.data_dir}')
        return list(map(models.read_variable_from_json, data_file_paths))


class XMLDataSource:
    """Class for handling XML data sources"""
    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir

    def load_catchment_data(self):
        """Load data files into list"""
        data_file_paths = glob.glob(os.path.join(self.data_dir, "rain_data_2015*.xml"))
        if len(data_file_paths) == 0:
            raise ValueError(
                f'No files found in the data directory: {self.data_dir}')
        return list(map(models.read_variable_from_xml, data_file_paths))


def analyse_data(data_source: CSVDataSource):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    works out the mean for each day, and then graphs the standard deviation
    of these means.
    """
    data = data_source.load_catchment_data()
    return compute_standard_deviaiton_by_day(data)


def compute_standard_deviaiton_by_day(data) -> pd.DataFrame:
    """Compute the standard deviation of a list of dataframes
    indexed with daily date values."""
    daily_std_list = map(models.daily_std, data)
    daily_standard_deviation = pd.concat(daily_std_list)
    return daily_standard_deviation
