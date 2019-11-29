## server-api-sentiment_a-docker
# Multi-platform project: Mongo/SQL - Create an API - Sentiment Analysis of chats - Deploy a Docker container 
------------
![alt](data:image/jpeg;base64,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)
