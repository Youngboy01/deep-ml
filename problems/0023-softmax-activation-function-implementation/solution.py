import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
    max_s = max(scores)
    numerator = [math.exp(s-max_s) for s in scores]
    denominator = sum(numerator)
    probabilities = [n/denominator for n in numerator]
	return probabilities