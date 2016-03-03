from MIR_Dict_Class import *
from MIR_Dict_fcns import *
from MIR_Dict_Corner_1 import *
from MIR_Dict_Corner_2 import *
from MIR_Dict_Corner_3 import *
from MIR_Dict_Corner_4 import *

def BinScore_1(MIR_before, MIR_after):
	return MIR_before + MIR_after

def BinScore_2(MIR_before, MIR_after):
	return MIR_before




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
		if feasibility and mirArea > mirAfter:
			placement = BlockToCorner(b, 1)
			mirAfter = mirArea
			binFeasibility = feasibility
			placementBlock = b
			binTreeAfter = treeAfter
			binMirCoord = mirCoord


		
		feasibility, treeAfter, mirArea, mirCoord = CalCorner_2(b, job_dta, W, L, tree)
		if feasibility and mirArea > mirAfter:
			placement = BlockToCorner(b, 2)
			mirAfter = mirArea
			binFeasibility = feasibility
			placementBlock = b
			binTreeAfter = treeAfter
			binMirCoord = mirCoord

		feasibility, treeAfter, mirArea, mirCoord = CalCorner_3(b, job_dta, W, L, tree)
		if feasibility and mirArea > mirAfter:
			placement = BlockToCorner(b, 3)
			mirAfter = mirArea
			binFeasibility = feasibility
			placementBlock = b
			binTreeAfter = treeAfter
			binMirCoord = mirCoord

		feasibility, treeAfter, mirArea, mirCoord = CalCorner_4(b, job_dta, W, L, tree)
		if feasibility and mirArea > mirAfter:
			placement = BlockToCorner(b, 4)
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

























