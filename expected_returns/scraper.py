import pandas as pd


def cape_ratio(scope: str = "World"):
    if scope == "Country":
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
        column_numbers = [x for x in range(capet.shape[1])]
        column_numbers.remove(8)

        capet.rename(columns={"index": "Date"}, inplace=True)
        return capet.iloc[:, column_numbers]
    elif scope == "World":
        cape_df = pd.read_html("https://siblisresearch.com/data/world-cape-ratio/")[0]
        cape_df["Global Stock Markets CAPE Ratio"] = cape_df[
            "Global Stock Markets CAPE Ratio"
        ].map(lambda x: 100 / x)

        return cape_df[["Global Stock Markets CAPE Ratio", "Date"]]
