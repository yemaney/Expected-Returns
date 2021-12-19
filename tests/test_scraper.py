import pandas as pd
from expected_returns.scraper import cape_ratio


def test_by_country():
    by_country = cape_ratio(scope='Country')
    assert len(by_country) == 6
    assert type(by_country) == pd.DataFrame


def test_international():
    international = cape_ratio(scope='World')
    assert len(international) == 11
    assert type(international) == pd.DataFrame
