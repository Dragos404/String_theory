def is_Palindrome(word):
    return word == word[::-1]
 
word = str(input("Insert your palindrome: "))
ans = is_Palindrome(word)
 
if ans:
    print("Yes")
else:
    print("No")
        

