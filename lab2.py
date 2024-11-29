import math


class Calculator:
    def __init__(self):
        """Ініціалізація калькулятора з пам'яттю та історією обчислень."""
        self.memory = None
        self.history = []

    def get_input(self):
        """Отримання чисел і оператора від користувача."""
        try:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            num2 = None
            if operator != '√':
                num2 = float(input("Введіть друге число: "))
            return num1, operator, num2
        except ValueError:
            print("Помилка: введено некоректне значення.")
            return self.get_input()

    def valid_operator(self, operator):
        """Перевірка, чи є оператор дійсним."""
        return operator in ['+', '-', '*', '/', '^', '√', '%']
#Поліморфізм
    def calculate(self, num1, operator, num2):
        """Виконання обчислень на основі введених даних."""
        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль неможливе.")
                result = num1 / num2
            elif operator == '^':
                result = num1 ** num2
            elif operator == '√':
                if num1 < 0:
                    raise ValueError("Корінь із від'ємного числа неможливий.")
                result = math.sqrt(num1)
            elif operator == '%':
                result = num1 % num2
            else:
                raise ValueError("Невідомий оператор.")

            # Збереження результату в пам'ять та додавання в історію
            self.memory = result
            self.history.append(f"{num1} {operator} {num2 if num2 is not None else ''} = {result}")
            return result
        except ZeroDivisionError as e:
            print(f"Помилка: {e}")
            return None
        except ValueError as e:
            print(f"Помилка: {e}")
            return None

    def run(self):
        """Основний цикл роботи калькулятора."""
        while True:
            num1, operator, num2 = self.get_input()

            if not self.valid_operator(operator):
                print("Невірний оператор. Спробуйте ще раз.")
                continue

            result = self.calculate(num1, operator, num2)
            if result is not None:
                print(f"Результат: {result}")

            # Перевірка, чи хоче користувач продовжити
            next_step = input("Бажаєте продовжити обчислення? (так/ні): ").strip().lower()
            if next_step != 'так':
                # Перегляд історії обчислень
                view_history = input("Бажаєте переглянути історію обчислень? (так/ні): ").strip().lower()
                if view_history == 'так':
                    print("\nІсторія обчислень:")
                    for record in self.history:
                        print(record)
                break


# Створення екземпляра класу і запуск програми
calculator = Calculator()
calculator.run()