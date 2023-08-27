# English dictionary with PyDictionary package

# pip install PyDictionary ## install this package first

# This code is a program that translates a word into its definition.
# It uses the PyDictionary package to look up the word in the dictionary.
# The package returns the word's definition as a list of strings.
# The code prints the list of strings.

from PyDictionary import PyDictionary

# This program translates a word into a definition.
# It uses the PyDictionary library to do so.

from PyDictionary import PyDictionary

def message_format(message):
    # This function makes the output look better by
    # formatting the message so that it is easier to read.
    message = str(message.values()).replace("dict_values(", "- ").replace("[", "").replace("]", "").replace("'", "").replace(",", "\n-")
    message = message[:-1]
    
    print(message)

def translate(word):
    # This function translates the word into a definition.
    # If the word cannot be found, it will say so.
    dictionary = PyDictionary()
    result = dictionary.meaning(word)
    if result is not None:
        message_format(result)
    else:
        print("Sorry, the word could not be found.")

def main():
    # This function runs the entire program.
    # It gets the word from the user and then calls
    # the function to translate the word.
    word = input("Enter a word: ")
    result = translate(word)

main()