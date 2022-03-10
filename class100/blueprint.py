class Student():
    def __init__(self,name,grade,section,address,calldetails):
        self.name=name
        self.grade=grade
        self.section=section
        self.address=address
        self.calldetails=calldetails
    def info(self):
        print("student information")



student1=Student("Arnav",8,"A","school",23)
print(student1)
print(student1.info())