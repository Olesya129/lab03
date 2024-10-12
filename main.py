def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Проходим по списку от начала до конца
        for j in range(0, n-i-1):
            # Если элемент больше следующего, меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Запрашиваем количество чисел
n = int(input("Введите количество чисел: "))

# Вводим числа и добавляем их в список
numbers = []
for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)

# Сортируем список с помощью пузырьковой сортировки
bubble_sort(numbers)

# Выводим отсортированный список
print("Отсортированные числа:", numbers)
