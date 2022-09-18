from Core.universal_model import UniversalModel
from Program.logger import logger


class ImaginaryModel(UniversalModel):

    def __init__(self, x, a):
        logger.info('Создано комплексное число')
        super().__init__()
        self.x = x
        self.a = a
