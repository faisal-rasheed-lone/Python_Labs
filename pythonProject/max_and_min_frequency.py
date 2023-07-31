str = input(" Enter String : ")
x = 0
char_arr = []
freq_arr = []
for i in str:
    if i not in char_arr:
        for j in str:
            if i == j:
                x += 1
        # print(i, " is ", x, "times")
        freq_arr.append(x)
        x = 0
        char_arr.append(i)

x = freq_arr.index(max(freq_arr))
print("MAX frequency is ", max(freq_arr), " and element is ", char_arr[x])

x1 = freq_arr.index(min(freq_arr))
print("MIN frequency is ", min(freq_arr), " and element is ", char_arr[x1])


from collections import Counter

string= "pppppppghhhijeuupffe"
print(string)

result= Counter(string)
print(result)
result= max(result, key=result.get)

print("Most frequent character: ",result)







