class Employee:
    name = "sardar"
    role = "Software Developer"
    salry = 20
    def info(self):
        print(f"{self.name} is a {self.role}")

a = Employee()
a.name = "uzair"
a.role = "Data Scientest"
a.salry = 50


b = Employee()
b.name = "usman"
b.role = "HR"
b.salry = 40


print(a.info())
print(b.info())
