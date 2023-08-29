import string
import docx

def word_counter(text):
    word_freq = {}

    # Remove punctuation and split into words
    words = text.translate(str.maketrans("", "", string.punctuation)).lower().split()

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

filename = r"C:\Users\nandh\Documents\chintu.docx"  # Change this to the actual file path

# Load the Word document
doc = docx.Document(filename)
doc_text = ""

# Extract text from paragraphs
for paragraph in doc.paragraphs:
    doc_text += paragraph.text + " "

word_frequency = word_counter(doc_text)
print("Word frequency:", word_frequency)
