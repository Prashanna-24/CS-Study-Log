requests=[176, 79, 34, 60, 92, 11, 41, 114]
inhead=50
more=[]
less=[]
less.append(0)
for i in requests:
    if i>inhead:
        more.append(i)
    if i<inhead:
        less.append(i)
more.append(199)
more.sort()
less.sort()
print(more)
print(less)
headcount=more[-1]-inhead+more[-1]-less[0]+less[-1]-less[0]
print(headcount)
