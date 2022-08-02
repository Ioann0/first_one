def anagrams(word, words):
    my_words = []
    for i in range(len(words)):
        if sorted(word) == sorted(words[i]):
            my_words.append(words[i])
    return my_words


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
