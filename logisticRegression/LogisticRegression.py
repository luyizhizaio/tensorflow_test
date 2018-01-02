__author__ = 'tend'

from numpy import *
import matplotlib.pyplot as plt
import time


def sigmoid(inX):
    return 1.0 / (1 +exp(-inX))

def trainLogRegression(train_x,train_y,opts):

    startTime = time.time()

    numSample,numFeatures = shape(train_x)

    alpha = opts['alpha'];maxIter=opts['maxIter']
    weights = ones((numFeatures,1))


    for k in range(maxIter):
        if opts['optimizeType'] == 'gradDescent':
            output= sigmoid(train_x * weights)
            error = train_y - output
            weights = weights + alpha *  train_x.transpose() * error




    print 'Congratulations, training complete! Took %fs!' %(time.time() - startTime)
    return weights


def testLogRegression(weights,test_x,test_y):

    numSamples,numFeatures = shape(test_x)
    matchCount =0
    for i in xrange(numSamples):
        predict = sigmoid(test_x[i,:] * weights)[0,0] >0.5
        if predict == bool(test_y[i,0]):
            matchCount +=1

    accuracy = float(matchCount) / numSamples
    return accuracy



def showLogRegress(weights,train_x, train_y):

    numSamples, numFeatures = shape(train_x)
    if numFeatures != 3:
        print "sorry , "
        return 1


    for i in xrange(numSamples):
        if int(train_y[i,0]) == 0:
            plt.plot(train_x[i,1],train_x[i,2],'or')
        elif int(train_y[i,0]) == 1:
            plt.plot(train_x[i,1],train_x[i,2],'ob')


    min_x = min(train_x[:, 1])[0,0]
    max_x = max(train_x[:, 1])[0,0]
    weights = weights.getA() # convert mat to array

    y_min_x = float(-weights[0] - weights[1] * min_x) / weights[2]
    y_max_x= float(-weights[0] - weights[1] * max_x) / weights[2]
    plt.plot([min_x,max_x],[y_min_x,y_max_x],'-g')
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()











