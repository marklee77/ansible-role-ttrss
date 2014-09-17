marklee77.ttrss
==================

The purpose of this role is to install ttrss to a web server and enable
access with nginx. 

Role Variables
--------------

Example Playbook
----------------

    - hosts: all
      sudo: True
      roles:
        - marklee77.mariadb
        - marklee77.modules-extra
        - marklee77.ttrss

Try it Out
----------

Check out the github repository, vagrant up, and load http://localhost:8888 in
your web browser.

License
-------

GPLv2

Author Information
------------------

http://stillwell.me

