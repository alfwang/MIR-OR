from MIR_Dict_Class import *
from MIR_Dict_fcns import *
from MIR_Dict_Corner_1 import *
from MIR_Dict_Corner_2 import *
from MIR_Dict_Corner_3 import *
from MIR_Dict_Corner_4 import *
from MIR_Dict_FitUpdate import *
from MIR_Dict_DataFileNames import *


def MainBatch(filename):
	# Reading file ---------------------------------------------------------------------------------	filename = input('Enter the dataset name:\n')
	# while filename not in dataFileNames:
	# 	filename = input('Invalid data file, enter again.\n')
	print 'Dataset ( ', filename, ' )load successfully'

	numJobs, binDimension, jobList = ReadData(filename)
	W, L = binDimension
	print 'Number of jobs:', numJobs
	print 'Bin Dimension: ', binDimension
	print 'Job List (before presorting): ', jobList



	# ---------------------------------------------------------------------------------
	


	# Sorting jobs ---------------------------------------------------------------------------------
	sortedJobList = Presort_1(jobList)
	fullJobList = CreateJobList(numJobs, sortedJobList)

	# Initializing bin list
	binList = [mirBin(1, W, L)]
	totalNumBin = 1

	# Iterate through every job
	for job in fullJobList:
		binScore = -1
		cornerPlacement = []
		placementBlock = []
		stackFeasibility = False
		stackScore = -1
		optBinIndex = []
		mirAfter = -1
		treeAfter = []
		mirCoord = []

		# iterate through every bin
		for i, b in enumerate(binList):
			# _ represents the bin that is being currently considered.
			_binFeasibility, _placement, _placementBlock, _binScore, _mirAfter, _treeAfter, _mirCoord= JobBinFit(b, job)
			if _binFeasibility and _binScore > binScore:
				optBinIndex = i
				cornerPlacement = _placement
				placementBlock = _placementBlock
				stackScore = _binScore
				mirAfter = _mirAfter
				treeAfter = _treeAfter
				mirCoord = _mirCoord
				stackFeasibility = _binFeasibility

				

		# If some bin in the stack is feasible, place the job in the bin and update
		if stackFeasibility:
			# print 'best placement decision\n:'
			optBin = binList[optBinIndex]
			UpdateBinJob(optBin, job, mirAfter, treeAfter, mirCoord, cornerPlacement)

		#If no bin in the stack is feasible, create a new bin and place the job
		else:
			totalNumBin += 1
			binList.append(mirBin(totalNumBin, W, L))
			UpdateFirstJob(binList[-1], job)


	# DisplayFinalResult(totalNumBin, binList, fullJobList)
	return	totalNumBin, binList, fullJobList



				





if __name__ == '__main__':
	result_BinUsed = {}
	result_Detailed = {}
	for dataset in dataFileNames:
		totalNumBin, binList, fullJobList = MainBatch(dataset)
		result_BinUsed[dataset] = totalNumBin
		result_Detailed[dataset] = [binList, fullJobList]
	
	print '\n\n\n\n\n\n---------------------- Results: ----------------------\n'
	DataSet = result_BinUsed.keys()
	DataSet.sort()
	for r in DataSet:
		print r, ' consumes ', result_BinUsed[r], 'bins\n'
		












