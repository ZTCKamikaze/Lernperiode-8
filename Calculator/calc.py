def addieren(x, y):
    return x + y

def subtrahieren(x, y):
    return x - y

def multiplizieren(x, y):
    return x * y

def dividieren(x, y):
    return x / y

print("Wählen Sie eine Operation aus:")
print("Option 1: Addieren")
print("Option 2: Subtrahieren")
print("Option 3: Multiplizieren")
print("Option 4: Dividieren")


while True:
    choice = input("Geben Sie Ihre gewünschte Operation ein (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Geben Sie die erste Zahl ein: "))
            num2 = float(input("Geben Sie die zweite Zahl ein: "))
        except ValueError:
            print("Ungültige Eingabe, bitte geben Sie eine Nummer ein: ")

        if choice == '1':
            print(num1, "+", num2, "=", addieren(num1, num2))
    
        elif choice == '2':
            print(num1, "-", num2, "=", subtrahieren(num1, num2))
    
        elif choice == '3':
            print(num1, "*", num2, "=", multiplizieren(num1, num2))
    
        elif choice == '4':
            print(num1, "/", num2, "=", dividieren(num1, num2))

        next_calculation = input("Möchten Sie eine weitere Berechnung durchführen? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Ungültige Eingabe")

