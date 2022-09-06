# Упражнение 143. Анаграммы
word = list(input('Enter the first word: '))
anagram = list(input('Enter the second word: '))
d1 = dict(zip(word, anagram))
d2 = dict(zip(anagram, word))
if d1.keys() == d2.keys():
    print(f"Entered words are anagrams")
else: 
    print(f"Entered words aren't anagrams")