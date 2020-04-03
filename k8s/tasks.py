#!/usr/bin/python3
"""Run these tasks from the project k8s/ directory"""
from invoke import task

@task
def deploy(c):
    "Run this to deploy the application stack to minikube"
    # c.run("kubectl create -f ./redis-deployment.yml")
    # c.run("kubectl expose ExternalName --name="redis" --type=ExternalName ")
    c.run("kubectl create -f ./redis-service.yml")
    c.run("kubectl create -f ./flask-container-service.yml")
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
    "Run the output of this command for Redis-cli access"
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
