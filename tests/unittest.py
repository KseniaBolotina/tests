import unittest

from unittest import TestCase
from main import check_age
from main import quadratic_equation
from main import check_email

class TestFunction(TestCase):
    def test_check_age_with_params(self):
        for i, (age, expected) in enumerate([(10, 'Доступ запрещён'), (20, 'Доступ разрешён')]):
            with  self.subTest(i):
                 self.assertEqual(expected, check_age(age))


    def test_quadratic_equation_with_params(self):
        for i, (a, b, c, expected) in enumerate([
            (1, 8, 15, (-3.0, -5.0)),
            (-4, 28, -49, 3.5),
            (1, 1, 1, 'корней нет')
        ]):
            with self.subTest(i):
                self.assertEqual(quadratic_equation(a, b, c), expected)


    def test_check_email_with_params(self):
        for i, (email, expected) in enumerate([
            ('Helloworld@.ru', True),
            ('мояпочта@нетология.ру', True),
            ('python@email@net', False),
            (' em@il.ru', False)
        ]):
            with self.subTest(i):
                self.assertEqual(check_email(email), expected)