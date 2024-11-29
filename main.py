from Data.Lab1.Interfaces.calculator import calculator
from Data.Lab2.Interfaces.main import run_calculator
from Data.Lab3.Interfaces.main import main3
from Data.Lab4.Interfaces.main import main4
from Data.Lab5.Interfaces.menu import menu5
from Data.Lab6.UTest.Utest import main6
from Data.Lab7.Interfaces.menu import main7
from Data.Lab8.Interfaces.menu import main8

def show_menu():
    print("\nMenu:")
    print("1. Lab 1")
    print("2. Lab 2")
    print("3. Lab 3")
    print("4. Lab 4")
    print("5. Lab 5")
    print("6. Lab 6")
    print("7. Lab 7")
    print("8. Lab 8")
    print("0. Exit")

def main():
    while True:
          show_menu()
          choice = input("Enter your choice (0 to exit): ")
          if choice == '1':
               calculator()
          elif choice == '2':
               run_calculator()
          elif choice == '3':
               main3()
          elif choice == '4':
               main4()
          elif choice == '5':
               menu5()
          elif choice == '6':
               main6()
          elif choice == '7':
               main7()
          elif choice == '8':
               main8()
          elif choice == '0':
               print("Exiting the program.")
               break
          else:
               print("Invalid choice, please try again.")

main()