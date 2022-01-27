import abc
import requests

from abc import ABCMeta


class CurrencyRate(metaclass=ABCMeta):
    @abc.abstractmethod
    def get_rate(self):
        pass


class GetCurrencyRate(CurrencyRate):
    def get_rate(self):
        data = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json').json()
        return data


class DollarsValueAdapter(GetCurrencyRate):
    def get(self):
        return str(self.get_rate()[26]['rate'])

