def isWordGuessed(secretWord,lettersGuessed):
    for x in secretWord:   
      if x in lettersGuessed:
          return True
      else:
          return False
      