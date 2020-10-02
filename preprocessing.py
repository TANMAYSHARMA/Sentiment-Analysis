# -*- coding: utf-8 -*-
"""Preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EvZcsoNh51f6YIUFjGewYJnB8Wg9L-vq
"""

# Commented out IPython magic to ensure Python compatibility.
# Mounting Google Drive to read file
from google.colab import drive
drive.mount('/content/drive')

# Change directory
# %cd /content/drive/My\ Drive/Colab\ Notebooks/IDS576/Project

# Import dataset
# Downloaded from: https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe
import pandas as pd
df = pd.read_csv("Hotel_Reviews.csv")

# Get negative reviews
df_negative = df[["Hotel_Name", "Negative_Review"]]
df_negative = df_negative.loc[df_negative["Negative_Review"] != "No Negative"]
df_negative["Sentiment"] = 0
df_negative.columns = ["Hotel_Name", "Review", "Sentiment"]

# Get positive reviews
df_positive = df[["Hotel_Name", "Positive_Review"]]
df_positive = df_positive.loc[df_positive["Positive_Review"] != "No Positive"]
df_positive["Sentiment"] = 1
df_positive.columns = ["Hotel_Name", "Review", "Sentiment"]

# Merge the two dfs
df_merged = pd.concat([df_negative, df_positive])

import re
import numpy as np

def preprocessText(review):
  # Convert to lowercase
  review = review.lower()

  # Remove punctuations
  review = re.sub('[^A-Za-z0-9]+', ' ', review)

  # Remove whitespaces at both ends
  review = review.strip()

  return review

# Apply preprocessing on all reviews
df_merged["Review"] = df_merged["Review"].apply(preprocessText)

# Replace blank rows with NaN
df_merged.replace("", np.nan, inplace=True)

# Drop empty rows
df_merged.dropna(inplace=True)

# Double check for missing values
df_merged.isnull().any()

# Split the dataset into a 80/20 proportion
# The training data will be further split into a 75/25 proportion while training the model
# Eventually we get 60% for training, 20% testing, and 20% validation
from sklearn.model_selection import train_test_split

training_set, validation_set = train_test_split(df_merged, test_size=0.2)

# Save as csv to work with later
training_set.to_csv("hotel_reviews_processed.csv", sep = ",", index = False)
validation_set.to_csv("validation_set.csv", sep = ",", index = False)