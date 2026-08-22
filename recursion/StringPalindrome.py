def Check(i,n):
    global a
    if i >= n/2:
        return True
    if a[i] != a[n-i-1]:
        return False
    return Check(i+1,n)





a = "astrirtsac"
print(Check(0,len(a)))