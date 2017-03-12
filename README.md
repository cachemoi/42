# Tweet Meter

We created the basis of a product which will predict if a person's tweets can affect a company's stock price.

This question is not solely academic, since there has been some online buzz about the possible effects of Trump's tweets
on a company's stock price.

We have a python script which pulls tweets given a username. It is a webscraper to get around the fact that twitter's search
API has some major limits that would make our product unusable.

The tweets are fed through a sentiment analysis pipeline to yield a mood rating. This is used as a feature vector.

The finacial data is turned into returns, and this is also used as a feature vector for our ML algorithm.

The data is fed into a neural network regression algorithm, and yields a coefficient of determination.

We use this coefficient of determination to judge if the person's tweets affect stock prices of a given company.

As a case study, we pulled 30000 tweets from Trump's account, and determined if they affected apple or microsoft stock.

According to our work, they do get affected.

Model on: https://gallery.cortanaintelligence.com/Experiment/Twitter-sanity-check-1

<img src="https://github.com/cachemoi/42/blob/master/model_screenshot.png" width="80%"/>
