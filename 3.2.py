import random

# пустой список
lst = []

# Заполнения
for _ in range(10):
    lst.append(random.randint(1, 100))

print("До перестановки:", lst)

# перенос
if len(lst) > 1:
    last = lst[-1]       # ласт элемепнт 
    lst.pop()            # удаляет элемент
    lst.insert(0, last)  # вставляет в начало элемент

print("Після перестановки:", lst)


