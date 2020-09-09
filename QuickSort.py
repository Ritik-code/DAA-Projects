def partition(arr,p,q): 
    i = ( p-1 )         
    x = arr[q]     
    for j in range(p , q):       
        if   arr[j] <= x: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[q] = arr[q],arr[i+1] 
    return ( i+1 ) 
  
def quickSort(arr,p,q): 
    if p < q:    
        pi = partition(arr,p,q) 
        quickSort(arr, p, pi-1) 
        quickSort(arr, pi+1, q) 


print('Quick Sorting by directly giving inputs.')
arr = [54,69,85,48,52]
n = len(arr)
quickSort(arr,0,n-1)
for i in range(len(arr)):
    print(arr[i])

print('Quick Sorting by taking input from user.')
n = int(input('Enter the number of elements: '))
arr2=[]
print('Enter the elements: ')
for i in range(0,n):
    ele = int(input())
    arr2.append(ele)
quickSort(arr2,0,n-1)
print('sorted elements: ')
for i in range(len(arr2)):
    print(arr2[i])