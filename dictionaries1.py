student = {
    "name":"rameen",
    "age":20,
    "grade":"A"
}

print("Hello world: ", student.items())
# for key in student.keys():
#     print(key,":",student[key])
# for value in student.values():
#     print(student[value])
for key, value in student.items():
    print(f"{key}:{value}")

