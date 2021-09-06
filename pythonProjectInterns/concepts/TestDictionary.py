#key value pair in curly bracket
# dictionary are indexed by key
#dictionary are mutable

student = {101:"rajesh",102:"suraj",103:"tom"}

print(student[102])

for i,j in student.items():
    print(i," and value is ",j)


for i in student.keys():
    print(i)

for i in student.values():
    print(i)

student[105] = "Ram"

print(student)

student[102] = "Shyam"

print(student)