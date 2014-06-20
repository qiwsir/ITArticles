#github公钥和推送

##在本地生成公钥

方法是：

    ssh-keygen -t  rsa -C "your email of github"

会询问存储地址，一般存在主目录下。还会询问密码，可以为空。如果不为空，则在推送的时候也要输入密码。

##安装xclip

用于在shell上将公钥内容复制到剪贴板（clipboard）上

    sudo apt-get install xclip

安装之后，运行下面的命令，完成复制

    xclip -sel clip < [path of id_rsa.pub]/id_rsa.pub    #id_rsa.pub是公钥存储文件

##在github上添加公钥

然后登录到github，在setting中找到ssh keys，点击add ssh key，将复制到剪贴板上的公钥复制过来。

在本地shell中通过下面的命令检验是否联通

    ssh -T git@github.com

##推送文件

进入到本地的目录，参考github上的帮助：

Create a new repository on the command line

    touch README.md

    git init

    git add README.md

    git commit -m "first commit"

    git remote add origin git@github.com:qiwsir/Yeashape.git    #这是我的github仓库

    git push -u origin master

Push an existing repository from the command line

    git remote add origin git@github.com:qiwsir/Yeashape.git

    git push -u origin master

上述操作，还可以合并为：

    git push git@github.com:qiwsir/Yeashape.git master

