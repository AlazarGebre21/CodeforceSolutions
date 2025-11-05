t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = [0] + a
    b.append(0)
    ans = 0

    for i in range(n+1):
        if a[i] > b[i]:
            ans += (a[i] - b[i])
    
    print(ans)

    