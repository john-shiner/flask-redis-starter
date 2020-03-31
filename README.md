# Minimal app with docker-compose, python3, flask, redis

app.py == minimal python flask/redis web app

To check code quality locally, you can run flake in a container:
* alias flake="docker run -ti --rm -v $(pwd):/apps alpine/flake8:3.5.0"
* flake --help
* flake app.py

Dockerfile ==  builds that app as a container (based on python 3.8 image)

docker-compose.yml == assembles the flask and redis containers into an application

Usage:

* docker-compose build  # build the containers in the docker-compose file

* docker-compose up  # add -d to run detached (in background)

* docker-compose stop  # stop the app, leave the containers

* docker-compose down  # stop the app, remove the containers (not the images)

Open/refresh http://localhost:8000 to see the app

## Kubernetes (minikube)

### k8s/ Commands

* deploy-app.sh
* remove-app.sh
* scale-web.sh

# after deploy script, running 'minikube services' to get exposed ports

Mon Mar 30 12:10:46 CDT 2020
|----------------------|---------------------------|--------------|-----------------------------|
|      NAMESPACE       |           NAME            | TARGET PORT  |             URL             |
|----------------------|---------------------------|--------------|-----------------------------|
| default              | kubernetes                | No node port |
| default              | redis                     |              | http://192.168.99.100:30059 |
| default              | web                       |              | http://192.168.99.100:30149 |
| kube-system          | kube-dns                  | No node port |
| kubernetes-dashboard | dashboard-metrics-scraper | No node port |
| kubernetes-dashboard | kubernetes-dashboard      | No node port |
|----------------------|---------------------------|--------------|-----------------------------|

# using redis-cli

| => redis-cli -h '192.168.99.100' -p 30059
192.168.99.100:30059> keys *
1) "_app:db:test"
2) "hits"
192.168.99.100:30059>
