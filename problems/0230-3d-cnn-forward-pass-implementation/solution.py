import numpy as np

def conv3d_forward_pass(
    input_volume: np.ndarray,
    kernel: np.ndarray,
    stride: tuple[int, int, int] = (1, 1, 1),
    padding: tuple[int, int, int] = (0, 0, 0)
) -> np.ndarray:
	"""
	Perform 3D convolution forward pass.
	
	Slide a 3D kernel over input volume, computing dot products.
	
	Args:
		input_volume: Shape (C, D, H, W)
		  C = channels, D = depth/time, H = height, W = width
		kernel: Shape (C, kD, kH, kW)
		  Must match input channels
		stride: (stride_d, stride_h, stride_w)
		  Step size in each dimension
		padding: (pad_d, pad_h, pad_w)
		  Zero-padding in each dimension
	
	Returns:
		Output volume: Shape (1, D_out, H_out, W_out)
		  Single output channel
		
	Process:
		1. Apply padding to input
		2. Calculate output dimensions
		3. For each output position:
		   - Extract 3D patch from input
		   - Compute element-wise product with kernel
		   - Sum all products -> single output value
	"""
	# Your code here
	ck,kd,kh,kw = kernel.shape
	input_c,i