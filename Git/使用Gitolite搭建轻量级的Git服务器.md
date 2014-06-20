#使用Gitolite搭建轻量级的Git服务器

在Git服务管理工具这个领域，主要有三种流行的方案，它们分别是

- Gitosis - 轻量级， 开源项目，使用SSH公钥认证，只能做到库级的权限控制。目前项目已经停止开发，不再维护。
- Gitolite - 轻量级，开源项目，使用SSH公钥认证，能做到分支级的权限控制。
- Git + Repo + Gerrit - 超级重量级，集版本控制，库管理和代码审核为一身。可管理大型及超大型项目。

大名鼎鼎的Android平台就是使用的 Git + Repo + Gerrit。对于个人，中小型企业及一些开源项目而言，如果没有特殊的要求，其实没有必要去架设上面第三种方案Git服务器。Gitolite提供的服务已经足够用。下面将详细讲解怎么搭建Gitolite服务器。

##安装Gitolite

Gitolite的安装需要分别在客户端和服务器端操作。搭建Gitolite的步骤如图所示。

![](http://wxpictures.qiniudn.com/201478.png)
 
在Ubuntu12.04 LTS上搭建Gitolite服务器的详细步骤，假设客户端和服务器端已经安装好了Git。如果还没有安装Git，请分别在客户端和服务器端运行下面的命令安装Git。

    $ sudo apt-get install git

###生成SSH key（客户端）

    $ ssh-keygen -t rsa -C HF

![](http://wxpictures.qiniudn.com/201479.png)

运行命令后，一直按回车键直到SSH key生成。

![](http://wxpictures.qiniudn.com/201480.png)

###将生成的SSH public key拷贝到服务器（客户端）

这里注意，为了区分SSH public key，请将SSH public key重命名，最好是用用户名命名。例如 <user-name>.pub

    $ mv /home/UBUNTUUSERS/hf/.ssh/id_rsa.pub HF.pub
    $ scp HF.pub hf@ubuntu-12.04-LTS:/tmp

##创建Git用户（服务器端）

    $ sudo adduser \
    > --system \
    > --shell /bin/bash \
    > --gecos 'Git SCM User' \
    > --group \
    > --disabled-password \
    > --home /home/git git

###下载Gitolite源码（服务器端）【1】

    $ sudo su git
    $ cd $HOME
    $ git clone http://github.com/sitaramc/gitolite

###安装Gitolite（服务器端）

    $ mkdir -p ${HOME}/bin
    $ ${HOME}/gitolite/install -to ${HOME}/bin

###设置SSH public key（服务器端）

    $ ${HOME}/bin/gitolite setup -pk /tmp/HF.pub


其实，到这里，Gitolite已经安装完成。接下来就是添加Git项目，用户和设置Git项目的访问权限了。但是如果你的服务器对SSH的权限做了限制，例如只有在sshusers用户组里的用户才可以SSH到服务器，那么你还需要做一个额外的设置那就是添加git用户及以后的Gitolite的用户到sshusers用户组。否则，当你克隆Git项目时，你将被提示输入密码。如下图：

![](http://wxpictures.qiniudn.com/201481.png)

###添加git用户sshusers用户组（服务器端）

![](http://wxpictures.qiniudn.com/201482.png)

###克隆Gitolite管理库（客户端）

    $ git clone git@ubuntu-12.04-LTS:gitolite-admin.git

你可以看到在管理库里，有两个目录， conf/和keydir/，其中conf/下面有个名为gitolite.conf的配置文件。

- conf/gitolite.conf 用于Git项目配置，访问权限设置。
- keydir/ 用于存储用户的SSH public key(公钥）。

Git项目配置和访问权限设置请看Gitolite的README.txt文档。

##配置Git项目（客户端）【2】

为了增加Git项目到Gitolite服务器，有两种方法：

###添加一个新的Git项目

- 修改gitolite.conf

例如，新建一个名为foo的Git项目，首先你需要在conf/gitolite.conf里注册foo项目。

假设你已经克隆了gitolite-admin.git项目，编辑conf/gitolite.conf，增加下面的内容【3】。

    repo foo
    RW+ = @all

然后提交这部分修改，并push到远程。

- 设置Git项目

    hf@ubuntu-12.04-LTS:~$ mkdir foo
    hf@ubuntu-12.04-LTS:~$ cd foo
    hf@ubuntu-12.04-LTS:~/foo$ git init
    Initialized empty Git repository in /home/UBUNTUUSERS/hf/foo/.git
    hf@ubuntu-12.04-LTS:~/foo (master)$ git remote add origin hf@ubuntu-12.04-LTS.git
    hf@ubuntu-12.04-LTS:~/foo (master)$ touch README
    hf@ubuntu-12.04-LTS:~/foo (master)$ git add README
    hf@ubuntu-12.04-LTS:~/foo (master)$ git commit -m "Initial commit"
    [master (root-commit) 997d5d8] Initial commit
    0 files changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 README
    hf@ubuntu-12.04-LTS:~/foo (master)$ git push origin master:refs/heads/master
    Counting objects: 3, done.
    Writing objects: 100% (3/3), 217 bytes, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To hf@ubuntu-12.04-LTS:foo.git
    * [new branch] master -> master

现在Git项目foo已经设置好了。用户可以从服务器上克隆foo了【4】。

    hf@ubuntu-12.04-LTS:~$ git clone hf@ubuntu-12.04-LTS:foo.git
    Cloning into 'foo'...
    remote: Counting objects: 3, done.
    remote: Total 3 (delta 0), reused 0 (delta 0)
    Receiving objects: 100% (3/3), done.

- 添加一个存在的Git项目

如果你有一个已经存在的项目，也想将其添加到Gitolite的服务器里。这很简单，但是首先你依然需要在gitolite.conf里注册这个项目。然后执行下面的操作：

    cd foo
    git remote rm origin
    git remote add origin hf@ubuntu-12.04-LTS.foo.git
    git push origin master

如果你有多个branch，那么checkout到那个branch，执行

    git push origin <branch-name>

注：
【1】 如果是企业内部网络，可能你需要设置HTTP代理，方法如下:

     $ export http_proxy=http://proxy.<server-name>.com:<port-number>/

例如： export http_proxy=http://proxy.server.com:8080/

【2】 此步骤仅Gitolite的管理员才有权限执行。

【3】 在这里，我们把foo项目的读写权限给了所有的Gitolite用户，实际的项目中，你最好不要这样做。请为不同级别的用户设置不同的权限。

【4】 由于我的客户端和服务器是同一台PC，所以这里域名都是ubuntu-12.04-LTS。

本文来源：[http://blog.chinaunix.net/uid-15174104-id-3843570.html](http://blog.chinaunix.net/uid-15174104-id-3843570.html)
