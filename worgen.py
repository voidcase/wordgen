from random import randint, choice

vowels = ["a","i","e","o","u","y"]
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z","sh","ch","th","ps"]
nonstarters = ["ng","nk","lk","nt","ck","ll","tt"]
nonenders = ["gn","sv"]
starter_cons = consonants + nonenders
ender_cons = consonants + nonstarters
reg_cons = consonants + nonstarters + nonenders

length = randint(1,5);
word = ""
if choice([True,False]):
    word = word + vowels[randint(0,len(vowels)-1)]
for i in range(0,length):
    word = word + reg_cons[randint(0,len(consonants)-1)]
    word = word + vowels[randint(0,len(vowels)-1)]
if choice([True,False]):
    word = word + ender_cons[randint(0,len(consonants)-1)]
print word
