import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import openai

# ========== ENTER YOUR OPENAI API KEY HERE ==========
openai.api_key = "<YOUR_API_KEY_HERE>"  # 🔒 Replace with your API key

# ========== LOAD DATA ==========
def load_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(subset=['review_text'], inplace=True)
    return df

# ========== EDA FUNCTIONS ==========python customer_review_analyzer.py
def plot_rating_distribution(df):
    plt.figure(figsize=(6,4))
    df['rating'].value_counts().sort_index().plot(kind='bar', color='skyblue')
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_wordcloud(df):
    text = " ".join(df['review_text'].tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Common Words in Reviews")
    plt.show()

# ========== GENAI FUNCTION ==========
def summarize_review(review):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes product reviews."},
                {"role": "user", "content": f"Summarize this review in one sentence: {review}"}
            ]
        )
        summary = response["choices"][0]["message"]["content"].strip()
        return summary
    except Exception as e:
        return f"Error: {e}"

# ========== MAIN ==========
def main():
    filepath = "data/reviews.csv"  # Make sure this file exists
    df = load_data(filepath)

    print("\n--- First 5 Reviews ---")
    print(df[['review_text', 'rating']].head())

    print("\n--- Plotting Rating Distribution ---")
    plot_rating_distribution(df)

    print("\n--- Generating Word Cloud ---")
    plot_wordcloud(df)

    print("\n--- Sample Review Summaries ---")
    for i in range(3):
        review = df.iloc[i]['review_text']
        summary = summarize_review(review)
        print(f"\nReview {i+1}: {review}\nSummary: {summary}")

if __name__ == "__main__":
    main()
