# count items in an array which are divide by 3 or 5

arr = [2,3,5,10,6,15]
count_num = 0

for x in arr:
    if x % 3 == 0:
        count_num = count_num + 1
    elif x % 5 == 0:
        count_num = count_num + 1

print(count_num)
