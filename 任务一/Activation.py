import numpy as np
import math
#激活函数及其导函数
def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1 - np.tanh(x)**1

def logistic(x):
    return 1/(1+math.e**(-x))

def logistic_prime(x):
    return 1/(math.e**(-x)+2+math.e**x)