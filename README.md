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

logs
----

```
$ kubectl logs -f swasthya-server-75df7cb8f9-x4wcn --namespace dev
loading urls to check health
checking health for servers
starting health check for 3 services.
'https://api.github.com' : 200
'https://twitter.com' : 200
'https://api.facebook.com' : 200
```

Also see
--------

- https://github.com/prayagupd/eccount-rest/tree/master/devops
