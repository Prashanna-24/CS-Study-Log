requests=[176, 79, 34, 60, 92, 11, 41, 114]
inhead=50
less=[]
more=[]
for i in requests:
    if i>inhead:
        more.append(i)
    if i<inhead:
        less.append(i)
more.sort()
less.sort(reverse=True)
print(more)
print(less)
seek=more[-1]-inhead+more[-1]-less[-1]
print(seek)
