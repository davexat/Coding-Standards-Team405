class student:
    def __init__(self, id, name):
        if len(id) == 0:
            print("Error: Received empty ID value")
            return
        
        if len(name) == 0:
            print("Error: Received empty name")
            return
        
        self.id = id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.is_honored = False
        self.letter = ""

    def add_grade(self, grade):
        max_grade = 100
        min_grade = 0

        if grade >= min_grade and grade <= max_grade:
            print("Error: grade value is out of range")
            return
        
        self.grades.append(grade)

    def calc_average(self):
        total = 0
        for x in self.grades:
            total += x
        avg = total / len(self.grades)

        if avg >= 90:
            self.letter = "A"
        elif avg >= 80:
            self.letter = "B"
        elif avg >= 70:
            self.letter = "C"
        elif avg >= 60:
            self.letter = "D"
        else:
            self.letter = "F"

        return avg

    def check_honor(self):
        if self.calc_average() > 90:
            self.is_honored = True

    def delete_grade_by_index(self, index):
        if index >= len(self.grades) or index < 0:
            print("Error: grade index is out of range")
            return
        
        del self.grades[index]

    def delete_grade_by_value(self, value):
        if value not in self.grades:
            print("Error: grade value does not exists")
            return
        
        self.grades.remove(value)

    def report(self):
        print("Student ID: " + self.id)
        print("Student Name: " + self.name)
        print(f"Grades Count: + {len(self.grades)}")
        print("Letter Grade: " + self.letter)
        print("Is Passed:", self.is_passed)
        print("Is Honored:", self.is_honored)


def startrun():
    a = student("x", "")
    a.add_grade(100)
    a.add_grade("Fifty")
    a.calc_average()
    a.check_honor()
    a.delete_grade_by_index(5)
    a.report()


startrun()
