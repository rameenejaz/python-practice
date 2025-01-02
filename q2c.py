# sentence=str(input("Enter a sentence to count characters: "))
# charList=[]
# char_count_dict={}
# for char in sentence.lower():
#     if char in char_count_dict:
#         # charList.append(char)
#         char_count_dict[char]+=1
#     else:
#         char_count_dict[char] = 1
# # print(f"There are {charCount} characters !")
# print("Character counts:", char_count_dict)
# print(f"There are {len(sentence)} characters in total!")

sentence=str(input("Enter a word or sentence to count char:"))
char_count_dict={}
for char in sentence.lower():
    if char in char_count_dict:
        char_count_dict[char]+=1
    else:
        char_count_dict[char]=1
print(f"Character counts: {char_count_dict} ")

