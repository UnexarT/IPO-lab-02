def eratos(num):
    a = [i for i in range(num + 1)]
    a[1] = 0
    i = 2
    while i <= num:
        if a[i] != 0:
            j = i + i
            while j <= num:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    print(a)
