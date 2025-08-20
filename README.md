# 📜 SMS Spam Classifier

This application predicts whether a given text message is spam or not. It uses a Bernoulli Naive Bayes model for classification and is deployed as a web interface using Streamlit.

# 🎯 Project Overview

The goal of this project is to create a simple, yet effective, tool for identifying spam SMS messages. The model is trained on a dataset of labeled text messages, learning to distinguish between legitimate ("ham") and fraudulent ("spam") content. The Streamlit interface makes the model easily accessible for real-world use.

# 🛠️ Technology Stack

- Machine Learning Model: Bernoulli Naive Bayes

- Web Framework: Streamlit

- Core Libraries:

  - scikit-learn: For the Naive Bayes model, text preprocessing and other machine learning utilities.

  - pandas: For data manipulation and analysis.

- Programming Language: Python

# 🚀 How to Run the Application

- Prerequisites: Python 3.8+ and pip

- Installation:

```Bash

git clone https://github.com/Roy2k5/SMS-Spam-Predict-App.git
cd SMS-Spam-Predict-App

pip install -r requirements.txt

streamlit run app.py
```

This will launch the application in your default web browser.

# 🎬 Demo

You can try it at https://spamsmspredict.streamlit.app/
![[demo/image.png]]

# 📂 File Structure

- app.py: The main Streamlit application file.

- model.pkl, vectorizer.pkl: pretrained model file.

- requirements.txt: Lists all necessary Python libraries.

- README.md: This file.

# 🤝 Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve the project.
