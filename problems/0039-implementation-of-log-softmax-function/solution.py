import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	scores = np.asarray(scores)
	max_score = np.max(scores)
	log_total = np.log(np.sum(np.exp(scores-max_score)))
	return scores-max_score-log_total
	pass