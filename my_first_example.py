from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

text = "I love buying clothes at Mango."
result = analyzer.polarity_scores(text)
print(result)