#!/usr/bin/env python3
"""Software for managing and tracking environmental data from our field
project."""

import argparse
import os
import re

from catchment import models, views, compute_data


def main(args):
    """The MVC Controller of the environmental data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    InFiles = args.infiles
    if not isinstance(InFiles, list):
        InFiles = [args.infiles]
    
    if args.full_data_analysis:
        
        file_format = re.sub(r".*\.(.*)$", "\\1", InFiles[0])
        
        if file_format == "csv":
            data_source = compute_data.CSVDataSource(os.path.dirname(InFiles[0]))
        elif file_format == "json":
            data_source = compute_data.JSONDataSource(os.path.dirname(InFiles[0]))  
        else:
            raise ValueError(f"Unsupported file format {file_format}")
        
        daily_standard_deviation = compute_data.analyse_data(data_source)

        graph_data = {
        'daily standard deviation': daily_standard_deviation
        }
        views.visualize(graph_data)

    for filename in InFiles:
        measurement_data = models.read_variable_from_csv(filename,
                                                         args.measurements)
        
        view_data = {
            'daily sum': models.daily_total(measurement_data),
            'daily average': models.daily_mean(measurement_data),
            'daily max': models.daily_max(measurement_data),
            'daily min': models.daily_min(measurement_data)
            }
        
        views.visualize(view_data)


def create_argparse():
    parser = argparse.ArgumentParser(
        description='A basic environmental data management system'
        )
    
    req_group = parser.add_argument_group("required_arguments")

    parser.add_argument(
        'infiles',
        nargs = '+',
        help = 'Input CSV(s) containing measurement data'
        )
    
    req_group.add_argument(
        "-m", "--measurements",
        help="Name of measurement data series to load")

    parser.add_argument('--full-data-analysis', action='store_true', dest='full_data_analysis')
    return parser


if __name__ == "__main__":
  
    parser = create_argparse()
    args = parser.parse_args()
    main(args)
