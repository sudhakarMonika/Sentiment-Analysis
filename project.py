from flask import Flask
from textblob import TextBlob
import matplotlib.pyplot as plt
import emoji
import nltk

nltk.download('punkt')

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    results = []

    for sentence in blob.sentences:
        polarity = sentence.sentiment.polarity
        if polarity > 0.2:
            emotion = "Joy 😄"
        elif polarity < -0.2:
            emotion = "Sadness 😢"
        else:
            emotion = "Neutral 😐"
        results.append((str(sentence), polarity, emotion))

    return results

def plot_sentiment(results):
    sentences = [r[0] for r in results]
    polarities = [r[1] for r in results]
    plt.figure(figsize=(8, 4))
    bars = plt.bar(range(len(results)), polarities, tick_label=[f"S{i+1}" for i in range(len(results))])
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title("Sentiment Polarity of Each Sentence")
    plt.ylabel("Polarity")
    for bar, emotion in zip(bars, [r[2] for r in results]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), emotion, ha='center', va='bottom', fontsize=8)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    while True:
        text = input("Enter your text (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Exiting the Sentiment Analyzer.")
            break

        print("\n--- Sentence-wise Analysis ---\n")
        results = analyze_sentiment(text)
        for sentence, polarity, emotion in results:
            print(f"Sentence: {sentence}")
            print(f"→ Polarity: {polarity:.2f}, Emotion: {emotion}\n")

        plot_sentiment(results)
