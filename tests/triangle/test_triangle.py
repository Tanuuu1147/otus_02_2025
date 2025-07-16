import pytest
from src.triangle import Triangle
import math

# Проверка корректных значений сторон — площадь и периметр
@pytest.mark.parametrize(
    "side_a, side_b, side_c, expected_perimeter, expected_area",
    [
        (3, 4, 5, 12, 6),
        (6.0, 7.0, 8.0, 21.0, math.sqrt(10.5 * (10.5 - 6) * (10.5 - 7) * (10.5 - 8)))
    ],
    ids=["integer sides", "float sides"]
)
def test_triangle_properties(side_a, side_b, side_c, expected_perimeter, expected_area):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == expected_perimeter
    assert math.isclose(t.area, expected_area, rel_tol=1e-9)


# Проверка через фикстуру - площадь и периметр
@pytest.mark.parametrize("sides", ["integer", "float"])
def test_triangle_area_with_fixture(create_triangle, sides):
    side_a, side_b, side_c = create_triangle(sides)
    t = Triangle(side_a, side_b, side_c)
    s = (side_a + side_b + side_c) / 2
    expected_area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    assert math.isclose(t.area, expected_area, rel_tol=1e-9)

@pytest.mark.parametrize("sides", ["integer", "float"])
def test_triangle_perimeter_with_fixture(create_triangle, sides):
    side_a, side_b, side_c = create_triangle(sides)
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == side_a + side_b + side_c

# Проверка на некорректные значения сторон
@pytest.mark.parametrize(
    "sides",
    [
        (1, 2, 3),
        (1, 1, 3),
        (0, 4, 5),
        (-1, 4, 5)
    ],
    ids=["sum equals third", "sum less", "zero side", "negative side"]
)
def test_triangle_invalid_sides(sides):
    side_a, side_b, side_c = sides
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)

# проверка на неправильный тип аргумента
def test_triangle_add_area_with_invalid_type():
    t = Triangle(3, 4, 5)
    with pytest.raises(ValueError):
        t.add_area('triangle')

