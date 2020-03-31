#! /bin/sh

kubectl scale --replicas=$1 deployment web 

date >> log.txt
echo "scaled web nodes to $1" >> log.txt
kubectl get pods >> log.txt
