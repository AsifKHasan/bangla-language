# -*- coding: utf-8 -*-

import ujson
import nltk
import string
import numpy as np


def unique_words(songs_list):
    gan = []
    other = []
    curated_word = []
    with open(songs_list) as songs:
        data = ujson.load(songs)
        for song in data:
            gan.extend(song[u"কথা"])

    for words in gan:
        word = nltk.word_tokenize(words)
        other.extend(word)
    for sorted_word in sorted(other):
        line = sorted_word.translate(sorted_word.maketrans('', '', string.punctuation))
        curated_word.append(line.strip(string.punctuation))
    unique_curated_words = np.unique(curated_word).tolist()
    with open("curated_word.txt", "w+")as word_file:
        word_file.write(str(unique_curated_words))
    print("Word Count:", len(unique_curated_words))



unique_words("songs-data.json")






