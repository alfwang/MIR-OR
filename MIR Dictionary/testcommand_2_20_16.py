from MIR_Dict_fcns import *
from MIR_Dict_Class import *
from MIR_Dict_Corner_1 import *
from MIR_TestCase_DataBase import *


if __name__ == '__main__':
	""" Test 1: tesing Feasibility_C1 """
	# testTree, testBin = GenerateTestTree(6)
	# b1 = '0_5_9_10'
	# b2 = '5_15_6_10'
	# b3 = '15_20_9_10'
	# b4 = '15_20_5_8'
	# b5 = '0_5_3_7'
	# b6 = '5_10_0_4'
	# b7 = '10_15_3_5'
	# b8 = '10_15_0_2'
	# b9 = '15_20_0_1'
	# blist = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

	# for i in range(1, 6):
	# 	for j in range (1, 6):
	# 		d = [4 * i, j]
	# 		job = testjob(d)
	# 		print '\n\n================================= job: ', d, '================================='
	# 		for (k, b) in enumerate(blist):
	# 			fea, inflCh = Feasibility_C1(b, testTree, job)
	# 			if fea:
	# 				print 'B ------------------------------------->', k + 1
	# 				print 'block dimension: ', b
	# 				print inflCh, '\n'



	""" Test 2: testing CondConnect_Parent """
	# testTree, testBin = GenerateTestTree(7)
	# b1 = '0_5_0_3'
	# b2 = '0_5_4_6'
	# b3 = '0_5_7_10'
	# b4 = '5_10_0_10'
	
	# targetBlock = '5_10_6_7'
	# CondConnect_Parent(targetBlock, testTree[b4][0], testTree)
	# DisplayTree(testTree)

	""" Test 3: testing CondConnect_Child """
	# testTree, testBin = GenerateTestTree(8)
	# DisplayTree(testTree)
	# b1 = '0_5_0_10'
	# b2 = '5_10_0_3'
	# b3 = '5_10_4_6' 
	# b4 = '5_10_7_10'
	
	# targetBlock = '0_5_5_10'
	# CondConnect_Child(targetBlock, testTree[b1][1], testTree)
	# DisplayTree(testTree)
				

	""" Test 4: testing delete block """
	testTree, testBin = GenerateTestTree(7)
	b1 = '0_5_0_3'
	b2 = '0_5_4_6'
	b3 = '0_5_7_10'
	b4 = '5_10_0_10'
	blist = [b1, b2, b3, b4]
	DisplayTree(testTree)
	for b in blist:
		tempTree = DuplicateTree(testTree)
		DeleteBlock(b, tempTree)
		print 'deleting ', b, 'from tree: >>>>>>>>>>>>>>'
		DisplayTree(tempTree)

	print 'The original tree: -------'
	DisplayTree(testTree)

















