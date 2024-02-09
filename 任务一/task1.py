import pandas as pd
import numpy as np
from numpy import doc
from net import Net
from layer import FC_Layer,Act_Layer
from loss import mse,mse_prime
from activation import logistic,logistic_prime
from pipeline import load_bag_of_words


BOW,sentiment = load_bag_of_words()
BOW = BOW.reshape(156060,1,16531)
sentiment = sentiment.reshape(-1,1,1)
print(sentiment.shape)
net = Net()
net.add(FC_Layer(BOW.shape[2],1))
net.set_loss(mse,mse_prime)
net.train(BOW,sentiment,epochs=1,learning_rate=0.001,report_frequency= 1)
for i in range(0,50):
    print(net.predict(BOW[i]))
net.train(BOW,sentiment,epochs=1,report_frequency= 1)
for i in range(0,50):
    print(net.predict(BOW[i]))
net.train(BOW,sentiment,epochs=1,report_frequency= 1)
for i in range(0,50):
    print(net.predict(BOW[i]))
net.train(BOW,sentiment,epochs=1,report_frequency= 1)
for i in range(0,50):
    print(net.predict(BOW[i]))
net.train(BOW,sentiment,epochs=1,report_frequency= 1)
for i in range(0,50):
    print(net.predict(BOW[i]))
net.train(BOW,sentiment,epochs=30,report_frequency= 1)
for i in range(0,50):
    print(net.predict(BOW[i]))