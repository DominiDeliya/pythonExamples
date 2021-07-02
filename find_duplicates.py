seq = [2,3,2,-1,5,3,-1,3]
seq.sort()
counter = 0

for x in range(0, len(seq)-1):

    if seq[x] == seq[x+1]:
        counter = counter + 1

print(counter)
