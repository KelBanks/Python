# Student grades
student_scores = {
    "Billy": 83,
    "Debbie": 79,
    "John": 98,
    "Shani": 72,
    "Pastora": 60,
    
}

student_grades = {}

for student in student_scores:
    scores = student_scores[student]
    if scores > 90:
        student_grades[student] = "Outstanding"
    elif scores > 80:
        student_grades[student] = "Exceeds expectations"
    elif scores > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)
