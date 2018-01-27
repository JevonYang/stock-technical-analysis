# -*- coding: utf-8 -*-

import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def is_positive(num):
    if num >= 0:
        return True
    else:
        return False


def frequency_for_up_and_down(code):
    data = ts.get_hist_data(code, ktype='D')
    p_change = np.array(data['p_change']).tolist()
    list_p_change, list_days, temp_list = [], [], []
    change = False
    first = p_change[0]
    temp_list.append(first)
    p_change.pop(0)
    privous = is_positive(first)
    for i in p_change:
        if privous == is_positive(i):
            temp_list.append(i)
        else:
            change = not change
            # print change
            list_p_change.append(np.sum(temp_list))
            list_days.append(len(temp_list))
            # print temp_list
            temp_list = []
            temp_list.append(i)
        privous = is_positive(i)
    list_p_change_up = list_p_change[::2]
    list_p_change_down = list_p_change[1::2]
    list_days_up = list_days[::2]
    list_days_down = list_days[1::2]
    print u'上涨周期涨幅中位数', np.median(list_p_change_up)
    print u'上涨周期天数中位数', np.median(list_days_up)
    print u'下跌周期跌幅中位数', np.median(list_p_change_down)
    print u'下跌周期天数中位数', np.median(list_days_down)
    # hist_up = np.histogram(list_days_up)
    # hist_down = np.histogram(list_days_down)
    # n = np.array(hist_up[0])
    # bins = np.array(hist_up[1])
    # print list_days_up
    # print n
    # fig = plt.figure()
    # plt.bar(len(n), n, 0.4)
    # plt.show()
