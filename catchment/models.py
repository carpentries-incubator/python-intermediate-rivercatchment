"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
import pandas as pd


class Instrument:
    """An Instrument taking Measurements"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.observations = pd.DataFrame(columns=['Value'], index=pd.to_datetime([]))
        
    def add_observation(self, value, date):
        self.observations[pd.to_datetime(date)] = value
    
    def __str__(self):
        return self.name
        
    @property
    def last_observation(self):
        return self.observations.iloc[-1]


class Location:
    """A Location, with Geographic Information"""
    def __init__(self, name, address):
        self.name = name
        self.address = address
       
    def __str__(self):
        return self.name


class Site(Location):
    """A Measurement Site"""
    def __init__(self, name, address):
        super().__init__(name, address)
        self.instruments = []
       
    def add_instrument(self, new_instrument):
        for instrument in self.instruments:
            if instrument.name == new_instrument.name:
                return
        self.instruments.append(new_instrument)
    
    def describe_instruments(self):
        for instrument in self.instruments:
            print(f'Instrument: {instrument.name}; description: {instrument.description}')


class WaterShed(Location):
    """A single water shed, containing multiple measurement sites"""
    def __init__(self, name, address):
        super().__init__(name, address)
        self.sites = []
        
    def add_site(self, new_site):
        for site in self.sites:
            if site.name == new_site.name:
                return
        self.sites.append(new_site)


def read_variable_from_csv(filename, variable, index="Date", sites="Site"):
    """Reads a named variable from a CSV file, and returns a
    pandas dataframe containing that variable. The CSV file must contain
    a column of dates, a column of site ID's, and (one or more) columns
    of data - only one of which will be read.

    :param filename: Filename of CSV to load
    :param variable: Name of Column to extract
    :param index: Column to use for date index (default: Date)
    :param sites: Column to use for site identifiers (default: Site)
    :return: 2D array of given variable. Index will be dates,
             Columns will be the individual sites
    """
    with open(filename) as f:
        dataset = pd.read_csv(f, usecols=[index, sites, variable])

    dataset = dataset.rename({index: 'OldDate'}, axis='columns')
    dataset[index] = [pd.to_datetime(x,dayfirst=True) for x in dataset['OldDate']]
    dataset = dataset.drop('OldDate', axis='columns')

    newdataset = pd.DataFrame(index=dataset[index].unique())

    for site in dataset[sites].unique():
        newdataset[site] = dataset[dataset[sites] == site].set_index(index)[variable]

    newdataset = newdataset.sort_index()

    return newdataset


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_total(data):
    """Calculate the daily total of a 2d data array.
    Index must be np.datetime64 compatible format."""
    return data.groupby(data.index.date).sum()

def daily_mean(data):
    """Calculate the daily mean of a 2d data array.
    Index must be np.datetime64 compatible format."""
    return data.groupby(data.index.date).mean()


def daily_max(data):
    """Calculate the daily max of a 2d data array.
    Index must be np.datetime64 compatible format."""
    return data.groupby(data.index.date).max()


def daily_min(data):
    """Calculate the daily min of a 2d data array.
    Index must be np.datetime64 compatible format."""
    return data.groupby(data.index.date).min()


def data_normalise(data):
    """correct data normalise function"""
    max = np.array(np.max(data, axis=0))
    return data / max[np.newaxis, :]


