import random
from collections import deque
arr = deque(range(0, 1000, random.randint(1, 31)))
random.shuffle(arr)
print(f"Original Input Array = {arr}")

def insertion_sort(arr):
	len_arr = len(arr)
	for i in range(0, len_arr):
		for j in range(i, -1, -1):
			if arr[i] > arr[j-1]
		arr[i], arr[min] = arr[min], arr[i]
	return arr

print(f"After Insertion Sorting : {insertion_sort(arr)}")