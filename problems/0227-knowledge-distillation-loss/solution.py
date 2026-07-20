import numpy as np

def distillation_loss(
	student_logits: np.ndarray,
	teacher_logits: np.ndarray,
	temperature: float = 1.0
) -> float:
	"""
	Compute knowledge distillation loss.
	
	L = T^2 * KL(softmax(teacher/T) || softmax(student/T))
	
	Args:
		student_logits: Logits from student model
		teacher_logits: Logits from teacher model
		temperature: Softmax temperature
		
	Returns:
		Distillation loss value
	"""
	# Your code here
	def softmax(logits):
		numerator = np.exp(logits - np.max(logits))
		denom = np.sum(numerator)
		return numerator/denom
	
	teacher_probs = softmax(teacher_logits/temperature)
	student_probs = softmax(student_logits/temperature)

	loss = np.dot(teacher_probs ,np.log(teacher_probs/student_probs))
	distillation_loss = ((temperature)**2)*loss
	return distillation_loss

	pass