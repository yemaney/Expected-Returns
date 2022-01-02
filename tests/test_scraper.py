from expected_returns.backend.scraper import cape_ratio


def test_by_country():
    by_country = cape_ratio(scope="Country")
    assert len(by_country) == 3
    assert type(by_country) == dict


def test_international():
    international = cape_ratio(scope="World")
    assert len(international) == 2
    assert type(international) == dict
