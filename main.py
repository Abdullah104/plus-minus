#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def plusMinus(arr):
#     # Write your code here
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     plusMinus(arr)


if __name__ == '__main__':
    length = int(input().strip())
    positives = 0
    negatives = 0
    zeros = 0
    numbers = list(map(int, input().split()))

    for number in numbers:
        if number > 0:
            positives += 1
        elif number < 0:
            negatives += 1
        elif number == 0:
            zeros += 1

    positivesRatio = positives / length
    negativesRatio = negatives / length
    zerosRatio = zeros / length

    print(positivesRatio)
    print(negativesRatio)
    print(zerosRatio)
