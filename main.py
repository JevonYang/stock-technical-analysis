#-*- coding: utf-8 -*-

import tushare as ts
import numpy as np
import pandas as pd

if __name__ == '__main__':
    data = ts.get_hist_data('sh',ktype='W')
    print(data)