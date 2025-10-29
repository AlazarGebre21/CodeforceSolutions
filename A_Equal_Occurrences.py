t = int(input())

for _ in range(t):
    n =  int(input())

    a = list(map(int, input().split()))

   

    my_dict = {}

    for num in a:
        my_dict[num] = my_dict.get(num, 0) + 1
    
    my_dict = dict(sorted(my_dict.items(), key= lambda item: item[1]))

    
    ans = 0

    length = len(my_dict)

    

    for value in my_dict.values():
        if length >= 0:
            ans = max(ans, length*value)
            length -= 1
    

    print(ans)
    

            

    
    