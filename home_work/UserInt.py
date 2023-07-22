"""Напишите программу для вычисления площади и периметра треугольника"""
from home_work.ExistenceError import TriangleExistError
from home_work.Triangle import Triangle

while True:
    print("Введите стороны длины сторон треугольника")
    try:
        side_A = input("Введите длину стороны a: ")
        if "." in side_A:
            side_A = float(side_A)
        else:
            side_A = int(side_A)
        side_B = input("Введите длину стороны b: ")
        if "." in side_B:
            side_B = float(side_B)
        else:
            side_B = int(side_B)
        side_C = input("Введите длину стороны c: ")
        if "." in side_C:
            side_C = float(side_C)
        else:
            side_C = int(side_C)
        triangle = Triangle(side_A, side_B, side_C)
        break
    except ValueError as e:
        print("Необходимо ввести числа")
    except TriangleExistError as e:
        print(e)
print(triangle.area())
print(triangle.perimetr())


