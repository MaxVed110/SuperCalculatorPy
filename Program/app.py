from Core.presenter import Presenter
from Core.real_calc_model import RealCalcModel
from Core.complex_calc_model import ComplexCalcModel
from logger import logger


def start():
    presenter = Presenter()

    while True:
        key = input('Выберете режим: R / I\nВыйти из программы - Е\n')
        if key == 'R':
            presenter.start_real(RealCalcModel())
        elif key == 'I':
            presenter.start_complex(ComplexCalcModel())
        elif key == 'E':
            logger.info('Выход из программны')
            print('Выход...')
            break
        else:
            print('Неверная команда')
