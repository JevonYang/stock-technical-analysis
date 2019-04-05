import pandas as pd
import numpy as np
import tushare as ts
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/postgres')


def hist_trade_chart(df):
    # df = pd.read_sql_table('tt_601890', engine)
    # print(df)
    df_price = df[['price_mean','buy_price_mean','sell_price_mean']]
    df_volume=df[['volume_mean','buy_volume_mean', 'neutral_volume_mean','sell_volume_mean']]
    df_amount=df[['amount_mean','buy_amount_mean', 'neutral_amount_mean','sell_amount_mean']]
    df_close = ts.get_hist_data(code='601890', start='2019-01-01', end='2019-04-04')['close']

    # x_axis = df['index'].tolist()
    x=np.arange(len(df))
    width = 0.3
    plt.bar(x-width, height = df_volume['buy_volume_mean'], width= width, label = 'buy-volume')
    plt.bar(x, height = df_volume['neutral_volume_mean'], width= width, label = 'neutral-volume')
    plt.bar(x+width, height=df_volume['sell_volume_mean'], width=width, label='sell-volume')
    plt.twinx()
    plt.plot(x, df_price['price_mean'].tolist(), label='price_mean')
    # plt.plot(x, df_price['price_mean'].tolist(), label='close_price')
    # plt.plot(x, df_price['sell_price_mean'].tolist(), label='sell-price')
    plt.legend(loc = "upper left")
    plt.xlabel("date")
    plt.ylabel("average amount")
    plt.title("amount")
    plt.show()
