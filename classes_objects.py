from student_class import Student #refers to the file and then the class

#can create object of a class much like a normal variable

student1 = Student("Tyler", "CPE", "3.6", False) #using the Student function, calls the init function from the imported file
student2 = Student("Jordan", "CPE", "3.3", True) 

print(student1.gpa)
print(student2.gpa)