i#!/usr/bin/python3
for i in range(100):
    j = i / 10
    v = i % 10
    if i == 99:
        print("{}".format(i))
        continue
    print("{}{}, ".format(int(j), v), end='')
