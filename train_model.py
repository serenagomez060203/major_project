import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Simulated dataset (replace with real data)
# Each row represents a student's responses to 15 questions (rated 1-5)
# The last column is the learning style label (0=Visual, 1=Auditory, 2=Kinesthetic)
data = {
    'Q1': [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
    'Q2': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'Q3': [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
    'Q4': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'Q5': [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
    'Q6': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'Q7': [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
    'Q8': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'Q9': [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
    'Q10': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'Q11': [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
    'Q12': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'Q13': [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
    'Q14': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'Q15': [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
    'LearningStyle': [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]  # Labels: 0=Visual, 1=Auditory, 2=Kinesthetic
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features (responses to questions) and labels (learning style)
X = df.iloc[:, :-1].values  # All columns except the last
y = df.iloc[:, -1].values   # Last column (LearningStyle)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(15,)),  # 15 input features (one for each question)
    Dense(32, activation='relu'),
    Dense(3, activation='softmax')  # 3 output classes (Visual, Auditory, Kinesthetic)
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=8, validation_split=0.2)

# Save the model
model.save('learning_style_model.h5')