"""
Word Occurrences
Estimate: 15 minutes
Actual: 20 minutes
"""

word_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    count = word_count.get(word, 0)
    word_count[word] = count + 1
words = list(word_count.keys())
words.sort()

length = max((len(word) for word in words))
for word in words:
    print(f"{word:{length}} : {word_count[word]}")