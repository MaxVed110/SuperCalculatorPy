from Core.model import Model
from Core.universal_model import UniversalModel
from Core.imaginary_model import ImaginaryModel
from Program.logger import logger


class ComplexCalcModel(Model, UniversalModel):

    def __init__(self):
        super().__init__()

    def resultSum(self):
        logger.debug('Сложение комплексных')
        return ImaginaryModel((self.x + self.y), (self.a + self.b))

    def resultDif(self):
        logger.debug('Вычитание комплексных')
        return ImaginaryModel((self.x - self.y), (self.a - self.b))

    def resultMult(self):
        logger.debug('Умножение комплексных')
        return ImaginaryModel((self.x * self.a - self.y * self.b), (self.x * self.b + self.y * self.a))

    def resultDiv(self):
        logger.debug('Деление комплексных')
        return ImaginaryModel(
            round(((self.x * self.a + self.y * self.b) / (self.b * self.b + self.a * self.a)), 2),
            round(((self.y * self.a - self.x * self.b) / (self.b * self.b + self.a * self.a)), 2))
