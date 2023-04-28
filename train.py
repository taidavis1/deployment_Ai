import tensorflow as tf
import csv
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
le = preprocessing.LabelEncoder()
scaler = preprocessing.MinMaxScaler()

class Data:
    def __init__(self , csv):
        self.csv = csv
    def read_data_csv(self):
        data = pd.read_csv(self.csv)
        return data        

class Train_Data():
    def __init__(self , model , epochs , x_data , y_data , loss_func , optimizer):
        self.model = model
        self.epochs = epochs
        self.x_data = x_data
        self.y_data = y_data
        self.loss_func = loss_func
        self.optimizer = optimizer
    def train_data(self):
        self.model.compile(
            optimizer=self.optimizer,
            loss=self.loss_func,
            metrics=['accuracy']
        )
        self.model.fit(self.x_data, self.y_data, epochs=self.epochs)
        # self.model.save("my_models")
    def overall_result(self , x_data_test , y_data_test):
        loss,accuracy = self.model.evaluate(x_data_test , y_data_test)
        print('Test loss:', loss)
        print('Test accuracy:', accuracy)
    def predictions(self, x_data_test):
        x_data_test = scaler.transform(x_data_test)
        predict = self.model.predict(x_data_test)
        return le.inverse_transform(predict.reshape(-1).round().astype(int))

def train_run_on():
    data = Data(csv= "t.csv")
    data = data.read_data_csv()
    x = data[['temp' , 'humidity' , 'windspeed' , 'cloudcover']].values
    y = data['description'].values
    y = le.fit_transform(y)
    x_train , x_test , y_train, y_test = train_test_split(x , y , shuffle=True , test_size=0.1)
    x_train = scaler.fit_transform(x_train)
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(4, input_dim = 4 , activation='relu' , name= "input"),
        tf.keras.layers.Dense(32, activation = 'relu' , name = "hidden_layer1"),
        tf.keras.layers.Dense(64, activation = 'relu' , name = "hidden_layer2"),
        tf.keras.layers.Dense(128, activation = 'relu' , name = "hidden_layer3"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, name="output")
    ])
    train_d = Train_Data(model=model , epochs = 50 , x_data = x_train, y_data = y_train , loss_func = 'mse', optimizer = 'adam')
    return train_d
