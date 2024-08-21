class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'purple', 'white', 'black', 'grey', 'yellow', 'green']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner: str = owner
        self.__model: str = __model
        self.__engine_power: int = __engine_power
        self.__color: str = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец {self.owner}\n')

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
