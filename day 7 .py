n = int(input("Enter number of students in the class: "))

present_count = 0
absent_count = 0

for rollno in range(1, n + 1):
    status = input("Enter 1 or 2 \n1. Present \n2. Absent : ")

    # check status
    if status == '1':
        present_count += 1
    elif status == '2':
        absent_count += 1
    else:
        print("Please select either 1 or 2")

print("Total number of students:", n)
print("Total number of presentees:", present_count)
print("Total number of absentees:", absent_count)

percentage = (present_count / n) * 100
print("Attendance percentage:", percentage)
