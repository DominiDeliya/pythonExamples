# find the score of the runner-up(second maximum score)
n = 5
arr = 2, 3, 6, 6, 5

arr2 = list(map(int, arr))
arr2.sort(reverse=True)

last_element = arr2[0]

for x in arr2:
    if x < last_element:
        break

print(x)
