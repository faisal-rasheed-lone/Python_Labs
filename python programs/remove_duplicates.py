str = input(" Enter String : ")
x = 0
str1 = ''
j = 0
char_arr = []
for i in str:
    if i not in char_arr:
        for j in str:
            if i == j:
                x += 1

        char_arr.append(i)
        str1 = str1 + i;
print(str1)

