## server-api-sentiment_a-docker
# This is a project involving multiple technologies:

- Write a code to upload a json to an online server (Mongo Atlas). The json file is a chat with multiple conversations, chats_Ids, user_Ids, names, date, etc.
- Write an API, which works remotely, to obtain(get) and write (post) information in the server.
- Work with mongo queries, through the API, to obtain different answers.
- Write a function which collect all comments of all users and perform a study of the sentiment, to get the average of positive or negative comments. The result is returned through the API
- Write a recommendation code to suggest users to new ones, based on their writings 

## How to:
- From src/
  - pymongo_code.py to link with Mongo Atlas
  - popuate.py to upload your json to Mongo Atlas
  - api.py to perform the queries using decorators (which will be the endings of the urls)

------------
## Future improvements:
- Write the .txt requirements file
- Write a docker image and upload it to heroku (deploy the docker)
- Perform the same actions in a SQL server
- Enrich the decorators and options to get from the API
​https://github.com/boyander/datamad-1019/tree/master/w5-d2-simple-api

## Links - API dev in python
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


https://www.digitalocean.com/community/tutorials/como-instalar-y-usar-docker-en-ubuntu-18-04-1-es

https://docs.docker.com/kitematic/

https://docs.docker.com/install/

https://github.com/Micro-learnings/Data-visualization

