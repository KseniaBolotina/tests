import pytest

from main import check_age
from main import quadratic_equation
from main import check_email


@pytest.mark.parametrize(
    'age, expected',
    (
        [10, 'Доступ запрещён'],
        [20, 'Доступ разрешён']
    )
)
def test_check_age(age, expected):
    assert check_age(age) == expected

@pytest.mark.parametrize(
    'a, b, c, expected',
    (
        [1, 8, 15, (-3.0, -5.0)],
        [-4, 28, -49, 3.5],
        [1, 1, 1, 'корней нет']
    )
)
def test_quadratic_equation(a, b, c, expected):
    assert quadratic_equation(a, b, c) == expected

@pytest.mark.parametrize(
    'email, expected',
    (
        ['Helloworld@.ru', True],
        ['мояпочта@нетология.ру', True],
        ['python@email@net', False],
        [' em@il.ru', False]
    )
)
def test_check_email(email, expected):
    assert check_email(email) == expected