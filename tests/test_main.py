import unittest

from unittest import TestCase

from main import discriminant

class TestMain(TestCase):

    def test_discriminant(self):
        list_numbers = [1, 2, 3]
        result = discriminant(*list_numbers)
        expected = -8
        self.assertEqual(expected, result)

    def test_discriminant_wrong(self):
        a = 1
        b = 2
        c = 3
        # result = discriminant(*list_numbers)
        # expected = -15
        self.assertRaises(ValueError, discriminant, a, b, c)


