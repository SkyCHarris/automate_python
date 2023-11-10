
#! A Short Program: Pig Latin

# Pig Latin is a silly made-up language that alters English words
# If a word begins with a vowel, the word yay is added to the end of it
# If a word begins with a consonant or consonant cluster (ch, gr), that consonant or cluster is moved to the end of the word followed by ay

# Output:

# Enter the English message to translate into Pig Latin:
# My name is Al Sweigart and I am 4,000 years old
# Ymay amenay isyay AlYAY EIGARTSWAY aandyay Iyay amyay 4,000 yearsyay oldyay.

# This program works by altering a string using the methods introduced in this chapter


# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []   # A list of the words in Pig latin
for word in message.split():
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1] + suffixNonLetters
        word = word[:1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # make the word lowercase for translation

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letter back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))


# 1. First, ask the user to enter the English text to translate into Pig Latin
# 2. Create a constant that holds every lowercase vowel letter (and y) as a tuple of strings
# 3. Create the pigLatin variable to store the words as we translate them into Pig Latin
# 4. Each word should be its own string, so message.split() gets a list of words as separate strings
# 5. The string is split() at each whitespace by default
# 6. Remove any non-letters from the start and end of each word
    # 6.a. Save non-letters to a variable named prefixNonletters
# 7. A loop that calls isalpha() on the first character in the word will determine if we should remove a character from a word and concatenate it to the end of prefixNonLetters
    # 7.a. If the entire word is made of non-letter characters, we can append it to the pigLatin list and continue to the next word to translate
    # 7.b. Need to also save the non-letters at the end of the word string
# 8. Make sure the program remembers if the word was in upper-case or title case so we can restore it after translating the word
# 9. To convert a word with Pig Latin suffix, need to remove all the consonants from the beginning of word:
# 10. Use a loop similar to the loop that removed non-letters from the start of word, but now pulling off consonants and storing them to a variable named prefixConsonants
# 11. Consonants at the start of the word are now in prefixConsonants, let's concatenate that variable and the string 'ay' to the end of word
    # 11.a. Otherwise we can assume the word begins with a vowel and we only need to concatenate 'yay'
# 12. We set the word to its lowercase version with word = word.lower()
    # 12.a. If word was originally uppercase or title case, this code converts it back to its original case
# 13. At end of for loop, append the word, along with any non-letter prefix or suffix, to the pigLatin list
# 14. After loop finishes, combine list of strings into a single string with the join() method
# 15. Pass single string to print()