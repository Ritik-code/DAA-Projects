def insertionSort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key

print('Insertion Sorting by directly giving inputs.')
arr=[85,96,78,52,45,21]
insertionSort(arr)
for i in range(len(arr)):
    print(arr[i])   

print('Insertion Sorting by taking inputs from user.')
arr2=[]
n=int(input('Input the size of array: '))
print('Enter the ',n,' elements.')
for i in range(0,n):
    ele = int(input())
    arr2.append(ele)
insertionSort(arr2)
print('Sorted Elements.')
for i in range(len(arr2)):
    print('%d'%arr2[i])