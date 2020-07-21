def selectionSort(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                min = j
        a[i],a[min] = a[min],a[i]

print('Selection Sorting by directly giving inputs.')
arr = [54,69,85,48,52]
selectionSort(arr)
for i in range(len(arr)):
    print(arr[i])

print('Selection Sorting by taking input from user.')
n = int(input('Enter the number of elements: '))
arr2=[]
print('Enter the elements: ')
for i in range(0,n):
    ele = int(input())
    arr2.append(ele)
selectionSort(arr2)
print('sorted elements: ')
for i in range(len(arr2)):
    print(arr2[i])