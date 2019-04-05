from Statistics.TradeRecord import get_tick_list
from Charts.charts import hist_trade_chart
# import pandas as pd
# engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/postgres')

if __name__ == '__main__':
    df = get_tick_list('300304', '2019-01-01', '2019-04-04')
    hist_trade_chart(df)

    # df_close = ts.get_hist_data(code='601890', start='2019-01-01', end='2019-04-04')['close']



