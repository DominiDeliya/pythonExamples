
seq = [2,3,2,-1,5,3,-1,3]
seq.sort()
counter = 0
seen = ''

for elm in seq:
    if elm == seen:
        counter += 1
    else:
        seen = elm

print(counter)
