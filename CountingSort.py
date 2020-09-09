def counting_sort(arr, largest):
    c = [0]*(largest + 1)
    for i in range(len(arr)):
        c[arr[i]] = c[arr[i]] + 1
    c[0] = c[0] - 1 
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
    result = [None]*len(arr)
    for x in reversed(arr):
        result[c[x]] = x
        c[x] = c[x] - 1
    return result


print('Counting Sort by directly giving inputs.')
arr = [54,69,85,48,52]
k=max(arr)
sorted_list = counting_sort(arr,k)
for i in range(len(sorted_list)):
    print(sorted_list[i])

print('Counting Sort by taking input from user.')
n = int(input('Enter the number of elements: '))
arr2=[]
print('Enter the elements: ')
for i in range(0,n):
    ele = int(input())
    arr2.append(ele)
k=max(arr)
sorted_list2 = counting_sort(arr2,k)
print('sorted elements: ')
for i in range(len(sorted_list2)):
    print(sorted_list2[i])    