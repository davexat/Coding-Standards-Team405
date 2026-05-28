class student:
    def __init__(self, id, name):
        if len(id) == 0:
            print("Received empty ID value")
            return
        
        if len(name) == 0:
            print("Received empty name")
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
           print("Error: grade value is out of range (0–100).")
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
            self.is_honored = True

    def delete_grade_by_index(self, index):
        if index >= len(self.grades) or index < 0:
            return
        
        del self.grades[index]

    def delete_grade_by_value(self, value):
        if value not in self.grades:
            return
        
        self.grades.remove(value)

    def report(self):
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print(f"Grades Count: + {len(self.grades)}")
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.add_grade(100)
    a.add_grade("Fifty")
    a.calc_average()
    a.check_honor()
    a.delete_grade_by_index(5)
    a.report()


startrun()
