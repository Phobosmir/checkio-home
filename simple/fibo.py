

# 0, 1, 2, 3, 5, 8

def get_fibo(n):
    v1, v2 = 0, 1
    for _ in range(n):
        v1, v2 = v2, v1+v2
    return  v1

def fibo_list(n):
    r = [0, 1]
    if n <= 2:
        return r[0:n]

    for _ in range(n-2):
        r.append(r[-2] + r[-1])

    return r

for i in range(10):
    print(fibo_list(i))
