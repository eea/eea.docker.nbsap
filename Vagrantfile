# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.synced_folder ".", "/var/local/eea.docker.nbsap", type: "nfs"
  config.vm.hostname = "nbsap.dev"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end
  config.vm.network "private_network", ip: "1.2.3.8"

  config.vm.provision :docker
  # config.vm.provision :docker_compose,
  #     yml: "/var/local/eea.docker.nbsap/docker-compose.yml",
  #     run: "always"
  end
