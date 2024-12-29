student = {
    "name":"rameen",
    "age":20,
    "grade":"A"
}
# print(f"My name is: {student['name']}")
# print(f"My age is: {student['age']}")
# print(f"Your grade is: {student['grade']}")
student["university"]="Comsats"
# print (student)
student["grade"]="A+"
print(student)
student["city"]="abu dhabi"
print(student)
student['name']="bro"
print(student)
student['extra']='new entry'
print(student)
del(student["name"])
print(student)
city=student.pop("city")
print(city)
print(student)
# for key in student.keys():
#     print(key,":",student[key])
# for value in student.values():
#     print(student[value])
for key,value in student.items():
    print(f"{key}:{value}")
