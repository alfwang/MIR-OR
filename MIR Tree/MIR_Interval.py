from MIR_Class import *

def read_data(filename):
	# This function takes an .txt and outputs:
	# Num_Jobs: the number of jobs in the data set
	# Bin_Dimension: a list that contains the dimension of the bin
	# Job_List: Job List

	with open(filename,'r') as data:
		Jobs = [ map(int, line.strip().split(' ')) for line in data]
	# print Jobs
	Num_Jobs = Jobs[0]
	# print Num_Jobs
	Bin_Dimension = Jobs[1]
	# print	Bin_Dimension
	Job_List = [x[: 2] for i, x in enumerate(Jobs) if i > 1]
	# print Job_List
	return Num_Jobs, Bin_Dimension, Job_List


def Presort_1(Job_List):
	# Sorting all the job in descending order regarding area
	Sorted_Job_List = sorted(Job_List, key = lambda x: x[0] * x[1], reverse = True)
	return Sorted_Job_List



def CreateJobList(Num_Jobs,Job_List):
	# This function is called after sorting so as to create the job data structure to 
	# store the placement information
	FullJobList = []
	for i in range(Num_Jobs):
		job = job_dta(i+1,Job_List[i][0],Job_List[i][1])
		FullJobList.append(job)
	return FullJobList



def GetPaths_dfs(root):
	# This function gets all the full path from the root to leaves
	# For instance, this would return [[root,a,c],[root,a,d],[root,b,d],[root,b,e]] for the most tested example
	# Notice that since root is always in the out put, it should be exluded when generating sub-path
	# This function is written with the help of XTT

	if not root or not root.coord:
		return []
	if not root.children:
		return [[root]]
	path = []
	for node in root.children:
		if not path:
			path = [[root] + x for x in GetPaths_dfs(node)]
		else:
			path += [[root] + x for x in GetPaths_dfs(node)]
	return path

def ShowPath(path):
	pathlist = []
	# The path list should be a two layer list. For instance, [['root','A','D'],['root','B','D']]
	for p in path:
		pstring = []
		for node in p:
			pstring.append(node.coord)
		pathlist.append([pstring])
	print pathlist


# def FindFullPath(LeafList):
# 	FullPath = []
# 	for leaf in LeafList:
# 		SinglePath = [[leaf]]
# 		while leaf.parent != None:
# 			SinglePath.insert(0,leaf.parent)
# 			leaf = leaf.parent
# 		FullPath.append(SinglePath)
# 	return FullPath

def GenerateSubPath(SinglePath):
	# This function generates all subpath of a fullpath which starts from the root and end with a leaf
	# For instance if the SinglePath is [A,B,C], the the output should be [[A],[B],[C],[A,B],[B,C],[A,B,C]]
	AllSubPath = []
	N = len(SinglePath)
	for n in range(1,N+1):
		for k in range(0,N-n+1):
			AllSubPath.append(SinglePath[k:k+n])
	return AllSubPath

def Cal_MIR_Cross(Path):
	# The input should be a sub-path in the tree which does not include the root.
	# Function returns:
	# Case 1: If MIR_Cross>0, return [MIR_Cross, MIR_Cross coord]
	# Case 2: If MIR_Cross=0, return [0, [0,0,0,0]]
	if len(Path) == 1:
		MIR_Cross = (Path[0].coord[1]-Path[0].coord[0]) * (Path[0].coord[3]-Path[0].coord[2])
		MIR_Cross_Coord = Path[0].coord
		# print 'Only one block, fast process'
		return MIR_Cross, MIR_Cross_Coord


	x_1 = Path[0].coord[0]
	x_2 = Path[-1].coord[1]
	if x_2 <= x_1:
		print 'Error: x_2<= x_1'
	
	y_1 = []
	for b in Path:
		y_1.append(b.coord[2])
	
	y_2 = []
	for b in Path:
		y_2.append(b.coord[3])

	y_1_max = max(y_1)
	y_2_min = min(y_2)
	if y_1_max < y_2_min:
		MIR_Cross = (y_2_min - y_1_max) * (x_2 - x_1)
		MIR_Cross_Coord = [x_1, x_2, y_1_max, y_2_min]
	else:
		MIR_Cross = 0
		MIR_Cross_Coord = [0, 0, 0, 0]
	return MIR_Cross, MIR_Cross_Coord




