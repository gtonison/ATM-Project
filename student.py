class student:
   def __init__(self, name ,age , grade):
       self.name = name
       self.age = age
       self.grade = grade
       
def get_grade(self):
    return self.grade
class course:
       def __init__(self, name , max_student , student):
           self.name = name
           self.max = max_student
           self.student  = []
       def add_student(self, student,):
           if len(self.student) < self.max_student:
               self.student.append(student)
               return True
           return False
       def get_average_grade(self):
           for student in self.grade:
               value = value + student.get_grade()
s1 = student("bill" , 84,18)  
s2 = student("Goodluck", 97,67)
s3 = student("EMEKA", 98,78) 

course1 = course("science" 2)
course1.add_student(s1)
course1.add_student(s2)


              