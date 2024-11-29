import unittest


class Calculator:
    """Простий калькулятор з основними операціями."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Ділення на нуль!")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Ініціалізація екземпляра калькулятора перед кожним тестом."""
        self.calc = Calculator()

    # Завдання 1: Тестування Додавання
    def test_addition(self):
        # Позитивні числа
        self.assertEqual(self.calc.add(2, 3), 5)
        # Від'ємні числа
        self.assertEqual(self.calc.add(-2, -3), -5)
        # Комбінація позитивного і негативного числа
        self.assertEqual(self.calc.add(-2, 3), 1)

    # Завдання 2: Тестування Віднімання
    def test_subtraction(self):
        # Позитивні числа
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Від'ємні числа
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        # Комбінація позитивного і негативного числа
        self.assertEqual(self.calc.subtract(3, -2), 5)

    # Завдання 3: Тестування Множення
    def test_multiplication(self):
        # Позитивні числа
        self.assertEqual(self.calc.multiply(3, 4), 12)
        # Від'ємні числа
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        # Множення на нуль
        self.assertEqual(self.calc.multiply(3, 0), 0)

    # Завдання 4: Тестування Ділення
    def test_division(self):
        # Позитивні числа
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Від'ємні числа
        self.assertEqual(self.calc.divide(-10, 2), -5)
        # Комбінація позитивного і негативного числа
        self.assertEqual(self.calc.divide(10, -2), -5)
        # Ділення на одиницю
        self.assertEqual(self.calc.divide(10, 1), 10)

    # Завдання 5: Тестування Обробки Помилок
    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertTrue("Ділення на нуль!" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
