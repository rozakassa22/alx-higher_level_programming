#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    i = chr(i)
    if i == 'q' or i == 'e':
        continue
    print("{}".format(i), end='')
