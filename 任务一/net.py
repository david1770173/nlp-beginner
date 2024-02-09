
class Net:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    def add(self, layer):
        self.layers.append(layer)

    def set_loss(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime

    def predict(self, X):
        data = X
        for layer in self.layers:
            data = layer.forward(data)
        return data

    def train(self, X, Y, epochs = 1, learning_rate = 0.0001):
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
            if (i+1) % 100 == 0:
                print("the mean loss of epoch", i+1, "=", err/len(X))