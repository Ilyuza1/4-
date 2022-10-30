def delete(list_, i=None):
    # TODO реализовать функцию удаления элемента из списка по индексу
    list_1 = []
    list_2 = []
    if i == None:
        i = len(list_)
        list_1 = list_[0:i - 1]
    else:
        list_1 = list_[0:i]
        list_2 = list_[i + 1:]
    return list_1 + list_2


print(delete([0, 0, 1, 2], i=0))
print(delete([0, 1, 1, 2, 3], i=1))
print(delete([0, 1, 2, 3, 4, 4]))