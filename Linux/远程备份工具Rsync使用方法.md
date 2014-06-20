#远程备份工具Rsync使用方法

关于Rsync的官方信息：https://help.ubuntu.com/community/rsync

从该网站上摘录的介绍信息：

Rsync is a fast and extraordinarily versatile file copying tool. It can copy locally, to/from another host over any remote shell, or to/from a remote rsync daemon. It offers a large number of options that control every aspect of its behavior and permit very flexible specification of the set of files to be copied. It is famous for its delta-transfer algorithm, which reduces the amount of data sent over the network by sending only the differences between the source files and the existing files in the destination. Rsync is widely used for backups and mirroring and as an improved copy command for everyday use.

如果使用命令行来完成备份工作，在ubuntu系统上已经默认安装了Rsync了，如果所用的其它linux系统，可以使用下面的命令安装：

    $ sudo apt-get install rsync xinetd

当然了，如果喜欢图形界面Rsync也能够满足，那就是：GRsync，详细信息请看：https://help.ubuntu.com/community/rsync#Grsync

基本语法：

    rsync options source destination

源和目标都可以是本地或远程，在进行远程传输的时候，需要指定登录名、远程服务器及文件位置

样例：

###1 在本地机器上对两个目录进行同步

    $ rsync -zvr /var/opt/installation/inventory/ /root/temp
    building file list … done
    sva.xml
    svB.xml
    sent 26385 bytes received 1098 bytes 54966.00 bytes/sec
    total size is 44867 speedup is 1.63
    $

参数：

- -z 开启压缩
- -v 详情输出
- -r 表示递归

###2 利用 rsync -a 让同步时保留时间标记

rsync 选项 -a 称为归档模式，执行以下操作

1. 递归模式
2. 保留符号链接
3. 保留权限
4. 保留时间标记
5. 保留用户名及组名

    $ rsync -azv /var/opt/installation/inventory/ /root/temp/
    building file list … done
    ./
    sva.xml
    svB.xml
    .
    sent 26499 bytes received 1104 bytes 55206.00 bytes/sec
    total size is 44867 speedup is 1.63
    $

###3 仅同步一个文件

    $ rsync -v /var/lib/rpm/Pubkeys /root/temp/
    Pubkeys
    sent 42 bytes received 12380 bytes 3549.14 bytes/sec
    total size is 12288 speedup is 0.99

##4 从本地同步文件到远程服务器

    $ rsync -avz /root/temp/ thegeekstuff@192.168.200.10:/home/thegeekstuff/temp/
    Password:
    building file list … done
    ./
    rpm/
    rpm/Basenames
    rpm/Conflictname
    sent 15810261 bytes received 412 bytes 2432411.23 bytes/sec
    total size is 45305958 speedup is 2.87

就像你所看到的，需要在远程目录前加上 ssh 登录方式，格式为 username@machinename:path

###5 同步远程文件到本地

和上面差不多，做个相反的操作

    $ rsync -avz thegeekstuff@192.168.200.10:/var/lib/rpm /root/temp
    Password:
    receiving file list … done
    rpm/
    rpm/Basenames
    .
    sent 406 bytes received 15810230 bytes 2432405.54 bytes/sec
    total size is 45305958 speedup is 2.87

###6 同步时指定远程 shell

用 -e 参数可以指定远程 ssh ，比如用 rsync -e ssh 来指定为 ssh

    $ rsync -avz -e ssh thegeekstuff@192.168.200.10:/var/lib/rpm /root/temp
    Password:
    receiving file list … done
    rpm/
    rpm/Basenames

    sent 406 bytes received 15810230 bytes 2432405.54 bytes/sec
    total size is 45305958 speedup is 2.87

###7 不要覆盖被修改过的目的文件

使用 rsync -u 选项可以排除被修改过的目的文件

    $ ls -l /root/temp/Basenames
    total 39088
    -rwxr-xr-x 1 root root 4096 Sep 2 11:35 Basenames
    $ rsync -avzu thegeekstuff@192.168.200.10:/var/lib/rpm /root/temp
    Password:
    receiving file list … done
    rpm/
    sent 122 bytes received 505 bytes 114.00 bytes/sec
    total size is 45305958 speedup is 72258.31
    $ ls -lrt
    total 39088
    -rwxr-xr-x 1 root root 4096 Sep 2 11:35 Basenames

