from MIR_Dict_Class import *


""" Converting string notation to interval notation and reverse function 
	------------------------------------------------------------------------------------------ """

def BlockToCoord(blockName):
	coord = [int(x) for x in blockName.split('_')]
	return coord

def BlockToCorner(blockName, cornerType):
	coord = BlockToCoord(blockName)
	if cornerType == 1:
		Corner = [coord[0], coord[2],1]
	elif cornerType == 2:
		Corner = [coord[0], coord[3],2]
	elif cornerType == 3:
		Corner = [coord[1], coord[3],3]
	elif cornerType == 4:
		Corner = [coord[1], coord[2],4]
	return Corner



def CoordToBlock(coord):
	blockName = '_'.join([str(x) for x in coord])
	return blockName







""" Reading and sorting jobs
	------------------------------------------------------------------------------------------ """
def ReadData(filename):
	# This function takes an .txt and outputs:
	# number: the number of jobs in the data set
	# binDimension: a list that contains the dimension of the bin
	# jobList: job list

	with open(filename,'r') as data:
		jobs = [ map(int, line.strip().split(' ')) for line in data]
	# print jobs
	numJobs = jobs[0]
	# print numJobs
	binDimension = jobs[1]
	# print	binDimension
	jobList = [x[: 2] for i, x in enumerate(jobs) if i > 1]
	# print Job_List
	return numJobs, binDimension, jobList


def Presort_1(jobList):
	# Sorting all the job in descending order regarding area
	sortedJobList = sorted(jobList, key = lambda x: x[0] * x[1], reverse = True)
	return sortedJobList



def CreateJobList(numJobs,jobList):
	# This function is called after sorting so as to create the job data structure to 
	# store the placement information
	numJobs = numJobs[0]
	fullJobList = []
	for i in range(0, numJobs):
		job = job_dta(i+1, jobList[i][0], jobList[i][1])
		fullJobList.append(job)
	return fullJobList






""" Calculating MIR
	------------------------------------------------------------------------------------------ """
def GetPaths_Dfs(root,tree):
	# 
	if not root or not tree[root]:
		return []
	if not tree[root][1]:
		return [[root]]
	path = []
	for node in tree[root][1]:
		if not path:
			path = [[root] + x for x in GetPaths_Dfs(node, tree)]
		else:
			path += [[root] + x for x in GetPaths_Dfs(node, tree)]
	return path

def GenerateSubPath(bin):
	path = GetPaths_Dfs('root', bin.tree)
	fullSubPath = []
	for p in path:
		N = len(p)
		for n in range(1, N + 1):
			for k in range(1, N - n + 1):
				temp = p[k: k + n]
				if temp not in fullSubPath:
					fullSubPath.append(temp)
	return fullSubPath


def CalMirCross(singlePath,L):
	if len(singlePath) == 1:
		coord = BlockToCoord(singlePath[0])
		mirCross = (coord[1] - coord[0]) * (coord[3] - coord[2])
		return mirCross, coord

	leftCoord = BlockToCoord(singlePath[0])
	rightCoord = BlockToCoord(singlePath[-1])
	x_left = leftCoord[0]
	x_right = rightCoord[1]
	if x_right <= x_left:
		print '\n\n\nError(CalMirCross.e1): leftCoord-->', leftCoord, 'rightCoord-->', rightCoord, '\n\n\n'

	y_lower = 0
	y_upper = L
	for b in singlePath:
		coord = BlockToCoord(b)
		if coord[2] > y_lower:
			y_lower = coord[2]
		if coord[3] < y_upper:
			y_upper = coord[3]

	if y_upper > y_lower:
		mirCross = (x_right - x_left) * (y_upper - y_lower)
		mirCrossCoord = [x_left, x_right, y_lower, y_upper]
		return mirCross, mirCrossCoord
	else:
		mirCross = 0
		mirCrossCoord = [0, 0, 0, 0]
		return mirCross, mirCrossCoord

def CalMirBin(bin):
	fullSubPath = GenerateSubPath(bin)
	mirArea = 0
	mirCoord = []
	L = bin.dimension[1]
	for p in fullSubPath:
		tempMirArea, tempMirCoord = CalMirCross(p,L)
		if tempMirArea > mirArea:
			mirArea = tempMirArea
			mirCoord = [tempMirCoord]
		elif tempMirArea == mirArea:
			mirCoord.append(tempMirCoord)
	return mirArea, mirCoord


