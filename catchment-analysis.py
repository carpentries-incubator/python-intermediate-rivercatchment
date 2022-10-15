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
    VariableName = args.varname

    print(InFiles)
    print(VariableName)

    for filename in InFiles:
        measurement_data = models.read_variable_from_csv(filename,VariableName)

        view_data = {'average': models.daily_mean(measurement_data),
                     'max': models.daily_max(measurement_data),
                     'min': models.daily_min(measurement_data)}

        views.visualize(view_data,VariableName)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic environmental data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing measurement data')

    parser.add_argument(
        '--varname',
        type=str,
        default='Water level continuous (mm)',
        help='Name of column to be loaded'
    )

    args = parser.parse_args()

    main(args)
