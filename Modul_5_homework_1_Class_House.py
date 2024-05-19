class House:  # создание класса

    def __init__(self, number_of_floors=10):
        # (self, number_of_floors=10) - параметры функции
        self.floors = number_of_floors  # атрибут экземпляра класса


house1 = House(10)  # создание эземпляра
def summa(number_of_floors):
    print("Текущий этаж равен", number_of_floors)
    if number_of_floors == 1:
        return 0
    else:
        return number_of_floors + summa(number_of_floors - 1)

summa(10)