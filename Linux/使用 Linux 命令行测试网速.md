#使用 Linux 命令行测试网速

当发现上网速度变慢时，人们通常会先首先测试自己的电脑到网络服务提供商（通常被称为“最后一公里”）的网络连接速度。在可用于测试宽带速度的网站中，Speedtest.net也许是使用最广泛的。

Speedtest.net的工作原理并不复杂：它在你的浏览器中加载JavaScript代码并自动检测离你最近的Speedtest.net服务器，然后向服务器发送HTTP GET and POST请求来测试上行/下行网速。

但在没有图形化桌面时（例如，当你通过命令行远程登陆服务器或使用没有图形界面的操作系统），基于flash、界面友好的Speedtest.net将无法工作。幸运的是，Speedtest.net提供了一个命令行版本——speedtest-cli。下面我将向你演示如何在Linux的命令行中使用speedtest-cli来测试宽带连接速度。

##安装speedtest-cli

speedtest-cli是一个用Python编写的轻量级Linux命令行工具，在Python2.4至3.4版本下均可运行。它基于Speedtest.net的基础架构来测量网络的上/下行速率。安装speedtest-cli很简单——只需要下载其Python脚本文件。

安装speedtest_cliShell

>$ wget https://raw.github.com/sivel/speedtest-cli/master/speedtest_cli.py
>$ chmod a+rx speedtest_cli.py
>$ sudo mv speedtest_cli.py /usr/local/bin/speedtest-cli
>$ sudo chown root:root /usr/local/bin/speedtest-cli</div>

##使用speedtest-cli测试网速

使用speedtest-cli命令也很简单，它不需要任何参数即可工作。

>$ speedtest-cli

输入这个命令后，它会自动发现离你最近的Speedtest.net服务器（地理距离），然后打印出测试的网络上/下行速率。

如果你愿意分享测试结果，你可以使用参数“–share”。它将会把你的测试结果上传到Speedtest.net服务器并以图形的方式分享给其他人。

如果你对目前所有可用的Speedtest.net服务器感兴趣，你可以使用参数“–list”。它会打印出所有的Speedtest.net服务器（按照离你的地理距离由近及远排序）。

原文：How to check Internet speed from the command line on Linux
转自：极客范 - 小道空空
