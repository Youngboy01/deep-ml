
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	v1abs  = (sum(num*num for num in v1))
	v1n = np.sqrt(v1abs)
	v2abs  = (sum(num*num for num in v2))
	v2n = np.sqrt(v2abs)

	cosine = np.dot(v1,v2)/np.dot(v1n,v2n)
	return cosine
	pass
