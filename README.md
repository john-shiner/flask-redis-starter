# Minimal app with docker-compose, k8s, python3, flask, redis

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

### Minikube deployment commands (run from k8s directory)

Invoke (inv) commands

* inv deploy            # brings up the application stack
* inv undeploy          # brings down the application stack
* inv scale -n <count>  # sets the web deployment replicas to 'count'

Redis client starter script

* ./redis-client.sh     # invokes redis client for exposed redis ports

After running the deploy command, run 'minikube services' to get exposed ports

