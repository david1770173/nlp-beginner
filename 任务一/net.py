
class Net:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    def add(self, layer):
        """add layer to the Neural network
        Args:
            layer (layer object): a layer object must implement forward(for calculating output)
            and backward(for gradient descent )
        """
        self.layers.append(layer)

    def set_loss(self, loss, loss_prime):
        """choose the loss function and loss_prime(the derivative of loss)

        Args:
            loss (_type_): _description_
            loss_prime (_type_): _description_
        """
        self.loss = loss
        self.loss_prime = loss_prime

    def predict(self, X):
        """ calculate the  output of the Net

        Args:
            X (nparray): input

        Returns:
            _type_:output
        """
        data = X
        for layer in self.layers:
            data = layer.forward(data)
        return data

    def train(self, X, Y, epochs = 100, learning_rate = 0.0001,report_frequency = 100):
        """updating weights and bias of each layer(activation layer excluded since they don't have W and B)

        Args:
            X (_type_): input
            Y (_type_): output
            epochs (int, optional): as its name. Defaults to 100.
            learning_rate (float, optional): how fast the NN learns, . Defaults to 0.0001.
            report_frequency (int, optional): after how many epoch the current loss is reported. Defaults to 100.
        """
        for i in range(epochs):
            err = 0
            for j in range(len(X)):
                data = X[j]
                for layer in self.layers:
                    data = layer.forward(data)
                err += self.loss(Y[j], data)
                error = self.loss_prime(Y[j], data)
                for layer in reversed(self.layers):
                    error = layer.backward(error, learning_rate)
            if (i+1) % report_frequency == 0:
                print("the mean loss of epoch", i+1, "=", err/len(X))