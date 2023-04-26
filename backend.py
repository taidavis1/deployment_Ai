import tensorflow as tf
import numpy as np
def predictions(input1 , input2 , input3 , input4):
    model = tf.keras.models.load_model("/Users/levanfuentes-parra/Desktop/Tai/Lab-Research/models/temp_model")
    return model.predict(np.asarray([input1 , input2 , input3 , input4]).astype(np.float32))