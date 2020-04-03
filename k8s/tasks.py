#!/usr/bin/python3
"""Run these tasks from the project k8s/ directory"""
from invoke import task

# @task
# def genredisyml(c):
#     "try out better use of yaml lables"
#     # kubectl run db --image=redis --replicas=1 --port=6379 \
#     #                         --labels='app=redis,role=master,tier=backend' \
#     #                         --dry-run --output=yaml > new-redis-master-deployment.yaml


@task
def deploy(c):
    "Run this to deploy the application stack to minikube"

    # replaces this script
    # kubectl create -f ./redis-deployment.yml
    # kubectl expose deployment redis --port=6379 --target-port=6379 --type=LoadBalancer --name=redis
    # kubectl create -f ./flask-container-service.yml
    # minikube service list

    # kubectl expose deployment db --selector='app=redis,role=master,tier=backend' \
    #                             --dry-run --output=yaml > new-redis-service.yaml

    c.run("kubectl create -f ./new-redis-deployment.yml")
    c.run("kubectl create -f ./new-redis-service.yml")
    c.run("kubectl create -f ./web-flask-deployment.yml")
    c.run("kubectl create -f ./web-flask-service.yml")
    c.run("minikube service list")

    c.run("date >> log.txt")
    c.run("minikube service list >>log.txt")
    c.run("minikube service web")

@task 
def undeploy(c):
    "Run this to remove the application stack from minikube"
    c.run("kubectl delete service web redis")
    c.run("kubectl delete deployment web redis")

    c.run("date >> log.txt")
    c.run("echo 'removed app' >> log.txt")
    c.run("kubectl get pods >> log.txt")

@task
def scale(c, num=3):
    "Run this to scale the web pods to <num> replicas"
    str = "kubectl scale --replicas={} deployment web".format(num)
    c.run(str)
    c.run("date >> log.txt")
    str = "echo scaled web nodes to {} >> log.txt".format(num)
    c.run(str)
    c.run("kubectl get pods >> log.txt")

@task
def db(c):
    "Run the output of this command for a parameterized Redis-cli command string"
    str = "        redis-cli -h $(minikube ip) -p $(kubectl get service redis --output='jsonpath={.spec.ports[0].nodePort}')"
    c.run("echo {}".format(str))

    # c.run(str)

@task
def dbport(c):
    "Run this to return the exposed port for the redis service"
    str = "kubectl get service redis --output='jsonpath={.spec.ports[0].nodePort}'"
    print("----")
    c.run(str)
    print("    ")
    print("    ")

@task
def webport(c):
    "Run this to return the exposed port for the web service"
    str = "kubectl get service web --output='jsonpath={.spec.ports[0].nodePort}'"
    print("----")
    c.run(str)
    print("    ")
    print("    ")

@task
def dash(c):
    "Run this to launch the minikube dashboard"
    str = "minikube dashboard"
    c.run(str)

