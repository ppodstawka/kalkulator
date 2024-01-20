def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        return "Nie można dzielić przez zero"

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Zakończe program")

    choice = input("Wpisz numer operacji (1/2/3/4/5): ")

    if choice == '5':
        print("Zakończ program.")
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if choice == '1':
            print(num1, "+", num2, "=", dodawanie(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", odejmowanie(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mnozenie(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", dzielnie(num1, num2))

    else:
        print("Nieprawidłowy wybór. Wybierz numer od 1 do 5.")
