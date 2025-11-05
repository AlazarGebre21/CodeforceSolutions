n, k = map(int, input().split())

a = list(map(int, input().split()))

if sum(a) % k == 0:
    minute = sum(a) // k
    i = 0
    j = 0
    ans = []
    flagNo = False

    while i < n:
        temp = 0
        while j < n:
            if temp == minute:
                break
            elif temp < minute:
                temp += a[j]
                j += 1
            elif temp > minute:
                flagNo = True
                break
        
        ans.append(j - i)
        i = j
    
    if flagNo:
        print("No")
    else:
        print("Yes")
        print(*ans)
       






else:
    print("No")
