import Core.view
from Core.real_calc_model import RealCalcModel
from Core.complex_calc_model import ComplexCalcModel


class Presenter:

    def __init__(self):
        self.model = None

    def start_real(self, real_model: RealCalcModel):

        self.model = real_model
        key = input('Выберите необходимую операцию: + - * / ...\n')
        self.model.set_x(Core.view.get_value('первое число'))
        self.model.set_y(Core.view.get_value('второе число'))
        if key == '+':
            Core.view.print_result(self.model.resultSum())
        elif key == '-':
            Core.view.print_result(self.model.resultDif())
        elif key == '*':
            Core.view.print_result(self.model.resultMult())
        elif key == '/':
            Core.view.print_result(self.model.resultDiv())
        else:
            print('Такой орерации не существует')

    def start_complex(self, complex_model: ComplexCalcModel):

        self.model = complex_model
        key = input('Выберите необходимую операцию: + - * / ...\n')
        self.model.set_x(Core.view.get_value('действительную часть первого числа'))
        self.model.set_a(Core.view.get_value('нимую часть первого числа'))
        self.model.set_y(Core.view.get_value('действительную часть второго числа'))
        self.model.set_b(Core.view.get_value('мнимую часть второго числа'))
        if key == '+':
            Core.view.print_complex_result(self.model.resultSum())
        elif key == '-':
            Core.view.print_complex_result(self.model.resultDif())
        elif key == '*':
            Core.view.print_complex_result(self.model.resultMult())
        elif key == '/':
            Core.view.print_complex_result(self.model.resultDiv())
        else:
            print('Такой орерации не существует')
