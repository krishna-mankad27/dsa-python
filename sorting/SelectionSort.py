def SelectionSort(arr):
    for i in range(len(arr)-1):
        min = arr[i]
        for j in range(i,len(arr)):
            if arr[j] < min:
                min= arr[j]
                arr[j],arr[i]=arr[i],arr[j]
    return arr

a = [7 ,4 ,1 ,5 ,3]
a = SelectionSort(a)
print(a)
        

 