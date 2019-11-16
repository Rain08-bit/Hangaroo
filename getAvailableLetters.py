def getAvailableLetters (lettersGuessed):
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    a = ""
    for x in Alphabet:
        if x not in lettersGuessed:
            a += x
    return a