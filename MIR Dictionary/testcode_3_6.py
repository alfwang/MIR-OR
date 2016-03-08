from MIR_Dict_fcns import *
from MIR_Dict_DataFileNames import *
from MIR_Dict_MainBatch import *
from MIR_Dict_Class import *


# for data in dataFileNames:
# 	DataSummary(data)
""" Test 1 """

# print '******************************************************************'
# print '******************************************************************'
# print '******************************************************************'
# print '******************************************************************'

Result = []
for data in dataFileNames:
	print '---------------------------------------------------------'
	totalNumBin, binList, fullJobList = MainBatch(data)
	Result.append([data, totalNumBin])

for r in Result:
	print r


""" Test 2 """
# filename = 'ngcut3.txt'
# DataSummary(filename)
# totalNumBin, binList, fullJobList = MainBatch(filename)
# for b in binList:
# 	DisplayBin(b)
	
# for j in fullJobList:
# 	DisplayJob(j)
# print 'Total # of Bins used: ', totalNumBin


""" Test 3  Job 17 in ngcut 3"""
# b1 = '6_7_4_8'
# b2 = '7_10_0_8'
# tree = {'root': [[],[b1]], \
# 	b1: [['root'], [b2]], \
# 	b2: [[b1], []]}
# blockList = [b1, b2]

# testBin = mirBin(1, 10, 10)
# testBin.tree = tree
# testBin.mir = 24
# testBin.mirCoord = [7, 10, 0, 8]
# testBin.blockList = blockList


# testJob = testjob([4,2])

# binFeasibility, placement, placementBlock, binScore, mirAfter, binTreeAfter, binMirCoord = JobBinFit(testBin, testJob)

# # feasibility, treeAfter, mirArea, mirCoord = CalCorner_3(b2, testJob, 10, 10, testBin.tree)
# # print feasibility
# # print treeAfter
# # print mirArea
# # print mirCoord



# print binFeasibility
# print placement
# print 1.0 / binScore
# print testBin.mir
# print mirAfter
# print binTreeAfter
# print binMirCoord 











