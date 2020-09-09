def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]  
        R = arr[mid:]  
  
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
  

print('Merge Sorting by directly giving inputs.')
arr = [54,69,85,48,52]
mergeSort(arr)
for i in range(len(arr)):
    print(arr[i])

print('Merge Sorting by taking input from user.')
n = int(input('Enter the number of elements: '))
arr2=[]
print('Enter the elements: ')
for i in range(0,n):
    ele = int(input())
    arr2.append(ele)
mergeSort(arr2)
print('sorted elements: ')
for i in range(len(arr2)):
    print(arr2[i])