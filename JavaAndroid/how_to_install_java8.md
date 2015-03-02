This article will help you to Install Oracle JAVA 8 (JDK/JRE 8u25) on Ubuntu 14.04 LTS, 12.04 LTS and 10.04 and LinuxMint systems using PPA File.

##Installing Java 8 on Ubuntu

Add the webupd8team Java PPA repository in your system and install Oracle java8 using following set of commands.

    $ sudo add-apt-repository ppa:webupd8team/java8

    $ sudo apt-get update

    $ sudo apt-get install oracle-java8-installer

##Verify Installed Java Version

After successfully installing oracle Java using above step verify installed version using following command.

    $ java -version

    java version "1.8.0_31"
    Java(TM) SE Runtime Environment (build 1.8.0_31-b13)
    Java HotSpot(TM) 64-Bit Server VM (build 25.31-b07, mixed mode)

##Configuring Java Environment

Webupd8team is providing a package to set environment variables, Install this package using following command.

    $ sudo apt-get install oracle-java8-set-default

**References:**

http://tecadmin.net/install-oracle-java-8-jdk-8-ubuntu-via-ppa/

If you want to know: How to Install Java 8 (Jdk 8u31) on CentOS/RHEL 7/6/5 and Fedora. You should read:

http://tecadmin.net/install-java-8-on-centos-rhel-and-fedora/
