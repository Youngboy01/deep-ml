import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    
    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')
    
    Returns:
        The computed norm as a float
    """
    # Your code here
    l2norm = np.sqrt(np.sum(arr**2))
    l1norm = np.sum(np.abs(arr))
    fronorm = np.sqrt(np.sum(arr**2))
    if norm_type == 'l2':
        return l2norm
    elif norm_type == 'l1':
        return float(l1norm)
    else:
        return fronorm
    pass