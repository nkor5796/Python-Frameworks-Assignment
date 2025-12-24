# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ---------------------------
# Load Data Function
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df = df.dropna(subset=['title'])
    return df

df = load_data()

# ---------------------------
# App Layout
# ---------------------------
st.title("CORD-19 Data Explorer")
st.write("An interactive exploration of COVID-19 research papers")

# Sidebar filters
year_range = st.slider("Select year range", 2015, 2023, (2019, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write(f"Showing {len(filtered)} papers from {year_range[0]} to {year_range[1]}")

# Publications by Year
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
st.bar_chart(top_journals)

# Word Cloud
st.subheader("Word Cloud of Titles")
titles = " ".join(filtered['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Show sample data
st.subheader("Sample Data")
st.dataframe(filtered[['title','journal','publish_time']].head(10))