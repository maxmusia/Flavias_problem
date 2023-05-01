
n, k = int(input()), int(input())
l = []
for i in range(1, n+1):
    l+=[i]
while len(l) != 1:
    l+= l[:(k-1)]
    del(l[:(k)])
    print(*l)
