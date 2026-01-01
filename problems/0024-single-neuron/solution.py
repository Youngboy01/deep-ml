import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities=[]
	# Your code here
    for x in features:
        z = sum(w*xi for w,xi in zip(weights,x))+bias
        probabilities.append(1/(1+math.exp(-z)))
    n = len(labels)
    mse = sum((p-t)**2 for p,t in zip(probabilities,labels))
    mse /= n
	return probabilities, mse