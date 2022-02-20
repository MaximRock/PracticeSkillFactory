import random


def quick_sort(lst):
    if len(lst) > 1:  # определяем что наш список имеет больше одного элемента
        elem = lst[random.randint(0, len(lst) - 1)]  # случайное определение первого и последнего элемента списка
        # разбиваем наш список на левый середина правый
        left = [i for i in lst if i < elem]  # левый проходим по списку переменная i меньше нашего элемента
        center = [i for i in lst if i == elem]  # центр проходим по списку переменная i равна нашему элементу
        right = [i for i in lst if i > elem]  # правый проходим по списку переменная i больше нашего элемента
        lst = quick_sort(left) + center + quick_sort(right)  # склеиваем список

    return lst  # вызываем функцию quick_sort

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)



a = input('Введите последовательность чисел: ')

# проверяем корректный ввод в список
while True:
    try:
        a_lst = list(map(int, a.split())) # если True выходим из цикла
        break
    except ValueError: # если False выводим сообщение и просим повторный ввод
        print('Введите только целое число!!!')
        a = input('Введите последовательность чисел повторно: ')

element = input('Введите одно число: ')

# проверяем корректный ввод в элемент для добавления в список
while True:
    try:
        element = int(element) # если True выходим из цикла
        break
    except ValueError: # если False выводим сообщение и просим повторный ввод
        print('Введите только целое число!!!')
        element = input('Введите число повторно: ')

# проверяем наличие элемента в списке
if element in a_lst:
    print(a_lst)
else:
    a_lst.append(element)

print(a_lst)

# сортируем по алгоритму
sort_a = quick_sort(a_lst)
print(*sort_a)

# ищем позицию элемента в отсортированом списке
if element >= max(sort_a):
    print('Введенное число является максимальным среди чисел последовательности')
    print('Индекс числа:', binary_search(sort_a, element, 0, len(sort_a)))
elif element <= min(sort_a):
    print('Введенное число является минимальное среди чисел последовательности')
    print('Индекс числа:', binary_search(sort_a, element, 0, len(sort_a)))
elif element in sort_a:
    print('Индекс соседнего элемента:', binary_search(sort_a, element, 0, len(sort_a)) - 1)
    print('Индекс введеного элемента:', binary_search(sort_a, element, 0, len(sort_a)))
