class Matrix:                    #First exercise
    def __init__(self, list):
        self.list = list

    def __str__(self):
        for item in self.list:
            for element_list in item:
                print (str(element_list), end=" ")
            print ()
        return ''

    def __add__(self, other):
        for self_item in range(len(self.list)):
            for other_item in range(len(other.list)):
                self.list[self_item][other_item] = self.list[self_item][other_item] + other.list[self_item][other_item]
        return Matrix.__str__(self)

object_1 = Matrix ([[1, 3, 5], [2, 4, 6], [3, 6, 9]])
object_2 = Matrix ([[11, 13, 15], [12, 14, 16], [13, 16, 19]])
print (object_1)
print(object_2)
print(object_1.__add__(object_2))

from abc import abstractmethod            #Second exercise

class Dress:
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def __add__(self, other):
        self.square = (self.size / 6.5 + 0.5) + (2 * other.size + 0.3)
        print (f"Для изготовления одежды требуется {self.square:.2f} ткани")
        return ''

class Coat(Dress):
    @property
    def dress_square(self):
        print (f"Для изготовления пальто требуется {(self.size / 6.5 + 0.5):.2f} ткани")
        return ''

class Jacket (Dress):
    @property
    def dress_square(self):
        print (f"Для изготовления пиджака требуется {(2 * self.size + 0.3):.2f} ткани")
        return ''

coat_1 = Coat(50)
jacket_1 = Jacket(48)
print(jacket_1.dress_square)
print(coat_1.dress_square)
print(coat_1.__add__(jacket_1))

class Cage:                                #Third exercise

    def __init__(self, length_cage):
        self.lenght_cage = length_cage

    def __add__(self, other):
        return f"Сумма двух клеток равна {self.lenght_cage + other.lenght_cage}"

    def __sub__(self, other):
        self.sub = self.lenght_cage - other.lenght_cage
        if self.sub > 0:
            return f"Разность двух клеток равна {self.sub}"
        else:
            return "Данные клетки нельзя вычитать"

    def __mul__(self, other):
        return f"Произведение двух клеток равно {self.lenght_cage * other.lenght_cage}"

    def __truediv__(self, other):
        return f"Результат деления клеток равен {round (self.lenght_cage / other.lenght_cage)}"

    def make_order(self, count_cell):
        self.rows = self.lenght_cage // count_cell
        self.fin_rows = self.lenght_cage % count_cell
        for item in range (self.rows):
            print('*'*count_cell)
        print ('*'*self.fin_rows)
        return ''

cage_1 = Cage(8)
cage_2 = Cage(36)
print(cage_2.__truediv__(cage_1))
print(cage_2.make_order(7))
