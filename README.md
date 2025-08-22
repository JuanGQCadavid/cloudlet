# Overview - Top botton view

The cloudlet in composed by one or more Pixel 4 phones. The cluster is being managed by docker swarm, this one is the responable of creating an overlay network layer that allows containers reached each other using the same ip adress.  Moreover, docker swarm is the responsable of distributing the load of the containers across each node. 

In order to have docker swarm, the only requisite is to have docker installed in each device. 

Each mobile phone has PostmaketOS as linux kernel.

Each mobile phone has one role in the docker swarm cluster, it could be ether Master (M) or Compute (C) node. Both of them (M, C) can and will host docker containers, the only difference is that only masters can deploy, update, or delete a stack in the cluster. When a cluster has more than one Master, then election process happens to select only one leader for the whole cluster, the remaining M nodes will be as candidates, as soon as the leader is not reacheble, the Master nodes will create a new term.

![Master compute](img/master-node.png)

> :warning: When the cluster has two active master, the leader election does not work.

![Overview](img/overview.png)

# Actual stacks.

The cluster has two stacks, one for adminstration and one application stack for testing.

> ⚠️ Be aware that the cluster made of Pixel 4 are a **ARMx32** bits!, What this means is that whatever is deployed must be compiled to linux/arm/v7 architecture in docker. This is a pain in the ass 🫠.


## Administration - Portainer

[portainer_agent](stacks/portainer_agent.yml) has two containers, an agent that will be deployed in all nodes and a administration palenl that will be only deploy on the manager with only one replica.

> ⚠️ The **MASTER_NODE_IP** is the ip of one of the master nodes, or the leader ip address, this IP will be the entry point for all nodes not matter where are they deployed.

This service could be accessed by *http://**MASTER_NODE_IP**:9000*, credentials on Aug 22 was admin/Asdf1234 but this could be change by [re-deploying](#deploy-and-update-an-stack) the stack.

![Portainer](img/portainer.png)
![Portainer cluster](img/portainer_cluster.png)

## Go coffe app - Demo application

> ☢️ The stack has a reverse proxy, this one is accesible by using an IP address, if you deploy this stack you should update the param services.web.environment.**REVERSE_PROXY_URL** with the master node Ip address.

[go_coffe.yml](stacks/go_coffe.yml) is a demo app in golang that helps to show that the cluster is able to support a whole application with backend, frontend, database and event streaming sources. Go coffe is compose of:

* postgres:14 
* rabbitmq:3.11
* Six golang applications under juangonzalout dockerhub account.

All previous images are ARMx32, which makes them suitable for working on the cluster.

![Go coffe](img/go-coffe.png)

### Volume test on Go coffe app

This project also contains a volumen test located on [locustfile.py](load_test/locustfile.py). In order to run the test, [locust](https://docs.locust.io/en/stable/installation.html) should be installed in the host machine.

Once Locus is installed you should:

``` sh
$ cd load_test
$ locust
```

Then type the ip address of the master node and [start the test](https://docs.locust.io/en/stable/quickstart.html).


This is the last load test demo on the cluster.

![loadtest](img/loadtest.png)

# Hows to

## Connect to a phone

> ⚠️ All four phones has the same password **1234**

* You could use the screem, password **1234**
* You could connect them to a **linux** laptop by cable, then connect by ssh, same credentials to all phones.
    * user: cloudlet
    * password: 1234

``` bash
$ ssh cloudlet@
```

## Set up a cluster


## Deploy and update an stack

## Destroy an stack

## Useful commands




