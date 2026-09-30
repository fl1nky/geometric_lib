import math

def area(r):
    """Вычисляет площадь круга по радиусу r.

    Параметр: r (int или float) - радиус.
    Возвращает: площадь круга (float), S = pi * r ** 2.

    Пример вызова:
    round(area(3), 2)
    28.27
    """
    return math.pi * r * r


def perimeter(r):
    """Вычисляет длину окружности по радиусу r.

    Параметр: r (int или float) - радиус.
    Возвращает: длина окружности (float), P = 2 * pi * r.

    Пример вызова:
    round(perimeter(3), 2)
    18.85
    """
    return 2 * math.pi * r

