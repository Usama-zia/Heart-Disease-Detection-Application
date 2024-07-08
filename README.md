
# Heart Disease Detection Application

Welcome to the Heart Disease Detection Application repository! This project is designed to predict the likelihood of heart disease in patients using machine learning algorithms.
(Work is ongoing on this project to introduce better performing ML models and include deep learning models.)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
Heart disease is a leading cause of death worldwide. Early detection is crucial for effective treatment and management. This application leverages machine learning to predict the presence of heart disease based on various medical attributes.

## Features
- User-friendly interface for inputting patient data
- Real-time prediction of heart disease risk
- Visualization of patient data and prediction results
- Detailed model evaluation and performance metrics

## Installation
To get a local copy up and running, follow these steps:

### Prerequisites
- Python 3.7+
- pip

### Clone the Repository
```sh
git clone https://github.com/Usama-zia/Heart-Disease-Detection-Application.git
cd Heart-Disease-Detection-Application
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
1. Run the application
   ```sh
   python app.py
   ```
2. Open your browser and go to `http://localhost:5000`
3. Input patient data to get the prediction

## Data
The dataset used for this project includes various medical attributes such as age, sex, blood pressure, cholesterol levels, and more. It is sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease).

## Model
This application utilizes several machine learning algorithms, including:
- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- Neural Networks

The models are trained and evaluated to choose the best performing ones based on accuracy, precision, recall, and F1 score.

## Results
The application provides a detailed summary of the prediction results, including:
- Predicted risk of heart disease
- Visualization of feature importance
- Model performance metrics

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

---
