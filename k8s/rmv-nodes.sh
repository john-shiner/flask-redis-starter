#! /bin/sh

kubectl apply -f ./flask-container-service.yml

date >> log.txt
echo 'removed web nodes' >> log.txt
kubectl get pods >> log.txt
