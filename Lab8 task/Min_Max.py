import os 
import math
os.system('cls')
def min_max (curDepth, Index,
			maxTurn, scores, 
			targetDepth):
	if (curDepth == targetDepth): 
		return scores[Index]
	
	if (maxTurn):
		return max(min_max(curDepth + 1, Index * 2, 
					False, scores, targetDepth), 
				min_max(curDepth + 1, Index * 2 + 1, 
					False, scores, targetDepth))
	else:
		return min(min_max(curDepth + 1, Index * 2, 
					True, scores, targetDepth), 
				min_max(curDepth + 1, Index * 2 + 1, 
					True, scores, targetDepth))
	

scores = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = math.log(len(scores), 2)
print("optimal value is : ", end = "")
print(min_max(0, 0, True, scores, treeDepth))