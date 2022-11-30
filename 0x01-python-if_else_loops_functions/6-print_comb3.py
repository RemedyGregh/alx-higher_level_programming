#!/usr/bin/python3

for j in range(10):
    for i in range(j + 1, 10):
        print("{}".format(str(j) + str(i)), end=(',\
    ' if int(str(j) + str(i)) < 89 else '\n'))
