import pandas as pd
from expected_returns.backend.scraper import cape_ratio


def test_by_country():
    by_country = cape_ratio(scope="Country")
    assert len(by_country) == 66
    assert type(by_country) == pd.DataFrame


def test_international():
    international = cape_ratio(scope="World")
    assert len(international) == 11
    assert type(international) == pd.DataFrame
