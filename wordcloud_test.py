from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = "Python Streamlit WordCloud Data Science AI Machine Learning Deep Learning Numpy Pandas Visualization"

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

# Show the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()