from student_class import No_Probation
#can create object of a class much like a normal variable

student1 = No_Probation("Tyler", "CPE", 3.6) #using the Student function, calls the init function from the imported file
student2 = No_Probation("Jordan", "CPE", 3.3) 



print(student1.on_honor_roll())
print(student2.on_honor_roll())