def count(arr):
    d = {0:0}
    l = []
    lar = 0
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        if d[i] > d[lar]:
            lar = i
        elif d[i]==d[lar]:
            if i<lar:lar = i
    print(lar)
a = list(map(int, input("Enter numbers: ").split()))
count(a)
