#murloc language
#vowels will turn to mrgl letter
#example dog = d mrgl g

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + " MRGL " #uses a for loop to loop through the letters in the user string input
            else:
                translation = translation + " mrgl " #and uses if statements to determine what capitilization to use for string based on vowel is capitalized or not
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))