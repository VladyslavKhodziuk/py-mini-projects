def add (a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
        if b == 0:
            return "Деление на ноль"
        return a / b

print("Калькулятор")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Выбери операцию (1/2/3/4): ")

a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))

if choice == "1":
    print("Результат:", add(a, b))
elif choice == "2":
    print("Результат:",subtract(a, b))
elif choice == "3":
    print("Результат:",multiply(a, b))
elif choice == "4":
    print("Результат:",divide(a, b))
else:
    print("Неверный результат!")
