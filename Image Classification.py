# -*- coding: utf-8 -*-
"""Submis_3_Pengembang_Fix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gxDywodKytWs6yLG3_0zSgoc8Lr2KRaF
"""

# Commented out IPython magic to ensure Python compatibility.
import zipfile
import os
import glob 
import warnings

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Activation, Dense, Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.optimizers import Adam
import tensorflow as tf

from keras.preprocessing import image
from google.colab import files
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# %matplotlib inline

!pip install kaggle

from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!ls ~/.kaggle

!kaggle datasets download -d moltean/fruits

!mkdir fruits
!unzip -qq fruits.zip -d fruits
!ls fruits

import os

fruits = os.path.join('/content/fruits/fruits-360_dataset/fruits-360/Training')

print(os.listdir(fruits))

fruits = ['Apple Granny Smith', 'Quince', 'Carambula', 'Pear Red', 'Tamarillo', 'Pineapple Mini', 'Plum 3', 'Granadilla', 'Strawberry Wedge', 'Raspberry', 'Grape Blue', 'Apricot', 'Cherry Wax Red', 'Grape White 4', 'Huckleberry', 'Tomato not Ripened', 'Apple Pink Lady', 'Onion Red', 'Grape White 2', 'Pear Forelle', 'Walnut', 'Nectarine Flat', 'Avocado', 'Banana Red', 'Cherry 1', 'Lemon', 'Kohlrabi', 'Apple Red Yellow 2', 'Apple Crimson Snow', 'Tomato Yellow', 'Strawberry', 'Peach Flat', 'Guava', 'Cocos', 'Pomelo Sweetie', 'Kaki', 'Ginger Root', 'Maracuja', 'Watermelon', 'Nut Forest', 'Apple Braeburn', 'Potato Red Washed', 'Pear Abate', 'Pomegranate', 'Salak', 'Grapefruit White', 'Apple Red Delicious', 'Cherry Rainier', 'Papaya', 'Grapefruit Pink', 'Clementine', 'Physalis', 'Pepper Yellow', 'Lychee', 'Blueberry', 'Pitahaya Red', 'Pepper Red', 'Tomato Maroon', 'Potato Sweet', 'Plum', 'Cactus fruit', 'Apple Golden 2', 'Corn', 'Tomato 4', 'Corn Husk', 'Pineapple', 'Plum 2', 'Mango Red', 'Cantaloupe 1', 'Tangelo', 'Apple Red Yellow 1', 'Redcurrant', 'Physalis with Husk', 'Banana Lady Finger', 'Cucumber Ripe', 'Grape White', 'Rambutan', 'Onion Red Peeled', 'Peach', 'Melon Piel de Sapo', 'Pear Stone', 'Beetroot', 'Mango', 'Grape White 3', 'Pepper Orange', 'Peach 2', 'Limes', 'Mulberry', 'Tomato 1', 'Tomato Heart', 'Banana', 'Apple Red 3', 'Passion Fruit', 'Tomato Cherry Red', 'Cantaloupe 2', 'Nut Pecan', 'Pepino', 'Eggplant', 'Kiwi', 'Pepper Green', 'Apple Red 1', 'Cherry 2', 'Mangostan', 'Lemon Meyer', 'Pear Kaiser', 'Onion White', 'Hazelnut', 'Potato Red', 'Grape Pink', 'Tomato 2', 'Pear Williams', 'Pear', 'Potato White', 'Chestnut', 'Cherry Wax Yellow', 'Apple Golden 3', 'Kumquats', 'Orange', 'Apple Red 2', 'Dates', 'Pear Monster', 'Cherry Wax Black', 'Mandarine', 'Fig', 'Avocado ripe', 'Apple Golden 1', 'Pear 2', 'Cucumber Ripe 2', 'Cauliflower', 'Nectarine', 'Tomato 3']

for fruits in fruits:
    print(f'{fruits} images: ', len(os.listdir(f'/content/fruits/fruits-360_dataset/fruits-360/Training/{fruits}')))

    total_image = len(list(glob.iglob("/content/fruits/fruits-360_dataset/fruits-360/Training/*/*.*", recursive=True)))
print("Total Data Image JPEG     : ",total_image)

import os

fruits = os.path.join('/content/fruits/fruits-360_dataset/fruits-360/Training')

import shutil

