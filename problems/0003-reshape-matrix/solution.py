import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    m,n = len(a),len(a[0])
    r,c = new_shape
    if m^n^r^c !=0:
        return []
    reshaped_matrix = [a[i*c:(i+1)*c] for i in range(r)]
	return reshaped_matrix