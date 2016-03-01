from MIR_Dict_fcns import *
from MIR_Dict_Class import *
from MIR_Dict_Corner_1 import *
from MIR_TestCase_DataBase import *

def main():
	# print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Refreshing Screen:\n'
	""" Test 1: testing UpdateTree_C1 """
	testTree, testBin, jobList = GenerateTestTree(10)
	b1 = '0_5_0_3'
	b2 = '0_5_4_6'
	b3 = '0_5_7_10'
	b4 = '5_10_0_10'
	b5 = '10_15_1_2'
	b6 = '10_15_3_6' 
	b7 = '10_15_7_8'
	b8 = '10_15_9_10'

	w, l = [15,2]
	job = job_dta(1,w,l)
	startBlockName = b1

	feasibility, potChain = Feasibility_C1(startBlockName, job, testTree)
	print feasibility
	
	print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
	print 'Job Dimension: [', w, ',', l, ']'
	print 'Block: ', startBlockName
	print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n'

	# tempTree = UpdateTree_C1(startBlockName, testTree, job)
	
	feasibility, treeAfter, mirArea, mirCoord = CalCorner_1(startBlockName, job, 20, 10, testTree)
	print 'Tree before: -------------------------\n'
	DisplayTree(testTree)
	print 'Tree after: -------------------------\n'
	print 'mirArea: ', mirArea
	print 'mirCoord: ', mirCoord
	if treeAfter:
		DisplayTree(treeAfter)


	# print PotentialChain_C1(b1, testTree)	










if __name__ == '__main__':
	main()