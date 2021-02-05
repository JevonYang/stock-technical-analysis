import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tseries.offsets import YearEnd
import threading


# stock_financial_abstract_df = ak.stock_financial_abstract(stock="300725")
# print(stock_financial_abstract_df)

def convert_float(value):
    try:
        return float(value)
    except BaseException:
        return 0


def financial_info(stock_code) -> pd.DataFrame:
    stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(stock=stock_code)
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


if __name__ == '__main__':
    print(financial_info(stock_code="300725")[lambda x: x.index.month == 12]['净资产报酬率(%)'].head(5).mean())
    financial_300725 = financial_info(stock_code="300725")[lambda x: x.index.month == 12]

    financial_300725.plot.bar(use_index=False, y=['净资产报酬率(%)', '资产报酬率(%)', '净资产增长率(%)', '总资产增长率(%)'])
    plt.show()

    # import akshare as ak
    # sw_index_df = ak.sw_index_cons(index_code="801150")

    # result = pd.DataFrame(columns=['code', 'name', 'mean_roe_5_years'])
    #
    # stock_zh_a_spot_df = ak.stock_zh_a_spot()
    #
    # for index, stock in stock_zh_a_spot_df.iterrows():
    #     mean_roe_5_years = financial_info(stock_code=stock['code'])[lambda x: x.index.month == 12]['净资产报酬率(%)'].head(
    #         5).mean()
    #     result = result.append({'code': stock['code'], 'name': stock['name'], 'mean_roe_5_years': mean_roe_5_years},
    #                            ignore_index=True)
    #
    # result.to_excel("./roe.xlsx")
