from collections import defaultdict
d = defaultdict(list)
list1 = []

n,m = map(int(input().split()))
for i in range(0,n):
    d[input()].append(i+1)
for j in range(0,m):
    list1+= [input()]

for k  in list1:
    if k in d:
        print(" ".join(map(str,d[k])))
    else:
        print(-1)