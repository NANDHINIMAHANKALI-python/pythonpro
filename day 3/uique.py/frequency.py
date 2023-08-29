
from collections import Counter

def frequency_counter(sentence, words):
    sentence_words = sentence.lower().split()
    word_counter = Counter(sentence_words)
    word_frequency = {word: word_counter[word] for word in words}
    return word_frequency

sentence = input("Enter a sentence: ")
word_list = input("Enter words separated by spaces: ").split()
frequency_result = frequency_counter(sentence, word_list)
print("Word frequency:", frequency_result)




