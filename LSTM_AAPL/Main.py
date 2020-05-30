import pandas as pd
import datetime
from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
import sklearn.preprocessing
import sklearn.metrics
import sklearn as sk


data = pd.read_csv('/mnt/c/Users/Mayur/source/repos/LSTM_AAPL/AAPL.csv', engine= 'python')
data = data.drop('Adj Close', axis = 1)
data_training = data[data['Date']<'2019-01-01'].copy()
data_test = data[data['Date']>='2019-01-01'].copy()
data_training = data.drop('Date', axis=1)
data_test = data.drop('Date', axis=1)
scaler = sk.preprocessing.MinMaxScaler()

data_training = scaler.fit_transform(data_training)
data_test = scaler.transform(data_test)

X_train = []
y_train = []
X_test = []
y_test = []

for i in range(60, data_training.shape[0]):
    X_train.append(data_training[i-60:i])
    y_train.append(data_training[i, 0])
for i in range(60, data_test.shape[0]):
    X_test.append(data_test[i-60:i])
    y_test.append(data_test[i, 0])


X_test = np.array(X_test)
y_test = np.array(y_test)
X_train = np.array(X_train)
y_train = np.array(y_train)


model = tf.keras.models.Sequential()

model.add(tf.keras.layers.LSTM(units = 60, activation = 'relu', return_sequences = True, input_shape = (X_train.shape[1], 5)))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.LSTM(units = 60, activation = 'relu', return_sequences = True))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.LSTM(units = 80, activation = 'relu', return_sequences = True))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.LSTM(units = 120, activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(units = 1))

model.compile(optimizer='adam', loss = 'mean_squared_error')

model.Summary()
input()

model.fit(x=X_train,
          y=y_train,
          epochs=5,
          validation_data = (X_test, y_test),
          batch_size = 64)

y_pred = model.predict(X_test)
accuracy = sk.metrics.mean_squared_error(y_true= y_test, y_pred= y_pred)
scale = 1/8.18605127e-04
y_pred = y_pred*scale
y_test = y_test*scale

plt.figure(figsize=(14,5))
plt.plot(y_test, color = 'red', label = 'Real Apple Stock Price')
plt.plot(y_pred, color = 'blue', label = 'Predicted Apple Stock Price')
plt.title('Apple Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Apple Stock Price')
plt.legend()
plt.show()

print("The accuracy of the trained model is: " + str(accuracy*100))

model.save('/mnt/c/Users/Mayur/source/repos/LSTM_AAPL/model.h5')