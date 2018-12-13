class TopGrader:
    topName = ""
    topGrade = 0

    def calc_grade(self, name):
        # current name grade
        grade = 0
        nameList = list(name)
        for letter in nameList:
            grade += ord(letter)
        # check if this new name has higher
        # grade then the global top grade
        if grade > self.topGrade:
            self.topName = name
            self.topGrade = grade

    def read_line(self, line):
        name = line.strip()
        self.calc_grade(name)

    def read_file(self, file_name):
        with open(file_name, "r", encoding="utf-8") as dataFile:
            for line in dataFile:
                self.read_line(line)

    def printTopGrader(self):
        print("{} -> {}".format(self.topName, self.topGrade))


def main():
    topGrader = TopGrader()
    topGrader.read_file("names.txt")
    topGrader.printTopGrader()


main()