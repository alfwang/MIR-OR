def corner1(blockName, tree, jobDta):
	
	get corner coordinate from blockName
	get job dimension

	if Feasibility_1(blockName, tree, job):
		feasibility = 1
		tempTree = update(blockName, tree, job)
		calculate mirArea and mirCoord of tempTree
		return feasibilty, tempTree, mirArea, mirCoord
	else:
		feasibility = 0
		mirCoord = None
		mirArea = None
		tempTree = None
		return feasibility, tempTree, mirArea, mirCoord

def Feasibility_C1(blockName, tree, job):
	w, l = jobDimension
	x1, x2, y1, y2 = BlockToCoord(blockName)
	floor = y1
	ceiling = y2
	init_cap_x = x2 - x1
	cap_y = y2 - y1

	PotentialChain_C1 = PotentialChain_C1(blockName, tree)

	influencedBlock = []

	""" Case 1: 
		The job height exceeds the block height, so feasilibity is false"""
	if l > cap_y:
		return False, influencedBlock

	""" Case 2:
		The job width <= cap_x, job height <= cap_y
		i.e. job fully in current block. """
	if w <= cap_x and l <= cap_y:
		influencedBlock.append(blockName)
		return True, influencedBlock

	""" Case 3:
		The job height <= cap_y, but job width > cap_x, then a search is needed. """
	if w > cap_x and l <= cap_y:
		influencedBlock.append(blockName)
		job cover coord =  corner coord + job dimension
		while job is not fully covered:
			go through effectiveChain









def EffectiveChain(blockName, tree):
	_n, coord = BlockToCoord(blockName)
	floor = coord[2]
	effectiveChain = [blockName]
	currentBlock = blockName
	while tree[currentBlock][1]:
		for b in tree[currentBlock][1]:
			_n, nextcoord = BlockToCoord(b)
			if floor >= nextcoord[2] and floor < nextcoord[3]:
				effectiveChain.append(b)
				currentBlock = b
				continue
	return effectiveChain











def UpdateTree(blockName, tree, job):
