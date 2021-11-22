def MergeSort(arr):
	if len(arr)>1:
		mid = len(arr)//2
		L = MergeSort(arr[:mid])
		R = MergeSort(arr[mid:])
		i, j, k = 0, 0, 0
		while i<len(L) and j <len(R):
			if L[i]<=R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		while i<len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j<len(R):
			arr[k] = R[j]
			j+= 1
			k+=1
	#return arr

	return arr
a = [5,5,4,3,2,1]
b = [1,3,2,5,4]
MergeSort(a)

MergeSort(b)
print(a)
print(b)
