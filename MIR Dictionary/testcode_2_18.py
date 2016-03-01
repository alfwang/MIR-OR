from MIR_Dict_fcns import *
from MIR_Dict_Class import *
from MIR_Dict_Corner_1 import *
from MIR_TestCase_DataBase import *

if __name__ == '__main__':
	""" Test the functions after deleting the first dimenison of the blockName [Done] """
	# allCaseList = AllCaseNumber()
	# for i in allCaseList:
	# 	testTree, testBin = GenerateTestTree(i)
	# 	print '-------------------------'
	# 	print 'Case Number: ', i, '\n'
	# 	print CalMirBin(testBin)


	""" Test the EffectiveChain function (this is a prototype for bottom left corner) """
	allCaseList = AllCaseNumber()
	for i in allCaseList:
		testTree, testBin = GenerateTestTree(i)
		print '============================================='
		print 'Case Number: ', i, '\n'
		for bl in testBin.blockList:
			print 'block: ', bl, '\n'
			print 'Effective Chain (on the right): ', EffectiveChain(bl, testTree)


	
	