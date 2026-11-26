# a Python program that counts how many times each word appears in a sentence
sentence = "failure is a steping stone of success"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Frequency:", freq)