
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


t1 = Technic('Пылесос', 1000, True)
print(t1.__dict__)

t1.a = 'Новый атрибут'
print(t1.__dict__)

boundary = 1500
print(t1.get_category(boundary))

