# -*- coding: utf-8 -*-

from collections import namedtuple, OrderedDict


def find_second_max(dict_array):
    stock_price_sorted = sorted(zip(dict_array.values(), dict_array.keys()))
    return stock_price_sorted[-2]


def find_second_max_and_min(dict_array):
    stock_price_sorted = sorted(zip(dict_array.values(), dict_array.keys()))
    return stock_price_sorted[0], stock_price_sorted[-1]


if __name__ == '__main__':
    price_str = '200'
    print u'旧的price_str id = {}'.format(id(price_str))
    price_str = price_str.replace(' ', '')
    print u'新的price_str id = {}'.format(id(price_str))

    price_array = price_str.split(',')
    # print price_array
    price_array.append('32.82')
    price_array.append('32.82')
    price_array.append('32.82')
    print price_array
    print set(price_array)
    # print price_array

    date_array = []
    date_base = 20170118
    # for _ in xrange(0, len(price_array)):
    #    date_array.append(str(date_base))
    #    date_base += 1
    # print date_array
    # price_cnt = len(price_array) -1
    # while price_cnt > 0:
    # date_array.append(str(date_base))
    #    date_base +=1
    #    price_cnt -=1
    # print date_array
    date_array = [str(date_base + ind) for ind, _ in enumerate(price_array)]
    print date_array

    stock_tuple_list = [(date, price)
                        for date, price in zip(date_array, price_array)]
    print stock_tuple_list
    # print u'20170119日价格：{}'.format(stock_tuple_list[1][1])
    print stock_tuple_list

    stock_namedtuple = namedtuple('stock', ('date', 'price'))
    stock_namedtuple_list = [stock_namedtuple(
        date, price) for date, price in zip(date_array, price_array)]
    print u'20170119日价格：{}'.format(stock_namedtuple_list[1].price)
    print stock_namedtuple_list

    stock_dict = {date: price for date, price in zip(date_array, price_array)}
    print stock_dict
    print stock_dict.keys(), stock_dict.values()

    stock_dict = OrderedDict((date, price)
                             for date, price in zip(date_array, price_array))
    print stock_dict.keys(), stock_dict.values()

    print min(stock_dict.values(), stock_dict.keys())

    if callable(find_second_max):
        print find_second_max(stock_dict)

    find_second_max_lambda = lambda dict_array: sorted(zip(dict_array.values(), dict_array.keys()))[-2]

    print find_second_max_lambda(stock_dict)

    print find_second_max_and_min(stock_dict)

    price_float_array = [float(price_str) for price_str in stock_dict.values()]
    pp_array = [(price1, price2) for price1, price2 in zip(price_float_array[:-1], price_float_array[1:])]

    print(pp_array)

    change_array = map(lambda pp: reduce(lambda a, b: round((b - a) / a, 3), pp), pp_array)
    change_array.insert(0, 0)
    print(change_array)

    stock_namedtuple = namedtuple('stock', ('date', 'price', 'change'))
    stock_dict = OrderedDict((date, stock_namedtuple(date, price, change)) for date, price, change in
                             zip(date_array, price_array, change_array))
    print(stock_dict)

    up_days= filter(lambda day: day.change>0, stock_dict.values())
