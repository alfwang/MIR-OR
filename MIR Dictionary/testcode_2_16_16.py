from MIR_Dict_fcns import *
from MIR_Dict_Class import *

if __name__ == '__main__':
	""" TestCase 1 """
	# print CoordToBlock(1, [2,3,4,5])
	# testTree = {'root': [[], ['a', 'b']], \
	# 	'a': [['root'], ['c']], \
	# 	'b': [['root'], ['d', 'e']], \
	# 	'c': [['a'], ['f', 'g']], \
	# 	'd': [['b'], ['g', 'h']], \
	# 	'e': [['b'], ['h', 'i']], \
	# 	'f': [['c'], []], \
	# 	'g': [['c', 'd'], []], \
	# 	'h': [['d', 'e'], []], \
	# 	'i': [['e'], []]}

	# testBin = testbin(testTree)
	# path = GetPaths_Dfs('root', testTree)
	# print path
	# print len(path)
	# print GenerateSubPath(testBin)
	# """ TestCase 1 """
	# testbin = bin(1,10,20)
	# b1 = '1_0_5_0_5'
	# b2 = '1_5_10_1_11'
	# testbin.tree = {'root':[[], [b1]], \
	# 	b1: [['root'], [b2]], \
	# 	b2: [[b1], []]}	
	# mirArea,  mirCoord = CalMirBin(testbin)	
	# print mirArea, mirCoord



	""" TestCase 2 """
	# testbin = bin(1,10,20)
	# b1 = '1_0_1.5_2.2_6.1'
	# b2 = '1_1.5_3_2.5_7'
	# b3 = '1_3_6_0_5'
	# testbin.tree = {'root':[[], [b1]], \
	# 	b1: [['root'], [b2]], \
	# 	b2: [[b1], [b3]], \
	# 	b3: [[b2], []]}	
	# mirArea,  mirCoord = CalMirBin(testbin)	
	# print mirArea, mirCoord

	""" TestCase 3 """
	# testbin = bin(1,10,20)
	# b1 = '1_0_5_0_5'
	# b2 = '1_0_4_7_10'
	# b3 = '1_4_10_6_10'
	# testbin.tree = {'root':[[], [b1,b2]], \
	# 	b1: [['root'], []], \
	# 	b2: [['root'], [b3]], \
	# 	b3: [[b2], []]}	
	# mirArea,  mirCoord = CalMirBin(testbin)	
	# print mirArea, mirCoord

	""" TestCase 4 """
	# testbin = bin(1,10,20)
	# b1 = '1_0_5_4_5'
	# b2 = '1_0_5_1_3'
	# b3 = '1_5_6_0_6'
	# testbin.tree = {'root':[[], [b1,b2]], \
	# 	b1: [['root'], [b3]], \
	# 	b2: [['root'], [b3]], \
	# 	b3: [[b1, b2], []]}	
	# mirArea,  mirCoord = CalMirBin(testbin)	
	# print mirArea, mirCoord


	""" Testing IsConnect """
	# leftBlock = '1_0_5_0_5'
	# rightBlock = '1_5_6_4_10'
	# print IsConnect(leftBlock, rightBlock)

	""" Testing ConnectBlocks """
	# testTree = {'root': [[], ['1_0_5_0_5']], \
	# 	'1_0_5_0_5': [['root'], []], \
	# 	'1_5_10_4_8': [[],[]]}
	# print 'testTree: \n', testTree, '\n ----------------- \n'
	# print IsConnect('1_0_5_0_5', '1_5_10_4_8')
	# newtree = ConnectBlocks(testTree, '1_0_5_0_5', '1_5_10_4_8')	
	# print 'old test tree: \n', testTree, '\n\n\n'
	# print 'new tree: \n', newtree, '\n\n\n'

	""" Testing DuplicateTree """
	# t1 = {'a': [[0], [1]], 'b': [[2], [3]]}
	# t2 = DuplicateTree(t1)
	# t2['a'][0].append('t2 tag')
	# t3 = DuplicateTree(t1)
	# t3['a'][0].append('t3 tag')

	# print t1
	# print t2
	# print t3








































