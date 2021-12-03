import sys
students = sys.argv[1]
names = sys.argv[2]
namesList = names.split(",")

with open(students, "r") as f:
    lines = f.readlines()

studentList = []

for line in lines:
    name, properties = line.split(":")[0], line.split(":")[1]
    school, dep = properties.split(",")[0], properties.split(",")[1]
    if "\n" in dep:
        dep = dep[:-1]
    studentList.append([name,school,dep])

student_dict = {student[0]:[student[1],student[2]] for student in studentList}

for name in namesList:
    try:
        print("Name: {}, University: {},{} ".format(name, student_dict[name][0], student_dict[name][1]))
    except:
        print("No record of '{}' was found".format(name))
