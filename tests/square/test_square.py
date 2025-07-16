import pytest
from src.square import Square

# Проверка корректных значений сторон — площадь и периметр
@pytest.mark.parametrize(
    "side, expected_area, expected_perimeter",
    [
        (4, 16, 16),              # integer
        (2.5, 6.25, 10.0),        # float
    ],
    ids=["integer side", "float side"]
)
def test_square_properties(side, expected_area, expected_perimeter):
    s = Square(side)
    assert s.area == expected_area
    assert s.perimeter == expected_perimeter

# Проверка площади и периметра через фикстуру
@pytest.mark.parametrize("sides", ["integer", "float"])
def test_square_area(create_square, sides):
    side = create_square(sides)
    s = Square(side)
    assert s.area == side * side

@pytest.mark.parametrize("sides", ["integer", "float"])
def test_square_perimeter(create_square, sides):
    side = create_square(sides)
    s = Square(side)
    assert s.perimeter == 4 * side


# Проверка на некорректные значения стороны
@pytest.mark.parametrize(
    "side",
    [0, -1, -2.5],
    ids=["zero side", "negative integer", "negative float"]
)
def test_square_invalid_side(side):
    with pytest.raises(ValueError):
        Square(side)



# проверка на неправильный тип аргумента
def test_square_add_area_with_invalid_type():
    s = Square(2)
    with pytest.raises(ValueError):
        s.add_area('circle')


# Тест с большим значением стороны
@pytest.mark.slow
def test_square_large_side():
    s = Square(100000)
    assert s.area == 100000 ** 2
    assert s.perimeter == 4 * 100000