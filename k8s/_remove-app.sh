#! /bin/sh

kubectl delete service web redis
kubectl delete deployment web redis

date >> log.txt
echo 'removed app' >> log.txt
kubectl get pods >> log.txt
