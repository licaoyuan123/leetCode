#Two methods of partition
def QuickSort(arr, left, right):
	if left<right:
		#p = PartitionLast(arr, left, right)
		p = PartitionLast(arr, left, right)
		QuickSort(arr, left, p-1)
		QuickSort(arr, p+1, right)

def PartitionFirst(arr, left, right):
	p = left
	p_value = arr[p]
	while left<right:
		while left<len(arr) and arr[left]<=p_value:
			left+=1
		while arr[right]>p_value:
			right -=1
		if left<right:
			arr[left], arr[right] = arr[right], arr[left]
	arr[right], arr[p] = arr[p], arr[right]
	return left

def PartitionLast(arr, left, right):
	p = right
	while left<right:
		while arr[left]<arr[p]:
			left += 1
		while right>left and arr[right]>=arr[p]:
			right -= 1
		if left<right:
			arr[left], arr[right] = arr[right], arr[left]
	arr[left], arr[p] = arr[p], arr[left]
	return left

#a = [4,3 ,2,2,1]
# a = [2,2,2,2,2]
a = [1,2,3,4,5]
QuickSort(a, 0, len(a)-1)
print(a)
