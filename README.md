# CausalImpact

# Wikipedia data Collection using SPARQLWrapper :

## The goal of this project is the investigate "How event driven is Wikipedia?"
- To reach a conclusion I can look for points of anomalies in the time series plot and look for a justification from another event dataframe (main events, birthdays , celebrations , deaths , release dates ...)


- Problem for this project is that in order to answer this question we need to evaluate wikipedia as a whole website not just select some articles
- Solution:  An idea could be to generate 10000 of  datatframes (people , events , science , art , dates ...) and then evaluate the time series dataframes.
- We can also have a language feature (fr, en , de ...) and then evaluate the user behaviour when it comes to language.

## The goal of this Notebook is Data collection:


First phase of the project is the data collection phase. For this we must have define different categories for our searches for example: list of people, events, dates, object…

- Specifically we want to select classes  in each of the defined cathegories: disasters, culture.
    - disasters will contain 3 classes: air accidents, Train collisions, helicopters
        - air accidents will contain the names of the air accidents that occured from 2015 to this day
    - culture will contain 3 classes: films, actors, charactors
        - each class will contain apropriate events that occured from 2015 to this day
        
In order to generate these terms I  used https://query.wikidata.org/  to extract the reseach query 

Get items to search: https://query.wikidata.org/querybuilder/?uselang=en


The next step is to extract the time series view data for each turm I used Analytics/AQS/Pageviews form the pything lib pageviewapi: 
https://pypi.org/project/pageviewapi/


- This page documents the Pageview API (v1), you can get pageview trends on specific articles or projects; filter by agent type or access method, and choose different time ranges and granularities; you can also get the most viewed articles of a certain project and timespan, and even check out the countries that visit a project the most. 


 
