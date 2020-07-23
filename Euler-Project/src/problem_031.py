#
# Python program to solve Euler Problem #31
#
# Link: https://projecteuler.net/problem=31
#
#
#


# ---------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------
import os
import sys
import time
import operator

from Log import Log


# ---------------------------------------------------------------------------------------------------------
# defines
# ---------------------------------------------------------------------------------------------------------

APPLICATION_NAME = "031"
THRESHOLD_VALUE = 0.005

# ---------------------------------------------------------------------------------------------------------
# utilities
# ---------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------------

# global counters
# could be grouped in a class
debug = False
#debug = True
solutions = 0
permutations = 0

def calc(target, coins, combi, level):
	
	# recursive calculation
	global debug
	global solutions
	global permutations
	
	# dump args
	if (debug):
		print "calc: target: {0} - level: {1}".format(target, level)
		print "calc: coins: {0}".format(coins)
		print "calc: combi: {0}".format(combi)
		time.sleep(0.5)
		
	# stats
	if (level == 0):
		permutations += 1
	
	# calculate current amount
	amount = sum(map(operator.mul, coins, combi))
	
	# remain target
	remain = target - amount
#	print "calc: target: {0} - level: {1} - amount: {1} - remain: {1}".format(target, level, amount, remain)
	
	# check target
#	if (remain == 0.0) and (level == 0):
	if (abs(remain) <= THRESHOLD_VALUE) and (level == 0):
		# found solution!
		print "calc: FOUND SOLUTION! "
		print "sol[{0:05d}]: {1}".format(solutions, combi)
		solutions += 1
		if (solutions % 1000) == 0:
			print "sols: {0}/{1}".format(solutions, permutations)
		
	# check level
	if (level < 1):
		return 0
	
	# iterate on level
	maxCoins = int(remain / coins[level - 1]) + 2		# need to adjust total coins above since rounding
	
	if (debug):
		print "calc: iterating: remain: {0} - coin: {1} - max: {2}".format(remain, coins[level - 1], maxCoins)
	
	for numCoins in range(maxCoins):
		combi[level - 1] = numCoins
#		print "calc: iterating: iter: {0}/{1} - COMBINATION: {2}".format(numCoins, maxCoins, combi)
#		print ""
		calc(target, coins, combi, level - 1)
		combi[level - 1] = 0

def main():

	# set application name
	Log.setApplicationName(APPLICATION_NAME)
	
	# start
	Log.trace("starting...")

	# setup coins and initial combination
	_coins = [ 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]
	_combi = [ 0 ] * len(_coins)
	
	print "031.main: coins: {0}".format(_coins)
	print "031.main: combi: {0}".format(_combi)

	# call recursive combination search
	calc(2.0, _coins, _combi, len(_combi))
	
	# print # of solutions
	Log.trace("done: # solutions: {0}".format(solutions))
	
	# end
	Log.trace("done!")


# ---------------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	main()
