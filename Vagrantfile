# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.network "forwarded_port", guest: 8080, host: 8080, 
    auto_correct: false

  config.vm.provider "virtualbox" do |v|
    v.memory = 1280
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "getroles.yml"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "site.yml"
    ansible.extra_vars = {
      ttrss_http_port: 8080,
      ttrss_require_ssl: false,
      ttrss_url: "http://localhost:8080/",
    }
  end

end
