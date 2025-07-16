import pytest

@pytest.fixture()
def create_rectangle():

    def _wrapper(sides: str):
        if sides == 'integer':
            return 3, 5
        elif sides == 'float':
            return 3.5, 5.5
        else:
            raise ValueError(f'sides must be integer or float')
    return _wrapper


@pytest.fixture()
def create_square():
    def _wrapper(sides: str):
        if sides == 'integer':
            return 4
        elif sides == 'float':
            return 2.5
        else:
            raise ValueError(f'sides must be integer or float')

    return _wrapper

@pytest.fixture()
def create_circle():
    def _wrapper(sides: str):
        if sides == 'integer':
            return 3
        elif sides == 'float':
            return 2.5
        else:
            raise ValueError(f'sides must be integer or float')
    return _wrapper

@pytest.fixture()
def create_triangle():
    def _wrapper(sides: str):
        if sides == 'integer':
            return 3, 4, 5
        elif sides == 'float':
            return 5.5, 6.5, 7.5
        else:
            raise ValueError(f'sides must be integer or float')
    return _wrapper