input_string = input("Enter a value : ")
char_frequency = {}

for charecter in input_string:
    if charecter in char_frequency:
        char_frequency[charecter] += 1
    else:
        char_frequency[charecter] = 

print("the Character frequency of given value:", char_frequency)
