from MIR_Dict_Class import *
from MIR_Dict_fcns import *

# Corner 1 is the bottom left corner.


def CalCorner_1(blockName, job_dta, W, L, tree):
	feasibility, potChain = Feasibility_C1(blockName, job_dta, tree)
	if feasibility:
		# print 'Check point 1'
		treeAfter = DuplicateTree(tree)
		treeAfter = UpdateTree_C1(blockName, job_dta, treeAfter)
		mirArea, mirCoord = CalMirTree(treeAfter, W, L)
		return feasibility, treeAfter, mirArea, mirCoord
	else:
		# print 'Check point 2'
		return feasibility, None, None, None






def PotentialChain_C1(blockName, tree):
	coord = BlockToCoord(blockName)
	floor = coord[2]
	return PC_C1_Rec(blockName, floor, tree)

def PC_C1_Rec(blockName, floor, tree):
	coord = BlockToCoord(blockName)
	if not tree[blockName][1]:
		return [blockName]
	else: 
		for b in tree[blockName][1]:
			nextcoord = BlockToCoord(b)
			if floor >= nextcoord[2] and floor < nextcoord[3]:
				return [blockName] + PC_C1_Rec(b, floor, tree)
		return [blockName]





def Feasibility_C1(blockName, job, tree):
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
	potChain_all = PotentialChain_C1(blockName, tree)
	rightPoint = x1 + w
	potChain = [b for b in potChain_all if rightPoint > BlockToCoord(b)[0]]
	potChain_ceilings = min([BlockToCoord(b)[3] for b in potChain])
	potChain_width = BlockToCoord(potChain[-1])[1] - x1

	if potChain_ceilings - floor >= l and w <= potChain_width:
		return True, potChain
	else:
		return False, []


def UpdateTree_C1(startBlockName, job, tree):
	feasibility, influencedChain = Feasibility_C1(startBlockName, job, tree)
	if not feasibility:
		print 'Warning(UpdateTree_C1.w1): Feasiblity is False, no updating required.\n'
		return 

	coord = BlockToCoord(startBlockName)
	w, l = job.dimension
	corner = [coord[0], coord[2]]
	lenInfluencedChain = len(influencedChain)
	tempTree = DuplicateTree(tree)
	jobCoverCoord = [corner[0], corner[0] + w, corner[1], corner[1] + l]

	for i, b in enumerate(influencedChain):
		if i == 0:
			UpdateTree_C1_T1(b, jobCoverCoord, tempTree)
		elif i > 0 and i < (lenInfluencedChain - 1):
			UpdateTree_C1_T2(b, jobCoverCoord, tempTree)
		elif i == (lenInfluencedChain - 1):
			UpdateTree_C1_T3(b, jobCoverCoord, tempTree)
	for b in influencedChain:
		DeleteBlock(b, tempTree)
	return tempTree

def UpdateTree_C1_T1(b, jobCoverCoord, tree):
	# Type 1 block (C1_T1) is the starting block
	# Get all necessary coordinates
	x1, x2, y1, y2 = BlockToCoord(b)
	jx1, jx2, jy1, jy2 = jobCoverCoord

	# The bottom left corner of the job and the starting block should overlap
	if x1 != jx1 or y1 != jy1:
		print 'Error(UpdateTree_C1_T1.e1): input should be the starting block, but it does not agree with the corner coordinates. \n'
		return
	
	# The height of the job should not exceed the ceiling
	if y2 < jy2:
		print 'Error(UpdateTree_C1_T1.e2): The job height exceeds the initial block'
		return

	# """ Case 1: Total Consumption """
	# If the job happens to consume all of the block, then delete the block from the tree
	if jx2 >= x2 and jy2 == y2:
		# Here the block should be deleted, but the deletion should be reserved to the end of the updating process
		# DeleteBlock(b, tree)
		ConsolidateCondConnect(['0_0_0_0'], b, 'Total_Consumption', tree)
		return

	# """ Case 2: Consume whole left part """
	if jx2 < x2 and jy2 == y2:
		C1 = CoordToBlock([jx2, x2, y1, y2])
		# print C1

		# CreateNewBlock(C1, tree)
		# SimplyConnect('root', C1, tree)
		# CondConnect_Child(C1, tree[b][1], tree)
		ConsolidateCondConnect([C1], b, 'Consume_Left', tree)

		return

	# """ Case 3: Consume whole bottom part """
	if jx2 >= x2 and jy2 < y2:
		C1 = CoordToBlock([x1, x2, jy2, y2])
		# CreateNewBlock(C1, tree)
		# CondConnect_Parent(C1, tree[b][0], tree)
		# CondConnect_Child(C1, tree[b][1], tree)
		ConsolidateCondConnect([C1], b, 'Consume_Bottom', tree)
		return

	# """ Case 4: L Shape """
	if jx2 < x2 and jy2 < y2:
		C1 = CoordToBlock([x1, jx2, jy2, y2])
		C2 = CoordToBlock([jx2, x2, y1, y2])
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



