from operator import itemgetter

lists = []

while True:
    s = input()
    if not s:
        break
    lists.append(tuple(s.split(',')))

print(sorted(lists, key=itemgetter(0, 1, 2)))