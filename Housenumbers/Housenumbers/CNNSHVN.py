import numpy as np
from scipy import io as sio
import tensorflow as tf
from matplotlib import pyplot as plt
from cv2 import imread

train_location = 'C:\\Users\\Mayur\\source\\repos\\Housenumbers\\Housenumbers\\Data_requirements\\train_32x32'
test_location = 'C:\\Users\\Mayur\\source\\repos\\Housenumbers\\Housenumbers\\Data_requirements\\test_32x32'
model_path = 'C:\\Users\\Mayur\\source\\repos\\Housenumbers\\Housenumbers\\Finished_data_and_model'
img = imread('C:\\Users\\Mayur\\source\\repos\\Housenumbers\\Housenumbers\\Data_requirements\\409.png')

def load_train_data():
    train_dict = sio.loadmat(train_location)
    X = np.asarray(train_dict['X'])

    X_train = []
    for i in range(X.shape[3]):
        X_train.append(X[:,:,:,i])
    X_train = np.asarray(X_train)

    Y_train = train_dict['y']
    for i in range(len(Y_train)):
        if Y_train[i]%10 == 0:
            Y_train[i] = 0
    Y_train = tf.keras.utils.to_categorical(Y_train,10)
    return (X_train,Y_train)

def load_test_data():
    test_dict = sio.loadmat(test_location)
    X = np.asarray(test_dict['X'])

    X_test = []
    for i in range(X.shape[3]):
        X_test.append(X[:,:,:,i])
    X_test = np.asarray(X_test)

    Y_test = test_dict['y']
    for i in range(len(Y_test)):
        if Y_test[i]%10 == 0:
            Y_test[i] = 0
    Y_test = tf.keras.utils.to_categorical(Y_test,10)
    return (X_test,Y_test)

X_test, Y_test = load_test_data()
X_train, Y_train = load_train_data()

X_test, X_train = X_test/255, X_train/255

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))

model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))

model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(128, activation = 'relu'))
model.add(tf.keras.layers.Dense(10, activation = 'softmax'))

model.summary()

input()

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, Y_train, 
                    epochs = 3, 
                    validation_data = (X_test, Y_test))

tf.keras.models.save_model(model, model_path,  overwrite=True, include_optimizer=True)

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()

img = imread('C:\\Users\\Mayur\\source\\repos\\Housenumbers\\Housenumbers\\Data_requirements\\409.png')
 
prediction = model.predict(img)                         

print(prediction)

input()


