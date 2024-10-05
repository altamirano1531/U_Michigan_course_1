# import math
# import os
# import random
# import re
# import sys


def compareTriplets(x,y):

    z = list([0,0])
    ctr = 0
    
    for val in x:
        if val > y[ctr]: z[0] = z[0] + 1
        elif val < y[ctr]: z[1] = z[1] + 1
        ctr = ctr + 1

     #print('Value 1=', z[0], 'Value 2=', z[1])

    return z


if __name__ == '__main__':

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = list(map(int, input().rstrip().split()))

    y = list(map(int, input().rstrip().split()))

    result = compareTriplets(x, y)

    print(result)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()



