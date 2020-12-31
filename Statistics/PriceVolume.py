import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts
import numpy as np
from utils import config
import time

if __name__ == '__main__':
    code = '600498.SH'  # sh
    ts.set_token(config.tushare_token())
    now = time.strftime('%Y%m%d')
    df = ts.pro_bar(ts_code=code, adj='qfq', start_date='20160101')  # , end_date=now

    # df = ts.get_hist_data(code, start='2010-01-01', ktype='D')
    df.to_csv('../tmp/' + code + '.csv', index=True, sep=',')
    df = pd.read_csv('../tmp/' + code + '.csv', encoding='GBK')
    df.set_index(pd.to_datetime(df["trade_date"], format='%Y%m%d'), inplace=True)
    print(df)
    df = df['2020':'2010']
    print(df)
    a1 = [np.percentile(df['close'], 10)] * len(df)
    a2 = [np.percentile(df['close'], 90)] * len(df)

    x_data = df.index
    y_data = df['close']
    y2_data = df['vol']

    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(x_data, y_data)
    ax1.plot(x_data, a1)
    ax1.plot(x_data, a2)

    ax2.plot(x_data, y2_data)

    b1 = [np.percentile(y2_data, 10)] * len(df)
    b2 = [np.percentile(y2_data, 90)] * len(df)
    ax2.plot(x_data, b1)
    ax2.plot(x_data, b2)

    # print(stats.pearsonr(df['close'], df['volume']))
    # print(stats.pearsonr(df['成交量'], df['成交金额']))
    plt.show()
