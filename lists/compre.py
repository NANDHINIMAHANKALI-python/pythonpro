# take multiple inputs from user using split()
input_numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in input_numbers]
even_numbers = (num for num in numbers if num % 2 == 0)
print("Even numbers:", list(even_numbers))

