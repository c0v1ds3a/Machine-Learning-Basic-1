import random

# Set the number of words in the script
num_words = 10000

# Create a list of random words
words = []
for i in range(num_words):
    words.append(random.choice(['apple', 'banana', 'orange', 'pear', 'pineapple', 'strawberry', 'grape', 'watermelon', 'mango', 'peach']))

# Create a list of random phrases
phrases = []
for i in range(num_words):
    phrases.append(random.choice(['The quick brown fox', 'Jumped over the lazy dog', 'Ate the juicy fruit', 'Ran to the nearest store', 'Fell into a deep hole']))

# Create a list of random sentences
sentences = []
for i in range(num_words):
    sentences.append(random.choice(phrases) + ' ' + random.choice(words) + '.')

# Create a list of random paragraphs
paragraphs = []
for i in range(num_words):
    paragraph = ''
    for j in range(random.randint(1, 5)):
        paragraph += random.choice(sentences) + ' '
    paragraphs.append(paragraph)

# Print the script
print('Random script:')
for paragraph in paragraphs:
    print(paragraph)
