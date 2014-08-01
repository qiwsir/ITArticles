#使用ssh公钥密钥自动登陆linux服务器

来源:http://7056824.blog.51cto.com/69854/403669/

作为一名 linux 管理员，在多台 Linux 服务器上登陆进行远程操作是每天工作的一部分。但随着服务器的增多，每次登陆，系统都会提示输入用户名和密码，频繁的输入用户名和密码是一件让人很烦的事情。也许有人说可以用一些客户端工具，比如：SecureCRT 等，的确使用这些软件会方便很多，但是这些软件不是价格昂贵的商业软件就是依附于特定平台才能安装使用，所以我今天介绍的是使用 ssh 自带的功能实现使用客户端工具所能带来的便利，那就是使用 ssh 的公钥密钥实现自动登陆。

测试环境：

- 操作系统：Red Hat Enterprise Linux AS release 4 (Nahant Update 8)
- 软件版本：OpenSSH_3.9p1, OpenSSL 0.9.7a
- 管理服务器：    ip：192.168.0.1    机器名：server
- 被管理服务器：ip：192.168.0.2    机器名：client

##第一步：生成 ssh 公钥密钥对

首先，如果你没有安装OpenSSH，请先安装，这个废话了，我们现在的 linux 服务器默认都安装 openssh 的软件。
生成公钥密钥对是在管理服务器上生成的：

    [root@server ~]# ssh-keygen -b 1024 -t rsa
    Generating public/private rsa key pair.     #提示正在生成rsa密钥对

    Enter file in which to save the key (/home/usrname/.ssh/id_dsa):     #询问公钥和私钥存放的位置，回车用默认位置即可

    Enter passphrase (empty for no passphrase):     #询问输入私钥密语，输入密语

    Enter same passphrase again:     #再次提示输入密语确认

    Your identification has been saved in /home/usrname/.ssh/id_dsa.     #提示公钥和私钥已经存放在/root/.ssh/目录下
    Your public key has been saved in /home/usrname/.ssh/id_dsa.pub.

    The key fingerprint is:
    x6:68:xx:93:98:8x:87:95:7x:2x:4x:x9:81:xx:56:94 root@server     #提示key的指纹 
 

简单说明一下：

- -b 1024　采用长度为1024字节的公钥/私钥对，最长4096字节，一般1024或2048就足够满足安全需要了，太长的话加密解密需要的时间也增长。
- -t rsa　 采用rsa加密方式的公钥/私钥对，除了rsa还有dsa方式，rsa方式最短不能小于768字节长度。

如果还需要使用更多其他参数请参考man ssh-keygen。

在生成密钥对的过程中你被询问：输入密码短句 Enter passphrase (empty for no passphrase) ，密码短句（passphrase）是你使用一个短语或者一句话作为密码输入，再由系统内部的加密或是散列算法生成虚拟密码后，进行下一步的认证。好处是增强了安全性不易被破解。看过很多文章，里面都把这个短句输入为空，也就是代表不使用密码短句。在这里我强烈要求你输入密码短句。有人会说使用密码短句后，登陆还要输入密码短句这样使用没有比使用用户名和密码登陆方便多少，我说请你不要急，接着看我的文章。

注意：如果你生成密钥对而不设置密码短语，那么如果你的私钥丢失了，那么就你的麻烦可能会比丢失用户名密码还严重。

##第二步：拷贝你的公钥到被管理的服务器上

在你的管理服务器上把你的公钥拷贝到被管理服务器上要进行自动登陆的用户目录下。

    [root@server ~]# scp .ssh/id_dsa.pub remote_usrname@192.168.0.2:      #比如你想使用用户peter登陆，则remote_usrname请以peter代替 
 

##改名和进行权限设置

登陆被管理的服务器，进入需要远程登陆的用户目录，把公钥放到用户目录的 .ssh 这个目录下（如果目录不存在，需要创建~/.ssh目录，并把目录权限设置为700），把公钥改名为authorized_keys2，并且把它的用户权限设成600。

    [peter@client ~]$ ls
    id_rsa.pub
    [peter@client ~]$ mkdir ~/.ssh     #如果当前用户目录下没有 .ssh 目录，请先创建目录
    [peter@client ~]$ chmod 700 ~/.ssh
    [peter@client ~]$ mv id_rsa.pub ~/.ssh
    [peter@client ~]$ cd ~/.ssh
    [peter@client ~]$ cat id_rsa.pub >> authorized_keys2
    [peter@client ~]$ rm -f id_rsa.pub
    [peter@client ~]$ chmod 600 authorized_keys2
    [peter@client ~]$ ls -l
    total 4
    -rw-------  1 peter peter 225 Oct 10 11:28 authorized_keys2 

