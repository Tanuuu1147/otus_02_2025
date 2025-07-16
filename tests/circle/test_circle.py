import pytest
import math
from src.circle import Circle

# Проверка корректных значений радиуса — площадь и периметр
@pytest.mark.parametrize(
    "radius, expected_area, expected_perimeter",
    [
        (3, math.pi * 3 ** 2, 2 * math.pi * 3),              # integer
        (2.5, math.pi * 2.5 ** 2, 2 * math.pi * 2.5),        # float radius
    ],
    ids=["integer radius", "float radius"]
)
def test_circle_properties(radius, expected_area, expected_perimeter):
    c = Circle(radius)
    assert math.isclose(c.area, expected_area, rel_tol=1e-9)
    assert math.isclose(c.perimeter, expected_perimeter, rel_tol=1e-9)

# Проверка площади через фикстуру
@pytest.mark.parametrize("sides", ["integer", "float"])
def test_circle_area(create_circle, sides):
    radius = create_circle(sides)
    c = Circle(radius)
    assert math.isclose(c.area, math.pi * radius ** 2, rel_tol=1e-9)


# Проверка периметра через фикстуру
@pytest.mark.parametrize("sides", ["integer", "float"])
def test_circle_perimeter(create_circle, sides):
    radius = create_circle(sides)
    c = Circle(radius)
    assert math.isclose(c.perimeter, 2 * math.pi * radius, rel_tol=1e-9)

# Проверка на некорректные значения радиуса
@pytest.mark.smoke
@pytest.mark.parametrize(
    "radius",
    [0, -1, -2.5],
    ids=["zero radius", "negative integer", "negative float"]
)
def test_circle_invalid_radius(radius):
    with pytest.raises(ValueError):
        Circle(radius)


# проверка на неправильный тип аргумента
def test_circle_add_area_with_invalid_type():
    c = Circle(2)
    with pytest.raises(ValueError):
        c.add_area('circle')