students = [1,2,3,4]
score_list = [24,33,50,88]

for _ in range(int(input())):

    temp = []

    name = input()
    score = float(input())

    temp.append(name)
    temp.append(score)

    score_list.append(score)
    students.append(temp)

score_list = list(dict.fromkeys(score_list))
score_list.sort()

if len(students) >= 2:
    second_lowest_students = []
    second_lowest_score = score_list[1]

    for i in students:
        if second_lowest_score in i:
            # print(i[0])
            second_lowest_students.append(i[0])
        else:
            pass
    print('\n'.join(sorted(second_lowest_students, key=lambda second_lowest_students: second_lowest_students)))

else:
    print(students[0][0])