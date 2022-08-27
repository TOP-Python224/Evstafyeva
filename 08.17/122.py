# Упражнение 122. «Поросячья латынь»

word = input('Введите слово: ')
vocalic = ['a', 'e', 'i', 'o', 'u']
if word[0] in vocalic:
    print (word + 'way')
    
elif word[1] in vocalic:
    pig_latin = word[1:] + word[0] + "ay"
    print(pig_latin)
    
elif word[2] in vocalic:           
    pig_latin = word[2:] + word[0] + word[1] + "ay"
    print(pig_latin)
    
elif word[3] in vocalic:           
    pig_latin = word[3:] + word[0] + word[1] + word[2] + "ay"
    print(pig_latin)    
    
# office -> officeway
# computer -> omputercay
# think -> inkthay
# string -> ingstray