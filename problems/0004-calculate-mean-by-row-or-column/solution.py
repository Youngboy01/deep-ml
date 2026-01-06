import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    n = len(matrix)
    m = len(matrix[0])
    if mode=='column':
        means=np.mean([[matrix[r][c] for r in range(n)] for c in range(m)],axis=1)
    elif mode=='row':
        means=np.mean([[matrix[r][c] for c in range(m)] for r in range(n)],axis=1)
	return means