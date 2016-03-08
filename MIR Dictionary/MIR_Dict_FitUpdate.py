from MIR_Dict_Class import *
from MIR_Dict_fcns import *
from MIR_Dict_Corner_1 import *
from MIR_Dict_Corner_2 import *
from MIR_Dict_Corner_3 import *
from MIR_Dict_Corner_4 import *

def BinScore_1(MIR_before, MIR_after):
	binScore = 1.0 / (MIR_before + MIR_after)
	return binScore

def BinScore_2(MIR_before, MIR_after):
	binScore = 1.0 / MIR_before
	return binScore

def TieBreaker(mirArea, mirAfter, blockName, cornerType, job_dta, placement):
	# If a tie happens (two placement decision happens to result in the same mir_after)
	# then compare the bottom left coordinate of the job
	# if the new placement is either more towards the left (x1' < x1)
	# or more towards the bottom (y1' < y1). Then break the tie and take the new coordinate as placement decision
	# Here benchMarkCoord and newCoord are the bottom left corner of the job
	if placement == [] or mirArea > mirAfter:
		return True
	
	w, l = job_dta.dimension
	if placement[2] == 1:
		benchMarkCoord = [placement[0], placement[1]]
	elif placement[2] == 2:
		benchMarkCoord = [placement[0], placement[1] - l]
	elif placement[2] == 3:
		benchMarkCoord = [placement[0] - w, placement[1] - l]
	elif placement[2] == 4:
		benchMarkCoord = [placement[0] - w, placement[1]]

	x, y, _cornerType = BlockToCorner(blockName, cornerType)
	if cornerType == 1:
		newCoord = [x, y]
	elif cornerType == 2:
		newCoord = [x, y - l]
	elif cornerType == 3:
		newCoord = [x - w, y - l]
	elif cornerType == 4:
		newCoord = [x - w, y]

	if newCoord[0] <= benchMarkCoord[0] and newCoord[1] <= benchMarkCoord[1]:
		return True
	else:
		return False
















def JobBinFit(b, job_dta):
	# print b
	mirBefore = b.mir
	tree = b.tree
	blockList = b.blockList
	W, L = b.dimension

	placement = []
	placementBlock = []
	mirAfter = -1
	binTreeAfter = []
	binFeasibility = False
	binMirCoord = []



	for b in blockList:
		
		feasibility, treeAfter, mirArea, mirCoord = CalCorner_1(b, job_dta, W, L, tree)
		# for debug purpose
		# print 'block: ', b, 'Corner 1', feasibility, mirArea, mirCoord

		if feasibility and mirArea >= mirAfter and TieBreaker(mirArea, mirAfter, b, 1, job_dta, placement):
			placement = BlockToCorner(b, 1)
			# for debug purpose
			# print 'Update Corner Decision: ', placement
			mirAfter = mirArea
			binFeasibility = feasibility
			placementBlock = b
			binTreeAfter = treeAfter
			binMirCoord = mirCoord


		
		feasibility, treeAfter, mirArea, mirCoord = CalCorner_2(b, job_dta, W, L, tree)
		# for debug purpose
		# print 'block: ', b, 'Corner 2', feasibility, mirArea, mirCoord

		if feasibility and mirArea >= mirAfter and TieBreaker(mirArea, mirAfter, b, 2, job_dta, placement):
			placement = BlockToCorner(b, 2)
			# for debug purpose
			# print 'Update Corner Decision: ', placement
			mirAfter = mirArea
			binFeasibility = feasibility
			placementBlock = b
			binTreeAfter = treeAfter
			binMirCoord = mirCoord

		feasibility, treeAfter, mirArea, mirCoord = CalCorner_3(b, job_dta, W, L, tree)
		# for debug purpose
		# print 'block: ', b, 'Corner 3', feasibility, mirArea, mirCoord

		if feasibility and mirArea >= mirAfter and TieBreaker(mirArea, mirAfter, b, 3, job_dta, placement):
			placement = BlockToCorner(b, 3)
			# for debug purpose
			# print 'Update Corner Decision: ', placement
			mirAfter = mirArea
			binFeasibility = feasibility
			placementBlock = b
			binTreeAfter = treeAfter
			binMirCoord = mirCoord

		feasibility, treeAfter, mirArea, mirCoord = CalCorner_4(b, job_dta, W, L, tree)
		# for debug purpose
		# print 'block: ', b, 'Corner 4', feasibility, mirArea, mirCoord

		if feasibility and mirArea >= mirAfter and TieBreaker(mirArea, mirAfter, b, 4, job_dta, placement):
			placement = BlockToCorner(b, 4)
			# for debug purpose
			# print 'Update Corner Decision: ', placement
			mirAfter = mirArea
			binFeasibility = feasibility
			placementBlock = b
			binTreeAfter = treeAfter
			binMirCoord = mirCoord

	if binFeasibility:
		binScore = BinScore_1(mirBefore, mirAfter)
	else:
		binScore = -1

	return binFeasibility, placement, placementBlock, binScore, mirAfter, binTreeAfter, binMirCoord


def UpdateBinJob(b, job_dta, mirAfter, treeAfter, mirCoord, placement):
	# Update job
	job_dta.bin = b.index
	job_dta.coord = placement

	# Update bin
	b.tree = treeAfter
	b.area -= job_dta.area
	b.mir = mirAfter
	b.mirCoord = mirCoord
	b.blockList = treeAfter.keys()
	b.blockList.remove('root')
	b.jobPlaced.append(job_dta.index)

def UpdateFirstJob(b, job_dta):
	if b.area != (b.dimension[0] * b.dimension[1]) or b.jobPlaced:
		print 'Error(UpdateFirstJob.e1): The bin is not a new bin.\n'
		return


	binFeasibility, placement, placementBlock, binScore, mirAfter, binTreeAfter, binMirCoord = JobBinFit(b, job_dta)
	if not binFeasibility:
		print 'Error(UpdateFirstJob.e2): First block infeasible.\n'
		return
	else:
		UpdateBinJob(b, job_dta, mirAfter, binTreeAfter, binMirCoord, placement)	

























