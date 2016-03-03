

class mirBin():
	def __init__(self, n, W, L):
		# Each block in the tree is represented by a sting, where
		# each dimension is separated by a underscore.
		# The four dimensions are the coordinate of the block
		# The convertion between string and coordination can be achieved with
		# 'BlockToCoord' and 'CoordToBlock' functions
		
		coord = [0, W, 0, L]
		firstBlock = '_'.join([str(x) for x in coord])
		# Tree is a dictionary that implies the structure of the bin. Each value
		# is a [[parent],[child]] form of list 
		# Each key is the block string
		self.tree = {'root': [[], [firstBlock]], \
			firstBlock: [['root'], []]}
		self.index = n
		self.dimension = [W, L]
		self.area = W * L
		self.mir = W * L 
		self.mirCoord = [0, W, 0, L]
		self.blockList = [firstBlock]
		self.jobPlaced = []
		# self.cornerList = [[1, 0, 0, firstBlock], [2, W, 0, firstBlock], [3, W, L, firstBlock], [4, 0, L, firstBlock]]

class testbin():
	def __init__(self,tree, W, L, blockList):
		self.tree = tree
		self.dimension = [W, L]
		self.blockList = blockList

class tempbin():
	""" This is exactly the same as testbin. But this is used to generate a temp bin 
		so as to calculate mir with only a tree """
	def __init__(self,tree, W, L, blockList):
		self.tree = tree
		self.dimension = [W, L]
		self.blockList = blockList

class job_dta():
	def __init__(self,n,w,l):
		# The job here is non-rotatable
		self.index = n
		self.dimension = [w,l]
		self.area = w * l
		self.bin = 0
		# job_dta.bin stores the bin number when a job is decided to be placed
		self.coord = [0, 0, 0]
		# job_dta.coord stores the coord of where the job is placed. 
		# the last dimension is the corner type
		# 1st and 2nd dimensions are (x,y)

class testjob():
	def __init__(self, dimension):
		self.dimension = dimension


