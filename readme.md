# Node Installation
This project provides ability to install swarm of test generator machines for android applications.
It installs docker containers on remote servers and setup the environment to generate tase cases.
This project uses [Ansible](https://www.ansible.com/) to interact with remote servers and docker service inside them.

This project provides following functionalities:
1. Installing docker containers
1. Setup multiple services necessary for geneating test cases inside containers
1. Updating source code and configurations of test generators
1. Fetching results and status of test generation