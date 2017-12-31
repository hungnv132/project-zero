import requests
from abc import ABC
from datetime import datetime, timedelta

VND_URL = 'https://www.vndirect.com.vn/portal/ajax/listed/SearchHistoricalPriceForSymbol.shtml'
DATE_FORMAT = '%d/%m/%Y'


class DataBox(ABC):

    def __init__(self, url, from_date=None, to_date=None):
        from_date = from_date if from_date else datetime.now().strftime(DATE_FORMAT)
        to_date = to_date if to_date else datetime.now().strftime(DATE_FORMAT)
        self.url = url
        self.from_date = from_date
        self.to_date = to_date

    def _pull_data(self):
        raise NotImplementedError('Please implement this method.')

    def pull_data_by_offset(self, offset):
        raise NotImplementedError('Please implement this method.')

    def pull_data_today(self):
        raise NotImplementedError('Please implement this method.')

    def _mapping(self):
        raise NotImplementedError('Please implement this method.')


class VNDDataBox(DataBox):

    def __init__(self):
        super(VNDDataBox, self).__init__(VND_URL)

    def _pull_data(self, symbol, from_date=None, to_date=None):
        from_date = from_date.strftime(DATE_FORMAT)
        to_date = to_date.strftime(DATE_FORMAT)
        payload = {
            'searchMarketStatisticsView.symbol': symbol,
            'strFromDate': from_date,
            'strToDate': to_date
        }
        print(self.url)
        print(payload)
        response = requests.post(self.url, data=payload).json()
        return response['model']['searchResult']

    def _mapping(self, data):
        return {
            'open': data['openPrice'],
            'close': data['closePrice'],
            'high': data['highPrice'],
            'low': data['lowPrice'],
            'volume': int(data['volume']),
            'ptvolume': int(data['ptVolume'])
        }

    def pull_data_today(self, symbol):
        from_date = to_date = datetime.now().strftime(DATE_FORMAT)
        data = self._pull_data(symbol, from_date, to_date)[0]['id']
        return self._mapping(data)

    def pull_data_by_offset(self, symbol, offset=0):
        date = datetime.now() + timedelta(days=offset)
        data = self._pull_data(symbol, date, date)[0]['id']
        return self._mapping(data)


class Quote(object):
    __slots__ = ("symbol", "open", "close", "high", "low", "volume", "ptvolume")

    def __init__(self, symbol=None, **kwargs):
        if not symbol:
            raise Exception("Please initialize 'symbol' property")
        self.symbol = symbol
        self.open = self.close = self.high = self.low = self.volume = self.ptvolume = 0
        self.set_prices(**kwargs)

    def set_prices(self, open=None, close=None, high=None, low=None, volume=None,
                   ptvolume=None):
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.ptvolume = ptvolume

    def update_prices_today(self, databox=None):
        if not databox:
            databox = VNDDataBox()
        data = databox.pull_data_by_offset(self.symbol, -2)
        self.set_prices(**data)

    def changed(self):
        return (self.close - self.open) / self.open *100


if __name__ == '__main__':
    quote = Quote('VCB')
    quote.update_prices_today()
    print(quote.open)
