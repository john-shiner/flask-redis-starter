kubectl expose deployment web --selector='app=flask,tier=frontend' --type=NodePort \
                                     --dry-run --output=yaml > web-flask-service.yaml