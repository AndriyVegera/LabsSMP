import pyfiglet
from termcolor import colored


class ASCIIArtGenerator:
    def __init__(self):
        self.text = ""
        self.font = "standard"
        self.color = "white"
        self.available_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        self.output = ""

    def get_user_input(self):
        """Отримання тексту від користувача."""
        self.text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")

    def choose_font(self):
        """Вибір шрифту користувачем."""
        fonts = pyfiglet.FigletFont.getFonts()
        print("\nДоступні шрифти:")
        print(", ".join(fonts[:10]), "...")  # Виведення перших 10 шрифтів для прикладу
        chosen_font = input("Введіть бажаний шрифт (за замовчуванням 'standard'): ").strip()
        if chosen_font in fonts:
            self.font = chosen_font
        else:
            print("Невідомий шрифт. Використовується стандартний шрифт.")

    def choose_color(self):
        """Вибір кольору тексту."""
        print("\nДоступні кольори:", ", ".join(self.available_colors))
        chosen_color = input("Введіть бажаний колір (за замовчуванням 'white'): ").strip()
        if chosen_color in self.available_colors:
            self.color = chosen_color
        else:
            print("Невідомий колір. Використовується білий колір.")

    def generate_ascii_art(self):
        """Генерація ASCII-арту."""
        try:
            figlet = pyfiglet.Figlet(font=self.font)
            self.output = figlet.renderText(self.text)
            print("\nПопередній перегляд:")
            print(colored(self.output, self.color))
        except Exception as e:
            print(f"Помилка при створенні ASCII-арту: {e}")

    def save_to_file(self):
        """Збереження ASCII-арту у файл."""
        file_name = input("Введіть ім'я файлу для збереження (наприклад, art.txt): ").strip()
        try:
            with open(file_name, 'w') as file:
                file.write(self.output)
            print(f"ASCII-арт збережено у файлі {file_name}")
        except Exception as e:
            print(f"Помилка при збереженні файлу: {e}")

    def run(self):
        """Основний цикл програми."""
        self.get_user_input()
        self.choose_font()
        self.choose_color()
        self.generate_ascii_art()

        # Питання про збереження
        save_option = input("Бажаєте зберегти результат у файл? (так/ні): ").strip().lower()
        if save_option == 'так':
            self.save_to_file()


# Запуск програми
if __name__ == "__main__":
    app = ASCIIArtGenerator()
    app.run()