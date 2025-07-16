from src.rectangle import Rectangle
import pytest

# Проверка площади через фикстуру
@pytest.mark.smoke
@pytest.mark.parametrize(
    'sides', ['integer', 'float'])
def test_rectangle_area_positive(create_rectangle, sides):
    side_a, side_b = create_rectangle(sides=sides)
    r = Rectangle(side_a, side_b)
    assert r.area == side_a*side_b

# Проверка периметра через фикстуру
@pytest.mark.smoke
@pytest.mark.parametrize(
    'sides', ['integer', 'float']
)
def test_rectangle_perimeter_positive(create_rectangle, sides):
    side_a, side_b = create_rectangle(sides=sides)
    r = Rectangle(side_a, side_b)
    assert r.perimeter == 2 * (side_a + side_b)


# Проверка на некорректные значения сторон
@pytest.mark.parametrize(
    'sides',
    [
        (0, 3),
        (3, 0),
        (-1, 2),
        (2, -1),
        (0, 0),
        (-2, -5),
    ],
    ids=[
        "zero side a", "zero side b",
        "negative a", "negative b",
        "both zero", "both negative"
    ]
)

def test_rectangle_invalid_sides(sides):
    side_a, side_b = sides
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


# Тест с большим значением стороны
def test_rectangle_large_sides():
    r = Rectangle(10000, 50000)
    assert r.area == 500_000_000
    assert r.perimeter == 2 * (10000 + 50000)



# проверка на неправильный тип аргумента
def test_add_area_with_invalid_type():
    r = Rectangle(1, 1)
    with pytest.raises(ValueError):
        r.add_area("rectangle")