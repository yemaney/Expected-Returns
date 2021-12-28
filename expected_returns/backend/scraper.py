import pandas as pd


def cape_ratio(scope: str = "World"):
    """
    Web scraper to collect cape ratios, using pandas.

    Parameters
    ----------
    scope : str, optional
        Option to control if the global cape ratio will be collected or wether
        cape ratios will be collected by Country, by default "World"

    Returns
    -------
    pd.DataFrame
        pandas dataframe of cape ratios collected in long format
    """

    if scope == "Country":
        cape_df = pd.read_html(
            "https://siblisresearch.com/data/cape-ratios-by-country/"
        )[0]

        dates = cape_df.columns[2:]
        cape_df.rename(columns={"Nation": "country"}, inplace=True)
        countries = cape_df["country"]

        for date in dates:
            cape_df[date] = cape_df[date].map(lambda x: 100 / x)

        cape_df = cape_df[dates].T
        cape_df.columns = countries
        cape_df.reset_index(inplace=True)
        column_numbers = [x for x in range(cape_df.shape[1])]
        column_numbers.remove(8)
        cape_df.rename(columns={"index": "date"}, inplace=True)
        cape_df = cape_df.iloc[:, column_numbers]
        cape_df = cape_df.reset_index()
        cape_df = pd.melt(cape_df, id_vars="date", value_vars=countries.to_list())
        cape_df.rename(columns={"value": "cape"}, inplace=True)
        return cape_df.to_dict()
    elif scope == "World":
        cape_df = pd.read_html("https://siblisresearch.com/data/world-cape-ratio/")[0]
        cape_df["cape"] = cape_df["Global Stock Markets CAPE Ratio"].map(
            lambda x: 100 / x
        )
        cape_df["date"] = cape_df["Date"]
        return cape_df[["cape", "date"]].to_dict()
