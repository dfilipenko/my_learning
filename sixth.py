import time               #First exercise
class TrafficLight:
    def running (self):
        while True:
            self.__color = 'red'
            print(self.__color)
            time.sleep(7)
            self.__color = 'yelow'
            print(self.__color)
            time.sleep(2)
            self.__color = 'green'
            print(self.__color)
            time.sleep(5)

light = TrafficLight()
light.running()

class Road:                         #Second exercise
    def mass (self, length, width):
        self._length = int(length)
        self._width = int(width)
        weight = length * width * 25 * 5
        print(f"Масса асфальта, необходимая для покрытия дороги составляет {weight}")
road_1 = Road()
road_1.mass(500, 10)

class Worker:                                 #Third exercise
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print (f"Имя сотрудника: {self.name} {self.surname}")
    def get_full_income(self):
        self.wage = self._income.get("wage")
        self.bonus = self._income.get("bonus")
        print (f"Общий доход сотрудника {int(self.wage) + int(self.bonus)}")

work_1 = Position('Ivan', 'Ivanov', 'ingenear', 5000, 2000)
work_2 = Position('Petr', 'Petrov', 'Master', 10000, 3000)
print (work_1.name, work_1.surname, work_1.position, work_1._income)
print (work_2.name, work_2.surname, work_2.position, work_2._income)
work_1.get_full_name()
work_1.get_full_income()

class Car:                           #Fourth exercisw
    def __int__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
    def go (self):
        if self.speed > 0:
            return f"Автомашина {self.name} в движении"
    def stop(self):
        if self.speed == 0:
            return f"Автомашина {self.name} остановилась"
    def turn(self, direction):
        return F"Автомашина {self.name} повернула {direction}"
    def show_speed(self):
        return f"Текущая скорость автомобиля {self.speed}"
class Towncar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__int__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print ("Превышение допустимой скорости")
class Workcar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__int__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print("Превышение допустимой скорости")
class Sportcar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__int__(speed, color, name, is_police)
    pass
class Polliscar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__int__(speed, color, name, is_police)
    pass
work = Workcar (60, 'green', 'ford', False)
print (work.go(), work.stop(), work.turn('направо'), work.show_speed())
police = Polliscar (200, 'black', 'lada', True)
print (police.go(), police.stop(), police.turn('направо'), police.show_speed())

class Stationery:       #Fifth exercise
    title = ""
    def draw(self):
        return "Запуск отрисовки"
class Pen(Stationery):
    def draw(self):
        return "Рисуем ручкой"
class Pencil(Stationery):
    def draw(self):
        return "Рисуем карандашом"
class Handle(Stationery):
    def draw(self):
        return "Рисуем маркером"
paint = Pen()
print (paint.draw())