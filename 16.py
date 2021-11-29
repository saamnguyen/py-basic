#Viết một chương trình chấp nhận đầu vào là một câu, 
# đếm số chữ cái và chữ số trong câu đó. Giả sử đầu vào sau được cấp cho chương trình: hello world! 123

#Thì đầu ra sẽ là:

#Số chữ cái là: 10
#Số chữ số là: 3

x = input("Input: ")
d = {"DIGITS":0, "LETTER":0}

for y in x:
    if y.isdigit():
        d["DIGITS"]+=1
    elif y.isalpha():
        d["LETTER"]+=1
    else:
        pass

print('Alpha: ', d["LETTER"])
print('Num: ',  d["DIGITS"])
