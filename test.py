# compare strings
def strings(s1,s2):
    s1=list(s1)
    s2=list(s2)
    count=0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count+=1
            s1[i]="_"
    if count>1:
        return -1
    else:
        return "".join(s1)
print(strings("0010","0110"))
