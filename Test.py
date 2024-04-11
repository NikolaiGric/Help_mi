import unittest
from main import Circle, Triangle


class TestShapeCalculator(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        expected_area = 78.5398163397
        self.assertAlmostEqual(circle.get_area(), expected_area, delta=0.0001)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        expected_area = 6
        self.assertEqual(triangle.get_area(), expected_area)

    def test_is_right_triangle(self):
        right_triangle = Triangle(3, 4, 5)
        non_right_triangle = Triangle(3, 4, 6)

        self.assertTrue(right_triangle.is_right_triangle())
        self.assertFalse(non_right_triangle.is_right_triangle())


if __name__ == '__main__':
    unittest.main()
