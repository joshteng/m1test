import os
import csv
import math
import time
from datetime import datetime, timedelta

import requests
import pytz
import ccxt
import pandas as pd
from talib import SMA


class Data:

    # only interval of 1d is supported now
    def get_historical_data_in_csv(self, symbol="BTCUSD", interval='1d', start_time=datetime(2019, 12, 31), end_time=datetime(2020, 12, 31)):
        filename = f"Binance-{symbol}-{interval}-{start_time.strftime('%d-%b-%Y')}-{end_time.strftime('%d-%b-%Y')}"

        filepath = "data/" + filename + '.csv'

        if os.path.isfile(filepath):
            return filepath


    @classmethod
    def unix_timestamp(self, date_obj):
        """Convert UTC date to milliseconds
        If using offset strings add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"
        See dateparse docs for formats http://dateparser.readthedocs.io/en/latest/
        :param date_str: date in readable format, i.e. "January 01, 2018", "11 hours ago UTC", "now UTC"
        :type date_str: str
        """
        # get epoch value in UTC
        epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)

        d = date_obj

        # if the date is not timezone aware apply UTC timezone
        if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
            d = d.replace(tzinfo=pytz.utc)

        # return the difference in time
        return int((d - epoch).total_seconds())

    @classmethod
    def date_to_milliseconds(self, date_obj):
        return int(Data.unix_timestamp(date_obj) * 1000.0)

    @classmethod
    def milliseconds_to_date(self, timestamp):
        return datetime.utcfromtimestamp(int(timestamp) / 1000.0)

    @classmethod
    def date_to_datestring(self, date_obj, format='%Y-%m-%d'):
        return date_obj.strftime(format)


data = Data()

data_csv = data.get_historical_data_in_csv(
        symbol='BTCBUSD',
        interval='1d',
        start_time=datetime(2020,1,1),
        end_time=datetime(2021, 12, 31))

portfolio_df = pd.read_csv(data_csv)

portfolio_df['DateTime'] = pd.to_datetime([Data.milliseconds_to_date(float(time)) for time in portfolio_df['DateTime']])

print(SMA(portfolio_df['Close']))
