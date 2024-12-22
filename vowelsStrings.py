sentence=str(input("Enter a sentence to find the vowels in it: "))
vowels="aeiou"
countVowel=0
for char in sentence.lower(): #for case sensitive
    if char in vowels:
        countVowel+=1
print(f"The sentence contains {countVowel} vowels")