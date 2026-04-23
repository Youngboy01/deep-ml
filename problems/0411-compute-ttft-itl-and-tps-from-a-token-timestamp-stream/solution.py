import numpy as np
def compute_inference_metrics(timestamps: list[float]) -> dict:
	"""
	Compute LLM inference performance metrics from token timestamps.
	
	Args:
		timestamps: List of floats where timestamps[0] is the request start time
		            and timestamps[1:] are the times when each output token was generated.
	
	Returns:
		Dictionary with keys 'ttft', 'tps', 'itl' containing the metric values.
	"""
	time = np.array(timestamps)
	ttft = time[1]-time[0]
	tps = (len(time)-1)/(time[-1]-time[0])
	itl = np.mean(np.diff(time[1:])) if len(time)!= 2 else 0.0
	return {
		'ttft': np.round(ttft,4), 
		'tps': np.round(tps,4), 
		'itl': np.round(itl, 4)
	}
	pass