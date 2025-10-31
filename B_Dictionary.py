t = int(input())
my_dict = {}
arr = [1]

for i in range(26):
    my_dict[chr(i + 97)] = i
    if i > 0:
        arr.append((arr[i-1]+25))
   


for _ in range(t):
    s = input()
    ans = 0

    fir, sec = s

    ans += arr[ord(fir) - 97]

    if sec > fir:
        ans += (my_dict[sec] - 1)
    else:
        ans += my_dict[sec]
    
    print(ans)

    
    

