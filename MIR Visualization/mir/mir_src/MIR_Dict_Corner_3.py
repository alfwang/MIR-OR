from MIR_Dict_Class import *
from MIR_Dict_fcns import *

# Corner 3 is the top right corner.

def CalCorner_3(blockName, job_dta, W, L, tree):
	feasibility, potChain = Feasibility_C3(blockName, job_dta, tree)
	if feasibility:
		# print 'Check point 1'
		treeAfter = DuplicateTree(tree)
		treeAfter = UpdateTree_C3(blockName, job_dta, treeAfter)
		mirArea, mirCoord = CalMirTree(treeAfter, W, L)
		return feasibility, treeAfter, mirArea, mirCoord
	else:
		# print 'Check point 2'
		return feasibility, None, None, None






def PotentialChain_C3(blockName, tree):
	coord = BlockToCoord(blockName)
	ceiling = coord[3]
	# print 'checkpoint 1'
	return PC_C3_Rec(blockName, ceiling, tree)


def PC_C3_Rec(blockName, ceiling, tree):
	coord = BlockToCoord(blockName)
	if tree[blockName][0] == ['root']:
		# print 'checkpoint 2'
		return [blockName]
	else: 
		for b in tree[blockName][0]:
			# print 'checkpoint 3'
			# print b
			nextcoord = BlockToCoord(b)
			if ceiling <= nextcoord[3] and ceiling > nextcoord[2]:
				# print 'checkpoint 4'
				return [blockName] + PC_C3_Rec(b, ceiling, tree)
		return [blockName]







def Feasibility_C3(blockName, job, tree):
	w, l = job.dimension
	x1, x2, y1, y2 = BlockToCoord(blockName)
	floor = y1
	ceiling = y2
	init_cap_x = x2 - x1
	init_cap_y = ceiling - floor

	# """ Case 1: job height exceeds initial block height -> infeasible """
	if l > init_cap_y:
		return False, []

	# """ Case 2: job height feasible, look at width """
	potChain_all = PotentialChain_C3(blockName, tree)
	leftPoint = x2 - w
	potChain = [b for b in potChain_all if leftPoint < BlockToCoord(b)[1]]
	potChain_floor = max([BlockToCoord(b)[2] for b in potChain])
	potChain_width = x2 - BlockToCoord(potChain[-1])[0] 

	if ceiling - potChain_floor >= l and w <= potChain_width:
		return True, potChain
	else:
		return False, []


def UpdateTree_C3(startBlockName, job, tree):
	feasibility, influencedChain = Feasibility_C3(startBlockName, job, tree)
	if not feasibility:
		print 'Warning(UpdateTree_C3.w1): Feasiblity is False, no updating required.\n'
		return 

	coord = BlockToCoord(startBlockName)
	w, l = job.dimension
	corner = [coord[1], coord[3]]
	lenInfluencedChain = len(influencedChain)
	tempTree = DuplicateTree(tree)
	jobCoverCoord = [corner[0] - w, corner[0], corner[1] - l, corner[1]]
	# print 'job Cover Coord:', jobCoverCoord
	for i, b in enumerate(influencedChain):
		if i == 0:
			UpdateTree_C3_T1(b, jobCoverCoord, tempTree)
		elif i > 0 and i < (lenInfluencedChain - 1):
			UpdateTree_C3_T2(b, jobCoverCoord, tempTree)
		elif i == (lenInfluencedChain - 1):
			UpdateTree_C3_T3(b, jobCoverCoord, tempTree)
	for b in influencedChain:
		DeleteBlock(b, tempTree)
	return tempTree

def UpdateTree_C3_T1(b, jobCoverCoord, tree):
	# Type 1 block (C2_T1) is the starting block
	# Get all necessary coordinates
	x1, x2, y1, y2 = BlockToCoord(b)
	jx1, jx2, jy1, jy2 = jobCoverCoord

	# The top right corner of the job and the starting block should overlap
	if x2 != jx2 or y2 != jy2:
		print 'Error(UpdateTree_C3_T1.e1): input should be the starting block, but it does not agree with the corner coordinates. \n'
		return
	
	# The bottom of the job should not be lower than the bottom of the block
	if jy1 < y1:
		print 'Error(UpdateTree_C3_T1.e2): The bottom of the job exceeds the bottom of the block.'
		return

	# """ Case 1: Total Consumption """
	# If the job happens to consume all of the block, then delete the block from the tree
	if jx1 <= x1 and jy1 == y1:
		# Here the block should be deleted, but the deletion should be reserved to the end of the updating process
		# DeleteBlock(b, tree)
		ConsolidateCondConnect(['0_0_0_0'], b, 'Total_Consumption', tree)
		return

	# """ Case 2: Consume whole right part """
	if jx1 > x1 and jy1 == y1:
		C1 = CoordToBlock([x1, jx1, y1, y2])
		# print C1

		# CreateNewBlock(C1, tree)
		# SimplyConnect('root', C1, tree)
		# CondConnect_Child(C1, tree[b][1], tree)
		ConsolidateCondConnect([C1], b, 'Consume_Right', tree)

		return

	# """ Case 3: Consume whole top part """
	if jx1 <= x1 and jy1 > y1:
		C1 = CoordToBlock([x1, x2, y1, jy1])
		# CreateNewBlock(C1, tree)
		# CondConnect_Parent(C1, tree[b][0], tree)
		# CondConnect_Child(C1, tree[b][1], tree)
		ConsolidateCondConnect([C1], b, 'Consume_Top', tree)
		return

	# """ Case 4: L Shape """
	if jx1 > x1 and jy1 > y1:
		C1 = CoordToBlock([x1, jx1, y1, y2])
		C2 = CoordToBlock([jx1, x2, y1, jy1])
		ConsolidateCondConnect([C1, C2], b, 'L_Shape', tree)


		# print 'newly created blocks: ', C1, C2
		# CreateNewBlock(C1, tree)
		# # print 'Debug point 1'
		# # DisplayTree(tree)
		# CreateNewBlock(C2, tree)
		# # print 'Debug point 2'
		# # DisplayTree(tree)
		# CondConnect_Parent(C1, tree[b][0], tree)
		# # print 'Debug point 3'
		# # DisplayTree(tree)
		# SimplyConnect(C1, C2, tree)
		# # print 'Debug point 4'
		# # DisplayTree(tree)
		# CondConnect_Child(C2, tree[b][1], tree)
		# # print 'Debug point 5'
		# # DisplayTree(tree)
		return



