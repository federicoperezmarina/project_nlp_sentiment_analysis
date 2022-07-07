# project_nlp_sentiment_analysis
This repository is about nlp ( natural language processing ). We will try to show some examples about nlp.

## Table of Contents
* [Docker image](#docker-image)
* [Docker build](#docker-build)
* [Docker run and execute](#docker-run-and-execute)
* [First example of sentiment analysis](#first-example-of-sentiment-analysis)
* [Many sentences example of sentiment analysis](#many-sentences-example-of-sentiment-analysis)

## Docker image
First of all we are going to use docker to prepare the environment in order to execute the sentiment analysis examples. 

This is the Dockerfile were we can see how to install python and library vaderSentiment.
```sh
FROM ubuntu:latest

COPY . /tmp/

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    pip3 install vaderSentiment
```

## Docker build
We need to create the docker image in order to launch / execute the code. This is the way to create the docker image
```sh
docker build -t python_nlp .
```

## Docker run and execute
Now we are able to use the image with the next command
```sh
docker run -it python_nlp /bin/bash
```

## First example of sentiment analysis
In this step we can go to the tmp directory in order to see the python / examples files.
```sh
cd /tmp/
ls -lha

#output
drwxrwxrwt 1 root root 4.0K Jul  7 20:22 .
drwxr-xr-x 1 root root 4.0K Jul  7 20:29 ..
drwxr-xr-x 7 root root 4.0K Jul  7 20:21 .git
-rw-r--r-- 1 root root  215 Jul  7 19:56 Dockerfile
-rw-r--r-- 1 root root  140 Jul  7 14:12 README.md
-rw-r--r-- 1 root root 2.8K Jul  7 20:21 many_sentences_example.py
-rw-r--r-- 1 root root  249 Jul  7 20:20 my_first_example.py
```

Now we are going to execute the first example:
```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

if __name__ == "__main__" :

	analyzer = SentimentIntensityAnalyzer()
	text = "The first lovely example of vaderSentiment."
	result = analyzer.polarity_scores(text)
	print(result)
```

How to execute the code
```sh
python3 my_first_example.py

#output
{'neg': 0.0, 'neu': 0.568, 'pos': 0.432, 'compound': 0.5859}
```

## Many sentences example of sentiment analysis
In the next example we are going to launch a code with several senteces
```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# --- examples -------
sentences = ["VADER is smart, handsome, and funny.",  # positive sentence example
             "VADER is smart, handsome, and funny!",  # punctuation emphasis handled correctly (sentiment intensity adjusted)
             "VADER is very smart, handsome, and funny.", # booster words handled correctly (sentiment intensity adjusted)
             "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
             "VADER is VERY SMART, handsome, and FUNNY!!!", # combination of signals - VADER appropriately adjusts intensity
             "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!", # booster words & punctuation make this close to ceiling for score
             "VADER is not smart, handsome, nor funny.",  # negation sentence example
             "The book was good.",  # positive sentence
             "At least it isn't a horrible book.",  # negated negative sentence with contraction
             "The book was only kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
             "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
             "Today SUX!",  # negative slang with capitalization emphasis
             "Today only kinda sux! But I'll get by, lol", # mixed sentiment example with slang and constrastive conjunction "but"
             "Make sure you :) or :D today!",  # emoticons handled
             "Catch utf-8 emoji such as such as 💘 and 💋 and 😁",  # emojis handled
             "Not bad at all"  # Capitalized negation
             ]

# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):

	# Create a SentimentIntensityAnalyzer object.
	sid_obj = SentimentIntensityAnalyzer()

	# polarity_scores method of SentimentIntensityAnalyzer
	# object gives a sentiment dictionary.
	# which contains pos, neg, neu, and compound scores.
	sentiment_dict = sid_obj.polarity_scores(sentence)
	
	print("Overall sentiment dictionary is : ", sentiment_dict)
	print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
	print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
	print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

	print("Sentence Overall Rated As", end = " ")

	# decide sentiment as positive, negative and neutral
	if sentiment_dict['compound'] >= 0.05 :
		print("Positive")

	elif sentiment_dict['compound'] <= - 0.05 :
		print("Negative")

	else :
		print("Neutral")



# Driver code
if __name__ == "__main__" :

	i = 0
	for sentence in sentences:
		print("\nSentence "+str(i)+": \n"+sentence)
		sentiment_scores(sentence)
		i += 1
```

How to execute the code
```sh
python3 many_sentences_example.py

#output
Sentence 0: 
VADER is smart, handsome, and funny.
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.254, 'pos': 0.746, 'compound': 0.8316}
sentence was rated as  0.0 % Negative
sentence was rated as  25.4 % Neutral
sentence was rated as  74.6 % Positive
Sentence Overall Rated As Positive

Sentence 1: 
VADER is smart, handsome, and funny!
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.248, 'pos': 0.752, 'compound': 0.8439}
sentence was rated as  0.0 % Negative
sentence was rated as  24.8 % Neutral
sentence was rated as  75.2 % Positive
Sentence Overall Rated As Positive

Sentence 2: 
VADER is very smart, handsome, and funny.
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.299, 'pos': 0.701, 'compound': 0.8545}
sentence was rated as  0.0 % Negative
sentence was rated as  29.9 % Neutral
sentence was rated as  70.1 % Positive
Sentence Overall Rated As Positive

Sentence 3: 
VADER is VERY SMART, handsome, and FUNNY.
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.246, 'pos': 0.754, 'compound': 0.9227}
sentence was rated as  0.0 % Negative
sentence was rated as  24.6 % Neutral
sentence was rated as  75.4 % Positive
Sentence Overall Rated As Positive

Sentence 4: 
VADER is VERY SMART, handsome, and FUNNY!!!
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.233, 'pos': 0.767, 'compound': 0.9342}
sentence was rated as  0.0 % Negative
sentence was rated as  23.3 % Neutral
sentence was rated as  76.7 % Positive
Sentence Overall Rated As Positive

Sentence 5: 
VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.294, 'pos': 0.706, 'compound': 0.9469}
sentence was rated as  0.0 % Negative
sentence was rated as  29.4 % Neutral
sentence was rated as  70.6 % Positive
Sentence Overall Rated As Positive

Sentence 6: 
VADER is not smart, handsome, nor funny.
Overall sentiment dictionary is :  {'neg': 0.646, 'neu': 0.354, 'pos': 0.0, 'compound': -0.7424}
sentence was rated as  64.60000000000001 % Negative
sentence was rated as  35.4 % Neutral
sentence was rated as  0.0 % Positive
Sentence Overall Rated As Negative

Sentence 7: 
The book was good.
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.508, 'pos': 0.492, 'compound': 0.4404}
sentence was rated as  0.0 % Negative
sentence was rated as  50.8 % Neutral
sentence was rated as  49.2 % Positive
Sentence Overall Rated As Positive

Sentence 8: 
At least it isn't a horrible book.
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.678, 'pos': 0.322, 'compound': 0.431}
sentence was rated as  0.0 % Negative
sentence was rated as  67.80000000000001 % Neutral
sentence was rated as  32.2 % Positive
Sentence Overall Rated As Positive

Sentence 9: 
The book was only kind of good.
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.697, 'pos': 0.303, 'compound': 0.3832}
sentence was rated as  0.0 % Negative
sentence was rated as  69.69999999999999 % Neutral
sentence was rated as  30.3 % Positive
Sentence Overall Rated As Positive

Sentence 10: 
The plot was good, but the characters are uncompelling and the dialog is not great.
Overall sentiment dictionary is :  {'neg': 0.327, 'neu': 0.579, 'pos': 0.094, 'compound': -0.7042}
sentence was rated as  32.7 % Negative
sentence was rated as  57.9 % Neutral
sentence was rated as  9.4 % Positive
Sentence Overall Rated As Negative

Sentence 11: 
Today SUX!
Overall sentiment dictionary is :  {'neg': 0.779, 'neu': 0.221, 'pos': 0.0, 'compound': -0.5461}
sentence was rated as  77.9 % Negative
sentence was rated as  22.1 % Neutral
sentence was rated as  0.0 % Positive
Sentence Overall Rated As Negative

Sentence 12: 
Today only kinda sux! But I'll get by, lol
Overall sentiment dictionary is :  {'neg': 0.127, 'neu': 0.556, 'pos': 0.317, 'compound': 0.5249}
sentence was rated as  12.7 % Negative
sentence was rated as  55.60000000000001 % Neutral
sentence was rated as  31.7 % Positive
Sentence Overall Rated As Positive

Sentence 13: 
Make sure you :) or :D today!
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.294, 'pos': 0.706, 'compound': 0.8633}
sentence was rated as  0.0 % Negative
sentence was rated as  29.4 % Neutral
sentence was rated as  70.6 % Positive
Sentence Overall Rated As Positive

Sentence 14: 
Catch utf-8 emoji such as such as 💘 and 💋 and 😁
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.615, 'pos': 0.385, 'compound': 0.875}
sentence was rated as  0.0 % Negative
sentence was rated as  61.5 % Neutral
sentence was rated as  38.5 % Positive
Sentence Overall Rated As Positive

Sentence 15: 
Not bad at all
Overall sentiment dictionary is :  {'neg': 0.0, 'neu': 0.513, 'pos': 0.487, 'compound': 0.431}
sentence was rated as  0.0 % Negative
sentence was rated as  51.300000000000004 % Neutral
sentence was rated as  48.699999999999996 % Positive
Sentence Overall Rated As Positive
```

The ``compound`` score is computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive). This is the most useful metric if you want a single unidimensional measure of sentiment for a given sentence. Calling it a 'normalized, weighted composite score' is accurate. 
 
It is also useful for researchers who would like to set standardized thresholds for classifying sentences as either positive, neutral, or negative.  
Typical threshold values (used in the literature cited on this page) are:

**positive sentiment**: ``compound`` score >=  0.05
**neutral  sentiment**: (``compound`` score > -0.05) and (``compound`` score < 0.05)
**negative sentiment**: ``compound`` score <= -0.05






