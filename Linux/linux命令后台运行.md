#linux命令后台运行

##一、 简介

Linux/Unix 区别于微软平台最大的优点就是真正的多用户，多任务。因此在任务管理上也有别具特色的管理思想。

我们知道，在 Windows 上面，我们要么让一个程序作为服务在后台一直运行，要么停止这个服务。而不能让程序在前台后台之间切换。而 Linux 提供了 fg 和bg 命令，让你轻松调度正在运行的任务。假设你发现前台运行的一个程序需要很长的时间，但是需要干其他的事情，你就可以用 Ctrl-Z ，挂起这个程序，然后可以看到系统提示：

[1]+ Stopped /root/bin/rsync.sh 然后我们可以把程序调度到后台执行：（bg 后面的数字为作业号）

    #bg 1

    [1]+ /root/bin/rsync.sh &

用 jobs 命令查看正在运行的任务：

    #jobs

    [1]+ Running /root/bin/rsync.sh &

如果想把它调回到前台运行，可以用

    #fg 1

    /root/bin/rsync.sh

这样，你在控制台上就只能等待这个任务完成了。

& 将指令丢到后台中去执行

[ctrl]+z 將前台任务丟到后台中暂停

jobs 查看后台的工作状态

fg %jobnumber 将后台的任务拿到前台来处理

bg %jobnumber 将任务放到后台中去处理

kill 管理后台的任务

##二、& 

在Linux中，当在前台运行某个作业时，终端被该作业占据；而在后台运行作业时，它不会占据终端。可以使用&命令把作业放到后台执行。实际上，这样是将命令放入到一个作业队列中了：

    $ ./test.sh &

    [1] 17208

    $ jobs -l

    [1]+ 17208 Running ./test.sh &

在后台运行作业时要当心：需要用户交互的命令不要放在后台执行，因为这样你的机器就会在那里傻等。不过，作业在后台运行一样会将结果输出到屏幕上，干扰你的工作。如果放在后台运行的作业会产生大量的输出，最好使用下面的方法把它的输出重定向到某个文件中：

    command >out.file 2>&1 &

在上面的例子中，2>&1表示所有的标准输出和错误输出都将被重定向到一个叫做out.file 的文件中。 当你成功地提交进程以后，就会显示出一个进程号，可以用它来监控该进程，或杀死它。

例：查找名为“httpd.conf”的文件，并把所有标准输出和错误输出重定向到find.dt的文件中：

    # find /etc/httpd/ -name "httpd.conf" -print >find.dt 2>&1 &

    [2] 7832

成功提交该命令之后，系统给出了它的进程号7832。 对于已经在前台执行的命令，也可以重新放到后台执行，首先按ctrl+z暂停已经运行的进程，然后使用bg命令将停止的作业放到后台运行，例如对正在前台执行的tesh.sh使用ctrl+z挂起它：

    $ ./test.sh

    [1]+ Stopped ./test.sh

    $ bg %1

    [1]+ ./test.sh &

    $ jobs -l

    [1]+ 22794 Running ./test.sh &

但是如上方到后台执行的进程，其父进程还是当前终端shell的进程，而一旦父进程退出，则会发送hangup信号给所有子进程，子进程收到hangup以后也会退出。如果我们要在退出shell的时候继续运行进程，则需要使用nohup忽略hangup信号，或者setsid将将父进程设为init进程(进程号为1)

    $ echo $$

    21734

    $ nohup ./test.sh &

    [1] 29016

    $ ps -ef | grep test

    515 29710 21734 0 11:47 pts/12 00:00:00 /bin/sh ./test.sh

    515 29713 21734 0 11:47 pts/12 00:00:00 grep test

    $ setsid ./test.sh &

    [1] 409

    $ ps -ef | grep test

    515 410 1 0 11:49 ? 00:00:00 /bin/sh ./test.sh

    515 413 21734 0 11:49 pts/12 00:00:00 grep test

