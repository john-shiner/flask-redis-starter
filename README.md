# Minimal app with docker-compose, python3, flask, redis

app.py == minimal python flask/redis web app

Dockerfile ==  builds that app as a container (based on python 3.8 image)

docker-compose.yml == assembles the flask and redis containers into an application

Usage:

* docker-compose build  # build the containers in the docker-compose file

* docker-compose up  # add -d to run detached (in background)

* docker-compose stop  # stop the app, leave the containers

* docker-compose down  # stop the app, remove the containers (not the images)

Open/refresh http://localhost:5000 to see the app
