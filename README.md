# Newtral - The Neutral News Filter
Reading the news can be overwhelming and intimidating at times. It’s hard to tell what’s fact and what’s opinion. With Newtral, we bring your attention to the facts.

## Submission
Submitted for HackUTD Fall 2019
### Awards
- Cognizant: Best Text Objectivity Analysis
- Overall top 5 among 110 submissions

## Inspiration
Reading the news can be overwhelming and intimidating at times. You should be able to form your own opinions, but to do so you need unbiased sources. It’s hard to tell what’s fact and what’s opinion as it may be subtle. With Newtral, we bring your attention to the facts.

## What it does
Our chrome extension, when activated, scans the news article and highlights objective lines of the article while noting sentences that are more subjective based on the emotional threshold using an API we built to help the reader better analyze the article reported.

## How we built it
- The Parser code was made in Python using TextBlob to calculate the subjectivity score and PyMongo to connect to the database.
- The server code was made in Node.js using Express and Mongoose and hosted on Google Cloud App Engine.
- The client code was made in JavaScript, HTML and CSS using Google Chrome APIs.

## Challenges we ran into
Google Chrome Extensions split up its JavaScript files so we had to figure out the correct way to pass data between them.

## Accomplishments that we're proud of
We are very proud that we all challenged ourselves and learned a lot during this hackathon. We are proud that we were able to discuss our different ideas for this application and collaborate to create a useful app for our fellow newsreaders.

## What we learned
This was the first time we have made a Google Chrome extension so we learned how they are developed. We also have been wanting to learn more about Artificial Intelligence and this was the first time we were able to learn and apply Natural Language Processing.

## What's next for Newtral
We found that TextBlob does not always accurately rank the subjectivity of questions, especially rhetorical or leading questions often found in news articles. In the future, we would add support for these types of questions. In addition to this, we currently support CNN, BBC, Fox News, and New York Times articles, but would like to add support for many more news sources in the future.

## Demo
https://www.youtube.com/watch?v=kJJ_b9R2dqg

## Devpost
https://devpost.com/software/newtral-the-neutral-news-filter
