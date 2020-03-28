swasthya
--------

![](swasthya.png)

```
brew install helm

eval $(minikube docker-env) ## in order be in minikube context/ makes containers avail
docker build -t swasthya-server:1.0 .
kubectl create namespace dev
kubectl apply -f k8s-healthcheck-deployment.yaml --namespace dev
```


Also see
--------

- https://github.com/prayagupd/eccount-rest/tree/master/devops
