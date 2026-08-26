def UnionSortedArray(num1,num2):
    i,j = 0 , 0
    union = []
    while i < len(num1) and j < len(num2):
        if num1[i] <= num2[j]:
            if len(union)== 0 or union[-1] != num1[i]:
                union.append(num1[i])
            i+=1
        else:
            if len(union)== 0 or union[-1] != num2[j]:
                union.append(num2[j])
            j+=1
    while i < len(num1):
        if len(union)== 0 or union[-1] != num1[i]:
            union.append(num1[i])
        i+=1
    while j< len(num2):
        if len(union)== 0 or union[-1] != num2[j]:
            union.append(num2[j])
        j+=1
    return union
print(UnionSortedArray([1, 2, 3, 4, 5],[1, 2, 7]))
