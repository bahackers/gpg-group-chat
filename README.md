# GPG group chat

[![GitHub version](https://img.shields.io/badge/version-dev-brightgreen.svg)]()
[![Snap CI branch](https://img.shields.io/snap-ci/bahackers/gpg-group-chat/master.svg?maxAge=2592000)](https://snap-ci.com/bahackers/gpg-group-chat/branch/master)
[![Python version](https://img.shields.io/badge/python-3.4-blue.svg)]()
[![license](https://img.shields.io/badge/license-GPL-blue.svg?maxAge=2592000)]()

## Setting up

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

### Run the tests

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

## Run the markdown lint

Once the gem **mdl** is installed run:

```shell
$ ./run md-lint
```

If the gem in not installed, its possible installing it using the command:

```shell
gem install bundler
bundle install
```

## Issue board

[Waffle.io/bahackers/gpg-group-chat](https://waffle.io/bahackers/gpg-group-chat)
