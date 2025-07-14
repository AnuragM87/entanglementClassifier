import numpy as np
from qutip import rand_dm
from backend.utils.quantum_utils import is_entangled_ppt
from backend.data.features import compute_chsh_features
from sklearn.model_selection import train_test_split
from tensorflow import keras

# Parameters
N = 5000  # Number of samples

# Generate dataset
X = []
y = []
for _ in range(N):
    rho = rand_dm([2, 2])
    features = compute_chsh_features(rho)
    label = int(is_entangled_ppt(rho))
    X.append(features)
    y.append(label)
X = np.array(X)
y = np.array(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build model
model = keras.Sequential([
    keras.layers.Input(shape=(4,)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(8, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1)

# Evaluate
loss, acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {acc:.4f}")

# Save model
model.save('backend/models/entanglement_classifier.h5')
print("Model saved to backend/models/entanglement_classifier.h5") 