from abc import ABCMeta, abstractmethod


class Model:
    __metaclass__ = ABCMeta

    @abstractmethod
    def resultSum(self):
        """Сложить 2 числа"""

    @abstractmethod
    def resultDif(self):
        """Вычесть 2 числа"""

    @abstractmethod
    def resultMult(self):
        """Умножить 2 числа"""

    @abstractmethod
    def resultDiv(self):
        """Разделить 2 числа"""
