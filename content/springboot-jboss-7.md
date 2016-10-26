---
layout: post
title: Deploying Springboot applications on Jboss 7
date: 2016-03-01
category: java
---

Due to client, budget or technology constraints, sometimes we see ourselves having to use older, even obsolete versions of a given software/technology/language. The most recent here was having to use JBoss AS 7 to deploy some Java applications including one developed using [Spring Boot](http://projects.spring.io/spring-boot/). 

The process to turn a Spring Boot application into a deployable war is quite straightforward and well explained in their extensive [documentation](http://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#howto-create-a-deployable-war-file) and it consists of two steps:

1. Change your build tool file (pom.xml for us using Maven) to change the project packaging to war;
2. Update your main application class to extend `SpringBootServletInitializer`;

This does not work out of the box with Jboss 7, and it doesn't give any logs or errors save for the 404s when trying to access the application.

As it turns out, the problem is that Jboss 7 doesn't work well with the servlet mapping of `/` provided by the default spring configuration. The servlet path must be changed to `/*` for it to work, which can be done by adding the line 

```
server.servlet-path=/*
```

to the application.properties file. 
