class TriangleExistError(Exception):
    def __str__(self):
        return "Такой треугольник не существует"
