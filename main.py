import os
import sys
import time

import akshare as ak
import pandas as pd

from Statistics.financial_analysis import finance_info
from Statistics.price_trend import price_trend, se_type


def project_dir():
    return os.path.abspath(os.path.dirname(__file__))


if __name__ == '__main__':

    start_time = time.process_time()

    result = pd.DataFrame(columns=['code', 'name', 'mean_roe_5_years', 'total_mv'])

    index_code: str = "801150"
    sw_index_df = ak.sw_index_cons(index_code=index_code)
    result.to_csv("./" + index_code + "roe.csv")
    for index, stock in sw_index_df.iterrows():
        mean_roe_5_years = finance_info(stock_code=stock['stock_code'])[lambda x: x.index.month == 12][
            '净资产报酬率(%)'].head(
            5).mean()
        total_mv = price_trend(stock_code=se_type(stock['stock_code'])).iloc[0]['total_mv']
        print({'code': stock['stock_code'], 'name': stock['stock_name'], 'mean_roe_5_years': mean_roe_5_years,
               'total_mv': total_mv})
        result = result.append(
            {'code': stock['stock_code'], 'name': stock['stock_name'], 'mean_roe_5_years': mean_roe_5_years,
             'total_mv': total_mv},
            ignore_index=True)
        result.to_csv("./" + index_code + "roe.csv", mode='a', header=False)

    roe_result = result.sort_values(by='mean_roe_5_years', ascending=False)
    # print(roe_result)
    # roe_result.reset_index().to_excel("./" + index_code + "roe.xls")
    # price_trend_plot(stock_code="sh600129", start="20180101")

    stop_time = time.process_time()
    cost = stop_time - start_time
    print("%s cost %s second" % (os.path.basename(sys.argv[0]), cost))