ignore_fruits = ['Lemon', 'Kohlrabi', 'Apple Red Yellow 2', 'Apple Crimson Snow', 'Tomato Yellow', 'Strawberry', 'Peach Flat', 'Guava', 'Cocos', 'Pomelo Sweetie', 'Kaki', 'Ginger Root', 'Maracuja', 'Watermelon', 'Nut Forest', 'Apple Braeburn', 'Potato Red Washed', 'Pear Abate', 'Pomegranate', 'Salak', 'Grapefruit White', 'Apple Red Delicious', 'Cherry Rainier', 'Papaya', 'Grapefruit Pink', 'Clementine', 'Physalis', 'Pepper Yellow', 'Lychee', 'Blueberry', 'Pitahaya Red', 'Pepper Red', 'Tomato Maroon', 'Potato Sweet', 'Plum', 'Cactus fruit', 'Apple Golden 2', 'Corn', 'Tomato 4', 'Corn Husk', 'Pineapple', 'Plum 2', 'Mango Red', 'Cantaloupe 1', 'Tangelo', 'Apple Red Yellow 1', 'Redcurrant', 'Physalis with Husk', 'Banana Lady Finger', 'Cucumber Ripe', 'Grape White', 'Rambutan', 'Onion Red Peeled', 'Peach', 'Melon Piel de Sapo', 'Pear Stone', 'Beetroot', 'Mango', 'Grape White 3', 'Pepper Orange', 'Peach 2', 'Limes', 'Mulberry', 'Tomato 1', 'Tomato Heart', 'Banana', 'Apple Red 3', 'Passion Fruit', 'Tomato Cherry Red', 'Cantaloupe 2', 'Nut Pecan', 'Pepino', 'Eggplant', 'Kiwi', 'Pepper Green', 'Apple Red 1', 'Cherry 2', 'Mangostan', 'Lemon Meyer', 'Pear Kaiser', 'Onion White', 'Hazelnut', 'Potato Red', 'Grape Pink', 'Tomato 2', 'Pear Williams', 'Pear', 'Potato White', 'Chestnut', 'Cherry Wax Yellow', 'Apple Golden 3', 'Kumquats', 'Orange', 'Apple Red 2', 'Dates', 'Pear Monster', 'Cherry Wax Black', 'Mandarine', 'Fig', 'Avocado ripe', 'Apple Golden 1', 'Pear 2', 'Cucumber Ripe 2', 'Cauliflower', 'Nectarine', 'Tomato 3']

for x in ignore_fruits:
  path = os.path.join(fruits, x)
  shutil.rmtree(path)

train_dir = os.path.join('/content/fruits/fruits-360_dataset/fruits-360/Training')
train_datagen = ImageDataGenerator(rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    shear_range=0.2,
    fill_mode = 'nearest',
    validation_split=0.2)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=8,
    class_mode='categorical',
    subset='training') 
validation_generator = train_datagen.flow_from_directory(
    train_dir, 
    target_size=(150, 150),
    batch_size=16,
    class_mode='categorical',
    subset='validation')

model_simple = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5), 
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(25, activation='softmax')])


model_simple.compile(
    optimizer='adam', 
    loss='categorical_crossentropy', 
    metrics=['accuracy'])

def scheduler(epoch, lr):
  if epoch < 5:
    return lr
  else:
    return lr * tf.math.exp(-0.1)

lr_schedule = tf.keras.callbacks.LearningRateScheduler(scheduler, verbose=1)
tb_callback = tf.keras.callbacks.TensorBoard(
    log_dir='logs', histogram_freq=0, write_graph=True, write_images=False,
    update_freq='epoch', embeddings_freq=0,
    embeddings_metadata=None
)

model_simple.summary()

batch_size = 16

with tf.device("/device:GPU:0"):
  history = model_simple.fit(train_generator, 
                    epochs =  25, 
                    steps_per_epoch = 1751//batch_size, 
                    validation_data = validation_generator, 
                    verbose = 1, 
                    validation_steps = 437//batch_size,
                    callbacks =[lr_schedule, tb_callback])

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

model_simple.save_weights('model_inception_weights.h5')
model_simple.save('model_inception.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model_simple)
tflite_model_simple = converter.convert()

with tf.io.gfile.GFile('model_simple.tflite', 'wb') as f:
  f.write(tflite_model_simple)