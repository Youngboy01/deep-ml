import numpy as np

class NeuralNetwork:
    '''
    Build a neural network from scratch using only NumPy.
    Required architecture: 784 → 128 (ReLU) → 10 (Softmax)
    '''
    def __init__(self, input_size=784, hidden_size=128, output_size=10, lr=0.01):
        '''
        Initialize network parameters.
        Use small random initialization (e.g., Xavier/He initialization).
        '''
        self.lr = lr
        # TODO: Initialize weights and biases
        self.w1 = np.random.randn(input_size,hidden_size)*np.sqrt(2/input_size)
        self.b1 = np.zeros((1,hidden_size))
        self.w2 = np.random.randn(hidden_size,output_size)*np.sqrt(2/hidden_size)
        self.b2  = np.zeros((1,output_size))
        # Hint: Use np.random.randn() with proper scaling
        pass
    def relu(self,x):
        return np.maximum(0,x)
    def softmax(self,x):
        e_x = np.exp(x-np.max(x, axis=1, keepdims=True))
        return e_x / np.sum(e_x,axis=1, keepdims=True)
    def forward(self, X):
        '''
        Forward pass through the network.
        
        Args:
            X: Input batch, shape (N, 784)
        
        Returns:
            probs: Class probabilities, shape (N, 10)
        
        Must cache intermediate values for backward pass!
        '''
        # TODO: Implement forward pass
        self.z1 = np.dot(X,self.w1) + self.b1
        self.a1 = self.relu(self.z1)
        self.z2 = np.dot(self.a1,self.w2) + self.b2
        probs = self.softmax(self.z2)
        # Layer 1: X @ W1 + b1, then ReLU
        # Layer 2: hidden @ W2 + b2, then Softmax
        return probs
        pass
    
    def backward(self,X,y,probs):
        '''
        Backward pass - compute gradients for all parameters.
        
        Args:
            X: Input batch, shape (N, 784)
            y: True labels, shape (N,)
            probs: Predicted probabilities from forward pass, shape (N, 10)
        
        Returns:
            loss: Scalar cross-entropy loss
        
        Must update self.W1, self.b1, self.W2, self.b2 using computed gradients!
        '''
        # TODO: Implement backward pass
        # 1. Compute loss
        # 2. Compute gradient of loss w.r.t. softmax output
        # 3. Backprop through linear layer 2
        # 4. Backprop through ReLU
        # 5. Backprop through linear layer 1
        # 6. Update all parameters using gradients
        n = y.shape[0]
        y_onehot = np.zeros_like(probs)
        y_onehot[np.arange(n),y] = 1
        loss = -np.sum(y_onehot*np.log(probs+1e-9))/n
        dz2 = (probs - y_onehot)/n
        dw2 = np.dot(self.a1.T,dz2)
        db2 = np.sum(dz2,axis=0,keepdims=True)
        da1 = np.dot(dz2,self.w2.T)
        dz1 = da1 * (self.z1>0)
        dw1 = np.dot(X.T,dz1)
        db1 = np.sum(dz1,axis=0,keepdims=True)
        self.w2 -= self.lr * dw2
        self.b2 -= self.lr * db2
        self.w1 -= self.lr * dw1
        self.b1 -= self.lr * db1
        return loss
        pass
    
    def train_step(self, X, y):
        '''
        Complete training step: forward + backward + update.
        
        Args:
            X: Input batch, shape (N, 784)
            y: True labels, shape (N,)
        
        Returns:
            loss: Scalar loss value
        '''
        probs= self.forward(X)
        loss = self.backward(X,y, probs)
        return loss
    
    def predict(self, X):
        '''
        Predict class labels.
        
        Args:
            X: Input batch, shape (N, 784)
        
        Returns:
            predictions: Predicted class labels, shape (N,)
        '''
        probs = self.forward(X)
        return np.argmax(probs, axis=1)