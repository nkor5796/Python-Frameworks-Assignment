# analysis_notebook.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from wordcloud import WordCloud

# ---------------------------
# Part 1: Load and Explore Data
# ---------------------------
df = pd.read_csv("metadata.csv")

print("Dataset shape:", df.shape)
print(df.info())
print("Missing values per column:\n", df.isnull().sum().head(15))

# ---------------------------
# Part 2: Clean Data
# ---------------------------
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df = df.dropna(subset=['title'])  # drop rows with no title
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# ---------------------------
# Part 3: Analysis & Visualizations
# ---------------------------

# 1. Publications by Year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# 2. Top Journals
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(8,5))
top_journals.plot(kind='barh')
plt.title("Top 10 Journals Publishing COVID-19 Papers")
plt.xlabel("Number of Papers")
plt.show()

# 3. Most Frequent Words in Titles
titles = " ".join(df['title'].dropna()).lower()
words = re.findall(r'\b\w+\b', titles)
common_words = Counter(words).most_common(20)
print("Most common words in titles:", common_words)

# 4. Word Cloud of Titles
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.show()

# 5. Distribution by Source
plt.figure(figsize=(8,5))
df['source_x'].value_counts().head(10).plot(kind='bar')
plt.title("Top Sources of Papers")
plt.xlabel("Source")
plt.ylabel("Count")
plt.show()