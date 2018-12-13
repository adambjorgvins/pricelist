def check_grade(grades):
  sum_of_grades = 0
  for num in grades:
    sum_of_grades += float(num)

  if sum_of_grades / len(grades) < 5:
      return False
  else:
      return True

def read_line(line):
    name_grade = line.strip().split(" ")
    name = name_grade[0]
    grades = name_grade[1:]
    if check_grade(grades):
      print("{} PASSED".format(name))
    else:
      print("{} FAILED".format(name))

def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as dataFile:
      for line in dataFile:
        read_line(line)

def main():
    read_file("grades.txt")

main()

