def palindrome(word):
    
    word = word.lower()
    
    #using slicing :[start: end: step]
    reversed_word = word[::-1]
    
    if word == reversed_word:
        return True
    else:
        return False
    
input_name = input("Enter a name: ")

if palindrome(input_name):
    print("given name is a palindrome")
else:
    print("given name is not a palindrome")