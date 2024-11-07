gradelst = []
studentGrade = 1

while studentGrade < 6:
    gradesinpt = float(input(f"Enter Grade {studentGrade}: "))
    
    if 40 <= gradesinpt <= 100: 
            gradelst.append(gradesinpt) 
            studentGrade += 1
    else:
        print("Invalid input.")

gradeavrg = sum(gradelst) / len(gradelst)

passing = 0
for gradesinpt in gradelst:
    if gradesinpt >= 75:
        passing += 1
        
passingPercent = (passing / len(gradelst)) * 100

print(f"Grades: " , gradelst)
print(f"Grade Average: " , gradeavrg)
print(f"Passed Grade: " , passing)
print(f"Percentage: " , passingPercent)
        