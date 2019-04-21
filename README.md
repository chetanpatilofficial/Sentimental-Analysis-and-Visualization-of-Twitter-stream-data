# Sentimental Analysis and Visualization of Twitter stream data related to General Elections in India
 
Using specific filters in Tweeter to pull the tweets related to Indian Election and process those live tweets to analyse trends, patterns, sentiments etc. and provide useful insights in form of dynamic visualizations.

Implemented three use-cases for Twitter Stream Data Analysis:
  * Use-case 1: Sentiment Analysis of tweets related to Indian National Election and visualization using Time-series Line Graphs
  representing three categories of sentiments - Positive, Negative & Neutral
  * Use-case 2: Visualization of tweets distribution among popular Political Parties in India using Time Series Donut chart
  * Use-case 3: Visualization of the Top-6 trending #Hashtags using Word-Cloud graphs

Project Workflow:
  * Once we are registered with Twitter APIs, we can consume the Twitter streams in real-time. 
  * I am using a NetCat utility which reads the tweet streams and publishes on a port 9999 on the localhost.
  * Our Spark instance then listens on the port 9999 and reads the live streams and processes it. 
  * All our use cases are implemented inside Spark using python code and libraries. 
  * Once the tweets are processed using custom business logic, the outputs in json format are pushed to multiple Kafka Topics We have a separate nodejs server setup up for reading the Kafka topic and perform visualizations using d3js

Infrastructure Setup:
  * Google Cloud (GCP) Compute Instance to host our Servers. (Specification: 4 cores CPU, 15 GB RAM, 500 GB HDD)
  * Apache Spark 2.4.1
  * Apache Kafka
  * NodeJS Server (Read from Kafka topic and push to d3.js UI)
  * D3.js for Data Visualization
  * Jupyter Notebook server for Coding in Python 3
  * Python 3.6
  * Java 8.x

Tools & Libraries:
  * Tweepy library to interact with Twitter APIs
  * NetCat utility to read the streams from Twitter API and publish on local port
  * Pyspark library to code in Spark on Python 3.6
  * Kafka libraries to interact with Kafka(Producer) in Python
  * TextBlob library for Sentiment Analysis
  * NLTK libraries for text processing
  * NodeJS kafka-node libraries to interact with Kafka(Consumer)
  * NodeJS socket.io libraries to push messages from Kafka to D3.js UI
