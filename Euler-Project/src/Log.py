#
# Log/trace utility class 
#
# Notes: 
#
# * calling function is automatically inserted in message
# * allows to wrap/define any additional information (stack, ...)
# * would server to bridge to any other logging system 
# * can be toggled on/off
# * given as an utility sample
#


# ---------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------
import os
import sys
import inspect
import traceback


# ---------------------------------------------------------------------------------------------------------
# defines
# ---------------------------------------------------------------------------------------------------------

APPLICATION_NAME = "Logtest"


# ---------------------------------------------------------------------------------------------------------
# utilities
# ---------------------------------------------------------------------------------------------------------

class Log(object):

	_applicationName = None
	
#	def __init__(self, appName):
#		self._applicationName = appName
	
	def __init__(self):
		pass
	
	@staticmethod
	def setApplicationName(name):
		Log._applicationName = name
	
	@staticmethod
	def printStack():
		# get call stack
		stack = inspect.stack()
#		stack.reverse()
#		stack_list = []
		caller = stack[1]
		print caller
		_, fileName, lineNumber, functionName, codeList, index = caller 
		print "function: {0}".format(functionName)
		
	@staticmethod
	def functionName():
		# get call stack
		stack = inspect.stack()
		caller = stack[2]
		_, fileName, lineNumber, functionName, codeList, index = caller
		return functionName

	@staticmethod
	def trace(prefix):

		# format message
		text = "{0}.{1}: {2}".format(Log._applicationName, Log.functionName(), prefix)
		
		# print it
		print text

# ---------------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------------

def test():
	total = 0
	for number in range(1000):
		if ((number % 3) == 0) or ((number % 5) == 0):
			total += number
	Log.trace("total: {0}".format(total))

def main():
	Log.setApplicationName(APPLICATION_NAME)
	
	Log.trace("starting...")
	test()
	Log.trace("done!")


# ---------------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	main()
