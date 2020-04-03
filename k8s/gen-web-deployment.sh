kubectl run web --image=johnshiner/flask-redis-frontend:v1 --replicas=1 --port=8080 \
                      --labels='app=flask,tier=frontend' \
                      --env="GET_HOSTS_FROM=dns" \
                      --dry-run --output=yaml > web-flask-deployment.yaml