def word_count(sentence):
    words = sentence.split(' ')
    counts = {}

    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    return counts
sentence = "the cat sat on the mat the cat"
print(word_count(sentence))