swasthya
--------

```
brew install helm


docker build -t swasthya-server:1.0 .
kubectl create namespace dev
kubectl apply -f k8s-healthcheck-deployment.yaml --namespace dev
```
