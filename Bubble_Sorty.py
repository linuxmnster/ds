def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

result = bubble_sort([64, 34, 25, 12, 22, 11, 90, 5])
print(result)