def CalMirTree(tree, W, L):
	# Since the functions above requires input to be the bin when calculating MIR
	# This function quickly generate a tempbin and calculate MIR without making much changes to the 
	# functions above
	blockList = tree.keys()
	blockList.remove('root')
	temp_Bin = tempbin(tree, W, L, blockList)
	mirArea, mirCoord = CalMirBin(temp_Bin)
	return mirArea, mirCoord



def CalBinArea(mirBin):
	# This function calculates the remaining area of a bin 
	area = 0
	# print mirBin.blockList
	for b in mirBin.blockList:
		if b != 'root':
			coord = BlockToCoord(b)
			area += (coord[1]-coord[0]) * (coord[3]-coord[2])
	return area




""" Connecting and disconnecting blocks
	------------------------------------------------------------------------------------------ """


def DuplicateTree(inputTree):
	outputTree = {x: [[y1 for y1 in inputTree[x][0]], [y2 for y2 in inputTree[x][1]]] for x in inputTree}
	return outputTree

def IntervalOverlap(interval_1, interval_2):
	# This will be used as a subfunction of Overlap.
	# This function take two intervals on the same axis and find out whether they overlap
	# If overlap, return the overlapping interval; otherwise return false
	# Note: if two intervals intersect at a single point, the function returns False
	a, b = interval_1
	c, d = interval_2
	# Data check
	olp = [-1, 0]
	if a >= b or c >= d:
		print '\n\n\nError(IntervalOverlap.e1) in the interval input\n\n\n'
	elif c <= a and a <= d and d <= b:
		olp = [a, d]
	elif a <= c and d <= b:
		olp = [c, d]
	elif a <= c and c <= b and b <= d:
		olp = [c, b]
	elif c <= a and b <= d:
		olp = [a, b]

	if olp == [-1,0] or olp[0] == olp[1]:
		return False
	else:
		return olp



def IsConnect(leftBlock, rightBlock):
	# This function takes two blockName input and check whether they are connected.
	# Function does not allow input to be 'root'
	leftCoord = BlockToCoord(leftBlock)
	rightCoord = BlockToCoord(rightBlock)
	if leftCoord[1] == rightCoord[0] and IntervalOverlap([leftCoord[2], leftCoord[3]], [rightCoord[2], rightCoord[3]]):
		return True
	else:
		return False


def SimplyConnect(block1, block2, tree):
	# This function requires all inputs exist before calling
	# print 'Fcn SimplyConnect--Check Input: block1/block2:', block1, block2
	if block1 == 'root':
		if tree[block2][0]:
			print 'Error(SimplyConnect.e0.1): Trying to connect block2 to root but block2.parent is not empty.'
			return
		else:
			tree['root'][1].append(block2)
			tree[block2][0].append('root')
			return
	elif block2 == 'root':
		if tree[block1][0]:
			print 'Error(SimplyConnect.e0.2): Trying to connect block2 to root but block2.parent is not empty.'
			return
		else:
			tree['root'][1].append(block1)
			tree[block1][0].append('root')
			return
	else:
		c1 = BlockToCoord(block1)
		c2 = BlockToCoord(block2)
		
		if c1[1] == c2[0]:
			leftBlock = block1
			rightBlock = block2
		elif c1[0] == c2[1]:
			leftBlock = block2
			rightBlock = block1
		else:
			print '\n\n\nError(ConnectBlocks.e1): X COORDINATES OF 2 BLOCKS ARE NOT ALIGNED\n\n\n'
			return

		if not IsConnect(leftBlock, rightBlock):
			print '\n\n\nError(ConnectBlocks.e2): TWO BLOCKS ARE NOT CONNECTED\n\n\n'
			return

		if rightBlock in tree[leftBlock][1] or leftBlock in tree[rightBlock][0]:
			print '\n\n\nWarning(ConnectBlocks.w1): AT LEAST ONE BLOCK IS IN THE OTHER ONE\' LIST.\n\n\n'
			return
		else:
			tree[leftBlock][1].append(rightBlock)
			tree[rightBlock][0].append(leftBlock)
			return




def CreateNewBlock(blockName, tree):
	if blockName in tree:
		print '\n\nWanrnig(CreateNewBlock.w1): The block already exists in the tree. Please check for duplication.\n\n'
		return
	else:
		tree[blockName] = [[], []]

