#!/usr/bin/env python3
"""Software for managing and tracking environmental data from our field project."""

import argparse

from catchment import models, views


def main(args):
    """The MVC Controller of the environmental data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    InFiles = args.infiles
    if not isinstance(InFiles, list):
        InFiles = [args.infiles]
    
    
    for filename in InFiles:
        measurement_data = models.read_variable_from_csv(filename)
        
        view_data = {'daily sum': models.daily_total(measurement_data), 'daily average': models.daily_mean(measurement_data), 'daily max': models.daily_max(measurement_data), 'daily min': models.daily_min(measurement_data)}
        
        views.visualize(view_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic environmental data management system')
    
    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing measurement data')
    
    args = parser.parse_args()
    
    main(args)
