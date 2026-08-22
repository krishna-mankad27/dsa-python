def total(i,ttl):
    if i < 1:
        print(ttl)
        return 
    total(i-1,ttl+i)
    return

n = int(input("enter num: "))
t = 0
total(n,t)
print("Code ran succesfully")