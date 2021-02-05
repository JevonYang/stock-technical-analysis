#!/usr/bin/env python
# coding: utf-8

import datetime

import akshare as ak
import matplotlib.pyplot as plt
import pandas as pd


def get_classify_index(
    start="2017-12-31", 
    end=datetime.datetime.now().strftime("%Y-%m-%d"), 
    freq="Week") -> pd.DataFrame:
    sw_index_spot_df = ak.sw_index_spot()
    result_index = pd.DataFrame()
    for code in sw_index_spot_df['指数代码']:
        sw_index_df = ak.sw_index_daily_indicator(index_code=code, start_date=start,
                                                  end_date=end,
                                                  data_type=freq)
        init_price = float(sw_index_df.iloc[-1].at['close'])
        sw_index_df['relate_price'] = sw_index_df['close'].astype('float').apply(
            lambda x: (x - init_price) / init_price)
        result_index[sw_index_df.iloc[-1].at['index_name']] = sw_index_df['relate_price']
    result_index = result_index.iloc[::-1].reset_index(drop=True).T
    return result_index.sort_values(by=result_index.shape[1] - 1, ascending=False)


if __name__ == '__main__':
    result = get_classify_index(start="2019-12-31", freq="Day")

    result.head(5).T.plot()
    plt.legend(loc='best')
    plt.show()

    result[result.shape[1] - 1].plot.bar()
    plt.show()
