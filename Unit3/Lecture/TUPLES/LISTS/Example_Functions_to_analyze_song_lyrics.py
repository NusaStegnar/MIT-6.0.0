# create a frequency dictionary mapping str:int
# find word that occurs the most and how many times
    # use a list, in case there is more than one word
    # return a tuple (list,int) for (words_list, highest_freq)
# find the words that occur at least X times
    # let user choose “at least X times”, so allow as parameterS
    # return a list of tuples, each tuple is a (list, int) 
    # containing the list of words ordered by their frequency
# IDEA: From song dictionary, find most frequent word. 
# Delete most common word. Repeat. 
# It works because you are mutating the song dictionary.

def lyrics_to_frequencies(lyrics):
    my_dictionary = {}
    for word in lyrics:
        if word in my_dictionary:
            my_dictionary[word] += 1
        else:
            my_dictionary[word] = 1
    return my_dictionary

nina = ["Redki", "ljudje", "so", "še", "takšni", "kot", "ti",
"vsem", "se", "neskončno", "mudi",
"Ti", "me", "poslušaš", "v", "tišini", "začutiš", "stvari",
"ki", "jih", "srce", "govori",
"Če", "po", "naključju", "se", "nama", "zgodi",
"da", "pot", "med", "nama", "se", "razdeli",
"če", "me", "nemir", "prevzame",
"vem", "da", "na", "dosegu", "rok", "boš", "zame",
"le", "ti", "ti", "takšen", "si",
"Ker", "brez", "besed", "boš", "povedal", "da", "imaš", "me", "rad",
"in", "brez", "besed", "boš", "priznal", "s", "pogledom", "takrat",
"da", "sva", "v", "redu", "in", "vse", "dobro", "bo",
"da", "boš", "ujel", "mi", "modro", "nebo",
"Ljudje", "ki", "čutijo", "kot", "ti",
"imajo", "nekaj", "kar", "v", "drugih", "več", "ni",
"tople", "oči",
"Kdo", "še", "v", "teh", "časih", "besedo", "drži",
"upanje", "v", "drugem", "budi",
"A", "jaz", "naslonim", "se", "nate", "zaupam", "stvari",
"ki", "jih", "razumeš", "le", "ti"
"Če", "po", "naključju", "se", "nama", "zgodi",
"da", "pot", "med", "nama", "se", "razdeli",
"če", "me", "nemir", "prevzame",
"vem", "da", "na", "dosegu", "rok", "boš", "zame",
"le", "ti", "ti", "takšen", "si",
"Ker", "brez", "besed", "boš", "povedal", "da", "imaš", "me", "rad",
"in", "brez", "besed", "boš", "priznal", "s", "pogledom", "takrat",
"da", "sva", "v", "redu", "in", "vse", "dobro", "bo",
"da", "boš", "ujel", "mi", "modro", "nebo",
"Ljudje", "ki", "čutijo", "kot", "ti",
"imajo", "nekaj", "kar", "v", "drugih", "več", "ni",
"tople", "oči",
"Človek", "človeku", "bližina", "se", "zdi",
"če", "mu", "ob", "strani", "stoji",
"in", "ne", "glede", "kaj", "med", "nama", "se", "kdaj", "zgodi",
"vem", "da", "ob", "meni", "boš", "ti"
]

puslar = lyrics_to_frequencies(nina)
print(puslar)

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return(words, best)

(words, best) = most_common_words(puslar)
print(words)
# ["da"]
print(best)
# 11

def words_often(freqs, min_times):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= min_times:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(words_often(puslar, 5))
# [(['da'], 11), (['boš'], 9), (['ti', 'se'], 8), (['v'], 7), (['me', 'nama', 'in'], 5)]