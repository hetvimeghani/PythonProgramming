#Hetvi Meghani - D21CE171
from logging import root

class student(object):
    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno

class exam(student):
    def __init__(self, name, rollno, marks):
        super().__init__(name, rollno)
        self.marks=marks

class result(exam):
    def __init__(self, name, rollno, marks):
        super().__init__(name,rollno,marks)
        self.result=marks
        self.total_marks=self.result/600*100
        self.percentage=self.total_marks

    def display(self):
        return self.percentage

s=result("Hetvi",171,500)
print(s.display())