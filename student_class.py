class Student:
    def __init__(self, name, major, gpa, is_on_probation): #in the init function it is defining what a student is
        self.name = name
        self.major = major #name of student object will be equal to the one we passed in
        self.gpa = gpa #the actual object gpa is going to be gpa passed in
        self.is_on_probation = is_on_probation #can use class inside classes_objects.py

        #self refers to actual object and stores attributes for object
        #can model any object and give it attributes
    
class No_Probation:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False