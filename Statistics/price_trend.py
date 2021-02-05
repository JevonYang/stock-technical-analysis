import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt
import datetime


def price_trend(
        stock_code, 
        start="20100101", 
        end=datetime.datetime.now().strftime("%Y%m%d")
    ) -> pd.DataFrame:
    stock_a_indicator_df = ak.stock_a_lg_indicator(stock=stock_code[-6:])
    stock_a_indicator_df['trade_date'] = pd.to_datetime(stock_a_indicator_df['trade_date'])
    # stock_a_indicator_df = stock_a_indicator_df.set_index(['trade_date'])
    stock_a_indicator_df['date'] = stock_a_indicator_df['trade_date']
    stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(symbol=stock_code, start_date="20100101", end_date=end, adjust="qfq")
    
    result = pd.merge(stock_zh_a_daily_qfq_df, stock_a_indicator_df, how='left', on=['date'])
    return result


if __name__ == '__main__':
    result = price_trend(stock_code="sz300725")
    print(result.columns)
    result.plot(use_index=True,x='date', y=['close','pb'], secondary_y=['pb'])
    plt.show()
    
