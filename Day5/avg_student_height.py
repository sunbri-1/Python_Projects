
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])



number_of_students = 0
sum_heights = student_heights[0] + student_heights[1] + student_heights[2] + student_heights[3] + student_heights[4]

for n in student_heights:
  number_of_students += 1
avg_height = sum_heights/number_of_students
print(round(avg_height))
