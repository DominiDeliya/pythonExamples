# count the number pairs in a given array
ar = 1 ,1 ,3 ,2 ,1 ,3 ,3 ,3 ,3

ar = list(map(int, ar))
ar.sort()
count = 0
i = 0
while i < len(ar)-1:
    current_x = ar[i]
    next_x = ar[i+1]
    if current_x == next_x:
        count = count + 1
        i = i+2
    else:
        i = i+1


print(count)
