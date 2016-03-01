from MIR_Class import *


def IsConnect(LeftBlock,RightBlock):
	# This function takes two blocks and test if they are connected
	# This function neglects the children list of LeftBlock and the parent list of RightBlock

	(b1_x1, b1_x2, b1_y1, b1_y2) = LeftBlock.coord
	(b2_x1, b2_x2, b2_y1, b2_y2) = RightBlock.coord
	if b1_x2 == b2_x1 and IntervalOverlap([b1_y1, b1_y2], [b2_y1, b2_y2]):
		return True
	else:
		return False




def Connect(LeftBlock, RightBlock):
	# This function connect two blocks by adding the right block to the left block's children list
	# and by adding the left block to the right block's parent list
	# This function also checks the conditions that the two blocks are actually connected in the bin

	# Check whether two blocks are already in each other's list. If TRUE, then error
	if RightBlock in LeftBlock.children:
		print 'The right block (', RightBlock.coord,') already exists in the left block\'s (', LeftBlock.coord,')children list.'
		return
	if LeftBlock in RightBlock.parent:
		print 'The left block (', LeftBlock.coord,') already exists in the right block\'s (', RightBlock.coord,')parent list.'
		return


	# Check wether the two blocks are actually connected:
	if LeftBlock.coord[1] == RightBlock.coord[0] and LeftBlock.coord[3] > RightBlock.coord[2] and LeftBlock.coord[2] < RightBlock.coord[3]:
		LeftBlock.children.append(RightBlock)
		RightBlock.parent.append(LeftBlock)
		return LeftBlock, RightBlock
	else:
		print 'Some error has occured in the function Connect, please check whether the two blocks are actually connected.'


def Disconnect(LeftBlock,RightBlock):
	# This function disconnects two blocks by removing each block from the other's children/parent list
	# It also checks the condition necessary for such operation

	# Check whether two blocks are already in each other's list, if FALSE, then error
	if RightBlock not in LeftBlock.children:
		print 'The right block (', RightBlock.coord,') does not exist in the left block\'s (', LeftBlock.coord,')children list.'
		return
	if LeftBlock not in RightBlock.parent:
		print 'The left block (', LeftBlock.coord,') does not exist in the right block\'s (', RightBlock.coord,')parent list.'
		return

	# Check whether the two blocks are actually disconnected
	if LeftBlock.coord[1] == RightBlock.coord[0] and LeftBlock.coord[3] > RightBlock.coord[2] and LeftBlock.coord[2] < RightBlock.coord[3]:
		print 'The right block (', RightBlock.coord,') and the left block (', LeftBlock.coord,'). are actually connected'
	else:
		LeftBlock.children.remove(RightBlock)
		RightBlock.parent.remove(LeftBlock)

def IntervalOverlap(interval_1, interval_2):
	# This will be used as a subfunction of Overlap.
	# This function take two intervals on the same axis and find out whether they overlap
	# If overlap, return the overlapping interval; otherwise return false
	a, b = interval_1
	c, d = interval_2
	# Data check
	olp = [-1, 0]
	if a >= b or c >= d:
		print 'Error in the interval input'
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






def Overlap(B1, B2):
	# This function takes the coord of two blocks and examine whether the two blocks overlap

	coord_1_x = B1[0:2]
	coord_1_y = B1[2:4]
	coord_2_x = B2[0:2]
	coord_2_y = B2[2:4]

	# coord_1_x = B1.coord[0:2]
	# coord_1_y = B1.coord[2:4]
	# coord_2_x = B2.coord[0:2]
	# coord_2_y = B2.coord[2:4]

	olp_x = IntervalOverlap(coord_1_x, coord_2_x)
	olp_y = IntervalOverlap(coord_1_y, coord_2_y)

	if olp_x and olp_y:
		Overlap_Area = (olp_x[1] - olp_x[0]) * (olp_y[1] - olp_y[0])
		Overlap_Coord = olp_x + olp_y
	else:
		Overlap_Area = 0
		Overlap_Coord = []
	return Overlap_Area, Overlap_Coord

def InnerEdgePoint(p,rect):
	# This function decides geometrical relationship between a point [x,y] and a rectangle [x1, x2, y1, y2]
	# Output: 0 = p is outside rect
	#         1 = inner point
	#         2 = edge point
	#         3 = corner point

	x, y = p
	x1, x2, y1, y2 = rect
	if x1 < x and x < x2 and y1 < y and y < y2:
		output = 1
	elif (x1 == x or x2 == x) and y1 < y and y < y2:
		output = 2
	elif x1 < x and x < x2 and (y1 == y or y2 == y):
		output = 2
	elif p in [[x1,y1],[x1,y2],[x2,y1],[x2,y2]]:
		output = 3
	else:
		output = 0
	return output

















