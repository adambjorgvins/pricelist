
def check_grade(grades:int):
    grade = []
    sum_of_grades = sum(grade)
    if sum_of_grades / len(grades) < 5:
        return False
    else:
        return True


def read_line(line):
    name_grade = line.strip().split(" ")
    name = name_grade[0]
    grade = name_grade[1:]
    pass_fail = check_grade(grade)
    if pass_fail:
        return name[True]
    else:
        return name[False]


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as dataFile:
        for line in dataFile:
            read_line(line)


def main():
    file = input("Enter file")
    read_file(file)



main()