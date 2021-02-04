n=int(input())
l = [int(i) for i in input().split()]
maximum=0
for i in l:
    c = l.count(i)
    m = l.count(i-1)
    c = c+m
    if c>maximum:
        c=maximum
print(maximum)
