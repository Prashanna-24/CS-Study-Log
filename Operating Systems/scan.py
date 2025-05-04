requests=[176, 79, 34, 60, 92, 11, 41, 114]
inh=50
less=[]
more=[]
for i in requests:
    if i>inh:
        more.append(i)
    if i<inh:
        less.append(i)
more.sort()
less.sort(reverse=True)
less.append(0)
print(less)
print(more)
tseek=inh-less[-1]+more[-1]-less[-1]
print("totalseektime",tseek)