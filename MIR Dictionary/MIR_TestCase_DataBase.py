from MIR_Dict_Class import *
from MIR_Dict_fcns import *

""" 
	This data base consists all the cases that I thought about and used in testing
	functions in MIR (Dictionary)
	When using the case, refer to the hard copy for graphical view
"""

def AllCaseNumber():
	intCaseNumber = range(1,13)
	specialCaseNumber = [4.1, 5.1]
	allCaseList = intCaseNumber + specialCaseNumber
	allCaseList.sort()
	return allCaseList


def GenerateTestTree(caseNumber):

	if caseNumber == 1:
		b1 = '0_5_0_5'
		b2 = '5_6_1_7'
		tree = {'root': [[], [b1]],\
			b1: [['root'], [b2]],\
			b2: [[b1], []]}
		blockList = [b1, b2]
		jobList = []

	elif caseNumber == 2:
		b1 = '0_5_0_5'
		b2 = '5_10_1_6'
		tree = {'root': [[], [b1]], \
			b1: [['root'], [b2]], \
			b2: [[b1], []]}
		blockList = [b1, b2]
		jobList = []
	
	elif caseNumber == 3:
		b1 = '0_5_0_5'
		b2 = '5_10_1_11'
		tree = {'root': [[], [b1]], \
			b1: [['root'], [b2]], \
			b2: [[b1], []]}
		blockList = [b1, b2]
		jobList = []

	elif caseNumber == 4:
		b1 = '0_5_0_5'
		b2 = '0_4_7_9'
		b3 = '4_10_6_10'
		tree = {'root': [[], [b1, b2]], \
			b1: [['root'], []], \
			b2: [['root'], [b3]],\
			b3: [[b2], []]}
		blockList = [b1, b2, b3]
		jobList = []

	elif caseNumber == 4.1:
		b1 = '0_5_0_5'
		b2 = '0_4_7_10'
		b3 = '4_10_6_10'
		tree = {'root': [[], [b1, b2]], \
			b1: [['root'], []], \
			b2: [['root'], [b3]],\
			b3: [[b2], []]}
		blockList = [b1, b2, b3]
		jobList = []
			
	elif caseNumber == 5:
		b1 = '0_5_0_5'
		b2 = '5_10_0_1'
		tree = {'root': [[], [b1]], \
			b1: [['root'], [b2]], \
			b2: [[b1], []]}	
		blockList = [b1, b2]	
		jobList = []

	elif caseNumber == 5.1:
		b1 = '0_5_0_5'
		b2 = '5_10_2_3'
		tree = {'root': [[], [b1]], \
			b1: [['root'], [b2]], \
			b2: [[b1], []]}		
		blockList = [b1, b2]
		jobList = []

	elif caseNumber == 6:
		b1 = '0_5_9_10'
		b2 = '5_15_6_10'
		b3 = '15_20_9_10'
		b4 = '15_20_5_8'
		b5 = '0_5_3_7'
		b6 = '5_10_0_4'
		b7 = '10_15_3_5'
		b8 = '10_15_0_2'
		b9 = '15_20_0_1'
		tree = {'root': [[], [b1, b5]], \
			b1: [['root'], [b2]], \
			b2: [[b1, b5], [b3, b4]], \
			b3: [[b2], []], \
			b4: [[b2], []], \
			b5: [['root'], [b2, b6]], \
			b6: [[b5],[b7, b8]], \
			b7: [[b6], []], \
			b8: [[b6], [b9]],\
			b9: [[b8], []]}		
		blockList = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
		jobList = []

	elif caseNumber == 7:
		b1 = '0_5_0_3'
		b2 = '0_5_4_6'
		b3 = '0_5_7_10'
		b4 = '5_10_0_10'
		tree = {'root': [[], [b1, b2, b3]], \
			b1: [['root'], [b4]], \
			b2: [['root'], [b4]], \
			b3: [['root'], [b4]], \
			b4: [[b1, b2, b3], []]}
		blockList = [b1, b2, b3, b4]
		jobList = []

	elif caseNumber == 8:
		b1 = '0_5_0_10'
		b2 = '5_10_0_3'
		b3 = '5_10_4_6' 
		b4 = '5_10_7_10'
		tree = {'root': [[], [b1]], \
			b1: [['root'], [b2, b3, b4]], \
			b2: [[b1], []], \
			b3: [[b1], []], \
			b4: [[b1], []]}
		blockList = [b1, b2, b3, b4]
		jobList = []

	elif caseNumber == 9:
		b1 = '0_5_0_3'
		b2 = '0_5_4_6'
		b3 = '0_5_7_10'
		b4 = '5_10_0_10'
		b5 = '10_15_0_2'
		b6 = '10_15_3_6' 
		b7 = '10_15_7_8'
		b8 = '10_15_9_10'
		tree = {'root': [[], [b1, b2, b3]], \
			b1: [['root'], [b4]], \
			b2: [['root'], [b4]], \
			b3: [['root'], [b4]], \
			b4: [[b1, b2, b3], [b5, b6, b7, b8]], \
			b5: [[b4], []],\
			b6: [[b4], []],\
			b7: [[b4], []],\
			b8: [[b4], []],}
		blockList = [b1, b2, b3, b4, b5, b6, b7, b8]
		jobList = [[2, 10], [3, 4], [2,5], [2,9]]
		jobList += [[5, i] for i in range(1,11)]

	elif caseNumber == 10:
		# this is an updated version of testcase 9
		b1 = '0_5_0_3'
		b2 = '0_5_4_6'
		b3 = '0_5_7_10'
		b4 = '5_10_0_10'
		b5 = '10_15_1_2'
		b6 = '10_15_3_6' 
		b7 = '10_15_7_8'
		b8 = '10_15_9_10'
		tree = {'root': [[], [b1, b2, b3]], \
			b1: [['root'], [b4]], \
			b2: [['root'], [b4]], \
			b3: [['root'], [b4]], \
			b4: [[b1, b2, b3], [b5, b6, b7, b8]], \
			b5: [[b4], []],\
			b6: [[b4], []],\
			b7: [[b4], []],\
			b8: [[b4], []],}
		blockList = [b1, b2, b3, b4, b5, b6, b7, b8]
		jobList = [[2, 10], [3, 4], [2,5], [2,9]]
		jobList += [[5, i] for i in range(1,11)]

	elif caseNumber == 11:
		# this is an updated version of testcase 10
		b1 = '0_5_0_3'
		b2 = '0_5_4_6'
		b3 = '0_5_7_10'
		b4 = '5_10_0_10'
		b5 = '10_15_1_2'
		b6 = '10_20_3_6' 
		b7 = '10_15_7_8'
		b8 = '10_15_9_10'
		tree = {'root': [[], [b1, b2, b3]], \
			b1: [['root'], [b4]], \
			b2: [['root'], [b4]], \
			b3: [['root'], [b4]], \
			b4: [[b1, b2, b3], [b5, b6, b7, b8]], \
			b5: [[b4], []],\
			b6: [[b4], []],\
			b7: [[b4], []],\
			b8: [[b4], []],}
		blockList = [b1, b2, b3, b4, b5, b6, b7, b8]
		jobList = [[2, 10], [3, 4], [2,5], [2,9]]
		jobList += [[5, i] for i in range(1,11)]

	elif caseNumber == 12:
		# this is an updated version of testcase 10
		b1 = '0_5_0_3'
		b2 = '0_5_4_6'
		b3 = '0_5_7_10'
		b4 = '5_10_0_10'
		b5 = '10_15_1_2'
		b6 = '10_20_3_5' 
		b7 = '10_15_6_7'
		b8 = '10_15_9_10'
		tree = {'root': [[], [b1, b2, b3]], \
			b1: [['root'], [b4]], \
			b2: [['root'], [b4]], \
			b3: [['root'], [b4]], \
			b4: [[b1, b2, b3], [b5, b6, b7, b8]], \
			b5: [[b4], []],\
			b6: [[b4], []],\
			b7: [[b4], []],\
			b8: [[b4], []],}
		blockList = [b1, b2, b3, b4, b5, b6, b7, b8]
		jobList = [[2, 10], [3, 4], [2,5], [2,9]]
		jobList += [[5, i] for i in range(1,11)]




	else:
		print 'The Case number does not exist'
		return None, None
	testBin = testbin(tree, 20, 10, blockList)
	return tree, testBin, jobList


def GenerateFullBin(caseNumber, W, L):
	# Creating a tree using the above caseNumber
	testTree, _testBin, _jobList = GenerateTestTree(caseNumber)
	# print 'testTree', testTree , '\n'
	
	realisticBin = mirBin('testBin', W, L)
	
	realisticBin.tree = testTree
	# print 'realisticBin.tree: ', realisticBin.tree, '\n'

	realisticBin.blockList = testTree.keys()
	realisticBin.blockList.remove('root')

	realisticBin.area = CalBinArea(realisticBin)
	mirArea, mirCoord = CalMirBin(realisticBin)
	realisticBin.mir = mirArea
	realisticBin.mirCoord = mirCoord
	
	return realisticBin







