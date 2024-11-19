def selection_sort(list):
    for i in range(0, len(list)-1):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j

        list[i], list[min] = list[min], list[i]
    return list

list = selection_sort([5,3,8,6,7,2])
print(list)