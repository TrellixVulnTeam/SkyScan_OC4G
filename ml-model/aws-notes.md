# Notes on using AWS
A collection of notes on how to use these notebooks on AWS.

## Setup

### Starting an EC2 instance

1. Search for the `Deep Learning Base AMI (Ubuntu 18.04)` AMI. 
1. Select a `p2.xlarge` instance type.
1. Under Configure Security Group, add a custom TCP rule for **TCP** and Port **8888** open to anywhere - This is for the Jupyter Notebook Server
1. Under Configure Security Group, add a custom TCP rule for **TCP** and Port **5151** open to anywhere - This is for the Voxel51 server.
1. Create a KeyPair if you don't have one yet registered. I stored mine in ~/.aws
1. Changes its permissions: `chmod 0600 ~/.aws/Macbook.pem`
1. SSH there: `ssh -i ~/.aws/macbook.pem ubuntu@192.168.108.217`
1. You can test to make sure Docker + Nvidia GPU is work with: `sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi`
1. I think we need to use Personal Access Tokens to pull down the Private Repo from Github, more details here: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
1. You can now do `git clone https://github.com/IQTLabs/SkyScan-Private.git` to clone the Repo. Use your username (*lberndt@iqt.org*) and the Personal Access Token as the password.
1. Now go follow the readme...

### Upgrade Docker Compose
We need to do this so we can use `docker-compose` with a GPU easily. From https://docs.docker.com/compose/install/
1. `sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
1. `sudo chmod +x /usr/local/bin/docker-compose`
1. 


### Setting up EFS

1. https://labzero.com/blog/mount-amazon-efs-drives-inside-docker-for-simple-network-storage
1. Create EFS
1. Create a security group rule to allow for NFS for the EFS connection: **TCP** and Port **2049**
1. View the Filesystem
1. Under Network, create a mountpoint


### Starting up the server

1. `cd ~/SkyScan-Private/ml-model/`
1. `docker-compose build` If it is the first time or if you have new code
1. `docker-compose up`


If you **stop** the AWS instance while the container is running, the container should automatically start back up again when you **start** the instance the next time.

### Copying Media to EC2
Before you can write you will need to set the directories to by owned by the Ubuntu user: ` sudo chown -R ubuntu:ubuntu *`
`rsync -avz -e "ssh -i ~/.aws/macbook.pem" capture-5-13 ubuntu@192.168.108.217:/home/ubuntu/SkyScan-Private/ml-model/media/`
`scp  -p -i ~/.aws/macbook.pem capture-5-13 ubuntu@192.168.108.217:/home/ubuntu/SkyScan-Private/ml-model/media/`

### Copying JSON Export to EC2
````
scp -i <path & filename>.pem <filename>.json ubuntu@<private.ip.address>:~/SkyScan-Private/ml-model/media
````

### Shutting down, but leaving the server running
You can just close your terminal window and the Contain with the Jupyter notebook will keep running.

### Docker Commands

List the running containers:
`docker ps`

