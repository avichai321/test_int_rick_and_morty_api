# Rick and Morty api test

This a python script api who pull out from "Rick and Morty api" specific characters.
this is also a test from int collage
in the api just the python code:
https://localhost/8080

there is two sub endpoints

* /fetch_char = who represent the results from the api
* /healthcheck = who show the server status

# Repository structure

The main files in this repository are:

* `Dockerfile` specifies how the application is built and packaged
* `Yamls folder` contains yaml to deploy the app with k8s (Tested with minikube)


# Yamls

in order to build the app in k8s or minikube you need to use the 3 yamls
* `service` who give you the service of the app whos connect to the depolyment
* `deployment` the app give you two replicas change as you want
* `ingress` who give you the app that you can see her in http port with clusterIP

deploy the yaml in the current order

# helm Chart

the application is also can deploy with helm chart

* the helm chart tgz file is also in the folder you can deploy it with `helm install app ./rick-and-morty-rest-api-0.1.0.tgz`
* the app will open in browser in http port 80 like the yamls deploy 


# Github Action
 i build github action who check if the endpoind of my app are reachable and the code is okay

there are few importent stages in this workflow and one job who called deploy who contians this stages

* `Checkout repository` = the simple check for the repo before start

* `Set up Minikube` - set a minikube eniviroment

* `Install Helm` - install helm for using helm commands

* `Sleep for 30 seconds` - gave some time to minikube enviroment to fully implemted

* `Add Minikube IP to /etc/hosts` - to use my local domain i need to implent the domain name in /etc/host with minikube ip

* `Check Minikube Status After Deploy` - check again all the components of the minikube app

* `Deploy to Kubernetes` - deploy the helm chart of my app to the minikube enviroment

* `Wait for deployment` - wait until all the pods of the app is running

* `Sleep for 30 seconds` - give time to the ingress service in my app to fully upload and get the ingress ip

* `Test Fetch Characters Endpoint` - check if the path /fetch_char is reachable 

* `Test Health Check Endpoint` - check if the path /healthcheck is reachable

* `Stop Minikube` finish all and shutdown the minikube


# Created By

Avichai Dahan course May 23