import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts
import numpy as np

if __name__ == '__main__':
    # df = pd.read_csv("./data/000001.csv", encoding='GBK')
    code = '600498'  # sh
    df = ts.get_hist_data(code, start='2010-01-01', ktype='D')
    df.to_csv(code + ".csv", index=True, sep=',')
    df = pd.read_csv('./' + code + '.csv', encoding='GBK')
    # print(df)
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index(df['date'])
    df = df['2020':'2014']
    # print(df)
    a1 = [np.percentile(df['close'], 10)] * len(df)
    a2 = [np.percentile(df['close'], 90)] * len(df)

    x_data = df.index
    y_data = df['close']
    y2_data = df['volume']

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
