
list_words = input("Enter a list of words: ").split()

counts = {}

for word in list_words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for word, count in counts.items():
    print(word, count)
