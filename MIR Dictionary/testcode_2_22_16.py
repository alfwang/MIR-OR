from MIR_Dict_fcns import *
from MIR_Dict_Class import *
from MIR_Dict_Corner_1 import *
from MIR_TestCase_DataBase import *

def main():
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Refreshing Screen:\n'
	""" Test 1: testing TotalConsumption 
		[It turns out that TotalConsumption is useless, since its job can be done by DeleteBlock"""
	# print '----------------------  The Oringial Tree  -----------------------------------------------'
	# testTree, testBin = GenerateTestTree(8)
	# b1 = '0_5_0_10'
	# b2 = '5_10_0_3'
	# b3 = '5_10_4_6' 
	# b4 = '5_10_7_10'
	# blist = [b1, b2, b3, b4]
	# DisplayTree(testTree)

	# for b in blist:
	# 	print '---------------------------------------------------------------------'
	# 	tempTree = DuplicateTree(testTree)
	# 	TotalConsumption(b, tempTree)
	# 	print 'TotalConsumption target block: ', b, ' from tree >>>>>>>>>'
	# 	DisplayTree(tempTree)

	# print 'The original tree: -------'
	# DisplayTree(testTree)


	""" Test 2: testing UpdateTree_C1_T1 """
	testTree, testBin, jobList = GenerateTestTree(9)
	b1 = '0_5_0_3'
	b2 = '0_5_4_6'
	b3 = '0_5_7_10'
	b4 = '5_10_0_10'
	b5 = '10_15_0_2'
	b6 = '10_15_3_6' 
	b7 = '10_15_7_8'
	b8 = '10_15_9_10'
	blockList = [b1, b2, b3, b4, b5, b6, b7, b8]
	DisplayTree(testTree)



	b = b4
	print '-------------------- block: ', b , '------------------------'
	for job in jobList:
		w, l = job 
			
		print '-------------------- job: ', job , '------------------------'
		
		tempTree = DuplicateTree(testTree)
		x1, x2, y1, y2 = BlockToCoord(b)
		jobCoverCoord = [x1, x1 + w, y1, y1 + l]
		UpdateTree_C1_T1(b, jobCoverCoord, tempTree)
		DeleteBlock(b, tempTree)
		DisplayTree(tempTree)




	












if __name__ == '__main__':
	main()