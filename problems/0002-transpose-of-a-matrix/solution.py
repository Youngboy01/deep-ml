def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    n = len(a)
    m = len(a[0])
    b = [[a[r][c] for r in range(n)] for c in range(m)]
    return b
        
    pass