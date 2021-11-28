#find all numbers divisible by 7 and not multiple of 5. within range(2000, 3000). resulting numbers
#string one line and separated by commas
j = []
for i in range(2000, 3201):
	if(i % 7 == 0 and i % 5 != 0):
		j.append(str(i))
print(', '.join(j));