###8 仅仅同步目录权（不同步文件）

使用 -d 参数

    $ rsync -v -d thegeekstuff@192.168.200.10:/var/lib/ .
    Password:
    receiving file list … done
    logrotate.status
    CAM/
    YaST2/
    acpi/
    sent 240 bytes received 1830 bytes 318.46 bytes/sec
    total size is 956 speedup is 0.46

###9 查看每个文件的传输进程

使用 – -progress 参数

    $ rsync -avz – -progress thegeekstuff@192.168.200.10:/var/lib/rpm/ /root/temp/
    Password:
    receiving file list …
    19 files to consider
    ./
    Basenames
    5357568 100% 14.98MB/s 0:00:00 (xfer#1, to-check=17/19)
    Conflictname
    12288 100% 35.09kB/s 0:00:00 (xfer#2, to-check=16/19)
    .
    .
    .
    sent 406 bytes received 15810211 bytes 2108082.27 bytes/sec
    total size is 45305958 speedup is 2.87

###10 删除在目的文件夹中创建的文件

用 – -delete 参数

    # Source and target are in sync. Now creating new file at the target.
    $ > new-file.txt
    $ rsync -avz – -delete thegeekstuff@192.168.200.10:/var/lib/rpm/ .
    Password:
    receiving file list … done
    deleting new-file.txt
    ./

    sent 26 bytes received 390 bytes 48.94 bytes/sec
    total size is 45305958 speedup is 108908.55

###11 不要在目的文件夹中创建新文件

有时能只想同步目的地中存在的文件，而排除源文件中新建的文件，可以使用 – -exiting 参数

    $ rsync -avz –existing root@192.168.1.2:/var/lib/rpm/ .
    root@192.168.1.2′s password:
    receiving file list … done
    ./

    sent 26 bytes received 419 bytes 46.84 bytes/sec
    total size is 88551424 speedup is 198991.96

###12 查看源和目的文件之间的改变情况

用 -i 参数

    $ rsync -avzi thegeekstuff@192.168.200.10:/var/lib/rpm/ /root/temp/
    Password:
    receiving file list … done
    >f.st…. Basenames
    .f….og. Dirnames

    sent 48 bytes received 2182544 bytes 291012.27 bytes/sec
    total size is 45305958 speedup is 20.76


输出结果中在每个文件最前面会多显示 9 个字母，分别表示为

    > 已经传输
    f 表示这是一个文件
    d 表示这是一个目录
    s 表示尺寸被更改
    t 时间标记有变化
    o 用户被更改
    g 用户组被更改

###13 在传输时启用包含和排除模式

    $ rsync -avz – -include ‘P*’ – -exclude ‘*’ thegeekstuff@192.168.200.10:/var/lib/rpm/ /root/temp/
    Password:
    receiving file list … done
    ./
    Packages
    Providename
    Provideversion
    Pubkeys

    sent 129 bytes received 10286798 bytes 2285983.78 bytes/sec
    total size is 32768000 speedup is 3.19


###14 不要传输大文件

使用 – - max-size 参数

    $ rsync -avz – -max-size=’100K’ thegeekstuff@192.168.200.10:/var/lib/rpm/ /root/temp/
    Password:
    receiving file list … done
    ./
    Conflictname
    Group
    Installtid
    Name
    Sha1header
    Sigmd5
    Triggername

    sent 252 bytes received 123081 bytes 18974.31 bytes/sec
    total size is 45305958 speedup is 367.35

###15 传输所有文件

不管有没有改变，再次把所有文件都传输一遍，用 -W 参数

    # rsync -avzW thegeekstuff@192.168.200.10:/var/lib/rpm/ /root/temp
    Password:
    receiving file list … done
    ./
    Basenames
    Conflictname
    Dirnames
    Filemd5s
    Group
    Installtid
    Name
    
    sent 406 bytes received 15810211 bytes 2874657.64 bytes/sec
    total size is 45305958 speedup is 2.87

说明：Rsync 使用所谓的”Rsync演算法”来使本地和远程两个主机之间的文件达到同步，这个算法只传送两个文件的不同部分，而不是每次都整份传送，因此速度相当快。

