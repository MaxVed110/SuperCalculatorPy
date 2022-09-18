from Core.model import Model
from Core.universal_model import UniversalModel
from Program.logger import logger


class RealCalcModel(Model, UniversalModel):

    def __init__(self):
        super().__init__()

    def resultSum(self):
        logger.debug('Сложение действительных')
        return self.x + self.y

    def resultDif(self):
        logger.debug('Вычитание действительных')
        return self.x - self.y

    def resultMult(self):
        logger.debug('Умножение действительных')
        return self.x * self.y

    def resultDiv(self):
        logger.debug('Деление действительных')
        return round((self.x / self.y), 2)
