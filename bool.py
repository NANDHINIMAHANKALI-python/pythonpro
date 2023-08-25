from faker import Faker
from random import randint

def print_employees_below_value(sal_list,value):

 fake = Faker()
 employees = [fake.name() for _ in range(1,21)]
 #employee_list =[fake.name() for _ in range(1,21)]
employees =['Shannon Nguyen', 'Nancy Gonzalez', 'Jessica Davis', 'Ashley Lawrence',
'Lauren Miranda', 'Barbara Holmes', 'Stacie Fernandez', 'Craig Wagner', 'Gary Little', 'Joseph Doyle', 'Catherine Johnson',
'David Hicks', 'Stephanie Barajas', 'Andrew Goodwin', 'Amy Holmes', 'Jose Richardson', 'Jennifer Moses', 'Debra Williams', 
'Joshua Park', 'Angela Taylor']

print(employees)
print(len(employees))
  
 

sal_list = [randint(10000,70000)for _ in range(1,21)]
print(sal_list)
value = 50000
#result =0
for i in range(len(sal_list)):

    if sal_list[i]< value:
    
        print(f"Name:{employees[i]},  salary:{sal_list[i]} " )
    else:
       print(f"Names:{employees[i]},   salary:{sal_list[i]} ")


for i in range(len(employees)):
     if sal_list[i]< value:
         print(employees[i],sal_list[i],True)
     else:
         print(employees[i],sal_list[i],False)
#MEMBERSHIP OPERATER
for employee in employees:
   if 'richardson' in employees:
      print(True)
   else:
      print(False)

#IDENTITY OPERATOR
for i in range(len(sal_list)):
     if sal_list[i]==50000:
         print(f"employee:{employees[i]},  salary:{sal_list[i]},  ia equal to 50000:True")
     else:
          print(f"employee:{employees[i]},  salary:{sal_list[i]},  ia not equal to 50000:False")

     
    




   



