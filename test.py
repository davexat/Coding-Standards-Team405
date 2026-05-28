class student:
    def __init__(self, id, name):
        if len(id) == 0:
            return
        
        if len(name) == 0:
            return
        
        self.id = id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grade(self, grade):
        max_grade = 100
        min_grade = 0
        if grade >= min_grade and grade <= max_grade:
            return
        
        self.grades.append(grade)

    def calc_average(self):
        total = 0
        for x in self.grades:
            total += x
        avg = total / len(self.grades)
        return avg

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print(f"Grades Count: + {len(self.grades)}")
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.add_grade(100)
    a.add_grade("Fifty")  # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
