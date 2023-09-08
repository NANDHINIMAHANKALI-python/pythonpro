def find_word_in_file(filename, word):
    line_numbers = []
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if word in line:
                line_numbers.append(line_number)
    
    if line_numbers:
        return f'Word "{word}" found in the following lines: {line_numbers}'
    else:
        return f'Word "{word}" not found in the file.'

filename = r"C:\Users\nandh\Desktop\CHINTU.txt"
word_to_find = "Python"
result = find_word_in_file(filename, word_to_find)
print(result)
