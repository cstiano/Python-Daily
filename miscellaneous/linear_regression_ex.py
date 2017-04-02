import tensorflow as tf 
import numpy as np 

class parameters():
	def  __init__(self):
		self.DATA_LENGTH = 10000
		self.LEARNING_RATE = 1e-10
		self.REG = 1e-10
		self.NUM_EPOCHS = 2000
		self.BATCH_SIZE = 5000
		self.DISPLAY_STEP = 100 #epoch

def generate_data(data_length):
	"""
	Load tha data
	"""
	X = np.array(range(data_length))
	y = 3.657*X + np.random.randn(*X.shape)*0.33
	return X, y

def generate_batches(data_length, batch_size):
	"""
	Create &lt; num_batches; batches from X and y
	"""
	X, y = generate_data(data_length)

	#Create batches
	num_batches = data_length // batch_size
	data_X = np.zeros([num_batches, batch_size], dtype = np.float32)
	data_y = np.zeros([num_batches, batch_size], dtype = np.float32)
	for batch_num in range(num_batches):
		data_X[batch_num:] = X[batch_num*batch_size: (batch_num+1)*batch_size]
		data_y[batch_num:] = y[batch_num*batch_size: (batch_num+1)*batch_size]
		yield data_X[batch_num].reshape(-1,1), data_y[batch_num].reshape(-1,1)

def generate_epochs(num_epochs, data_length, batch_size):
	"""
	Create batches for &lt; num_epochs; epochs
	"""
	for epoch_num in range(num_epochs):
		yield generate_batches(data_length, batch_size)