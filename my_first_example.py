from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

if __name__ == "__main__" :

	analyzer = SentimentIntensityAnalyzer()
	text = "The first lovely example of vaderSentiment."
	result = analyzer.polarity_scores(text)
	print(result)