def Cal_MIR_Bin(BinRoot):
	FullPathList = GetPaths_dfs(BinRoot)
	MIR_Area = 0
	MIR_Area_Coord = []

	FullSubPathList =[]
	for p in FullPathList:
		NewSubPath = GenerateSubPath(p[1:len(p)+1])
		FullSubPathList = FullSubPathList + NewSubPath
	for sub_p in FullSubPathList:
		Temp_MIR, Temp_MIR_Coord = Cal_MIR_Cross(sub_p)
		if Temp_MIR > MIR_Area:
			MIR_Area = Temp_MIR
			MIR_Area_Coord = Temp_MIR_Coord
	return MIR_Area, MIR_Area_Coord







# Main function:

# if __name__ == '__main__':
	
# 	# Reading Data -----------------------------------------------
# 	filename = 'gcut1.txt'
# 	Num_Jobs, Bin_Dimension, Job_List = read_data(filename)
# 	print Num_Jobs, Bin_Dimension, Job_List 
	
# 	print 'Bin Dimension:'
# 	print Bin_Dimension
# 	W = Bin_Dimension[0]
# 	L = Bin_Dimension[1]

# 	# Initialize Bin -----------------------------------------------
# 	Bin_List = []
# 	NumberBinUsed = 1
# 	Bin_List.append(NewBin(1,W,L))

# 	# Presorting Jobs and create job list -----------------------------------------------
# 	Job_List = Presort_1(Job_List)
# 	FullJobList = CreateJobList(Num_Jobs,Job_List)
# 	print 'Full Job List:'
# 	for j in FullJobList:
# 		print j.index, j.dimension, j.bin, j.coord

# 	# Packing jobs
# 	for jobindex, CurrentJob in enumerate(FullJobList):
# 		BinFeasibility = []
# 		BinPlacement = []
# 		BinScore = []
# 		for i, CurrentBin in enumerate(Bin_List):
# 			feasibility, placement, MIR_before, MIR_after = BinJobPlacement(CurrentBin, CurrentJob)
			
# 			# MIR Score Calculation
# 			CurrentScore = MIR_before + MIR_after

# 			BinFeasibility.append(feasibility)
# 			BinPlacement.append(placement)
# 			BinScore.append(CurrentScore)

# 		if sum(BinFeasibility)>0:
# 			OptBinIndex = [i for i,j in enumerate(BinScore) if j == max(BinScore)]
# 			OptBinIndex = OptBinIndex[0]
			
# 			OptBin = Bin_List[OptBinIndex]
# 			Updated_Bin = UpdateBin(OptBin,CurrentJob,BinPlacement[OptBinIndex])
# 			Bin_List[OptBinIndex] = Updated_Bin

# 			Updated_Job = UpdateJob(CurrentJob,OptBin,BinPlacement[OptBinIndex])
# 			FullJobList(jobindex) = Updated_Job
# 		else:
# 			NumberBinUsed = NumberBinUsed + 1
# 			Bin_List.append(NewBin(NumberBinUsed - 1, W, L))

# 			OptBinIndex = NumberBinUsed - 1

# 			OptBin = Bin_List[OptBinIndex]
# 			Updated_Bin = FirstJobNewBin(OptBin,CurrentJob)
# 			Bin_List[OptBinIndex] = Updated_Bin

# 			Updated_Job = UpdateJob(CurrentJob,OptBin,[0,0,0,0]])
# 			FullJobList(jobindex) = Updated_Job




