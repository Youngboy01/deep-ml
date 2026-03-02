
import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
	a= sum(y_true)
	b = sum(y_pred)
	intersection = sum(y_true & y_pred)
	union = sum(y_true | y_pred)
	result = intersection/union
	return round(result, 3)
