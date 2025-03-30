def sum_of_lists (list1, list2):
    if len(list1) != len(list2):
        if len(list1) > len(list2):
            list2 += [0] * (len(list1) - len(list2))
        else:
            list1 += [0] * (len(list) - len(list1))
    return [x+y for x,y in zip(list1, list2)]


list1 = [int(i) for i in input(f"Введите через пробел числа первого списка: ").split()]
list2 = [int(i) for i in input(f"Введите через пробел числа второго списка: ").split()]

print(sum_of_lists(list1, list2))