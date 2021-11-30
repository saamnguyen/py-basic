
netAmount = 0

while True:
    s = input('Giao dich: ')
    if not s:
        break
    values = s.split(' ')
    operation = values[0]
    amout = values[1]

    if operation == 'D':
        netAmount+=int(amout)
        print(netAmount)
    elif operation == 'W':
        netAmount-=int(amout)
        print(netAmount)
    else:
        pass

print(netAmount)