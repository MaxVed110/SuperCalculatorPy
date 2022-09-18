from Core.imaginary_model import ImaginaryModel
from Program.logger import logger


def get_value(phrase: str):
    logger.debug('Введено значение')
    buf = input(f'Введите {phrase}\n')
    while not buf.isnumeric():
        print('Введите число')
        buf = input(f'Введите {phrase}\n')
    return float(buf)


def print_result(result):
    logger.debug('Печать результата')
    print(f'Результат: {result}')


def print_complex_result(complex_result: ImaginaryModel):
    logger.debug('Печать результата')
    if complex_result.a < 0:
        print(f'Результат: {complex_result.x} -i{complex_result.a}')
    else:
        print(f'Результат: {complex_result.x} +i{complex_result.a}')
