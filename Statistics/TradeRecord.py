from utils.DateList import DateList
import tushare as ts
import pandas as pd


def get_tick_list(code, start, end):
    date_list = DateList(start, end).generate()

    result = pd.DataFrame(columns=('price_mean',
                                   'price_std',
                                   'price_min',
                                   'price_25',
                                   'price_50',
                                   'price_75',
                                   'price_max',

                                   'volume_mean',
                                   'volume_std',
                                   'volume_min',
                                   'volume_25',
                                   'volume_50',
                                   'volume_75',
                                   'volume_max',

                                   'amount_mean',
                                   'amount_std',
                                   'amount_min',
                                   'amount_25',
                                   'amount_50',
                                   'amount_75',
                                   'amount_max',

                                   'buy_price_mean',
                                   'buy_price_std',
                                   'buy_price_min',
                                   'buy_price_25',
                                   'buy_price_50',
                                   'buy_price_75',
                                   'buy_price_max',

                                   'buy_volume_mean',
                                   'buy_volume_std',
                                   'buy_volume_min',
                                   'buy_volume_25',
                                   'buy_volume_50',
                                   'buy_volume_75',
                                   'buy_volume_max',

                                   'buy_amount_mean',
                                   'buy_amount_std',
                                   'buy_amount_min',
                                   'buy_amount_25',
                                   'buy_amount_50',
                                   'buy_amount_75',
                                   'buy_amount_max',

                                   'neutral_price_mean',
                                   'neutral_price_std',
                                   'neutral_price_min',
                                   'neutral_price_25',
                                   'neutral_price_50',
                                   'neutral_price_75',
                                   'neutral_price_max',

                                   'neutral_volume_mean',
                                   'neutral_volume_std',
                                   'neutral_volume_min',
                                   'neutral_volume_25',
                                   'neutral_volume_50',
                                   'neutral_volume_75',
                                   'neutral_volume_max',

                                   'neutral_amount_mean',
                                   'neutral_amount_std',
                                   'neutral_amount_min',
                                   'neutral_amount_25',
                                   'neutral_amount_50',
                                   'neutral_amount_75',
                                   'neutral_amount_max',

                                   'sell_price_mean',
                                   'sell_price_std',
                                   'sell_price_min',
                                   'sell_price_25',
                                   'sell_price_50',
                                   'sell_price_75',
                                   'sell_price_max',

                                   'sell_volume_mean',
                                   'sell_volume_std',
                                   'sell_volume_min',
                                   'sell_volume_25',
                                   'sell_volume_50',
                                   'sell_volume_75',
                                   'sell_volume_max',

                                   'sell_amount_mean',
                                   'sell_amount_std',
                                   'sell_amount_min',
                                   'sell_amount_25',
                                   'sell_amount_50',
                                   'sell_amount_75',
                                   'sell_amount_max',
                                   ))

    for item in date_list:
        temp = pd.DataFrame(ts.get_tick_data(code, date=item, src='tt'))
        if not temp.empty:
            df_describe = temp.describe()
            df_buy_describe = temp[temp.type == '买盘'].describe()
            df_neutral_describe = temp[temp.type == '中性盘'].describe()
            df_sell_describe = temp[temp.type == '卖盘'].describe()
            result_row = []

            result_row += df_describe['price'].tolist()[1:]
            result_row += df_describe['volume'].tolist()[1:]
            result_row += df_describe['amount'].tolist()[1:]
            result_row += df_buy_describe['price'].tolist()[1:]
            result_row += df_buy_describe['volume'].tolist()[1:]
            result_row += df_buy_describe['amount'].tolist()[1:]
            result_row += df_neutral_describe['price'].tolist()[1:]
            result_row += df_neutral_describe['volume'].tolist()[1:]
            result_row += df_neutral_describe['amount'].tolist()[1:]
            result_row += df_sell_describe['price'].tolist()[1:]
            result_row += df_sell_describe['volume'].tolist()[1:]
            result_row += df_sell_describe['amount'].tolist()[1:]
            result.loc[item] = result_row
    return result