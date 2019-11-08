def bubbleSort(arr,n):
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
arr =[]
n = int(input("Enter number of elements"))
for k in range(n):
    arr.append(n)
 
bubbleSort(arr,len(arr))
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]) 
