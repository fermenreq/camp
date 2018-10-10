---
layout: default
---

# The XWiki Use-case

To execute CAMP on XWiki.
```bash
git clone https://github.com/STAMP-project/camp 
cd camp/docker/ && docker build -t camp-tool:latest .
cd ../samples/stamp/xwiki/ && docker run -it -v $(pwd):/root/workingdir camp-tool:latest /bin/bash start.sh
```
This should generate four folders, i.e. ```camp/samples/stamp/xwiki/compose1, camp/samples/stamp/xwiki/compose2, camp/samples/stamp/xwiki/compose3, camp/samples/stamp/xwiki/compose4```. Each folder contains four docker-compose files which set up XWiki differently. Possible options are on the picture below.
![Alt text](/assets/images/xwiki_var.png "Possible variation in XWiki")
XWiki can run on different application servers, different version of java, and can be hooked up to various DBs. These variations are captured in ```camp/samples/stamp/xwiki/features.yml```
```yaml
java:
  openjdk: [openjdk9, openjdk8]
appsrv:
  tomcat: [tomcat7, tomcat8, tomcat85, tomcat9]
db:
  mysql: [mysql8, mysql5]
  postgres: [postgres9, postgres10]
xwiki: [xwiki9mysql, xwiki9postgres, xwiki8mysql, xwiki8postgres]
```
We call these possible variations - features, e.g. the feature ```java``` contains a sub-feature, which in return contains other features, i.e. ```openjdk8```, ```openjdk9```. To build docker files from a feature selection, we need to define rules. Those rules are found in ```camp/samples/stamp/xwiki/images.yml```. See below:
```yaml
downloadimages:
  OpenJdk8:
    features: [openjdk8]
    name: openjdk
    tag: 8
...
buildingrules:
  Tomcat7:
    requires: [java]
    adds: [tomcat7]
  Xwiki8Postgres:
    requires: [tomcat]
    adds: [xwiki8postrgres]
    depends: [postrgres]
...
``` 
CAMP evaluates and chains such rules. A chain results in a valid selection of the features and compliance to constraints and the meta-model of CAMP. Each rule corresponds to a docker image. A chain of the rules stacks a set of images onto each other yielding a new image. A valid chain may look as follows (chains are generated by CAMP and could be found in ```/camp/samples/stamp/xwiki/genimages.yml```):
```yaml
- chain:
  - {rule: Xwiki8Postgres}
  - {rule: Tomcat7}
  - {name: openjdk, tag: 8}
  features: [tomcat7, openjdk8, xwiki8postgres]
```
An execution of the above chain would result in a new image. CAMP takes a docker image from ```camp/samples/stamp/xwiki/repo/Tomcat7/``` and substitutes the from statement with ```FROM openjdk:8``` yielding a new image called ```tomcat7:openjdk-8```. A docker file for the image is located in ```camp/samples/stamp/xwiki/repo/build/tomcat7--openjdk-8```. Further, CAMP takes another docker image in ```camp/samples/stamp/xwiki/repo/Xwiki8Postgres/``` and substitutes ```FROM tomcat:8-jre8``` with ```tomcat7:openjdk-8```. This generates a new docker image ```xwiki8postgres:tomcat7-openjdk-8``` in ```camp/samples/stamp/xwiki/repo/build/xwiki8postgres--tomcat7-openjdk-8```. Therefore, CAMP generates the new image which good be used to test XWiki in different configurations, e.g. Tomcat 7, openjdk8, Postgres. Depending on defined constraints, CAMP can generate multiple images. In the given example, CAMP creates 8 new images. Each image gives us a **diverse deployment environment**.

To generate a **diverse topology**, CAMP requires ```camp/samples/stamp/xwiki/composite.yml``` as follows:
```yaml
services:
  web:
    imgfeature: [xwiki]
    mandatory: true
  mysql:
    imgfeature: [mysql]
  postgres:
    imgfeature: [postgres]
images:
  Postgres9: {name: postgres, tag: "9", features: [postgres9]}
  ...
constraints:
  - Not(services['mysql'].alive() == services['postgres'].alive())
...
``` 
The file defines a skeleton for a docker-compose file, the file represents 150% model, which contains all possible services. We also associate each service with a feature, e.g. ```web``` is associated with ```xwiki```. We also define rules in the ```image``` section, e.g. ```Postgres9``` realizes the ```postgres9``` feature. The images is built from a default image with the label ```postgres:9```. We also define a constraint which postulates that we cannot have mysql and postgres in the same docker-compose file. Each service is filled with data from the ```/camp/samples/stamp/xwiki/docker-compose/docker-compose.yml```, where ```image``` is substituted with **diverse deployment environment**, e.g. ```xwiki8postgres:tomcat7-openjdk-8``` realizes the feature ```xwiki``` and therefore, the image implements the ```web``` service. The ```postgres:9``` image realizes the feature ```postgres``` and therefore, it implements the service ```postgres```. In the given example, CAMP generates four different docker-compose files by varying the services in ```camp/samples/stamp/xwiki/composite.yml``` and generated **diverse deployment environment**s