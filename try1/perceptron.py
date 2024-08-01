import numpy as np
class Perceptron:
    def __init__(self,input_size,learning_rate,epochs):
        self.input_size=input
        self.learning_rate=learning_rate
        self.epochs=epochs
        self.weight=np.zeros(input_size)
        self.bias=0
        self.error=[]
    def activation(self,x):
        return 1 if x>=0 else 0 
    def train(self,X,Y):
        for i in range(self.epochs):
            total_error=0
            for idx,x_i in enumerate(X):
                Output=np.dot(x_i,self.weight)+self.bias
                y_pred=self.activation(Output)
                Error=Y[idx]-y_pred
                print(f'Epoch_{i}:{Error}')
                total_error+=Error**2
                print(total_error)
                #Update weight and bias
                self.weight+=self.learning_rate*Error*x_i
                self.bias+=self.learning_rate*Error
            mse=total_error/len(X)
            self.error.append(mse)
    def predict(self,X):
        Predictions=[]
        for x_i in X:
            output=np.dot(x_i,self.weight)+self.bias
            pred=self.activation(output)
            Predictions.append(pred)
        return Predictions
