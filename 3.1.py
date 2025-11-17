# Введення чисел
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

# Введення операції
operation = input("Введіть операцію (+, -, *, /): ")

# вычисление
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Помилка: ділення на нуль неможливе!")
        result = None
    else:
        result = num1 / num2
else:
    print("Невідома операція!")
    result = None

#  вывод результата
if result is not None:
    print("Результат:", result)
