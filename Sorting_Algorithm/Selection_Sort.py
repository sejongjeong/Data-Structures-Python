import random
from collections import deque
arr = deque(range(0, 1000, random.randint(1, 31)))
random.shuffle(arr)
print(f"Original Input Array = {arr}")

def selection_sort(arr):
	len_arr = len(arr)
	for i in range(0, len_arr-1):
		min = i
		for j in range(i, len_arr):
			if arr[min] > arr[j]:
				min = j
		arr[i], arr[min] = arr[min], arr[i]
	return arr

print(f"After Selection Sorting : {selection_sort(arr)}")