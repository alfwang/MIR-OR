class BlockNode():
	def __init__(self, coord, children, parent):
		self.coord = coord  
		# this is the coordinate of the block
		# self.area = (coord[1]-coord[0]) * (coord[3]-coord[2])
		# area of the block
		self.children = children
		# children is a list, storing all the blocks connected on the right. If no block on the right, children =[]
		self.parent = parent
		# parent is a list, storing all the blocks connected on the left. If no block on the left, parent = root
		self.flag = ''
		# The flag is for indicating if a block should not appear in an updated tree. Used only in debugging

class NewBin():
	def __init__(self,n,W,L):
		root = BlockNode('root', [], [])
		# root is a blocknode, storing no coordinate. When initializing, the only child of the root is the block with full dimension. 
		B1 = BlockNode([0,W,0,L], [], [root])
		# When initializing, there is only one block. When initializing, this block is the only block connected to the root.
		root.children.append(B1)
		# Connecting the block to the root
		self.TreeRoot = root
		# TreeRoot is the root of the tree
		self.LeafList = [B1]
		# LeafList Stores all leaves in the tree
		self.index = n
		# index is the bin's number
		self.Area = W * L
		self.MIR = W * L
		self.MIR_Coord = [0,W,0,L]
		# MIR_Coord is the coordinate of the maximum inscribed rectangle
		self.BLockList = [B1]
		# BlockList stores all the non-root block in the tree
		self.CornerList = [[1,0,0,B1], [2,W,0,B1], [3,W,L,B1], [4,0,L,B1]]
		# In CornerList, the first dimension is the corner type:
		# 1 = bottom left corner
		# 2 = bottom right corner
		# 3 = top right corner 
		# 4 = top left corner
		# The second and third dimension is the coordinate [x,y] of the corner
		# The fourth dimension is the blocknode the corner belongs to



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
		# the first dimension is the corner type
		# 2nd and 3rd dimensions are (x,y)
