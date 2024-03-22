import numpy as np
import numpy.testing as npt
from pathlib import Path


def test_analyse_data_csv():
    from catchment.compute_data import analyse_data, CSVDataSource
    path = Path.cwd() / "data"
    data_source = CSVDataSource(path)
    result = analyse_data(data_source)
    expected_output = [ [0.        , 0.18801829],
                       [0.10978448, 0.43107373],
                       [0.06066156, 0.0699624 ],
                       [0.        , 0.02041241],
                       [0.        , 0.        ],
                       [0.        , 0.02871518],
                       [0.        , 0.17227833],
                       [0.        , 0.04866643],
                       [0.        , 0.02041241],
                       [0.88952727, 0.        ],
                       [0.        , 0.02041241],
                       [0.        , 0.        ],
                       [0.02041241, 0.        ],
                       [0.        , 0.        ],
                       [0.        , 0.        ],
                       [0.        , 0.        ],
                       [0.        , 0.        ],
                       [0.0349812 , 0.02041241],
                       [0.02871518, 0.02041241],
                       [0.02041241, 0.        ],
                       [0.02041241, 0.        ],
                       [0.        , 0.02041241],
                       [0.        , 0.        ],
                       [0.        ,     np.nan],
                       [0.02041241, 0.        ],
                       [0.        , 0.02041241],
                       [0.        , 0.02041241],
                       [0.02041241, 0.        ],
                       [0.13449059, 0.        ],
                       [0.18285024, 0.19707288],
                       [0.19176008, 0.13915472]]
    npt.assert_array_almost_equal(result, expected_output)


def test_analyse_data_json():
    from catchment.compute_data import analyse_data, JSONDataSource
    path = Path.cwd() / "data"
    data_source = JSONDataSource(path)
    result = analyse_data(data_source)
    expected_output = [ [0.        , 0.18801829],
                       [0.10978448, 0.43107373],
                       [0.06066156, 0.0699624 ],
                       [0.        , 0.02041241],
                       [0.        , 0.        ],
                       [0.        , 0.02871518],
                       [0.        , 0.17227833],
                       [0.        , 0.04866643],
                       [0.        , 0.02041241],
                       [0.88952727, 0.        ],
                       [0.        , 0.02041241],
                       [0.        , 0.        ],
                       [0.02041241, 0.        ],
                       [0.        , 0.        ],
                       [0.        , 0.        ],
                       [0.        , 0.        ],
                       [0.        , 0.        ],
                       [0.0349812 , 0.02041241],
                       [0.02871518, 0.02041241],
                       [0.02041241, 0.        ],
                       [0.02041241, 0.        ],
                       [0.        , 0.02041241],
                       [0.        , 0.        ],
                       [0.        ,     np.nan],
                       [0.02041241, 0.        ],
                       [0.        , 0.02041241],
                       [0.        , 0.02041241],
                       [0.02041241, 0.        ],
                       [0.13449059, 0.        ],
                       [0.18285024, 0.19707288],
                       [0.19176008, 0.13915472]]
    npt.assert_array_almost_equal(result, expected_output)


def test_analyse_data_xml():
    from catchment.compute_data import analyse_data, XMLDataSource
    path = Path.cwd() / "data"
    data_source = XMLDataSource(path)
    result = analyse_data(data_source)
    expected_output = [ [0.        , 0.18801829],
                       [0.10978448, 0.43107373],
                       [0.06066156, 0.0699624 ],
                       [0.        , 0.02041241],
                       [0.        , 0.        ],
                       [0.        , 0.02871518],
                       [0.        , 0.17227833],
                       [0.        , 0.04866643],
                       [0.        , 0.02041241],
                       [0.88952727, 0.        ],
                       [0.        , 0.02041241],
                       [0.        , 0.        ],
                       [0.02041241, 0.        ],
                       [0.        , 0.        ],
                       [0.        , 0.        ],
                       [0.        , 0.        ],
                       [0.        , 0.        ],
                       [0.0349812 , 0.02041241],
                       [0.02871518, 0.02041241],
                       [0.02041241, 0.        ],
                       [0.02041241, 0.        ],
                       [0.        , 0.02041241],
                       [0.        , 0.        ],
                       [0.        ,     np.nan],
                       [0.02041241, 0.        ],
                       [0.        , 0.02041241],
                       [0.        , 0.02041241],
                       [0.02041241, 0.        ],
                       [0.13449059, 0.        ],
                       [0.18285024, 0.19707288],
                       [0.19176008, 0.13915472]]
    npt.assert_array_almost_equal(result, expected_output)