def CondConnect_Parent(targetBlock, refParentList, tree):
	# 	 This function creates a block and a reference parent list. It goes through the parent list and check if the target block
	# 	 is connected on the right
	# 	 If the new parent list is empty, the function will add 'root' to the new parent list
	if targetBlock not in tree:
		CreateNewBlock(targetBlock, tree)

	newParentList = []

	if refParentList == ['root']:
		tree[targetBlock][0] = ['root']
		tree['root'][1].append(targetBlock)
	else:
		newParentList.extend([b for b in refParentList if IsConnect(b, targetBlock)])
		if not newParentList:
			newParentList.append('root')
		tree[targetBlock][0] = newParentList
		for p in newParentList:
			tree[p][1].append(targetBlock)



def CondConnect_Child(targetBlock, refChildList, tree):
	# This function creates a new block and look at a reference child list. It goes through the child list and check if the target block
	# is connected on the left.

	if targetBlock not in tree:
		CreateNewBlock(targetBlock, tree)

	newChildList = []
	newChildList.extend([b for b in refChildList if IsConnect(targetBlock, b)])
	tree[targetBlock][1] = newChildList
	for c in newChildList:
		tree[c][0].append(targetBlock)


def DeleteBlock(blockName, tree):
	# This function deletes a block from a tree dictionary and all the arcs that associated with the block
	if blockName not in tree:
		print 'Error(DeleteBlock.e1): The block is not in the tree'
		return
	else:
		for p in tree[blockName][0]:
			tree[p][1].remove(blockName)
		for c in tree[blockName][1]:
			tree[c][0].remove(blockName)
			if not tree[c][0]:
				tree[c][0].append('root')
				tree['root'][1].append(c)
		del tree[blockName]

# def TotalConsumption(targetBlock, tree):
# 	# Total consumption means that the block is totally consumed by (part of) the job.
# 	# So two steps are carried out:
# 	# Step 1: remove the block from the tree
# 	# Step 2: go through the childList of the target block. If a block's parentList is empty, add 'root' to it. 
# 	if targetBlock not in tree:
# 		print 'Error(TotalConsumption.e1): The block is not in the tree'
# 		return
# 	else:
# 		DeleteBlock(targetBlock, tree)
		
# 		# print '=> => => => => => => => => =>'
# 		# print 'influencedChildList: ', influencedChildList
# 		# print 'before Connecting with the root'
# 		# DisplayTree(tree)
# 		# print '<= <= <= <= <= <= <= <= <= <='

# 		# for b in influencedChildList:
# 		# 	if not tree[b][0]:
# 		# 		tree[b][0].append('root')
# 		# 		tree['root'][1].append(b)
# 		# 		print 'haha'


