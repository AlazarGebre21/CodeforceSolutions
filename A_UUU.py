from collections import defaultdict
n, k =  map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

my_dict = defaultdict(list)

for i in range(n):
    my_dict[a[i]].append(b[i])

arr = []
arr2 = []
for values in my_dict.values():
    values.sort(reverse=True)
    arr.append(values[1:])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr2.append(arr[i][j])

arr2.sort()

print(sum(arr2[:k-len(my_dict)]))


