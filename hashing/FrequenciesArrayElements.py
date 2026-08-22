def count(arr):
    d = {}
    l = []
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for key , value in d.items():
        l.append([key,value])
a = list(map(int, input("Enter numbers: ").split()))
count(a)
