from faker import Faker
from random import randint

fake=Faker()

def modify_list(names):
 names= [fake.name() for _ in range(1,21)]

 print(names)
 print(len(names))
names = ['Robert Lawrence', 'Erin Simmons', 'Eugene Fitzgerald', 'William Pruitt', 'Carl Smith', 'Kelly Morris', 'Amber Barnett',
              'David Burnett', 'Gary Williams', 'Heidi Mcdonald', 'Debra Navarro', 'Donna Joseph', 'Melinda Hanna', 'Jill Williams', 
              'Michael Norris', 'Jpessica Anderson', 'Andre Fitzgerald', 'Julie Wiggins', 'Sara Delgado', 'Julie Crawford']

numbers = [randint(10,70)for _ in range(1,21)]
print(numbers)

#INSERT-------------------------

"""num_tuple = (4, 5, 6)
 
# inserting a tuple to the list
numbers.insert(2, num_tuple)
 
print(numbers)

names.insert(4,'nandhu')
print(names)
numbers.insert(5,6)
print(numbers)
numbers.insert(4, 10)
print(numbers)

names.insert(-1, 'kavvi')
print(names)"""

def insert_element(numbers, index, element):
    numbers.insert(index, element)
    return numbers
numbers = insert_element(numbers, 2, 60)
print(numbers)


def insert_element(lst, index, element):
    lst.insert(index, element)


def insert_element(lst, index, element):
    if index < 0 or index > len(lst):
        print("Invalid index!")
    else:
        lst.insert(index, element)

    insert_element(numbers, -1, 60)
    print(numbers)

def insert_elements(lst, index, elements):
    for element in elements:
        lst.insert(index, element)
        index += 1

insert_elements(names, 2, ['naga','manu','swarna'])
print(names)


"""#Index------------------------------------------------

#Using index to find the position of a specific name
print(numbers.index(63))

index= names.index("Carl Smith")
    
print("madified list: ",names)
print("index of 'nani': ",index)
print(names.index("nandhu"))
try:
#except ValueError:

 print("Error:Name not found in the list")

except Exception as e:
  print("error:",str(e))"""

def find_element(lst, element):
    try:
        index = lst.index(element)
        return index
    except ValueError:
        print("Error:name not found in te list")

result = find_element(numbers, 14)
print(result)

def find_all_elements(lst, element):
    indices = []
    for i, value in enumerate(lst):
        if value == element:
            indices.append(i)
    return indices


result = find_all_elements(numbers, 5)
print(result)
# Clear---------------------------------------------------

"""names.clear()
print(names)

print("List1 before deleting is : " + str(numbers))
 
# Clearing list1 by assigning an empty list
numbers = []
print("List1 after clearing using an empty list : " + str(numbers))

# Clearing list using slicing
st = numbers[:0]
print(numbers) """

def list_empty(lst):
    return len(lst) == 0 
print(list_empty(numbers))

empty_list = []
print(list_empty(empty_list))
#clear list
def clear_list(lst):
    lst.clear()
clear_list(names)
print(names)



          
  












