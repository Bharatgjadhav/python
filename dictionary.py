students = [{'marks':20},
            {'marks':21},
            {'marks':20},
            {'marks':23}]

# return all students whose marks is greater than 20
students_filtered = {key:value for key,value for students.items() if value > 20}
print(students_filtered)