import cv2
import numpy as np
import tensorflow as tf
import os


def get_model_path():
    model_path = os.path.join(os.getcwd(), 'vgg')
    return model_path


def predict_image_class(image_path):
    model_path = get_model_path()
    model = tf.keras.models.load_model(model_path)

    img = cv2.imread(image_path)
    img = cv2.resize(img,(256,256))
    img = np.expand_dims(img, axis=0)

    img_class = model.predict(img, batch_size=1)
    score = tf.nn.softmax(img_class[0])
    class_names = ['acne', 'actinic', 'melonama']
    return class_names[np.argmax(score)]
