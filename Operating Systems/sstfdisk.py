requests=[176, 79, 34, 60, 92, 11, 41, 114]
intial_p=50
totalhead=0
cur_p=intial_p
while requests:
    min_seek=99999
    next=None
    for r in requests:
        seek_t=abs(r-cur_p)
        if seek_t< min_seek:
            min_seek=seek_t
            next=r
    totalhead+=min_seek
    cur_p=next
    requests.remove(next)
    print(next,end=",")
print()
print('total head movement',totalhead)