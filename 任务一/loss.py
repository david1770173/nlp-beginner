import numpy as np

# loss function and its derivative
def mse(y_true, y_pred):
    return np.mean(np.power(y_true-y_pred, 2))

def mse_prime(y_true, y_pred):
    #todo:what's the point of me writing /y_true.size??? Must figure this out.
    return 2*(y_pred-y_true)/y_true.size

