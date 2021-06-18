def is_anagram(text1, text2):
    str1 = input('inputhereone : ')
    str2 = input('inputheretwo: ')
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)

print(is_anagram('Justin Timberlake', "I'm a jerk but listen"))

