import pandas as pd
import numpy as np
import os
import tensorflow as tf
import cv2
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import InputLayer
from tensorflow.keras import Input
from tensorflow.keras.layers import Flatten
from tensorflow.keras.models import Sequential, Model
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

IMG_WIDTH=200
IMG_HEIGHT=200
img_folder="/users/sarahgrace/PycharmProjects/ComputerVision/Train/"

# plt.figure(figsize=(20,20))
# test_folder="/users/sarahgrace/PycharmProjects/Train/Left"
# for i in range(5):
#     file = random.choice(os.listdir(img_folder))
#     image_path= os.path.join(img_folder, file)
#     img=mpimg.imread(image_path)
#     ax=plt.subplot(1,5,i+1)
#     ax.title.set_text(file)
#     plt.imshow(img)

def create_dataset(img_folder):
    img_data_array = []
    class_name = []

    for dir1 in os.listdir(img_folder):
        for file in os.listdir(os.path.join(img_folder, dir1)):
            image_path = os.path.join(img_folder, dir1, file)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH))
            image = np.array(image)
            image = image.astype('float32')
            image /= 255
            img_data_array.append(image)
            class_name.append(dir1)
    return img_data_array, class_name


# extract the image array and class name
img_data, class_name = create_dataset("/users/sarahgrace/PycharmProjects/ComputerVision/Train/")

# MAKE TESTING DATASET
img_folder2="/users/sarahgrace/PycharmProjects/ComputerVision/Test/"

def create_dataset(img_folder2):
    img_data_array2 = []
    test_name = []

    for dir1 in os.listdir(img_folder2):
        for file in os.listdir(os.path.join(img_folder2, dir1)):
            image_path = os.path.join(img_folder2, dir1, file)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH))
            image = np.array(image)
            image = image.astype('float32')
            image /= 255
            img_data_array2.append(image)
            test_name.append(dir1)
    return img_data_array2, test_name


# extract the image array and class name
test_data, test_name = create_dataset("/users/sarahgrace/PycharmProjects/ComputerVision/Test/")

target_dict={k: v for v, k in enumerate(np.unique(class_name))}
target_dict

target_val=  [target_dict[class_name[i]] for i in range(len(class_name))]

test_dict={k: v for v, k in enumerate(np.unique(test_name))}
test_dict

test_val=  [target_dict[test_name[i]] for i in range(len(test_name))]

model=tf.keras.Sequential(
        [
            tf.keras.layers.InputLayer(input_shape=(IMG_HEIGHT,IMG_WIDTH, 1)),
            tf.keras.layers.Conv2D(filters=32, kernel_size=3, strides=(2, 2), activation='relu'),
            tf.keras.layers.Conv2D(filters=64, kernel_size=3, strides=(2, 2), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(6)
        ])
model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

x=np.array(img_data, np.float32)
x = x.reshape(-1,200,200,1)

test_data = np.array(test_data, np.float32)
test_data = test_data.reshape(-1,200,200,1)

history = model.fit(x, y=np.array(list(map(int,target_val)), np.float32), epochs=5)


# TEST MODEL ON TEST DATA
classifications = model.predict(test_data)

print(classifications[0])

test_val = np.array(list(map(int,test_val)), np.float32)

test_loss, test_acc = model.evaluate(test_data, test_val, verbose=2)
print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_data)

np.argmax(predictions[0])