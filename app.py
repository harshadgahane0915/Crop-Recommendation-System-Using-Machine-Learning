# from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# import joblib

# # Initialize the Flask app
# app = Flask(__name__)

# # Load the trained model and scaler
# model = joblib.load('crop_tree_model.pkl')
# scaler = joblib.load('scaler.pkl')

# # Route for home page
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Route for handling form submission and prediction
# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         # Get input values from the form
#         N = float(request.form['N'])
#         P = float(request.form['P'])
#         K = float(request.form['K'])
#         temperature = float(request.form['temperature'])
#         humidity = float(request.form['humidity'])
#         ph = float(request.form['ph'])
#         rainfall = float(request.form['rainfall'])

#         # Create a DataFrame for the input
#         input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
#                                   columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

#         # Scale the input data
#         input_scaled = scaler.transform(input_data)

#         # Predict using the loaded model
#         prediction = model.predict(input_scaled)

#         # Render the result back to the webpage
#         return render_template('result.html', prediction=prediction[0])

# if __name__ == '__main__':
#     app.run(debug=True)

# import threading
# from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# import joblib
# import time

# # Initialize Flask app
# app = Flask(__name__)

# # Load the trained model and scaler
# model = joblib.load('crop_tree_model.pkl')  # Ensure model file is in the correct directory
# scaler = joblib.load('scaler.pkl')

# # Define the Flask routes
# @app.route('/')
# def home():
#     # Render the HTML form from a template
#     return render_template('home.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get user inputs from the form
#     N = float(request.form['N'])
#     P = float(request.form['P'])
#     K = float(request.form['K'])
#     temperature = float(request.form['temperature'])
#     humidity = float(request.form['humidity'])
#     ph = float(request.form['ph'])
#     rainfall = float(request.form['rainfall'])

#     # Create a DataFrame for input
#     input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
#                               columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

#     # Scale the input data
#     input_scaled = scaler.transform(input_data)

#     # Predict using the loaded model
#     prediction = model.predict(input_scaled)

#     # Return the prediction as an HTML response
#     return f'<h1>Recommended Crop: {prediction[0]}</h1><a href="/">Go back</a>'

# # Function to run Flask app in a thread
# def run_flask():
#     app.run(port=5000, debug=False, use_reloader=False)

# # Start Flask app in a separate thread
# flask_thread = threading.Thread(target=run_flask)
# flask_thread.start()

# # Give Flask a moment to start
# time.sleep(1)

# print("Flask app is running. Open http://127.0.0.1:5000 in your browser.")

# Load the trained model and scaler




# try:
#     model = joblib.load('crop_tree_model.pkl')  # Ensure model file is in the correct directory
#     scaler = joblib.load('scaler.pkl')
# except Exception as e:
#     print(f"Error loading model or scaler: {e}")

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get user inputs from the form
#         N = float(request.form['N'])
#         P = float(request.form['P'])
#         K = float(request.form['K'])
#         temperature = float(request.form['temperature'])
#         humidity = float(request.form['humidity'])
#         ph = float(request.form['ph'])
#         rainfall = float(request.form['rainfall'])

#         # Create a DataFrame for input
#         input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
#                                   columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

#         # Scale the input data
#         input_scaled = scaler.transform(input_data)

#         # Predict using the loaded model
#         prediction = model.predict(input_scaled)

#         # Return the prediction as an HTML response
#         return f'<h1>Recommended Crop: {prediction[0]}</h1><a href="/">Go back</a>'
#     except Exception as e:
#         print(f"Error during prediction: {e}")
#         return "An error occurred during prediction. Please check the input values."



# import threading
# from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# import joblib
# import time

# # Initialize Flask app
# app = Flask(__name__)

# # Load the trained model and scaler
# try:
#     model = joblib.load('crop_tree_model.pkl')  # Ensure model file is in the correct directory
#     scaler = joblib.load('scaler.pkl')
# except Exception as e:
#     print(f"Error loading model or scaler: {e}")

# # Define the Flask routes
# @app.route('/')
# def home():
#     # Render the HTML form from a template
#     return render_template('home.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get user inputs from the form
#         N = float(request.form['N'])
#         P = float(request.form['P'])
#         K = float(request.form['K'])
#         temperature = float(request.form['temperature'])
#         humidity = float(request.form['humidity'])
#         ph = float(request.form['ph'])
#         rainfall = float(request.form['rainfall'])

#         # Create a DataFrame for input
#         input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
#                                   columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

#         # Scale the input data
#         input_scaled = scaler.transform(input_data)

#         # Predict using the loaded model
#         prediction = model.predict(input_scaled)

#         # Return the prediction as an HTML response
#         return f'<h1>Recommended Crop: {prediction[0]}</h1><a href="/">Go back</a>'
#     except Exception as e:
#         print(f"Error during prediction: {e}")
#         return "An error occurred during prediction. Please check the input values."

# # Function to run Flask app in a thread
# def run_flask():
#     app.run(port=5000, debug=True, use_reloader=False)

# # Start Flask app in a separate thread
# flask_thread = threading.Thread(target=run_flask)
# flask_thread.start()

# # Give Flask a moment to start
# time.sleep(1)

# print("Flask app is running. Open http://127.0.0.1:5000 in your browser.")





import threading
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import time

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and scaler
try:
    model = joblib.load('crop_tree_model.pkl')  # Ensure model file is in the correct directory
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    print(f"Error loading model or scaler: {e}")

# Define the Flask routes
@app.route('/')
def home():
    # Render the HTML form from a template
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs from the form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Create a DataFrame for input
        input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                                  columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

        # Scale the input data
        input_scaled = scaler.transform(input_data)

        # Predict using the loaded model
        prediction = model.predict(input_scaled)

        # Render the prediction result in result.html
        return render_template('result.html', prediction=prediction[0])
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "An error occurred during prediction. Please check the input values."

# Function to run Flask app in a thread
def run_flask():
    app.run(port=5000, debug=True, use_reloader=False)

# Start Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Give Flask a moment to start
time.sleep(1)

print("Flask app is running. Open http://127.0.0.1:5000 in your browser.")



