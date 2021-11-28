# input n (int)
#output: 1-> n {n : n * n}

x = int(input("Input: "))

y = dict();

for i in range(1, x + 1):
    y[i] = i * i

print(y)