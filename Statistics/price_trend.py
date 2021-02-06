import datetime

import akshare as ak
import matplotlib.pyplot as plt
import pandas as pd


def price_trend(
        stock_code,
        start="20100101",
        end=datetime.datetime.now().strftime("%Y%m%d")
) -> pd.DataFrame:
    stock_a_indicator_df = ak.stock_a_lg_indicator(stock=stock_code[-6:])
    stock_a_indicator_df['trade_date'] = pd.to_datetime(stock_a_indicator_df['trade_date'])
    # stock_a_indicator_df = stock_a_indicator_df.set_index(['trade_date'])
    stock_a_indicator_df['date'] = stock_a_indicator_df['trade_date']
    stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(symbol=stock_code, start_date=start, end_date=end, adjust="qfq")
    return pd.merge(stock_zh_a_daily_qfq_df, stock_a_indicator_df, how='left', on=['date'])


def se_type(stock_code: str) -> str:
    if stock_code.startswith("6"):
        return "sh" + stock_code
    elif stock_code.startswith("0") or stock_code.startswith("3"):
        return "sz" + stock_code
    else:
        return stock_code


def price_trend_plot(
        stock_code,
        start="20100101",
        end=datetime.datetime.now().strftime("%Y%m%d")
) -> pd.DataFrame:
    result = price_trend(stock_code=stock_code, start=start, end=end)
    print(result.columns)
    result.plot(use_index=True, x='date', y=['close', 'pe', 'pb'], secondary_y=['pb'])
    plt.show()


if __name__ == '__main__':
    price_trend_plot(stock_code="sz000952")
