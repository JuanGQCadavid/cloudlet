# Overview - Top botton view

The cloudlet in composed by one or more Pixel 4 phones. The cluster is being managed by docker swarm, this one is the responable of creating an overlay network layer that allows containers reached each other using the same ip adress.  Moreover, docker swarm is the responsable of distributing the load of the containers across each node. 

In order to have docker swarm, the only requisite is to have docker installed in each device. 

Each mobile phone has PostmaketOS as linux kernel.

Each mobile phone has one role in the docker swarm cluster, it could be ether Master (M) or Compute (C) node. Both of them (M, C) can and will host docker containers, the only difference is that only masters can deploy, update, or delete a stack in the cluster. When a cluster has more than one Master, then election process happens to select only one leader for the whole cluster, the remaining M nodes will be as candidates, as soon as the leader is not reacheble, the Master nodes will create a new term.

> :warning: When the cluster has two active master, the leader election does not work.

![Overview](img/overview.png)

# Actual stacks.

The cluster has two stacks, one for adminstration and one application stack for testing.

> ⚠️ Be aware that the cluster made of Pixel 4 are a **ARMx32** bits!, What this means is that whatever is deployed must be compiled to linux/arm/v7 architecture in docker. This is a pain in the ass 🫠.


## Administration - Portainer

[portainer_agent](stacks/portainer_agent.yml) has two containers, an agent that will be deployed in all nodes and a administration palenl that will be only deploy on the manager with only one replica.

> ⚠️ The **MASTER_NODE_IP** is the ip of one of the master nodes, or the leader ip address, this IP will be the entry point for all nodes not matter where are they deployed.

This service could be accessed by *http://**MASTER_NODE_IP**:9000*, credentials on Aug 22 was admin/Asdf1234 but this could be change by [re-deploying](#deploy-and-update-an-stack) the stack.

## Go coffe app - Demo application



# Hows to

## Set up a cluster

## Deploy and update an stack

## Destroy an stack

## Useful commands




