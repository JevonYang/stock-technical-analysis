import datetime


class DateList():
    """取区间日期模块，主要传入两个参数:
    Quriqi('20180601','20180608').suanriqi()  将会返回list类型
    此类用的模块为datetime
    """

    def __init__(self, start_date, end_date):
        self.start = start_date
        self.end = end_date
        self.generate()

    def generate(self):
        date_start = datetime.datetime.strptime(self.start, '%Y-%m-%d')
        date_end = datetime.datetime.strptime(self.end, '%Y-%m-%d')
        date_list = []
        while date_start < date_end:
            date_start += datetime.timedelta(days=1)
            period = date_start.strftime('%Y-%m-%d')
            date_list.append(period)
        return date_list
