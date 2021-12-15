import pandas as pd
from expected_returns.scraper import cape_ratio


def test_by_country():
    by_country = cape_ratio(by_country=True)
    assert len(by_country) == 6
    assert type(by_country) == pd.DataFrame


def test_international():
    international = cape_ratio(by_country=False)
    assert len(international) == 11
    assert type(international) == pd.DataFrame