def UpdateTree_C3_T2(b, jobCoverCoord, tree):
	# Type 2 block(s) are the ones in the middle. And the job must go through type 2 blocks (otherwise, the block would be a type 3 block)
	# Get all necessary coordinates
	x1, x2, y1, y2 = BlockToCoord(b)
	jx1, jx2, jy1, jy2 = jobCoverCoord

	# Check input 
	if jx1 >= x1 or jx2 <= x2:
		print 'Error(UpdateTree_C3_T2.e1): jobCoverCoord does not exceed block width.'
		return
	elif jy1 < y1 or jy2 > y2:
		print 'Error(UpdateTree_C3_T2.e2): jobCoverCoord exceeds block height.'
		return

	# Case 1: Total Consumption 
	elif jy1 == y1 and jy2 == y2:
		ConsolidateCondConnect(['0_0_0_0'], b, 'Total_Consumption', tree)
		return

	# """ Case 2: Consume whole bottom part """
	elif jy1 == y1 and jy2 < y2:
		C1 = CoordToBlock([x1, x2, jy2, y2])
		ConsolidateCondConnect([C1], b, 'Consume_Bottom', tree)
		return

	# """ Case 3: Consume whole top part """
	elif jy1 > y1 and jy2 == y2:
		C1 = CoordToBlock([x1, x2, y1, jy1])
		ConsolidateCondConnect([C1], b, 'Consume_Top', tree)
		return

	# """ Case 4: Consume middle part """
	elif jy1 > y1 and jy2 < y2:
		C1 = CoordToBlock([x1, x2, y1, jy1])
		C2 = CoordToBlock([x1, x2, jy2, y2])
		ConsolidateCondConnect([C1, C2], b, 'Parallel', tree)
		return

	else:
		print 'Error(UpdateTree_C3_T2.e3): Unknown Error.'
		return


def UpdateTree_C3_T3(b, jobCoverCoord, tree):
	x1, x2, y1, y2 = BlockToCoord(b)
	jx1, jx2, jy1, jy2 = jobCoverCoord

	# Check input
	if jx1 < x1 or jx2 <= x2:
		print 'Error(UpdateTree_C3_T3.e0): jobCoverCoord width error.'
		return
	elif jy1 < y1 or jy2 > y2:
		print 'Error(UpdateTree_C3_T2.e2): jobCoverCoord exceeds block height.'
		return


	# """ Case 1: Total Consumption """
	elif jx1 == x1 and jy1 == y1 and jy2 == y2:
		ConsolidateCondConnect(['0_0_0_0'], b, 'Total_Consumption', tree)
		return

	# """ Case 2: Consume whole bottom """
	elif jx1 == x1 and jy1 == y1 and jy2 < y2:
		C1 = CoordToBlock([x1, x2, jy2, y2])
		ConsolidateCondConnect([C1], b, 'Consume_Bottom', tree)
		return

	# """ Case 3: Consume whole top """
	elif jx1 == x1 and jy1 > y1 and jy2 == y2:
		C1 = CoordToBlock([x1, x2, y1, jy1])
		ConsolidateCondConnect([C1], b, 'Consume_Top', tree)
		return

	# """ Case 4: Consume middle part """
	elif jx1 == x1 and jy1 > y1 and jy2 < y2:
		C1 = CoordToBlock([x1, x2, jy2, y2])
		C2 = CoordToBlock([x1, x2, y1, jy1])
		ConsolidateCondConnect([C1,C2], b, 'Parallel', tree)
		return

	# """ Case 5: L_Shape at top left corner """
	elif jx1 > x1 and jy1 == y1 and jy2 < y2:
		C1 = CoordToBlock([x1, jx1, y1, y2])
		C2 = CoordToBlock([jx1, x2, jy2, y2])
		ConsolidateCondConnect([C1,C2], b, 'L_Shape', tree)
		return

	# """ Case 6: L_shpe at bottom left corner """
	elif jx1 > x1 and jy1 > y1 and jy2 == y2:
		C1 = CoordToBlock([x1, jx1, y1, y2])
		C2 = CoordToBlock([jx1, x2, y1, jy1])
		ConsolidateCondConnect([C1,C2], b, 'L_Shape', tree)
		return

	# """ Case 7: Consume whole right """
	elif jx1 > x1 and jy1 == y1 and jy2 == y2:
		C1 = CoordToBlock([x1, jx1, y1, y2])
		ConsolidateCondConnect([C1], b, 'Consume_Right', tree)
		return

	# """ Case 8: C shape"""
	elif jx1 > x1 and jy1 > y1 and jy2 < y2:
		C1 = CoordToBlock([x1, jx1, y1, y2])
		C2 = CoordToBlock([jx1, x2, jy2, y2])
		C3 = CoordToBlock([jx1, x2, y1, jy1])
		ConsolidateCondConnect([C1, C2, C3], b, 'C_Shape', tree)
		return





	


































































	



























