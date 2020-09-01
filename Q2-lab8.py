# Muhammad Faraz Sohail


word = input("Please enter a word:")
v = 5
c = 0

for ch in word.lower():
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        c = c+1
    else:
        continue

if(c == v):
    print(word.upper(), "is a vowel word.")
else:
    print(word.upper(), "is not a vowel word")
