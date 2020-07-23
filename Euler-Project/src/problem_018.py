#
# Python program to solve Euler Problem #18
#
# Link: https://projecteuler.net/problem=18
#
#
#


# ---------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------
import os
import sys

import numpy as np

from Log import Log


# ---------------------------------------------------------------------------------------------------------
# defines
# ---------------------------------------------------------------------------------------------------------

APPLICATION_NAME = "018"
DATA_FILE_PATH = "../data/p018_triangle.txt" 


# ---------------------------------------------------------------------------------------------------------
# utilities
# ---------------------------------------------------------------------------------------------------------

def load(path):
    
    # size is hardcoded... sorry!    
    size = (15, 15)
    data = np.zeros(size, np.int)
    
    # open file
    file = open(path, 'r')
    
    # loop on lines/tokens
    for row, line in enumerate(file):
        tokens = line.split(' ')
        for col, token in enumerate(tokens):
            data[row, col] = int(token)

    # return array
    return data
    
    
def findMaxPath(data):
    
    # get data size
    N = data.shape[0]
    M = data.shape[1]
    
    Log.trace("data: size: {0}x{1}".format(N, M))
 
    # make copy of array
    accum = np.copy(data)
    
    # initialize max path to zero
    maxPath = 0

    # loop on all cells and propagate accumulated sum downwards
    for row in range(1, N):
        
        for col in range(0, M):
            
            # accumulate sum downwards
            if (col > 0):
                accum[row, col] += max(accum[row - 1, col - 1], accum[row - 1, col])
            else:
                accum[row, col] += accum[row - 1, col]
                
            maxPath = max(maxPath, accum[row, col])

    # print accum matrix
    print "accum: "
    print accum

    # return max value
    return maxPath
    

# ---------------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------------

def main():
    
    # set application name
    Log.setApplicationName(APPLICATION_NAME)

    # start
    Log.trace("starting...")

    # load data from file
    data = load(DATA_FILE_PATH)

    # print data matrix
    print "data: " 
    print data
   
    # find/print max path
    result = findMaxPath(data)
    Log.trace("max is: {0}".format(result))    
    
    # end
    Log.trace("done!")


# ---------------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
