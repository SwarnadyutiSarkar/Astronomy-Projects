import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models

# Load data (simulated example)
def load_data():
    # Simulated galaxy images (replace with your data loading code)
    num_samples = 1000
    image_size = 64
    X = np.random.rand(num_samples, image_size, image_size, 1)  # Simulated galaxy images
    y = np.random.randint(0, 3, num_samples)  # Simulated galaxy types: 0=spiral, 1=elliptical, 2=irregular
    return X, y

# Preprocess data
def preprocess_data(X, y):
    # Normalize pixel values to range [0, 1]
    X = X.astype('float32') / 255.0
    # One-hot encode target labels
    y = tf.keras.utils.to_categorical(y, num_classes=3)
    return X, y

# Define CNN model architecture
def create_model(input_shape):
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(3, activation='softmax'))  # Output layer with 3 classes
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Plot training history
def plot_history(history):
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Training and Validation Loss')
    plt.show()

if __name__ == '__main__':
    # Load data
    X, y = load_data()

    # Preprocess data
    X, y = preprocess_data(X, y)

    # Split data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create CNN model
    input_shape = X_train.shape[1:]
    model = create_model(input_shape)

    # Train the model
    history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_val, y_val))

    # Plot training history
    plot_history(history)
