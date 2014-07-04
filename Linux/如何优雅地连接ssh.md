#如何优雅地连接ssh

作为一个开发者，经常要面对管理一大堆服务器的情况，对unix类服务器，我们一般用ssh连接来管理。那么你一般怎么连接ssh，输入密码？弱爆了，既难得记，又不安全。现在俺们都用证书来连接

使用证书来管理连接至少有如下两个好处

- 安全，目前生成证书的方式不管是RSA还是DSA无论从位数上还是加密方式上都比自己生成的密码安全许多。
- 方便，有了证书以后你就不用再记忆密码了，系统会自动使用证书跟服务器接驳，这一过程不需要人工干预

使用证书连接ssh也非常简单，首先你得生成一个证书，在shell中输入如下命令

    ssh-keygen -t rsa -C joyqi -f my-key-file

- -t定义的是加密方式，一般有rsa和dsa两种
- -C定义的是注释，一般也可以不写
- -f定义了输出的证书文件名，不需要写后缀，因为生成的证书包含了公钥和私钥两个文件，它会自动帮你加文件名。

我们执行后可以看到如下结果

    $ ssh-keygen -t rsa -C joyqi -f my-key-file
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in my-key-file.
    Your public key has been saved in my-key-file.pub.
    The key fingerprint is:
    57:75:20:37:e2:53:29:ef:86:09:8e:1b:47:2b:6f:88 joyqi
    The key's randomart image is:
    +--[ RSA 2048]----+
    |            o *o.|
    |           ..*.o |
    |            +o   |
    |          o. ..  |
    |        S+.o +   |
    |        +.+ o o  |
    |       . B   .   |
    |      E o o      |
    |         .       |
    +-----------------+
    $ ls
    my-key-file     my-key-file.pub

可以在上面的命令执行完成，我们已经得到两个文件my-key-file和my-key-file.pub。前者就是你的私钥，是由你自己个人保存的，后者是公钥，你需要把它上传到任何你想用这个私钥来登录的服务器上。

ok，现在你需要把公钥文件上传到服务器上，一般我建议用scp命令

    scp my-key-file.pub loginname@yourdomain.com:.

把loginname和yourdomain.com分别替换为你的登录名和服务器地址。上传完后我们需要告诉服务器，以后处理loginname的登录时用公钥来验证，现在最后一次用ssh密码登录你的服务器，并执行如下命令

    cat my-key-file.pub >> ~/.ssh/authorized_keys

在后面我们都用loginname来特指你自己的登录名，用yourdomain.com来特指你的服务器地址，请自行脑补

其中my-key-file.pub是我们刚刚上传的公钥文件名。现在我们还要告诉本机，连接yourdomain.com的时候使用my-key-file这个私钥来登录

退出ssh连接，回到本地。将刚才生成的my-key-file文件拷贝到~/.ssh目录下

    cp my-key-file ~/.ssh/

然后编辑~/.ssh/config文件，如果没有，就创建一个，在其中写入如下配置内容

    Host yourdomain.com
         IdentityFile ~/.ssh/my-key-file

很简单吧，一看就懂，根据你的需要自行修改。最后还有一步，别忘了将本地缓存的公钥文件删掉，因为那是你以前没有上传公钥时，缓存的服务器默认公钥，现在你用了自己生成的公钥就得把这个老的记录删掉

打开~/.ssh/known_hosts文件，找到包含yourdomain.com的那一行，将它删掉，然后保存退出

现在，你就可以正常登录服务器了，输入ssh loginname@yourdomain.com，第一次登录会出现

    The authenticity of host 'yourdomain.com (xxx.xxx.xxx.xxx)' can't be established.
    RSA key fingerprint is xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx.
    Are you sure you want to continue connecting (yes/no)?

这是因为你刚才把公钥删掉了，系统在连接本地没有缓存公钥的服务器时会询问下你，输入yes即可，然后你没输入密码就登入了服务器。怎么样，是不是很方便。

