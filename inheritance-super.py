# The super() function allows you to call methods of the parent class in a child class, 
# often used to extend the behaviour in the child class without completely replacing it

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, and I'm {self.age} years old."
    
class Employee(Person):
    def __init__(self,name, age, job_title):
        super().__init__(name,age)
        self.job_title = job_title

    def introduce(self):
        parent_introduction = super().introduce()
        return f"{parent_introduction} I work as a {self.job_title}."
    
employee = Employee("Sphinx", 40, "Programmer")

print(employee.introduce())