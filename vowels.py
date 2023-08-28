def vowel_count(input_string):
    vowels = ['a','e','i','o','u']
    count_vowels = 0

    for char in input_string:
        if char in vowels:
              count_vowels += 1

    return count_vowels


input_string = input("Enter a string value: ")

num_vowels = vowel_count(input_string)

print("Number of vowels:", num_vowels)






    