上面的试验演示了使用nohup/setsid加上&使进程在后台运行，同时不受当前shell退出的影响。那么对于已经在后台运行的进程，该怎么办呢？可以使用disown命令：

    $ ./test.sh &

    [1] 2539

    $ jobs -l

    [1]+ 2539 Running ./test.sh &

    $ disown -h %1

    $ ps -ef | grep test

    515 410 1 0 11:49 ? 00:00:00 /bin/sh ./test.sh

    515 2542 21734 0 11:52 pts/12 00:00:00 grep test

另外还有一种方法，即使将进程在一个subshell中执行，其实这和setsid异曲同工。方法很简单，将命令用括号() 括起来即可：

    $ (./test.sh &)

    $ ps -ef | grep test

    515 410 1 0 11:49 ? 00:00:00 /bin/sh ./test.sh

    515 12483 21734 0 11:59 pts/12 00:00:00 grep test

注：本文试验环境为Red Hat Enterprise Linux AS release 4 (Nahant Update 5),shell为/bin/bash，不同的OS和shell可能命令有些不一样。例如AIX的ksh，没有disown，但是可以使用nohup -p PID来获得disown同样的效果。

还有一种更加强大的方式是使用screen，首先创建一个断开模式的虚拟终端，然后用-r选项重新连接这个虚拟终端，在其中执行的任何命令，都能达到nohup的效果，这在有多个命令需要在后台连续执行的时候比较方便：

    $ screen -dmS screen_test

    $ screen -list

    There is a screen on:

    27963.screen_test (Detached)

    1 Socket in /tmp/uscreens/S-jiangfeng.

    $ screen -r screen_test

##三、 nohup

如果你正在运行一个进程，而且你觉得在退出帐户时该进程还不会结束，那么可以使用nohup命令。该命令可以在你退出帐户之后继续运行相应的进程。nohup就是不挂起的意思( no hang up)。 该命令的一般形式为：

    nohup conmmand &

如果使用nohup命令提交作业，那么在缺省情况下该作业的所有输出都被重定向到一个名为nohup.out的文件中，除非另外指定了输出文件：

    nohup command > myout.file 2>&1

在上面的例子中，输出被重定向到myout.file文件中。

##四、.*，？，[...]，[!...]等

下面就是这些特殊字符：

* 匹配文件名中的任何字符串，包括空字符串。

？ 匹配文件名中的任何单个字符。

[...] 匹配[ ]中所包含的任何字符。

[!...] 匹配[ ]中非感叹号！之后的字符。

当s h e l l遇到上述字符时，就会把它们当作特殊字符，而不是文件名中的普通字符，这样用户就可以用它们来匹配相应的文件名。

1)列出以i或o开头的文件名： #ls [io]*

2)列出log.开头、后面跟随一个数字、然后可以是任意字符串的文件名： #ls log.[0-9]*

3)与例二相反，列出log.开头、后面不跟随一个数字、然后可以是任意字符串的文件名 : #ls log.[!0-9]*

4)列出所有以LPS开头、中间可以是任何两个字符，最后以1结尾的文件名：#ls LPS??1

5)列出所有以大写字母开头的文件名：$ ls [A-Z]* 6)列出所有以. 开头的文件名（隐含文件，例如. profile、.rhosts、.histo ry等）: $ ls .*

其他相关命令：

jobs：查看当前有多少在后台运行的命令

fg：将后台中的命令调至前台继续运行。如果后台中有多个命令，可以用 fg %jobnumber将选中的命令调出，%jobnumber是通过jobs命令查到的后台正在执行的命令的序号(不是pid)

bg：将一个在后台暂停的命令，变成继续执行。如果后台中有多个命令，可以用bg %jobnumber将选中的命令调出，%jobnumber是通过jobs命令查到的后台正在执行的命令的序号(不是pid)

##杀死进程

杀死已经启动的程序和普通方式一样：

pkill -9 name

killall name

kill pid …

