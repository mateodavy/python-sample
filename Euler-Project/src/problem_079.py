#
# Python program to solve Euler Problem #79
#
# Link: https://projecteuler.net/problem=79
#
#
#


# ---------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------
import os
import sys


# ---------------------------------------------------------------------------------------------------------
# defines
# ---------------------------------------------------------------------------------------------------------

PATH_KEYLOG = "../data/p079_keylog.txt"


# ---------------------------------------------------------------------------------------------------------
# utilities
# ---------------------------------------------------------------------------------------------------------

class Histogram(object):

	_digits = {}

	def __init__(self):
		print "079.Histogram: constructor..."
		numDigits = 10
#		self._digits = [ 0 for digit in range(numDigits) ]
		self._digits = { }
		
		
	def add(self, number):
		for digitVal in number:
			print "079.Histogram.add: digit: {0}".format(digitVal)
			if digitVal in self._digits:
				self._digits[digitVal] += 1
			else:
				self._digits[digitVal] = 1
			
	def dump(self):
		numDigits = 10
#		print "079.Histogram.dump: digits: {0}".format(self._digits)
		for digitPos in range(numDigits):
#			digitCount = 0
			digitCount = '?'
			digitVal = str(digitPos)
			if digitVal in self._digits:
				digitCount = self._digits[digitVal]
			print "079.Histogram.dump: histo[{0}]: {1}".format(digitVal, digitCount)
			

# ---------------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------------

def main():
	print "079.main: starting..."

	keylog = open(PATH_KEYLOG, 'r')
	
	histogram = Histogram()
	
	pos = 0
	for line in keylog:
		key = line.strip('\n')
		print "key[{0:03d}]: {1}".format(pos, key)
		histogram.add(key)
		pos += 1

	histogram.dump()

	print "079.main: done!"


# ---------------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	main()
