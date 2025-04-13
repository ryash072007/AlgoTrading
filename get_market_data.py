import yfinance
import pandas

training_start_date: str = "2012-01-01"
training_stop_date: str = "2017-01-01"

test_start_date: str = "2017-01-01"
test_stop_date: str = "2020-01-01"

def get_stock_data(ticker: str, start_date: str, end_date: str) -> pandas.DataFrame:
    data: pandas.DataFrame = yfinance.download(ticker, start=start_date, end=end_date, multi_level_index=False)
    return data


if __name__ == "__main__":
    training_data: pandas.DataFrame = get_stock_data("AMZN", training_start_date, training_stop_date)
    training_data.to_csv("training_data/AMZN.csv")

    testing_data: pandas.DataFrame = get_stock_data("AMZN", test_start_date, test_stop_date)
    testing_data.to_csv("test_data/AMZN.csv")