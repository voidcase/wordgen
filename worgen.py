from random import randint

vowels = ["a","i","e","o","u","y"]
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
length = randint(1,7);
word = ""
for i in range(0,length):
    word = word + consonants[randint(0,len(consonants)-1)]
    word = word + vowels[randint(0,len(vowels)-1)]
print word
