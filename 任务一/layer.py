import numpy as np
class Layer:
    def forward(self):
        """
        return Y = X·W +B
        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    def backward(self):
        """_
        return dE/dX of this layer, will be used as dE/dY of the previous layer
        do gradient descent if this is not a activation layer
        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

class FC_Layer(Layer):
    # input_size = number of this layer's neurons
    # output_size = number of next layer's neurons
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size) - 0.5
        self.bias = np.random.rand(1, output_size) - 0.5
        self.input = None

    # calculate output, will be used as next layer's input
    def forward(self, input_data):
        self.input = input_data
        output = np.dot(self.input, self.weights) + self.bias
        return output

    # output_error = dE/dY
    # bias_error = dE/dB input_error = dE/dX weights_error = dE/dW
    # return dE/dX, will be used as dE/dY of the previous layer
    def backward(self, output_error, learning_rate):
        bias_error = output_error
        input_error = np.dot(output_error, self.weights.T)
        weights_error = np.dot(self.input.T, output_error)
        self.weights = self.weights - learning_rate * weights_error
        self.bias = self.bias - learning_rate * bias_error
        return input_error

class Act_Layer(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    # calculate output of the NET
    def forward(self, input_data):
        self.input = input_data
        return self.activation(input_data)

    # output_error = dE/dY
    # return dE/dX, will be used as dE/dY of the previous layer
    # Y = Activation(x), dE/dX = dE/dY * dY/dX
    # = output_error * Activation_Prime(X)
    def backward(self, output_error, learning_rate):
        return self.activation_prime(self.input)*output_error
