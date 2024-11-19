def binary_search(list, key):
    lower = 0
    upper = len(list) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if list[mid] == key:
            return mid
        else:
            if list[mid] < key:
                lower = mid+1
            else:
                upper = mid-1
    return False

list = list(range(1,11))
print(list)
key = int(input("Enter a number to find : "))
result = binary_search(list,key)
if result == False:
    print("specified Number Not Found!!\n")
else:
    print(f"Key/Number found at Position {result+1}")