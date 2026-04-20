# Spam_or_not
# 📩 Spam SMS Detection using Machine Learning

A **Machine Learning project** that detects whether an SMS message is **Spam or Ham (Not Spam)** using **Natural Language Processing (NLP)** techniques and **Naive Bayes classification models**.

This project demonstrates the **complete ML workflow**, from **data preprocessing and feature engineering to model training and evaluation**.

Try it: https://spamornot-01.streamlit.app/

---

# 📖 Table of Contents

* Project Overview
* Dataset
* Project Workflow
* Exploratory Data Analysis
* Text Preprocessing
* Feature Engineering
* Model Training
* Results
* Project Structure
* Installation
* Usage
* Future Improvements

---

# 🚀 Project Overview

Spam messages are a major issue in messaging platforms. This project builds a **Spam SMS Detection System** that automatically classifies messages as:

* **Ham** → Legitimate message
* **Spam** → Unwanted promotional or malicious message

The model uses **TF-IDF feature extraction** and **Naive Bayes algorithms** to perform classification.

---

# 📊 Dataset

The project uses the **SMS Spam Collection Dataset**, containing thousands of labeled SMS messages.

| Label | Meaning                         |
| ----- | ------------------------------- |
| ham   | Legitimate message              |
| spam  | Unwanted or promotional message |

Example messages:

| Label | Message                                     |
| ----- | ------------------------------------------- |
| ham   | Hey, are we meeting today?                  |
| spam  | Congratulations! You have won a free prize! |

---

# 🧠 Machine Learning Pipeline

The project follows a **complete ML pipeline**:

```
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Text Preprocessing
      ↓
Feature Extraction (TF-IDF)
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Saving
```

---

# 📈 Exploratory Data Analysis (EDA)

EDA was performed to understand message patterns.

Key insights:

* Dataset contains **more ham messages than spam**
* Spam messages typically contain **more characters and words**
* Spam messages contain **repetitive promotional keywords**

Visualizations used:

* Pie chart for class distribution
* Histogram for message length
* Pair plots
* Correlation heatmap
* Word frequency charts

Libraries used:

* Matplotlib
* Seaborn
* WordCloud

---

# 🧹 Text Preprocessing

Text preprocessing is applied before training the model.

Steps performed:

1. Convert text to lowercase
2. Tokenization
3. Remove punctuation
4. Remove stopwords
5. Apply stemming using **Porter Stemmer**

Example transformation:

Original message:

```
Congratulations! You have won a free ticket!!!
```

Processed message:

```
congratul free ticket
```

---

# 🔢 Feature Engineering

Text data is converted into numerical vectors using:

### TF-IDF Vectorization

```
TfidfVectorizer(max_features = 3000)
```

This extracts the **3000 most important words** from the dataset.

---

# 🤖 Model Training

Three **Naive Bayes models** were trained and evaluated.

| Model         | Description                  |
| ------------- | ---------------------------- |
| GaussianNB    | Works with continuous data   |
| MultinomialNB | Best for text classification |
| BernoulliNB   | Suitable for binary features |

Best performing model:

✅ **Multinomial Naive Bayes**

---

# 📊 Model Evaluation

Evaluation metrics used:

* Accuracy Score
* Precision Score
* Confusion Matrix

These metrics help measure the performance of the spam classifier.

---

# ▶️ Usage

Run the Python script:

```
python spam.py
```

The script will:

* Clean the dataset
* Train the model
* Evaluate performance
* Save the trained model

---

# 🔮 Future Improvements

Possible enhancements:

* Build a **Streamlit web application**
* Add **Deep Learning models (LSTM, BERT)**
* Use **larger datasets**
* Implement **real-time spam detection**
* Deploy using **Docker or cloud services**
---
