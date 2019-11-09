# Full Stack Application Development Using Python-Flask


## A Brief Introduction

A full stack application using python flask and and a suitable database with it. (MongoDB/SQL)

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. ... However, Flask supports extensions that can add application features as if they were implemented in Flask itself.

Flask is a micro web application framework. ... Flask does however include a web server that can be used for testing and development. But when you're ready to host your app or put it into production, you should choose a different web server to use with it.

Python can be used to build server-side web applications. While a web framework is not required to build web apps, it's rare that developers would not use existing open source libraries to speed up their progress in getting their application working. Python is not used in a web browser.



# Pre-requisites

One must have Python installed in his local system for deploying this Full stack application easily. Other than Python one must also have to install Python-Flask and its dependencies as mentioned in the requirements.txt file.

## Usage of Python Library "Newspaper3k" 


# Running this Web Application

using nohup (no hangup) 
```
nohup flask run &
```

**You can also run the Application via Gunicorn (Web Server)**

```
gunicorn --workers 4 --access-logfile /var/tmp/gunicorn.logs --bind 0.0.0.0:5000 wsgi:app
``` 

**workers = 4 (The number of worker processes. This number should generally be between 2-4 workers per core in the server.)**

**access-logfile = path of the file, where logs are to be saved**

**bind = Specify a server socket to bind.**


# Checking the User Interface

https://localhost:5000/


# ARCHITECTURE OF THE APPLICATION




# FEW ASPECTS RELATED TO USING PYTHON-FLASK

## Testing

Something that is not tested can be a headache. Python Flask actually provides a way to test your application, We can simply use libraries named as PyTest for testing Flask web services and APIs


## Security

For security of our RESTFUL API, we can use mulitple options, which are provide by Python-flask like Flask-JWT tokens, Flask OAuth2 libraries, Moreover one can have route authentication and authorization implemented in his web service.
In short vast variety of fruitful solutions are there, it depends on scenario and infrastructure that how one must chose to secure the endpoints and routes present in web service.

## Scalibility

A three tier architecture for scaling REST API to a huge infrastructure must be useful, One must kept database and webserver at two different nodes, and in between them there should be a load balancer that will handle the bulk amount of requests coming to the API. In this all the requests must be successfully handled and your web service can be easily scaled to a bigger infra.

## Documentation

This RESTFUL-API is written using Python-Flask, Huge, extensive and detailed documentation for flask is provided (http://flask.pocoo.org/docs/1.0/), Furthermore a very strong support is also there on multiple platform all around the web.

## Deployment

In the current scenario, Python-Flask own development web server is used to run the service. one must not use this technique on a production web server, Mulitple other web servers dedicated for running such type of service are present such as "Gunicorn" is a good example, we can also use "Apache" or "Nginx" for that. Also proper database either SQL or No-SQL depends on the usage setup must be used with the deployment.
