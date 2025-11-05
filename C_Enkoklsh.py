from math import ceil

t = int(input())

for _ in range(t):
    k = int(input())

    a = list(map(int, input().split()))
    d = sum(a)

    f_one = 0

    for i in range(len(a)):

        if a[i] == 1:
            f_one = i
    

    no_weeks = ceil(k/d)

    no_days = no_weeks * d
    

    for i in range(len(a)-1,-1,-1):
        if a[i] == 0:
            no_days -= 1
            continue
        else:
            no_days -= a[i]
            if no_days >= k:
                continue
            else:
                break
    
    print(no_days - (f_one - 0))
            
