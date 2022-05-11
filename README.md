
Slack Status
============

A simple Python Util for updating slack status.

# Getting Started
## Requirements

1. **Python 3.9.x**
~~~
$ virtualenv -p python3 venv
$ source venv/bin/activate
~~~

2. **Requirement**
~~~
$ pip install -e .
~~~

## Setting

You'll need your slack app token from https://api.slack.com/apps/

with "User Token Scopes": 'users.profile:write'

And create User OAuth Token: (e.g.) xoob-12341234-5667788....

You can check your Token in this online test: https://api.slack.com/methods/users.profile.set/test

## RUN

You can see startup options with --help before running.
~~~
$ auto --help
$ auto --token=(your token)
~~~
