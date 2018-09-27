
gradebook = []
lowest = 100.00
secondLowest = 100.00

for _ in range(int(input())):
    name = input()
    score = float(input())
    student = []
    student.append(name)
    student.append(score)
    gradebook.append(student)
    
    print('lowest: {0} secondLowest: {1}'.format(lowest, secondLowest))
    if score < lowest:
        secondLowest = lowest
        lowest = score
    elif score != lowest and score < secondLowest:
        secondLowest = score
        

gradebook.sort()

for (student, grade) in gradebook:
    if grade == secondLowest:
        print(student)
    
