import sys

digit_string = int(sys.argv[1])

for i in range(digit_string):
    print(" "*(digit_string-i-1) + "#"*(i+1))
