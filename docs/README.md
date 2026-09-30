# Geometric lib

## Общее описание

Библиотека вычисляет площади и периметры: прямоугольника, круга, квадрата, и треугольника. 

На вход - параметры типа `int` или `float`.

П - число Пи.

## Описание функций

### circle.py (Круг)

circle.area(r) вычисляет площадь S = Пr2.
Параметр r - радиус, `int` или `float`. 
Возвращает площадь типа `float`.

circle.perimeter(r) вычисляет длину окружности P = 2Пr.
Параметр r - радиус, `int` или `float`. 
Возвращает длину типа `float`.

```python
import circle

print(circle.area(3))       # 28.27
print(circle.perimeter(3))  # 18.85
```

### rectangle.py (Прямоугольник)

rectangle.area(a, b) вычисляет площадь S = ab.
Параметры a, b - две стороны, `int` или `float`.
Возвращает площадь: `int` или `float`.

rectangle.perimeter(a, b) вычисляет периметр P = 2(a + b).
Параметры a, b - две стороны, `int` или `float`.
Возвращает периметр: `int` или `float`.

```python
import rectangle

print(rectangle.area(4, 3))       # 12
print(rectangle.perimeter(4, 3))  # 14
```

### square.py (Квадрат)

square.area(a) вычисляет площадь S = a².
Параметр a - сторона, `int` или `float`.
Возвращает площадь: `int` или `float`.

square.perimeter(a) вычисляет периметр P = 4a.
Параметр a - сторона, `int` или `float`.
Возвращает периметр: `int` или `float`.

```python
import square

print(square.area(4))       # 16
print(square.perimeter(4))  # 16
```

### triangle.py (Треугольник)

triangle.area(a, h) вычисляет площадь S = ah / 2.
Параметр a - основание, h - высота;
оба параметра - `int` или `float`. Возвращает площадь типа `float`.

triangle.perimeter(a, b, c) вычисляет периметр P = a + b + c.
Параметры a, b, c - три стороны, `int` или `float`.
Возвращает периметр: `int` или `float`.

```python
import triangle

print(triangle.area(4, 3))           # 6.0
print(triangle.perimeter(3, 4, 5))   # 12
```

## История изменений


- `8ba9aeb` - добавлены модули круга и квадрата.
- `d078c8d` - добавлена документация с формулами.
- `5c9418c` - добавлен модуль прямоугольника.
- `239bf96` - добавлен модуль треугольника.
