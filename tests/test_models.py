"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pandas.testing as pdt
import datetime
import pytest

########## daily mean ##########
@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (
            pd.DataFrame(
                data=[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                        pd.to_datetime('2000-01-01 02:00'),
                        pd.to_datetime('2000-01-01 03:00')],
                columns=['A', 'B']
            ),
            pd.DataFrame(
               data=[[0.0, 0.0]],
               index=[datetime.date(2000, 1, 1)],
               columns=['A', 'B']
            )
        ),
        (
            pd.DataFrame(
                data=[[1, 2], [3, 4], [5, 6]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                        pd.to_datetime('2000-01-01 02:00'),
                        pd.to_datetime('2000-01-01 03:00')],
                columns=['A', 'B'],
            ),
            pd.DataFrame(
                data=[[3.0, 4.0]],
                index=[datetime.date(2000, 1, 1)],
                columns=['A', 'B']
            )
        ),
    ])
def test_daily_mean(test_input, expected_output):
    """Test mean function works for array of zeroes and positive integers."""
    from catchment.models import daily_mean
    pdt.assert_frame_equal(daily_mean(test_input), expected_output)


########## daily min ##########
@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (
            pd.DataFrame(
                data=[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                        pd.to_datetime('2000-01-01 02:00'),
                        pd.to_datetime('2000-01-01 03:00')],
                columns=['A', 'B']
            ),
            pd.DataFrame(
               data=[[0.0, 0.0]],
               index=[datetime.date(2000, 1, 1)],
               columns=['A', 'B']
            )
        ),
        (
            pd.DataFrame(
                data=[[1, 2], [3, 4], [5, 6]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                        pd.to_datetime('2000-01-01 02:00'),
                        pd.to_datetime('2000-01-01 03:00')],
                columns=['A', 'B'],
            ),
            pd.DataFrame(
                data=[[1, 2]],
                index=[datetime.date(2000, 1, 1)],
                columns=['A', 'B']
            )
        ),
    ])
def test_daily_min(test_input, expected_output):
    """Test mean function works for array of zeroes and positive integers."""
    from catchment.models import daily_min
    pdt.assert_frame_equal(daily_min(test_input), expected_output)


########## daily_max ##########
@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (
            pd.DataFrame(
                data=[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                        pd.to_datetime('2000-01-01 02:00'),
                        pd.to_datetime('2000-01-01 03:00')],
                columns=['A', 'B']
            ),
            pd.DataFrame(
               data=[[0.0, 0.0]],
               index=[datetime.date(2000, 1, 1)],
               columns=['A', 'B']
            )
        ),
        (
            pd.DataFrame(
                data=[[1, 2], [3, 4], [5, 6]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                        pd.to_datetime('2000-01-01 02:00'),
                        pd.to_datetime('2000-01-01 03:00')],
                columns=['A', 'B'],
            ),
            pd.DataFrame(
                data=[[5, 6]],
                index=[datetime.date(2000, 1, 1)],
                columns=['A', 'B']
            )
        ),
    ])
def test_daily_max(test_input, expected_output):
    """Test mean function works for array of zeroes and positive integers."""
    from catchment.models import daily_max
    pdt.assert_frame_equal(daily_max(test_input), expected_output)


########## data_normalise ##########
# note that we buld the dataframes in the function here unlike above
# but we can also build it in the decorator
@pytest.mark.parametrize(
    "test_data, test_index, test_columns, expected_data, expected_index, expected_columns",
    [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [pd.to_datetime('2000-01-01 01:00'),
                pd.to_datetime('2000-01-01 02:00'),
                pd.to_datetime('2000-01-01 03:00')],
            ['A', 'B', 'C'],
            [[0.14, 0.25, 0.33], [0.57, 0.63, 0.66], [1.0, 1.0, 1.0]],
            [pd.to_datetime('2000-01-01 01:00'),
                pd.to_datetime('2000-01-01 02:00'),
                pd.to_datetime('2000-01-01 03:00')],
            ['A', 'B', 'C']
        ),
    ])
def test_normalise(test_data, test_index, test_columns, expected_data, expected_index, expected_columns):
    """Test normalisation works for arrays of one and positive integers.
       Assumption that test accuracy of two decimal places is sufficient."""
    from catchment.models import data_normalise
    pdt.assert_frame_equal(data_normalise(pd.DataFrame(data=test_data, index=test_index, columns=test_columns)),
                           pd.DataFrame(data=expected_data, index=expected_index, columns=expected_columns),
                           atol=1e-2)

