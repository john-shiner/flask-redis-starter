#!/usr/bin/python3
"""Run these tasks from the project k8s/ directory"""
from invoke import task

# @task
# def genredisyml(c):
#     "try out better use of yaml lables"
    # kubectl run db --image=redis --replicas=1 --port=6379 \
    #                         --labels='app=redis,tier=backend' \
    #                         --dry-run --output=yaml > new-redis-deployment-xx2.yaml

@task
def gh(c):
    "Open the current github branch on GitHub"
    c.run("open $(git remote -v | cut -f 1 -d ' ' |cut -f 2 | sed 1d | cut -d '.' -f1-2)/tree/$(git rev-parse --abbrev-ref HEAD)")
    
@task
def deploy(c):
    "Run this to deploy the application stack to minikube"

    # kubectl expose deployment db --selector='app=redis,tier=backend' \
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
    "Run this to remove (all) the application stack(s) from minikube"
    # c.run("kubectl delete service web redis")
    # c.run("kubectl delete deployment web redis")
    c.run("kubectl delete all --all")

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

