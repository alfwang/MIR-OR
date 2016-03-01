from MIR_Dict_fcns import *
from MIR_Dict_Class import *
from MIR_Dict_Corner_1 import *
from MIR_Dict_Corner_2 import *
from MIR_Dict_Corner_3 import *
from MIR_Dict_Corner_4 import *
from MIR_Dict_FitUpdate import *
from MIR_TestCase_DataBase import *


def main():
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Refreshing Screen:\n'
	""" Test 1: testing  JobBinFit"""

	# # testTree, _testBin, jobList = GenerateTestTree(12)
	# b1 = '0_5_0_3'
	# b2 = '0_5_4_6'
	# b3 = '0_5_7_10'
	# b4 = '5_10_0_10'
	# b5 = '10_15_1_2'
	# b6 = '10_20_3_5' 
	# b7 = '10_15_6_7'
	# b8 = '10_15_9_10'
	# blockList = [b1, b2, b3, b4, b5, b6, b7, b8]

	# w = input('w: ')
	# l = input('l: ')
	# job = job_dta(1, w, l)
	# caseNumber = 12
	# W = 20
	# L = 10

	# testBin = GenerateFullBin(caseNumber, W, L)
	# print 'before placing the job:\n'
	# DisplayBin(testBin)

	# print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
	# print 'Job Dimension: [', w, ',', l, ']'
	# print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n'

	# binFeasibility, placement, placementBlock, binScore, \
	# 	mirAfter, binTreeAfter, binMirCoord = JobBinFit(testBin, job)


	# print 'binFeasibility: ', binFeasibility
	# print 'placement: ', placement
	# print 'placementBlock: ', placementBlock
	# print 'binScore: ', binScore
	# print 'mirBefore: ', testBin.mir
	# print 'mirAfter: ', mirAfter
	# print 'binMirCoord: ', binMirCoord
	
	# # print 'TreeBefore: '
	# # DisplayTree(testBin.tree)
	# print 'TreeAfter: '
	# DisplayTree(binTreeAfter)
	# if binFeasibility:
	# 	UpdateBinJob(testBin, job, mirAfter, binTreeAfter, binMirCoord, placement)
	# 	print 'After Updating:'
	# 	DisplayBin(testBin)
	# 	DisplayJob(job)
	# else:
	# 	print '\033[94m Job not feasible in current bin.\n \033[0m'

	""" Test 2: testing UpdateFirstJob """
	b = mirBin(1,20,10)
	# b.area = 20
	DisplayBin(b)
	job = job_dta(10,10,5)
	DisplayJob(job)
	UpdateFirstJob(b, job)

	print 'After Updating ----------------'
	DisplayBin(b)
	DisplayJob(job)

	







if __name__ == '__main__':
	main()