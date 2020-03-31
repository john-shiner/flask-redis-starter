#! /bin/sh

kubectl create -f ./redis-deployment.yml
kubectl expose deployment redis --port=6379 --target-port=6379 --type=LoadBalancer --name=redis
kubectl create -f ./flask-container-service.yml
minikube service list

date >> log.txt
minikube service list >>log.txt
minikube service web
