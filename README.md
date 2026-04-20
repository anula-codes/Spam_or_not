# Spam_or_not
# Spam SMS Detection using Machine Learning

A **Machine Learning project** that detects whether an SMS message is **Spam or Ham (Not Spam)** using **Natural Language Processing (NLP)** techniques and **Naive Bayes classification models**.

This project demonstrates the **complete ML workflow**, from **data preprocessing and feature engineering to model training and evaluation**.

Try it: https://spamornot-01.streamlit.app/

---

# Project Overview

Spam messages are a major issue in messaging platforms. This project builds a **Spam SMS Detection System** that automatically classifies messages as:

* **Ham** → Legitimate message
* **Spam** → Unwanted promotional or malicious message

The model uses **TF-IDF feature extraction** and **Naive Bayes algorithms** to perform classification.

---

# Dataset

The project uses the dataset spam.csv, containing thousands of labeled SMS messages.

| Label | Meaning                         |
| ----- | ------------------------------- |
| ham   | Legitimate message              |
| spam  | Unwanted or promotional message |

Example messages:

| Label | Message                                     |
| ----- | ------------------------------------------- |
| ham   | Hey, are we meeting today?                  |
| spam  | Congratulations! You have won a free prize! |

<img width="826" height="293" alt="image" src="https://github.com/user-attachments/assets/0bd611f8-55d6-4a66-bae2-e62db3a68920" />

---

# Machine Learning Pipeline

The project follows a **complete ML pipeline**:

```
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
# Data Cleaning

- The dataset is loaded from `spam.csv` using **Latin-1 encoding** to handle special characters.
- Three unnamed, empty columns (**`Unnamed: 2`**, **`Unnamed: 3`**, **`Unnamed: 4`**) are **dropped** as they carry no useful information.
  
<img width="474" height="240" alt="image" src="https://github.com/user-attachments/assets/186d6c3b-da59-43d5-b793-72ddc2ae15ea" />


- The remaining columns `v1` and `v2` are **renamed** to **`Target`** and **`Text`** for clarity.
  
<img width="490" height="236" alt="image" src="https://github.com/user-attachments/assets/01a2fa91-f780-43ed-bc77-d5dd42a6f1f9" />

  
- The `Target` column is **label-encoded**, converting string labels **`ham → 0`** and **`spam → 1`**.
- A **null check** confirms there are **no missing values** in the dataset.
- **Duplicate rows** are identified and removed (keeping the first occurrence), reducing the dataset from **5,572 to 5,169 rows**.
- The result is a clean **two-column dataset** ready for further analysis.


---

# Exploratory Data Analysis (EDA)

EDA was performed to understand message patterns.

Key insights:

* Dataset contains **more ham messages than spam**
  
<img width="165" height="166" alt="image" src="https://github.com/user-attachments/assets/fcf220d3-7fe8-47ff-a4f2-1a00e41d48b0" />

* Spam messages typically contain **more characters and words**
* Spam messages contain **repetitive promotional keywords**

Visualizations used:

* Pie chart for class distribution
  
<img width="523" height="453" alt="image" src="https://github.com/user-attachments/assets/dbc8a816-b9b6-425e-810e-3e2988a75967" />

* Histogram for message length
  
<img width="571" height="433" alt="download (1)" src="https://github.com/user-attachments/assets/1c965c2f-dd4c-49ab-890c-74a263f1b538" />

* Pair plots

<img width="806" height="741" alt="download (2)" src="https://github.com/user-attachments/assets/262bd340-bdb1-4733-908a-78e5daf38ee7" />

* Correlation heatmap
  
<img width="609" height="418" alt="download (3)" src="https://github.com/user-attachments/assets/5023b097-97c1-4215-ac92-925816e43d0f" />

* Word frequency charts

<img width="518" height="510" alt="download (4)" src="https://github.com/user-attachments/assets/74b25c13-7700-4625-be6f-1849c62d9c5a" />

<img width="518" height="510" alt="download (5)" src="https://github.com/user-attachments/assets/19ebc81a-3ed6-4c93-a8e5-bd3c0b737ee0" />


Libraries used:

* Matplotlib
* Seaborn
* WordCloud

---

# Text Preprocessing

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

# Feature Engineering

Text data is converted into numerical vectors using:

### TF-IDF Vectorization

```
TfidfVectorizer(max_features = 3000)
```

This extracts the **3000 most important words** from the dataset.

---

# Model Training

Three **Naive Bayes models** were trained and evaluated.

| Model         | Description                  |
| ------------- | ---------------------------- |
| GaussianNB    | Works with continuous data   |
| MultinomialNB | Best for text classification |
| BernoulliNB   | Suitable for binary features |

Best performing model:

**Multinomial Naive Bayes**

---

# Model Evaluation

Evaluation metrics used:

* Accuracy Score: 0.9709864603481625
* Precision Score: 1.0
* Confusion Matrix:

| | Predicted Ham | Predicted Spam |
|---|---|---|
| **Actual Ham** | 896 | 0 |
| **Actual Spam** | 30 | 108 |

These metrics help measure the performance of the spam classifier.

---

# Future Improvements

Possible enhancements:

* Add **Deep Learning models (LSTM, BERT)**
* Use **larger datasets**
* Implement **real-time spam detection**
* Deploy using **Docker or cloud services**
