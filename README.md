ploy
====

Continuous integration

* 100% free and open-source
* Run on your own workstation or server.
* Based on python packages only. Can be installed in one step.


Getting started
---------------

Start the ploy server:
```shell
ploy start
```

Create a file named `ploy.yml` in your repository root with build instructions:
```YAML
- echo "Hello"
- echo "World!"
```


Use at home with ngrok
----------------------

[Ngrok](https://ngrok.com/) is a handy tool which helps to expose Ploy running
on your home machine (where it may be behind a router, or without a static IP)
to the internet, which is necessary if you want to work with github webhooks for
example. Download it from their website, extract the
zip-file and run it in a (separate) terminal:

```
ngrok http 6543
```
It will tell you at which address you can find your Ploy.

