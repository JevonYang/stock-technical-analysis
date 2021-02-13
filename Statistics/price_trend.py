import datetime
import os

import akshare as ak
import matplotlib.pyplot as plt
import pandas as pd

from utils.config import project_dir


def price_cache_dir() -> str:
    return os.path.join(os.path.join(project_dir(), 'tmp', 'stock_price'))


def price_trend(
        stock_code,
        start="20160101",
        end=datetime.datetime.now().strftime("%Y%m%d")
) -> pd.DataFrame:
    data_file = os.path.join(price_cache_dir(), stock_code + '.csv')
    try:
        price_trend_df = pd.read_csv(data_file, index_col=0)
        price_trend_df.index = pd.to_datetime(price_trend_df.index)
        return price_trend_df
    except FileNotFoundError:
        stock_a_indicator_df = ak.stock_a_lg_indicator(stock=stock_code[-6:])
        stock_a_indicator_df['trade_date'] = pd.to_datetime(stock_a_indicator_df['trade_date'])
        stock_a_indicator_df['date'] = stock_a_indicator_df['trade_date']
        stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(symbol=stock_code, start_date=start, end_date=end, adjust="qfq")
        price_trend_df = pd.merge(stock_zh_a_daily_qfq_df, stock_a_indicator_df, how='left', on=['date'])
        price_trend_df.set_index(['date'], drop=True, inplace=True)
        price_trend_df.to_csv(data_file)
        return price_trend_df


def se_type(stock_code: str) -> str:
    if stock_code.startswith("6"):
        return "sh" + stock_code
    elif stock_code.startswith("0") or stock_code.startswith("3"):
        return "sz" + stock_code
    else:
        return stock_code


def price_trend_plot(
        stock_code,
        start="20200101",
        end=datetime.datetime.now().strftime("%Y%m%d")
) -> pd.DataFrame:
    result = price_trend(stock_code=stock_code, start=start, end=end)
    print(result.columns)
    result.plot(use_index=True, y=['close', 'pe', 'total_mv'], secondary_y=['total_mv'])
    plt.show()


if __name__ == '__main__':
    price_trend_plot(stock_code="sz300725")
    # df = price_trend(stock_code="sz300725")
    # print(df.iloc[0])
    # print(df.iloc[-1])
