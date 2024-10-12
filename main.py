def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        # Проходим по списку от начала до конца
        for j in range(0, n-i-1):
            # В зависимости от направления сравниваем и меняем местами
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Запрашиваем количество чисел
n = int(input("Введите количество чисел: "))

# Вводим числа и добавляем их в список
numbers = []
for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)

# Запрашиваем направление сортировки
direction = input("Введите направление сортировки (возрастание/убывание): ").lower()

# Определяем, сортировать по возрастанию или по убыванию
if direction == "возрастание":
    ascending = True
elif direction == "убывание":
    ascending = False
else:
    print("Неверное направление сортировки, выбрано сортировать по возрастанию.")
    ascending = True

# Сортируем список
bubble_sort(numbers, ascending)

# Выводим отсортированный список
print("Отсортированные числа:", numbers)
