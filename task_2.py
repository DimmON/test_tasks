# Определение количества символов в названии с помощью декоратора
# Переопределение стандартных методов плохая практика, сделано только потому, что было указано в задании
# def len_name(func):
#     def wrapper(*args, **kwargs):
#         s = args[0].get_name()
#         count = 0
#         for _ in s:
#             count += 1
#         return count
#     return wrapper
#
#
# @len_name
# def len(object_name):
#     return


class Technic:
    @classmethod
    def __validate_bool(cls, arg):
        return isinstance(arg, bool)

    def __init__(self, name: str, price: float, availability: bool):
        self._name = name
        self._price = price
        if self.__validate_bool(availability):
            self._availability = availability
        else:
            self._availability = False

    def __setattr__(self, key, value):
        if key not in ('_name', '_price', '_availability'):
            pass  # Здесь можно генерировать ошибку
        else:
            object.__setattr__(self, key, value)

    def set_availability(self, availability: bool):
        if self.__validate_bool(availability):
            self._availability = availability

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_availability(self) -> bool:
        return self._availability

    def get_category(self, category_boundary):
        return 'Бюджетный' if self._price <= category_boundary else 'Дорогой'

    # Определение количества символов в названии с помощью магического метода
    def __len__(self):
        return len(self._name)


t1 = Technic('Пылесос', 1000, True)
t2 = Technic('Телевизор', 5000, True)

print(len(t1) < len(t2))

