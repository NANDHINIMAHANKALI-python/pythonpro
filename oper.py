from faker import Faker
from random import randint

fake=Faker()

employees = [fake.name() for _ in range(1,21)]
employees =['Shannon Nguyen', 'Nancy Gonzalez', 'Jessica Davis', 'Ashley Lawrence',
'Lauren Miranda', 'Barbara Holmes', 'Stacie Fernandez', 'Craig Wagner', 'Gary Little', 'Joseph Doyle', 'Catherine Johnson',
'David Hicks', 'Stephanie Barajas', 'Andrew Goodwin', 'Amy Holmes', 'Jose Richardson', 'Jennifer Moses', 'Debra Williams', 
'Joshua Park', 'Angela Taylor']

print(employees)
print(len(employees))


sal_list = [randint(10000,70000)for _ in range(1,21)]
print(sal_list)
value = 50000

for employee in employees:
    for i in range(len(sal_list)):
         if sal_list[i] < value:
             print(f"employee:{employees[i]},  salary:{sal_list[i]},   is below 50000:True")
         elif sal_list[i] > value:
             print(f"employee:{employees[i]},  salary:{sal_list[i]},  is above 50000:False")
         else:
             if sal_list[i] ==50000:
                 print(f"employee:{employees[i]},  salary:{sal_list[i]},  ia equal to 50000:False")

     