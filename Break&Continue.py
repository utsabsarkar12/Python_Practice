# use of break method
students = ["utsab", "somu", "anindo", "shikto", "niloy", "tasnia"]

for student in students:
    if student == "niloy":
        break;
    print(student)

# use of continue method

for student in students:
    if student == "anindo":
        continue;
    print(student)