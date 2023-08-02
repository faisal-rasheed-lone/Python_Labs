# program for checking special character
str = input("Enter string : ")
l = len(str)
i = 0
flag = 0
s_characters = """~`!@#$%^&*()_+=]}{["':;<>,.?/ :"""
while i < l:
    if str[i] in s_characters:
        flag = 1
        if str[i] == '#':
            print("hash sign ")
        elif str[i] == '%':
            print("percent sign ")
        elif str[i] == '@':
            print("at the rate sign  ")
        elif str[i] == '$':
            print("dollar sign ")
        else:
            print(" other signs ")
        break
    i += 1

if flag == 1:
    print("string contains special character ")
else:
    print("doesn't contain any special character ")

s_characters = """~`!@#$%^&*()_+=]}{["':;<>,.?/ :"""
s = input("enter string ")


