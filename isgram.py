def is_isogram():
    word = input("Insert your isogram: ")
    if type(word) != str:
        raise TypeError('Argument should be a string')
    elif word == "":
      return (word, False)
    else:
        word = word.lower()
        for char in word:
            if word.count(char) > 1:
                print(word, False)
            else:
                print(word, True) 
is_isogram()