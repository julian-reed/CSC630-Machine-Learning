from variable_object_oriented import Variable, exp, log
import numpy as np
import math
import random

"""
A version of the logitic regression class that is only accurate for the first two dimensions of X
"""

class LogisticRegression():
        
    global_m = 0
    global_b = 0
    m = 0
    b = 0
    
    #Creates dictionary used as params
    @staticmethod 
    def toDict(m, b, test_m, test_b):
        values = {}
        for i in range(len(m)):
            if type(m[i]) == Variable:
                values[m[i].name] = test_m[i]
            else:
                values['m%s'%i] = test_m[i]
        if type(b) == Variable:
            values[b.name] = test_b
        else:
            values['b'] = test_b
        return values
    
    
    def fit(self, X, y, lr = 0.01):
        """
        lr = learning rate, default = 0.01 (as suggested by Dr. Z)
        """
        #Initialize variables
        self.learning_rate = lr
        loss_values = []
        pred_values = []
        self.num_samples, self.num_features = X.shape
        m = [Variable(name='m%s'%i) for i in range(self.num_features)]
        b = Variable(name='b')
        
        #calculate pred values for each X value (y_hat)
        for i in range(self.num_samples):
            pred = 1/(1 + Variable.exp(-1 *
                sum([m[j] * X[i, j] for j in range(self.num_features)], b) ))
            pred_values.append(pred)
        
        #defining the loss function
        loss = sum((0-y[i] * Variable.log(pred_values[i]) - (1-y[i]) * Variable.log(1-(pred_values[i])))for i in range(self.num_samples))
        
        #start gradient descent
        #step 1: generate random numbers:
        test_m = [random.random() * 1.5 for i in range(self.num_features)]
        test_b = random.random() * 1.5
        
        #step 2: calculate the gradient with m and b, need dictionary to pass into grad function
        # while step size > ?
        for iteration in range(1000): 
            #calculate params with respect to each m and b respectively, passing in the other as a constant so it has no gradient
            params_m = LogisticRegression.toDict(m, 1, test_m, 1)
            params_b = LogisticRegression.toDict(test_m, b, test_m, test_b)
            loss_grad_b = loss.grad(params_b)
            loss_grad_m = loss.grad(params_m)
        
        #step 3: take a step by subtracting lr * gradient from old param value, and reset values, repeat step 2
            step_size_m = lr * loss_grad_m
            step_size_b = lr * loss_grad_b[-1]
            for i in range(self.num_features):
                test_m[i] -= step_size_m[i]
            test_b -= step_size_b
            
        
        #assign final values to global vairables so they can be used in predict()
        
        LogisticRegression.global_m = test_m
        LogisticRegression.global_b = test_b
        LogisticRegression.m = m
        LogisticRegression.b = b
        
    #Predicts y values based on inputed testing data
    def predict(self, X):
        #checking to make sure model has been fit
        if LogisticRegression.global_m == 0 and LogisticRegression.global_b == 0:
            return "Please fit model before trying to predict"
        y_preds = [] 
        self.num_samples, self.num_features = X.shape
        params = LogisticRegression.toDict(LogisticRegression.m, LogisticRegression.b, LogisticRegression.global_m, LogisticRegression.global_b)
        for i in range(self.num_samples):
            var_exp = Variable.exp(-1 *
                sum([LogisticRegression.global_m[j] * X[i, j] for j in range(self.num_features)], LogisticRegression.global_b) )
            pred = 1/(1+var_exp.evaluate(params))
            if pred >= 0.5:
                y_preds.append(1)
            else:
                y_preds.append(0)
        return y_preds
