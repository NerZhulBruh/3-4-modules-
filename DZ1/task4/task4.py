with open('input.txt', 'r') as f:
    words = f.read().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
word_counts_list = list(word_counts.items())
word_counts_list.sort(key=lambda tup: tup[1], reverse=True)
with open('output.txt', 'w') as f:
    for i in range(10):
        word, count = word_counts_list[i]
        f.write(f'{word},{count}\n')