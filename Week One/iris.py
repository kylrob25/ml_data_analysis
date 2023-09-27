# iris classificaiton using tensorflow

# matplotlib library for plotting
import matplotlib.pyplot as plt

# scikit learn library for machine learning
from sklearn import datasets
from sklearn.model_selection import train_test_split

# tensorflow libray allows us to build neural networks
# needs to be installed using: pip install tensorflow rather than conda

import tensorflow as tf


# load iris data
iris = datasets.load_iris()
x, y = iris.data, iris.target


# split data into training and testing sets. 80% training, 20% testing
x_vals_train, x_vals_test, y_vals_train, y_vals_test = train_test_split(x, y, test_size=0.2, random_state=0)


# set up model
neural_net = tf.keras.models.Sequential(
    [
        tf.keras.layers.Dense(50, activation=tf.nn.relu),
        tf.keras.layers.Dense(25, activation=tf.nn.relu),
        tf.keras.layers.Dense(1),
    ]
)

# set up loss function and optimizer
loss = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

# set up training
neural_net.compile(optimizer=optimizer, loss=loss, metrics=["accuracy"])

# train model
history = neural_net.fit(x_vals_train, y_vals_train, epochs=20, batch_size=10)

# evaluate model
results = neural_net.evaluate(x_vals_test, y_vals_test, verbose=2)

# print results
print("Test Loss: ", results[0])
print("Test Accuracy: ", results[1])

# plot loss over time
plt.plot(history.history["loss"])
plt.title("Model Loss")
plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.show()
