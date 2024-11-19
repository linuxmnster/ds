def linear_search(list, key):
	for i in range(len(list)):
		if list[i] == key:
			return i
	return -1

arr = [3, 7, 2, 9, 5]
key = 9
result = linear_search(arr, key)

if result == -1:
	print(f"key {key} not found in {arr}")
else:
	print(f"key {key} found at {result+1} position") 