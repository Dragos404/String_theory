def is_panagram(sentence):
    alp='abcdefghijklmnopqrstuvwxyz'  
    for letter in alp:   
        sentence = input("input here: ")      
        if letter in sentence.lower(): 
            print(True)           
    print(False)  

is_panagram(sentence='a')