import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample news data (replace with your own data)
data = {
    'Title': [
        'Global Economy Faces Uncertainty Amid Trade War',
        'Celebrities Shine at Oscars Night',
        'Political Turmoil Hits Country As Election Day Approaches',
        'Breaking News: New Tech Innovations to Shape Future Economy',
        'Entertainment Industry Struggles Amidst Global Pandemic'
    ],
    'Category': ['Business', 'Entertainment', 'Politics', 'Business', 'Entertainment'],
    'Content': [
        "Global economy faces uncertainty as trade wars escalate between countries. \
        Economists warn about the long-term effects on global trade, markets, and economies.",
        "The Oscars were a star-studded affair with numerous celebrities in attendance. The night was filled with amazing performances and fashion.",
        "As the election day approaches, political leaders are scrambling to secure votes. Recent polls indicate a close race.",
        "New tech innovations are expected to change the way economies function. Experts predict a booming future for AI and automation technologies.",
        "The entertainment industry has faced tremendous challenges during the global pandemic, with theaters closing and production halting."
    ]
}

# Load data into a DataFrame
df = pd.DataFrame(data)

# Tokenize and clean text globally so that it can be used in both sections
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(' '.join(df['Content']))
filtered_words = [word.lower() for word in word_tokens if word.isalpha() and word.lower() not in stop_words]

# Streamlit App Layout
st.title("News Articles Analysis Dashboard")

# Sidebar for options
st.sidebar.header("Select Analysis Type")

analysis_option = st.sidebar.selectbox(
    "Choose analysis",
    ("Overview", "Category Distribution", "Word Frequency", "Sentiment Analysis", "Word Cloud")
)

# Overview of the data
if analysis_option == "Overview":
    st.write("### Data Overview")
    st.write(df)

# News Category Distribution (Bar Chart)
elif analysis_option == "Category Distribution":
    st.write("### News Category Distribution")
    category_counts = df['Category'].value_counts()
    st.bar_chart(category_counts)

# Word Frequency Analysis (Bar Chart)
elif analysis_option == "Word Frequency":
    st.write("### Word Frequency Analysis")

    # Count word frequencies
    word_freq = pd.Series(filtered_words).value_counts().head(10)
    
    # Plot word frequencies
    st.bar_chart(word_freq)

# Sentiment Analysis (Pie Chart with Matplotlib)
elif analysis_option == "Sentiment Analysis":
    st.write("### Sentiment Analysis of Articles")

    # Function to calculate sentiment
    def get_sentiment(text):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            return "Positive"
        elif sentiment < 0:
            return "Negative"
        else:
            return "Neutral"

    # Apply sentiment analysis
    df['Sentiment'] = df['Content'].apply(get_sentiment)

    # Plot sentiment distribution
    sentiment_counts = df['Sentiment'].value_counts()

    # Create pie chart using Matplotlib
    fig, ax = plt.subplots()
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

    st.pyplot(fig)

# Word Cloud (Visualize most frequent words)
elif analysis_option == "Word Cloud":
    st.write("### Word Cloud")

    # Create word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_words))

    # Display word cloud
    st.image(wordcloud.to_array())
