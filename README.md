# Full Stack Application Development Using Python-Flask
hello

## A Brief Introduction

A full stack application using python flask and and a suitable database with it. (MongoDB/SQL).
Python-Flask is a micro web framework written in Python which is used to develop small and large scale web applications. It is easy to use and its also scalable.


# Pre-requisites

## Python Flask with gunicorn

One must have Python installed in his local system for deploying this Full stack application easily. Other than Python one must also have to install Python-Flask and its dependencies as mentioned in the requirements.txt file.

## Usage of Python Library "Newspaper3k"

For scraping the news, we have used the python-library "Newspaper3k", which scrapes news web URLs to fetch and retrieve different kind of information using different techniques.

View a working online demo here: http://newspaper-demo.herokuapp.com

# Running this Web Application

**using nohup (no hangup)**
```
nohup flask run &
```

**You can also run the Application via Gunicorn (Web Server)**

```
gunicorn --workers 4 --access-logfile /var/tmp/gunicorn.logs --bind 0.0.0.0:5000 wsgi:app
``` 

**workers = 4** (The number of worker processes. This number should generally be between 2-4 workers per core in the server.)

**access-logfile =** path of the file, where logs are to be saved

**bind =** Specify a server socket to bind.


# Checking the User Interface

https://localhost:5000/


# Few Aspects Related To Using Python-Flask

## Testing

Something that is not tested can be a headache. Python Flask actually provides a way to test your application, We can simply use libraries named as PyTest for testing Flask web services and APIs


## Security

For security of Flask based Web Application or RESTFUL API, we can use mulitple options, which are provide by Python-flask like **Flask-JWT tokens, Flask OAuth2** libraries, Moreover one can have route authentication and authorization implemented in his web service.
In short vast variety of fruitful solutions are there, it depends on scenario and infrastructure that how one must chose to secure the endpoints and routes present in web service. Furthermore Python-Flask also has libraries for **session management** and **role based authentication** mechanisms.

## Scalibility

A three tier architecture for scaling web application to a huge infrastructure must be useful, One must kept database and webserver at two different nodes, and in between them there should be a load balancer that will handle the bulk amount of requests coming to the API or Web application. In this manner all the requests must be successfully handled and your web application can be easily scalable to a bigger infrastructure. Moreover it is easy to contanerized python-flask application and it can be easily moved to any clustered environment based on Docker-Swarm or Kubernetes.

## Documentation

This RESTFUL-API is written using Python-Flask, Huge, extensive and detailed documentation for flask is provided (http://flask.pocoo.org/docs/1.0/), Furthermore a very strong support is also there on multiple platform all around the web.

## Deployment

In the current scenario, Python-Flask own development web server is used to run the service. one must not use this technique on a production web server, Mulitple other web servers dedicated for running such type of service are present such as "Gunicorn" is a good example, we can also use "Apache" or "Nginx" for that. Also proper database either SQL or No-SQL depends on the usage setup must be used with the deployment.
