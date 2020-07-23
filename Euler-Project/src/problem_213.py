#
# Python program to solve Euler Problem #213
#
# Link: https://projecteuler.net/problem=213
#
# Notes:
#
# * 50 iterations is not enough to generate the desired precision (6 decimals)
# * calculation does not seem to be consistent even in the large numbers, depends on something?
#
#


# ---------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------
import os
import sys

import time
import random

import numpy as np

from Log import Log


# ---------------------------------------------------------------------------------------------------------
# defines
# ---------------------------------------------------------------------------------------------------------

APPLICATION_NAME = "213"

#NUMBER_OF_ITERATIONS = 50
NUMBER_OF_ITERATIONS = 1000


# ---------------------------------------------------------------------------------------------------------
# utilities
# ---------------------------------------------------------------------------------------------------------

class Stats(object):
    
    # constructor/initialize
    def __init__(self):
        self._values = [ ]
        
    def clear(self):
        self._values = [ ]
        
    def add(self, value):
        self._values.append(value)
        
    def getAverage(self):
        # compute average, could use numpy or else
        total = sum(self._values)
        count = len(self._values)
        average = float(total) / float(count)
        print "Stats.dump: getAverage: # values: {0} - sum: {1} - average: {2}".format(count, total, average)
        #npavg = np.average(self._values)
        #print "Stats.dump: getAverage: numpy - average: {0}".format(npavg)
        return average
    
    def dump(self):
        average = self.getAverage()
        print "Stats.dump: average: {0:.6f}".format(average)
    

class Grid(object):
    
    # default grid size
    GRID_SIZE = (30, 30)
    
    # constructor/initialize
    def __init__(self):
        self._grids = [ np.ones(Grid.GRID_SIZE, np.int) ] * 2
        self._index = 0     # initial source grid index
        self._gridS = self._grids[self._index]
        self._gridT = self._grids[1 - self._index]
        
    # swap internal buffers
    def _swap(self):
        self._index = 1 - self._index 
        self._gridS = self._grids[self._index]
        self._gridT = self._grids[1 - self._index]
        
    # initialize 
    def init(self):
        # nothing for now
        pass
    
    # print empty cell ratio
    def printEmptyCellsRatio(self):
        ratio = self._computeEmptyCellsRatio()
        Log.trace("ratio: {0}".format(ratio))
        
    # get empty cells value
    def getNumberOfEmptyCells(self):
        N = self._gridS.shape[0]
        M = self._gridS.shape[1]
        emptyCells = 0
        for row in range(0, N):
            for col in range(0, M):
                if (self._gridS[row, col] == 0):
                    emptyCells += 1
        return emptyCells

    # compute empty cell ratio
    def _computeEmptyCellsRatio(self):
        # get data size
        N = self._gridS.shape[0]
        M = self._gridS.shape[1]
        emptyCells = 0
        totalCells = N * M
        totalFleas = 0
        for row in range(0, N):
            for col in range(0, M):
                totalFleas += self._gridS[row, col]
                if (self._gridS[row, col] == 0):
                    emptyCells += 1
        emptyRatio = float(emptyCells) / float(totalCells)
        Log.trace("grid: ratio: {0}".format(emptyRatio))
        Log.trace("grid: fleas: {0}".format(totalFleas))
        return emptyRatio
        
    # ring bell on grid (see problem description)
    def bell(self):
        
        # get data size
        N = self._gridS.shape[0]
        M = self._gridS.shape[1]
        
#        Log.trace("grid: move: {0}x{1}".format(N, M))
        
        # loop on all cells and shuffle fleas around
        for oldRow in range(0, N):
            for oldCol in range(0, M):
                # for all fleas in cell
                numFleas = self._gridS[oldRow, oldCol]
                for flea in range(numFleas):
                    
                    # generate random move
                    deltaRow = random.randint(-1, 1)
                    deltaCol = random.randint(-1, 1)
                    
                    # clamp result (or wrap around?)
                    newRow = oldRow + deltaRow
                    newCol = oldCol + deltaCol
                    if (newRow < 0):
                        newRow = 0
                    if (newRow >= N):
                        newRow = N - 1
                    if (newCol < 0):
                        newCol = 0
                    if (newCol >= M):
                        newCol = M - 1
                    
                    # remove flea from origin
                    self._gridS[oldRow, oldCol] -= 1
                    
                    # add to destination
                    self._gridT[newRow, newCol] += 1
                    
        # swap grids
        self._swap()

    # dump data
    def dump(self):   
                         
        # print source grid
        print "gridS: "
        print self._gridS
        
        # print target grid
        print "gridT: "
        print self._gridT
        
        # print ratio
        print "ratio: "
        self.printEmptyCellsRatio()
        
        # wait a while
        time.sleep(0.5)
    
   

# ---------------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------------

def main():
    
    # set application name
    Log.setApplicationName(APPLICATION_NAME)
    
    # start
    Log.trace("starting...")

    # get grid
    grid = Grid()
    
    # get stats
    stats = Stats()
    
    # iterate
    for iter in range(NUMBER_OF_ITERATIONS):
        
        # print
        Log.trace("iteration: {0:03d}".format(iter))
        
        # ring bell on grid
        grid.bell()
        
        # get # of empty cells, add to stats data
        numEmptyCells = grid.getNumberOfEmptyCells() 
        stats.add(numEmptyCells)
        
        # dump
#        grid.dump()
    
    # done 
    Log.trace("stats:")
    stats.dump()

    # end
    Log.trace("done!")


# ---------------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
