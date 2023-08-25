def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

input_value = input("Enter a sentence: ")
reversed_value = reverse_sentence(input_value)
print("after Reversed the sentence:", reversed_value)