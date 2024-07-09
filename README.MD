# Rick and Morty api test

This a python script api who pull out from "Rick and Morty api" specific characters.
this is also a test from int collage
in the api just the python code:
https://localhost/8080

there is two sub webs

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

# Created By

Avichai Dahan course May 23