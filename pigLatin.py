# pigLatin.py
#
# Convert words into different sounding, similar looking words
#
# Muhammad Nauman
# UIN: 927008027
# Oct 8 2018
# ENGR 102-213
#
# Lab 7b - 1

# Pre-processor
pig_latin = ''
sentence = input("Input a sentence whose words you wanna convert to pig latin (words will be separated by spaces. "
                 "Please do not input more than one space at a time as it will cause an error): ")
words = sentence.strip(' .,\"\':;-_`~/').split(' ')

# Processor
for word in words:
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y':
        word += "yay"
        pig_latin += word + ' '
    else:
        word = word[1:] + word[0] + "ay"
        pig_latin += word + ' '

# Post-processor
print(pig_latin)
