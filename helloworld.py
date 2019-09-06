print("This line will be printed.")
students = []
students.append("Bob")
students.append("Joee")
students.append("Tom")
first_name = students[0]
print(first_name)
first_name = first_name[:-1]
print(first_name)
longest_name = ''
for student in students:
    if len(student) > len(longest_name):
        longest_name = student
print (longest_name)
