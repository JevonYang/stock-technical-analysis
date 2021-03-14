import os
import sys
import time

import akshare as ak
import pandas as pd
import numpy as np

from Statistics.financial_analysis import finance_info
from Statistics.price_trend import price_trend, se_type


def project_dir():
    return os.path.abspath(os.path.dirname(__file__))


def compound_annual_growth_rate(list_growth):
    init: float = 1.0
    for growth in list_growth:
        init = init * (1 + growth / 100)
    return init


def classify_index_financial(index_code: str):
    result = pd.DataFrame(columns=['code', 'name', '2015', '2016', '2017', '2018', '2019', 'total_mv', 'cagr'])

    # index_code: str = "801150"
    sw_index_df = ak.sw_index_cons(index_code=index_code)
    # result.to_csv("./" + index_code + "roe.csv")
    for _, stock in sw_index_df.iterrows():
        roe_5_years = finance_info(stock_code=stock['stock_code'])[lambda x: x.index.month == 12][
            '净资产报酬率(%)'].head(5)
        # print(type(roe_5_years.tolist()))
        cagr = compound_annual_growth_rate(roe_5_years.tolist())
        total_mv = price_trend(stock_code=se_type(stock['stock_code'])).iloc[-1]['total_mv']
        item = {'code': stock['stock_code'], 'name': stock['stock_name'], 'total_mv': total_mv, 'cagr': cagr}
        for index_roe in roe_5_years.index:
            item.update({index_roe.strftime("%Y"): roe_5_years[index_roe]})
        print(item)
        # result.append(item, ignore_index=True).to_csv("./" + index_code + "roe.csv", mode='a', header=False)
        result = result.append(item, ignore_index=True)
    result.to_csv("./" + index_code + "roe.csv")
    return result


"""
 指数代码  指数名称      
0   801010  农林牧渔
1   801020    采掘
2   801030    化工
3   801040    钢铁
4   801050  有色金属
5   801080    电子
6   801110  家用电器
7   801120  食品饮料
8   801130  纺织服装
9   801140  轻工制造
10  801150  医药生物
11  801160  公用事业
12  801170  交通运输
13  801180   房地产
14  801200  商业贸易
15  801210  休闲服务
16  801230    综合
17  801710  建筑材料
18  801720  建筑装饰
19  801730  电气设备
20  801740  国防军工
21  801750   计算机
22  801760    传媒  
23  801770    通信
24  801780    银行 
25  801790  非银金融
26  801880    汽车
27  801890  机械设备
"""


def classify_index_financial_describe():
    sw_index_spot_df = ak.sw_index_spot()
    for index, row in sw_index_spot_df.iterrows():
        classify_item = classify_index_financial(index_code=row['指数代码'])
        describe_classify_index = classify_item.describe()[['total_mv', 'cagr']]
        describe_classify_index.to_csv('./' + row['指数代码'] + 'describe' + '.csv')


def classify_index_financial_conclusion():
    global sw_index_spot_df, index, row
    classify_index_financial_describe()
    result = pd.DataFrame()
    sw_index_spot_df = ak.sw_index_spot()
    for index, row in sw_index_spot_df.iterrows():
        df = pd.read_csv('./' + row['指数代码'] + 'describe.csv', index_col=0)
        index_name = row['指数名称']
        item = {
            'index_name': index_name,
            'index_code': row['指数代码'],
            'total_mv_25%': df['total_mv']['25%'],
            'total_mv_mean': df['total_mv']['mean'],
            'total_mv_75%': df['total_mv']['75%'],
            'cagr_25%': df['cagr']['25%'],
            'cagr_mean': df['cagr']['mean'],
            'cagr_75%': df['cagr']['75%']
        }
        result = result.append(item, ignore_index=True)
    result.to_excel("./classify_financial_conclusion.xlsx")
    import matplotlib.pyplot as plt
    result.plot.bar(x='index_name', y=['total_mv_mean', 'cagr_mean'], secondary_y='cagr_mean')
    # plt.legend()
    plt.show()


if __name__ == '__main__':
    start_time = time.process_time()

    # classify_index_financial(index_code="801080")

    classify_index_financial_describe()
    classify_index_financial_conclusion()

    stop_time = time.process_time()
    cost = stop_time - start_time
    print("%s cost %s second" % (os.path.basename(sys.argv[0]), cost))
