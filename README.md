
# This is a project involving several technologies:


- Write a code to upload a json file to an online server (Mongo Atlas). The json file is a chat with multiple conversations, chats_Ids, user_Ids, names, date, etc.

- Write an API, which works remotely.

- Write several functions to post and get all kind of information through the API using mongo queries.

![alt](https://raw.githubusercontent.com/albertovpd/server-api-sentiment_a-docker/master/output/messages2.png "decorators")

- Write a function which collect all comments of all users and perform a study of the sentiment, to get the average of positive or negative comments. The result is returned through the API.

![alt](https://raw.githubusercontent.com/albertovpd/server-api-sentiment_a-docker/master/output/messages1.png "stuff")

- Write a recommendation code to suggest users to new ones, based on their writings. This recommendation system is based on the analysis of chats, using some class of the <b>nltk</b>  library.

![alt](https://raw.githubusercontent.com/albertovpd/server-api-sentiment_a-docker/master/output/recommending.png "reco")

## How to:

- From src/
  - pymongo_code.py to link with Mongo Atlas.

  - populate.py to upload your json to Mongo Atlas.

  - api.py to perform the queries using decorators (which will be the endings of the urls). There are several functions with decorators for the purpose commented above.

  - In functions.py are saved the Sentiment reports and metrics imported in "recommender.ipynb". This is the only Jupyter Notebook script of my project and GitHub says all project is written in Jupyter Notebook... The curse of Jupyter Notebook on analysts.

# Conclusion.

## Accomplished goals.

    - Decorators.
    - Create your own API with several features.
    - Connect your API with an online server.
    - Request and post information. 
    - Process all the stored information.


## Future improvements:

- Write a docker image and upload it to heroku (deploy the docker)
- Perform the same actions in a SQL server
- Enrich the decorators and options to get from the API
​https://github.com/boyander/datamad-1019/tree/master/w5-d2-simple-api

----------------------

# References.

### Links - API dev in python
- [https://bottlepy.org/docs/dev/]
- [https://www.getpostman.com/]
​
## Links - NLP & Text Sentiment Analysis
- [https://www.nltk.org/]
- [https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386]
- [https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk]
​
# Links - Heroku & Docker & Cloud Databases
- [https://docs.docker.com/engine/reference/builder/]
- [https://runnable.com/docker/python/dockerize-your-python-application]
- [https://devcenter.heroku.com/articles/container-registry-and-runtime]
- [https://devcenter.heroku.com/categories/deploying-with-docker]
- Mongodb Atlas [https://www.mongodb.com/cloud/atlas]
- MySQL ClearDB [https://devcenter.heroku.com/articles/cleardb]

- https://www.digitalocean.com/community/tutorials/como-instalar-y-usar-docker-en-ubuntu-18-04-1-es

- https://docs.docker.com/kitematic/

- https://docs.docker.com/install/

- https://github.com/Micro-learnings/Data-visualization

