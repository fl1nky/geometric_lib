# Geometric lib

## Общее описание

Библиотека вычисляет площади и периметры: прямоугольника, круга, квадрата, и треугольника

На вход - параметры типа `int` или `float`

П - число Пи

Исходный проект: [smartiqaorg/geometric_lib](https://github.com/smartiqaorg/geometric_lib)

## Описание функций

### circle.py (Круг)

circle.area(r) вычисляет площадь S = Пr**2
Параметр r - радиус, `int` или `float`
Возвращает площадь типа `float`

circle.perimeter(r) вычисляет длину окружности P = 2Пr
Параметр r - радиус, `int` или `float`
Возвращает длину типа `float`

```python
import circle

print(circle.area(3))       # 28.274333882308138
print(circle.perimeter(3))  # 18.84955592153876
```

### rectangle.py (Прямоугольник)

rectangle.area(a, b) вычисляет площадь S = ab
Параметры a, b - две стороны, `int` или `float`
Возвращает площадь: `int` или `float`

rectangle.perimeter(a, b) вычисляет периметр P = 2(a + b)
Параметры a, b - две стороны, `int` или `float`
Ожидаемый результат по формуле: `int` или `float`
В исходной версии пропущено умножение на 2, поэтому функция возвращает a + b

```python
import rectangle

print(rectangle.area(4, 3))       # 12
print(rectangle.perimeter(4, 3))  # Получено 7, должно быть 14
```

### square.py (Квадрат)

square.area(a) вычисляет площадь S = a**2
Параметр a - сторона, `int` или `float`
Возвращает площадь: `int` или `float`

square.perimeter(a) вычисляет периметр P = 4a
Параметр a - сторона, `int` или `float`
Возвращает периметр: `int` или `float`

```python
import square

print(square.area(4))       # 16
print(square.perimeter(4))  # 16
```

### triangle.py (Треугольник)

triangle.area(a, h) вычисляет площадь S = ah / 2
Параметр a - основание, h - высота;
оба параметра - `int` или `float`. Возвращает площадь типа `float`

triangle.perimeter(a, b, c) вычисляет периметр P = a + b + c
Параметры a, b, c - три стороны, `int` или `float`
Возвращает периметр: `int` или `float`

```python
import triangle

print(triangle.area(4, 3))           # 6.0
print(triangle.perimeter(3, 4, 5))   # 12
```

## История изменений

- `8ba9aeb` - Add circle and square
- `d078c8d` - Add documentation
- `5c9418c` - add rectangle.py
- `239bf96` - add triangle.py
- `976ccc3` - Добавлены 1.txt и 2.txt
- `98d1b49` - Update README and function docstrings
- [ЛР4](https://github.com/fl1nky/geometric_lib/commit/main) - Добавлены 24 теста, README и отчёт ЛР4

## Тестирование

В `test_figures.py` четыре класса, по одному на фигуру
Они наследуют `unittest.TestCase`, а методы начинаются с `test_`

У каждой функции три проверки: положительные, нулевые и дробные значения
Всего 24 теста с правильными ожидаемыми ответами
Вручную проверены 8 примеров, по одному на каждую функцию
Это выбранный набор для ручной проверки, число примеров в задании не задано
Ответы для сравнения посчитаны заранее по формулам
`assertEqual` сравнивает точно, `assertAlmostEqual` сравнивает дроби с `places=7`

Запуск из папки проекта

```console
python -m unittest test_figures.py
```

Итог: запущено 24, успешно 22, FAIL 2
