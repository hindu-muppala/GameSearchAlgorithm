MAX, MIN = 1000, -1000
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha,beta):
 
 	if depth == 3:
 		return values[nodeIndex]
 	if maximizingPlayer:
 
 		best = MIN
 		for i in range(0, 2):
 
 			val = minimax(depth + 1, nodeIndex * 2 + i, False,values, alpha, beta)
 
	        	best = max(best, val)
 
	        	alpha = max(alpha, best)

 	        	if beta <= alpha:
 		    		break
 		return best

	else: 


 		best = MAX
 		for i in range(0, 2):
 # Recursively call minimax for the child nodes
			 val = minimax(depth + 1, nodeIndex * 2 + i, True,
values, alpha, beta)
 # Update the best value
 			best = min(best, val)
 # Update beta with the minimum value seen so far
 			beta = min(beta, best)
 # Perform alpha-beta pruning
 		if beta <= alpha:
 break
 			return best
# Sample values for the nodes in the tree
values = [3, 18, 6, 9, 1, 2, 0, -1]
# Perform minimax algorithm starting from the root node
print("The optimal value is:", minimax(0, 0, True, values, MIN,
MAX)) 