def UpdateTree_C1_T2(b, jobCoverCoord, tree):
	# Type 2 block(s) are the ones in the middle. And the job must go through type 2 blocks (otherwise, the block would be a type 3 block)
	# Get all necessary coordinates
	x1, x2, y1, y2 = BlockToCoord(b)
	jx1, jx2, jy1, jy2 = jobCoverCoord

	# Check input 
	if jx1 >= x1 or jx2 <= x2:
		print 'Error(UpdateTree_C1_T2.e1): jobCoverCoord does not exceed block width.'
		return
	elif jy1 < y1 or jy2 > y2:
		print 'Error(UpdateTree_C1_T2.e2): jobCoverCoord exceeds block height.'
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
		print 'Error(UpdateTree_C1_T2.e3): Unknown Error.'
		return


def UpdateTree_C1_T3(b, jobCoverCoord, tree):
	x1, x2, y1, y2 = BlockToCoord(b)
	jx1, jx2, jy1, jy2 = jobCoverCoord

	# Check input
	if jx1 >= x1 or jx2 > x2:
		print 'Error(UpdateTree_C1_T3.e0): jobCoverCoord width error.'
		return
	elif jy1 < y1 or jy2 > y2:
		print 'Error(UpdateTree_C1_T2.e2): jobCoverCoord exceeds block height.'
		return


	# """ Case 1: Total Consumption """
	elif jx2 == x2 and jy1 == y1 and jy2 == y2:
		ConsolidateCondConnect(['0_0_0_0'], b, 'Total_Consumption', tree)
		return

	# """ Case 2: Consume whole bottom """
	elif jx2 == x2 and jy1 == y1 and jy2 < y2:
		C1 = CoordToBlock([x1, x2, jy2, y2])
		ConsolidateCondConnect([C1], b, 'Consume_Bottom', tree)
		return

	# """ Case 3: Consume whole top """
	elif jx2 == x2 and jy1 > y1 and jy2 == y2:
		C1 = CoordToBlock([x1, x2, y1, jy1])
		ConsolidateCondConnect([C1], b, 'Consume_Top', tree)
		return

	# """ Case 4: Consume middle part """
	elif jx2 == x2 and jy1 > y1 and jy2 < y2:
		C1 = CoordToBlock([x1, x2, jy2, y2])
		C2 = CoordToBlock([x1, x2, y1, jy1])
		ConsolidateCondConnect([C1,C2], b, 'Parallel', tree)
		return

	# """ Case 5: L_Shape at top right corner """
	elif jx2 < x2 and jy1 == y1 and jy2 < y2:
		C1 = CoordToBlock([x1, jx2, jy2, y2])
		C2 = CoordToBlock([jx2, x2, y1, y2])
		ConsolidateCondConnect([C1,C2], b, 'L_Shape', tree)
		return

	# """ Case 6: L_shpe at bottom right corner """
	elif jx2 < x2 and jy1 > y1 and jy2 == y2:
		C1 = CoordToBlock([x1, jx2, y1, jy1])
		C2 = CoordToBlock([jx2, x2, y1, y2])
		ConsolidateCondConnect([C1,C2], b, 'L_Shape', tree)
		return

	# """ Case 7: Consume whole left """
	elif jx2 < x2 and jy1 == y1 and jy2 == y2:
		C1 = CoordToBlock([jx2, x2, y1, y2])
		ConsolidateCondConnect([C1], b, 'Consume_Left', tree)
		return

	# """ Case 8: Reverse C shape"""
	elif jx2 < x2 and jy1 > y1 and jy2 < y2:
		C1 = CoordToBlock([x1, jx2, jy2, y2])
		C2 = CoordToBlock([x1, jx2, y1, jy1])
		C3 = CoordToBlock([jx2, x2, y1, y2])
		ConsolidateCondConnect([C1, C2, C3], b, 'Reverse_C_Shape', tree)
		return





	


































































	



























