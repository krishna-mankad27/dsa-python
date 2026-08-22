def Rev(left,right):
    global a
    if left>=right:
        return
    a[left],a[right]=a[right],a[left]
    Rev(left+1,right-1)

a = [4,5,3,1,2]
Rev(0,len(a)-1)
print(a)
