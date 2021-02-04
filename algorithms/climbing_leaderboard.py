def climb(score,alice): 
    leaderboard=sorted(set(score),reverse=True)
    results=[]
    l=len(leaderboard)
    for i in alice:
        while (l>0 and i>=leaderboard[l-1]):
            l-=1
        results.append(l+1)
    return results

print(climb([100,100,50,40,40,20,10],[5,25,50,120]))

# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120