def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    n=len(matrix)
    m=len(matrix[0])
    result= [[matrix[r][c]*scalar for c in range(n)] for r in range(m)]
	return result