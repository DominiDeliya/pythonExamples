n = 5
arr = 2, 3, 6, 6, 5

arr2 = list(map(int, arr))
arr2.sort()
arr2.reverse()
print(arr2)
last_element = arr2[0]

for x in arr2:
    if x < last_element:
        break
print(x)
