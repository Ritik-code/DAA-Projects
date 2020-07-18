def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

print('Sorting by directly giving inputs.')
arr = [54,69,85,48,52]
bubbleSort(arr)
for i in range(len(arr)):
    print(arr[i])

print('Sorting by taking input from user.')
n = int(input('Enter the number of elements: '))
arr2=[]
print('Enter the elements: ')
for i in range(0,n):
    ele = int(input())
    arr2.append(ele)
bubbleSort(arr2)
print('sorted elements: ')
for i in range(len(arr2)):
    print(arr2[i])    