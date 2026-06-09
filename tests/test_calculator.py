import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from calculator import add, divide, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(6, 7), 42)

    def test_divide(self) -> None:
        self.assertEqual(divide(12, 3), 4)

    def test_divide_by_zero_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
