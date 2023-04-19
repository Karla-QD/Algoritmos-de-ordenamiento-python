def bubble(a):
    for limit in range (len(a), 0, -1):
        for i in range (limit -1):
            if a[i] > a[i + 1]:
                a[i], a[i+1] = a[i + 1], a[i]
    return a
    
a = [2, 3, 5, -6, -7]
print(bubble(a))