##测试使用密钥对进行远程登陆

    [root@server ~]# ssh peter@192.168.0.2
    Enter passphrase for key '/root/.ssh/id_rsa':      #提示输入密码短语，请输入刚才设置的密码短语
    Last login: Sun Oct 10 11:32:14 2010 from 192.168.0.1
    [peter@client ~]$ 
 
如果你不能用正确的登录，应该重新检查一下你的authorized_keys2的权限。也可能要检查.ssh目录的权限。

##使用 ssh-agent（ssh代理）自动输入密码短语

牢记你的“密码短句”，现在你可以用你的密钥而不是密码来登录你的服务器了，但是这样仍然没有省什么事，你还是要输入密钥的“密码短语”。有更简便的方法吗？答案就是采用SSH代理（ssh-agent），一个用来帮你记住“密码短语”的程序。 ssh-agent是OpenSSH中默认包括的ssh代理程序。

##登陆管理服务器

    [root@server ~]# ssh-agent
    SSH_AUTH_SOCK=/tmp/ssh-vEGjCM2147/agent.2147; export SSH_AUTH_SOCK;
    SSH_AGENT_PID=2148; export SSH_AGENT_PID;
    echo Agent pid 2148; 
 
当你运行ssh-agent，它会打印出来它使用的 ssh 的环境和变量。要使用这些变量，有两种方法，一种是手动进行声明环境变量，另一种是运行eval命令自动声明环境变量。

###方法一：手动声明环境变量

    [root@server ~]# SSH_AUTH_SOCK=/tmp/ssh-vEGjCM2147/agent.2147; export SSH_AUTH_SOCK;
    [root@server ~]# SSH_AGENT_PID=2148; export SSH_AGENT_PID;
    [root@server ~]# printenv | grep SSH     #检查 ssh 环境变量是否已经加入当前会话的环境变量
    SSH_AGENT_PID=2148
    SSH_AUTH_SOCK=/tmp/ssh-vEGjCM2147/agent.2147
 
###方法二：运行eval命令自动声明环境变量

    [root@server ~]# eval `ssh-agent`
    Agent pid 2157
    [root@server ~]# printenv | grep SSH     #检查 ssh 环境变量是否已经加入当前会话的环境变量
    SSH_AGENT_PID=2148
    SSH_AUTH_SOCK=/tmp/ssh-vEGjCM2147/agent.2147 
 
现在 ssh-agent 已经在运行了，但是 ssh-agent 里面是空白的不会有解密的专用密钥。我们要告诉它我们有私钥和这个私钥在哪儿。这就需要使用 ssh-add 命令把我们的专用密钥添加到 ssh-agent 的高速缓存中。

    [root@server ~]# ssh-add ~/.ssh/id_dsa
    Enter passphrase for /home/user/.ssh/id_dsa:     #输入你的密码短语
    Identity added: /home/user/.ssh/id_dsa (/home/user/.ssh/id_dsa) 
    [root@server ~]# ssh-add -l     #查看 ssh代理的缓存内容
    1024 72:78:5e:6b:16:fd:f2:8c:81:b1:18:e6:9f:77:6e:be /root/.ssh/id_rsa (RSA)

输入了密码短句，现在好了，你可以登录你的远程服务器而不用输入你的密码短语了，而且你的私钥是密码保护的。试试看是不是很爽！

    [root@server ~]# ssh peter@192.168.0.2
    Last login: Sun Oct 10 11:32:45 2010 from 192.168.0.1
    [peter@client ~]$ 
 
登陆服务器进行操作结束后，记得还要把 ssh-agent 关掉，不然其他人登陆后也可以远程了。

    [root@server ~]# ssh-agent -k
    unset SSH_AUTH_SOCK;
    unset SSH_AGENT_PID;
    echo Agent pid 2148 killed;
    [root@server ~]# ssh-add -l     #查看一下，缓存里已经没有了密钥了
    The agent has no identities. 
 
呵呵，爽了吧，当然了如果管理数量众多的服务器（服务器数量≥2位数），第一次上传公钥可能会是比较累的工作，但是以后就可以在维护工作中体会这种公钥密钥自动登陆的便利了。
