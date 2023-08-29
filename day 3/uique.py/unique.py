def unique_elements(input_list):
    unique_elements = []
    for item in input_list:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements


input_list = [3, 5, 2, 5, 7, 3, 8]

unique_elements = unique_elements(input_list)
print("Unique elements:", unique_elements)