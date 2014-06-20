#通过ssh连接远程服务器

注意：以下方法是在Ubuntu操作系统。

安装SSH：sudo apt-get install openssh-server

确认sshserver是否启动：ps -e |grep ssh

如果只有ssh-agent那ssh-server还没有启动，需要/etc/init.d/ssh start，如果看到sshd那说明ssh-server已经启动了。

ssh-server配置文件位于/ etc/ssh/sshd_config，在这里可以定义SSH的服务端口，默认端口是22，你可以自己定义成其他端口号，如222。然后重启SSH服务：

sudo /etc/init.d/ssh restart

ssh连接：ssh linuxidc（这里是远程服务器登录用户名）@192.168.1.1（这里是远程服务器IP）

然后根据提示输入密码。

以下方法也可以参考：

1. 启动ssh-server：$ /etc/init.d/ssh restart

2. 确认ssh-server已经正常工作。

$ netstat -tlp

tcp6    0    0 *:ssh                *:*                   LISTEN     -

看到上面这一行输出说明ssh-server已经在运行了。

3. 在客户端通过ssh登录服务器。假设服务器的IP地址是192.168.0.103，登录的用户名是hyx。

$ ssh -l hyx 192.168.0.103

接下来会提示输入密码，然后就能成功登录到服务器上了

