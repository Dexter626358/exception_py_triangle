from home_work.ExistenceError import TriangleExistError


class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if (side_a + side_b) > side_c and \
                (side_b + side_c) > side_a and \
                (side_c + side_a) > side_b:
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            raise TriangleExistError

    def area(self):
        half_perimetr = self.side_a + self.side_b + self.side_c / 2
        area = (half_perimetr * (half_perimetr - self.side_a) * (half_perimetr - self.side_b)
                * (half_perimetr - self.side_c)) ** 0.5
        return f"Площадь треугольника со сторонами {self.side_a}, {self.side_b}, {self.side_c} " \
               f"равна: {area}"

    def perimetr(self):
        return f"Периметр треугольника со сторонами {self.side_a}, {self.side_b}, {self.side_c} " \
               f"равен: {self.side_a + self.side_b + self.side_c}"