def ConsolidateCondConnect(targetBlockList, refBlock, Option, tree):
	# This function does CreateNewBlock, CondConnect_Parent, CondConnect_Child altogther
	# initialize refList 
	OptionList = ['Total_Consumption', 'Consume_Left', 'Consume_Right', 'Consume_Bottom', 'Consume_Top', 'Parallel', 'L_Shape', 'C_Shape', 'Reverse_C_Shape']
	if Option not in OptionList:
		print 'Error(ConsolidateCondConnect.e0): No option match.'
		return

	if refBlock not in tree:
		print 'Error(ConsolidateCondConnect.e1): the refBlock not in tree.'
		return

	for C in targetBlockList:
		if C in tree:
			print 'Error(ConsolidateCondConnect.e2): target blocks already in tree.'
			return

	
	refParentList = tree[refBlock][0]
	refChildList = tree[refBlock][1]
	lenTargetBlockList = len(targetBlockList)

	# print 'length of target block list:', targetBlockList, ':', lenTargetBlockList

	if lenTargetBlockList == 1:
		# Create one new block
		C1 = targetBlockList[0]
		

		if Option == 'Total_Consumption':
			# print 'Operate: Total_Consumption / Input:', Option
			# waiting for the block to be delete
			return
		
		CreateNewBlock(C1, tree)
		if Option == 'Consume_Left':
			# print 'Operate: Consume_Left / Input:', Option
			SimplyConnect('root', C1, tree)
			CondConnect_Child(C1, tree[refBlock][1], tree)
			return

		if Option == 'Consume_Right':
			# print 'Operate: Consume_Right / Input:', Option
			CondConnect_Parent(C1, tree[refBlock][0], tree)
			return

		if Option == 'Consume_Bottom' or Option == 'Consume_Top':
			# print 'Operate: Consume_Bottom(Top) / Input:', Option
			CondConnect_Parent(C1, tree[refBlock][0], tree)
			CondConnect_Child(C1, tree[refBlock][1], tree)
			return
	
	elif lenTargetBlockList == 2:
		# Create two new blocks
		C1, C2 = targetBlockList
		CreateNewBlock(C1, tree)
		CreateNewBlock(C2, tree)

		if Option == 'Parallel':
			# print 'Operate: Parallel / Input:', Option
			CondConnect_Parent(C1, tree[refBlock][0], tree)
			CondConnect_Child(C1, tree[refBlock][1], tree)
			CondConnect_Parent(C2, tree[refBlock][0], tree)
			CondConnect_Child(C2, tree[refBlock][1], tree)
			return

		if Option == 'L_Shape':
			# print 'Operate: L_Shape / Input:', Option
			CondConnect_Parent(C1, tree[refBlock][0], tree)
			SimplyConnect(C1, C2, tree)
			CondConnect_Child(C2, tree[refBlock][1], tree)
			return



	elif lenTargetBlockList == 3:
		C1, C2, C3 = targetBlockList
		CreateNewBlock(C1, tree)
		CreateNewBlock(C2, tree)
		CreateNewBlock(C3, tree)

		if Option == 'C_Shape':
			# print 'Operate: C_Shape / Input:', Option
			CondConnect_Parent(C1, tree[refBlock][0], tree)
			SimplyConnect(C1, C2, tree)
			SimplyConnect(C1, C3, tree)
			CondConnect_Child(C2, tree[refBlock][1], tree)
			CondConnect_Child(C3, tree[refBlock][1], tree)
			return

		if Option == 'Reverse_C_Shape':
			# print 'Operate: Reverse_C_Shape /Input:', Option
			CondConnect_Parent(C1, tree[refBlock][0], tree)
			CondConnect_Parent(C2, tree[refBlock][0], tree)
			SimplyConnect(C1, C3, tree)
			SimplyConnect(C2, C3, tree)
			CondConnect_Child(C3, tree[refBlock][1], tree)
			return

	else:
		print 'Error(ConsolidateCondConnect.e4): Unknown Error.'
		return





		

		




		













""" Display output and Visualization
	------------------------------------------------------------------------------------------ """

def DisplayTree(tree):
	# Display tree in a dictionary format
	if tree == [] or not tree:
		print 'Warning(DisplayTree.w1): Empty Tree\n'
		return
	print '\nDisplay Tree: ~~~~~~~~~~~~~~~~~~\n'
	treeKeys = tree.keys()
	treeKeys.sort()
	print '\033[91m',treeKeys[-1], ' parent: ', tree[treeKeys[-1]][0], ' children: ', tree[treeKeys[-1]][1], '\033[0m'

	treeKeys = sorted(treeKeys[: -1], key = lambda x: int(x.split('_')[0]))

	init = 'ro'
	for b in treeKeys:
		if b[0:2] != init:
			print '\033[91m|\033[0m'
			init = b[0:2]
		print '\033[91m', b, ' parent: ', tree[b][0], ' children: ', tree[b][1], '\033[0m'
	print '\nEnd ~~~~~~~~~~~~~~~~~~\n'



def DisplayBin(mirBin):
	# Display Bin
	print '\nDisplay Bin: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n'
	print 'Bin Index:  ', mirBin.index
	print 'Bin Dimension: ', mirBin.dimension
	print 'Bin Total Area:  ', mirBin.area
	print 'Bin MIR Area:  ', mirBin.mir
	print 'Bin Mir Coord:  ', mirBin.mirCoord
	print 'Bin BlockList(except root):  ', mirBin.blockList
	print 'Jobs placed in this bin:  ', mirBin.jobPlaced
	DisplayTree(mirBin.tree)

def DisplayJob(job_dta):
	print '\nDisplay Job: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n'
	print 'Job index: ', job_dta.index
	print 'Job dimension: ', job_dta.dimension
	print 'Job Area: ', job_dta.area
	print 'Job placed in bin #', job_dta.bin
	print 'Job placed at Corner ', job_dta.coord[0:-1], '-- Type ', job_dta.coord[-1], '\n'

	

def DisplayFinalResult(totalNumBin, binList, fullJobList):
	# binList
	for b in binList:
		DisplayBin(b)
	for job in fullJobList:
		DisplayJob(job)

	print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
	print 'Total Number of Bins used: ', totalNumBin
	print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'













		










