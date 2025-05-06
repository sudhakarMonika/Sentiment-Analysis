📘 Sentiment Analysis Using TextBlob and Flask
📌 Project Overview
This project performs sentence-level sentiment analysis on user-input text using TextBlob, a Natural Language Processing (NLP) library. The results include polarity scores and emotion tags such as Joy, Sadness, and Neutral. A bar graph is also generated to visualize sentiment polarity across sentences.

🎯 Features
Sentence-level sentiment analysis using TextBlob

Emotion categorization based on polarity (Joy, Sadness, Neutral)

Real-time user input via terminal

Graphical visualization using Matplotlib

Flask integrated (ready for web app expansion)

🧠 Technologies Used
Python

Flask

TextBlob

NLTK

Matplotlib

🛠️ How to Run the Project
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/sentiment-analysis-project.git
cd sentiment-analysis-project
2. Install Required Libraries
bash
Copy
Edit
pip install flask textblob matplotlib nltk
3. Run the Script
bash
Copy
Edit
python app.py
4. Enter Text Input
You'll be prompted in the terminal to enter your text. Type any paragraph or sentence.

📊 Sample Output
yaml
Copy
Edit
Sentence: I love this project!
→ Polarity: 0.5, Emotion: Joy 😄

Sentence: Sometimes it’s difficult to debug.
→ Polarity: -0.3, Emotion: Sadness 😢
Bar chart will display with labeled sentiments.

🔍 Future Scope
Deploy as a full web application using Flask

Add advanced models (like BERT or Vader) for deeper analysis

Handle multilingual sentiment analysis

📚 References
TextBlob Documentation

NLTK Library

Matplotlib Documentation

Research papers on sentiment analysis and emotion classification
