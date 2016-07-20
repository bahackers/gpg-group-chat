GPG group chat
==============

[![GitHub version](https://img.shields.io/badge/version-dev-brightgreen.svg)]()
[![Snap CI branch](https://img.shields.io/snap-ci/bahackers/gpg-group-chat/master.svg?maxAge=2592000)](https://snap-ci.com/bahackers/gpg-group-chat/branch/master)
[![Python version](https://img.shields.io/badge/python-3.4-blue.svg)]()
[![license](https://img.shields.io/badge/license-GPL-blue.svg?maxAge=2592000)]()

# Setting up

First of all make sure that your have Python 3, pip and virtualenv installed.

Onde you have all those installed clone the project and go to the directory
```shell
$ git clone git@github.com:bahackers/gpg-group-chat.git
$ cd gpg-group-chat
```

After that we recommend create a virtualenv to install the app dependencies
```shell
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python setup.py develop
```

## Run the tests

We are using PyTest, if you follow the setting up steps run the command
```shell
$ py.test ./test
```

## Run the app in server mode
```shell
$ gpg-group-chat --server
```

## Run the app in client mode
```shell
$ gpg-group-chat --client
```

## Basic usage flow

# Server starts with gpg-group-chat --server at 192.168.0.1
# The client1 starts with gpg-group-chat --client --server-ip=192.168.0.1 --public\_key=public\_key1
# The client1 connect to the server and the server stores the public key for client1
# The server send the current list of keys for client1 (contains public\_key1)
# The client2 starts with gpg-group-chat --client --server-ip=192.168.0.1 --public\_key=public\_key2
# The client2 connect to the server and the server stores the public key for client2
# The server send the current list of keys for client1 and client2 (contains public\_key1 and publick\_key2)
# The client3 starts with gpg-group-chat --client --server-ip=192.168.0.1 --public\_key=public\_key3
# The client3 connect to the server and the server stores the public key for client3
# The server send the current list of keys for client1, client2 and client3 (contains public\_key1, public\_key2 and public\_key3)
# The client2 disconnects from the server
# the server delete the public key from client 2 from the storage
# The server send the current list of keys for client1 and client3 (contains public\_key1 and public\_key3)
...

# Issue board

[Waffle.io/bahackers/gpg-group-chat](https://waffle.io/bahackers/gpg-group-chat)
