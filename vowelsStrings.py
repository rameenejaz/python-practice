sentence=str(input("Enter a sentence to find the vowels in it: "))
vowels="aeiou"
countVowel=0
vowel_list=[]
character_list=[]
characterCount=0
for char in sentence.lower():
    character_list.append(char)
    characterCount+=1
    if char in vowels:
        countVowel+=1
        vowel_list.append(char)
print(f"The sentence contains {countVowel} vowels, the vowels are: {vowel_list}")
print(f"The characters are: {character_list}")
print(f"There are {characterCount-1} characters")