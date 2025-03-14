# Learning Style Prediction Web Application
This project is a **web-based application** that predicts a student's **learning style** (visual, auditory, or kinesthetic) based on their responses to a series of questions. The application is built using **Flask** (a Python web framework) and integrates a **deep feedforward neural network** for making predictions.

## Project Overview
### Purpose
The goal of the project is to:
1. Collect student details (name, age, gender, semester) and their responses to a set of questions.
2. Use a machine learning model to predict the student's learning style.
3. Display the result in a user-friendly interface.

## Key Features
1. **User Interface**:
   - A **video background** loops continuously, creating an engaging experience.
   - The interface is divided into three sections:
     - **User Details Form**: Collects the student's name, age, gender, and semester.
     - **Quiz Section**: Displays one question at a time, with options to rate the question from 1 to 5.
     - **Result Page**: Displays the predicted learning style (visual, auditory, or kinesthetic).
2. **Machine Learning Integration**:
   - A **deep feedforward neural network** is used to predict the learning style based on the student's responses.
   - The model is trained on a dataset where each row contains:
     - 15 columns for question responses (rated 1-5).
     - 1 column for the learning style label (0=Visual, 1=Auditory, 2=Kinesthetic).
3. **Dynamic Question Flow**:
   - Questions are displayed one at a time.
   - The user rates each question, and their responses are stored.
   - After answering all questions, the responses are sent to the backend for prediction.
4. **Result Display**:
   - The result page dynamically displays the student's name and predicted learning style.
   - A **restart button** allows the user to take the quiz again.

## Technical Components
### Frontend
- **HTML/CSS**:
  - The user interface is built using HTML and styled with CSS.
  - A **video background** is added to enhance the visual appeal.
  - Buttons and inputs are styled with gradients, shadows, and animations.
- **JavaScript**:
  - Handles the quiz flow (displaying questions, collecting responses, and submitting data).
  - Uses `fetch` to send data to the Flask backend.

### Backend
- **Flask**:
  - A lightweight Python web framework used to handle HTTP requests and serve HTML templates.
  - Routes:
    - `/`: Renders the home page (`index.html`).
    - `/submit`: Handles form submission and returns the prediction as JSON.
    - `/result`: Renders the result page (`result.html`).
- **Deep Feedforward Neural Network**:
  - Built using **TensorFlow/Keras**.
  - The model has:
    - Input layer: 15 neurons (one for each question).
    - Hidden layers: 64 and 32 neurons with `relu` activation.
    - Output layer: 3 neurons with `softmax` activation (for 3 learning styles).
  - Trained on a dataset of student responses and learning style labels.

### Machine Learning
- **Training**:
  - The model is trained using a dataset where each row contains:
    - 15 question responses (rated 1-5).
    - 1 learning style label (0=Visual, 1=Auditory, 2=Kinesthetic).
  - The model is saved as `learning_style_model.h5`.
- **Prediction**:
  - The trained model is loaded in the Flask app.
  - Student responses are passed to the model, which predicts the learning style.

## Workflow
1. **User Interaction**:
   - The user enters their details (name, age, gender, semester) on the home page.
   - They answer 15 questions, rating each from 1 to 5.
   - After submitting the quiz, the result page displays their predicted learning style.
2. **Backend Processing**:
   - The Flask app receives the user's responses.
   - The responses are passed to the neural network model for prediction.
   - The predicted learning style is returned to the frontend.
3. **Result Display**:
   - The result page dynamically displays the student's name and learning style.
   - The user can restart the quiz by clicking the "Restart Quiz" button.

## Technologies Used
1. **Frontend**:
   - HTML, CSS, JavaScript.
2. **Backend**:
   - Flask (Python web framework).
3. **Machine Learning**:
   - TensorFlow/Keras (for building and training the neural network).
4. **Deployment**:
   - The app can be deployed using `gunicorn` or platforms like Heroku.

## How to Run the Project
1. **Install Dependencies**:
   ```pip install -r requirements.txt```
2. **Train the Model**:
```python train_model.py```
3. **Run the Flask App**:
```python app.py```
4. **Access the Application**:
Open your browser and go to http://127.0.0.1:5000.

## Example Use Case:
A student visits the application and enters their details.
They answer 15 questions about their learning preferences.
The application predicts their learning style (e.g., "John is a Visual learner").
The student can restart the quiz to try again.


With 💖,
Team 2B
(CSE' 2025)
(FCRIT, Mumbai, India)
