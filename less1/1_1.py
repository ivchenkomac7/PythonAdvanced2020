# Создать список из N элементов (от 0 до n с шагом 1). В этом списке
# вывести все четные значения.

x = []
for i in range(1, 100):
    if i % 2 == 0:
        x.append(i)
print(x)
