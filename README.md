NBSAP platform
==============


Project Name
------------
This project enables quick installation for the NBSAP platform using Docker.


Prerequisites - System packages
-------------------------------

These packages should be installed as superuser (root).

### Debian based systems ###

    apt-get install docker pip git
    pip install docker-compose

### RHEL based systems ###

    yum install docker git epel-release
    yum install python-pip
    pip install docker-compose

Prerequisites - System services
-------------------------------

These services should be running:

    sudo service docker start


Product directory
-----------------

Create a new user:

    useradd nbsap -d /var/local/nbsap

Create a docker group and add user `nbsap` to it:

    sudo groupadd docker
    sudo usermod -aG docker nbsap
    sudo service docker restart


Install project (dev)
---------------------
The following commands will be run as an unprivileged user in the product
directory:

    su nbsap
    cd

1. Clone the repository:

        git clone https://github.com/eea/eea.docker.nbsap.git --recursive
        cd eea.docker.nbsap

2. Copy enviroment files:

        cp -R env.example env


3. Start docker containers:

        docker-compose up -d

4. Migrate and load fixtures

        docker-compose run dev manage.py migrate
        docker-compose run dev manage.py load_fixtures



Deployment to rancher
----------------------

First time when deploying a new instance:

    rancher-compose -e env/<instance_name>.env up -d <instance_name>

After changing docker-compose or rancher-compose file:

    rancher-compose -e env/<instance_name>.env up -d --upgrade <instance_name>
    rancher-compose -e env/<instance_name>.env up -d --confirm-upgrade <instance_name>

When the image is changed:

    rancher-compose -e env/<instance_name>.env pull <instance_name>
    rancher-compose -e env/<instance_name>.env up -d --force-upgrade <instance_name>


Contacts
========

People involved in this project:

* Dragos Catarahia (dragos.catarahia at eaudeweb.ro)
* Iulia Chiriac (iulia.chiriac at eaudeweb.ro)
* Eduard Zaharia (eduard.zaharia at eaudeweb.ro)
