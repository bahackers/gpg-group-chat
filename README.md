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

1. Server starts with gpg-group-chat --server at 192.168.0.1
2. The client1 starts with gpg-group-chat --client --server-ip=192.168.0.1 --public-key=public-key1
3. The client1 connect to the server and the it stores the public key for client1
4. The server send the current list of keys for client1 (contains public key1)
5. The client2 starts with gpg-group-chat --client --server-ip=192.168.0.1 --public-key=public-key2
6. The client2 connect to the server and the it stores the public key for client2
7. The server send the current list of keys for client1 and client2 (contains public key1 and public key2)
8. The client3 starts with gpg-group-chat --client --server-ip=192.168.0.1 --public-key=public-key3
9. The client3 connect to the server and the it stores the public key for client3
10. The server send the current list of keys for client1, client2 and client3 (contains public key1, public key2 and public key3)
11. The client2 disconnects from the server
12. the server delete the public key from client 2 from the storage
13. The server send the current list of keys for client1 and client3 (contains public key1 and public key3)
...

# Issue board

[Waffle.io/bahackers/gpg-group-chat](https://waffle.io/bahackers/gpg-group-chat)
