---
layout: post
title: Websphere 7 on Ubuntu Linux
date: 2016-08-29 13:47:50 -0300
category: java
tags: reblog
---

Sharing from [this post][post-link], where I found the solution to a stupid problem:

Recently I had to go through installing IBM Websphere 7.0 on a Ubuntu VM for development purposes. 
Installing Websphere (and other IBM server products) is already a pain in the ass by itself, but it turned out even worse as the process of creating a profile in order to start a server was broken with no obvious solution.

The output for the manageprofiles.sh script was simply:

```
INSTCONFFAILED: The profile could not be created.  For more information, consult
the /opt/IBM/WebSphere/AppServer/logs/manageprofiles/AppSrv01_create.log file
```

Pouring through the log file (XML by default, really?) one could find the line

```
/opt/IBM/WebSphere/AppServer/profileTemplates/default/action/generateKeysForSingleProfile.ant:25:
wsadmin task failed with return code :-1
```

However it turns out (as per the link provided in the beggining of the post) that the issue lies in the shell script that calls the ant script. It seems that the script expects to be run with sh or bash, and breaks since in Ubuntu sh is usually symlinked to dash.

The rather simple solutions to the problem:

1. Link /bin/sh to bash

```
:::sh
sudo unlink /bin/sh
sudo ln -s /bin/bash /bin/sh
```

1. Reconfigure sh via dpkg
    
```
:::sh
sudo dpkg-reconfigure dash
```

[post-link]: http://www.cnblogs.com/BruceLeey/archive/2010/09/18/1830419.html
