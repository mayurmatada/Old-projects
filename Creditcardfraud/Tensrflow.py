import pandas as pd
import datetime
from matplotlib import pyplot as plt
import tensorflow as tf
import tensorboard as tb
import sklearn.model_selection
import sklearn.preprocessing
import sklearn as sk

log_dir ="C:\\Users\\Mayur\\source\\repos\\Creditcardfraud\\logs\\fit\\" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

data = pd.read_csv('C:\\Users\\Mayur\\source\\repos\\Creditcardfraud\\creditcard.csv')

fraud = data[data['Class'] == 1]
nonfraud = data[data['Class'] == 0]

nonfraud = nonfraud.sample(492)
dataset = fraud.append(nonfraud, ignore_index = True)


y = dataset['Class']
x = dataset.drop('Class', axis = 1)

y_train, y_test, x_train, x_test = sk.model_selection.train_test_split(y, x, test_size = 0.2)

scaler = sk.preprocessing.StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

y_train = y_train.to_numpy()
y_test = y_test.to_numpy()

x_train = x_train.reshape(787, 30, 1)
x_test  = x_test.reshape(197, 30, 1)

epochs = 20
model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Conv1D(32, 2, activation='relu', input_shape = x_train[0].shape))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.5))

model.add(tf.keras.layers.Conv1D(64, 2, activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.7))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.7))

model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer = 'adam', loss='binary_crossentropy', metrics=['accuracy'])


history = model.fit(x_train, y_train, epochs = 1, validation_data = (x_test, y_test), verbose = 1, callbacks=[tensorboard_callback])

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

print("TOTAL ACCURACY OF MODEL = %" + str(test_acc*100))

model.save('tensorflow.h5')
