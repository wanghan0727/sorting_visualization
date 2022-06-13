import random

def swap(nums, a, b):
	
	tmp = nums[a]
	nums[a] = nums[b]
	nums[b] = tmp


def bubble_sort(nums):
	
	if len(nums) == 1:
		return

	swapped = True
	n = len(nums)
	for i in range(n-1):
		if not swapped:
			break
		swapped = False
		for j in range(n-i-1):
			if nums[j] > nums[j+1]:
				swap(nums, j, j+1)
				swapped = True

			yield nums


def insertion_sort(nums):
	
	n = len(nums)
	for i in range(1, n):
		j = i
		while j > 0 and nums[j] < nums[j-1]:
			swap(nums, j, j-1)
			j -= 1
			yield nums




if __name__ == '__main__':

	nums = [1, 2, 3, 4, 5]
	random.shuffle(nums)
	print("unsorted: ", nums)

	generator = insertion_sort(nums)
	print("sorted: ", next(generator))

