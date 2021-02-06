import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tseries.offsets import YearEnd
import threading
import os
from utils.config import project_dir

CACHE_DIR = "../tmp/finance_reports"


def cache_dir():
    return os.path.join(os.path.join(project_dir(), 'tmp', 'finance_reports'))


def error_file_dir():
    return os.path.join(os.path.join(project_dir(), 'tmp', 'errors', 'finance.txt'))


def convert_float(value):
    try:
        return float(value)
    except Exception:
        return 0


def finance_info(stock_code) -> pd.DataFrame:
    data_file = os.path.join(cache_dir(), stock_code + '.csv')
    try:
        stock_financial_analysis_indicator_df = pd.read_csv(data_file, index_col=0)
    except FileNotFoundError:
        stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(stock=stock_code)
        stock_financial_analysis_indicator_df.to_csv(data_file)
    stock_financial_analysis_indicator_df.index = pd.to_datetime(stock_financial_analysis_indicator_df.index)
    stock_financial_analysis_indicator_df['净资产报酬率(%)'] = stock_financial_analysis_indicator_df['净资产报酬率(%)'].apply(
        convert_float)
    stock_financial_analysis_indicator_df['资产报酬率(%)'] = stock_financial_analysis_indicator_df['资产报酬率(%)'].apply(
        convert_float)
    stock_financial_analysis_indicator_df['总资产净利润率(%)'] = stock_financial_analysis_indicator_df['总资产净利润率(%)'].apply(
        convert_float)
    stock_financial_analysis_indicator_df['主营业务利润率(%)'] = stock_financial_analysis_indicator_df['主营业务利润率(%)'].apply(
        convert_float)
    stock_financial_analysis_indicator_df['净利润增长率(%)'] = stock_financial_analysis_indicator_df['净利润增长率(%)'].apply(
        convert_float)
    stock_financial_analysis_indicator_df['净资产增长率(%)'] = stock_financial_analysis_indicator_df['净资产增长率(%)'].apply(
        convert_float)
    stock_financial_analysis_indicator_df['总资产增长率(%)'] = stock_financial_analysis_indicator_df['总资产增长率(%)'].apply(
        convert_float)
    return stock_financial_analysis_indicator_df


def financial_info_plot(stock_code, y=None):
    if y is None:
        y = ['净资产报酬率(%)', '资产报酬率(%)', '净资产增长率(%)', '总资产增长率(%)']
    finance_info(stock_code=stock_code)[lambda x: x.index.month == 12].plot.bar(use_index=False, y=y)
    plt.show()


def save_finance_reports(classify_index_code):
    sw_index_df = ak.sw_index_cons(index_code=classify_index_code)
    for index, stock in sw_index_df.iterrows():
        try:
            finance_info(stock['stock_code'])
        except Exception:
            f = open(error_file_dir, 'a')
            f.write(stock['stock_code'] + '\n')
            f.close()


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

if __name__ == '__main__':
    sw_index_spot_df = ak.sw_index_spot()

    for index, row in sw_index_spot_df.iterrows():
        save_finance_reports(classify_index_code=row['指数代码'])

    print(error_file_dir())

