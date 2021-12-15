import pandas as pd


def cape_ratio(by_country: bool = False):
    if by_country:
        cape_df = pd.read_html(
            "https://siblisresearch.com/data/cape-ratios-by-country/"
        )[0]
        dates = cape_df.columns[2:]
        countries = cape_df["Nation"]

        for date in dates:
            cape_df[date] = cape_df[date].map(lambda x: 100 / x)

        capet = cape_df[dates].T
        capet.columns = countries
        capet.reset_index(inplace=True)
        capet.rename(columns={"index": "Date"})
        return capet
    else:
        cape_df = pd.read_html("https://siblisresearch.com/data/world-cape-ratio/")[0]
        cape_df["Global Stock Markets CAPE Ratio"] = cape_df[
            "Global Stock Markets CAPE Ratio"
        ].map(lambda x: 100 / x)

        return cape_df[["Global Stock Markets CAPE Ratio", "Date"]]
