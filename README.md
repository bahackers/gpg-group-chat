GPG group chat
==============

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

# Issue board

[Waffle.io/bahackers/gpg-group-chat](https://waffle.io/bahackers/gpg-group-chat)
