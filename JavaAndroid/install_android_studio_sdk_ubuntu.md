#在ubuntu中安装android studio and SDK

最近要参加GDG组织的一个android开发学习活动，趁机学习，充实自己。因为是绝对的小白，需要从零开始。

就从安装android studio和sdk开始。

###环境：ubuntu 14.04

1. 在官方网站下载android studio的源码，下载地址：http://developer.android.com/sdk/index.html，注意，要下载All Android Studio Packages的linux版本。

2. 下载之后，可以得到一个压缩文件，例如我下载的是android-studio-ide-135.1641136-linux.zip，运行如下指令：

	$ unzip android-studio-ide-135.1641136-linux.zip

于是得到了一个名为：android-studio的文件夹，将这个文件夹移动到你愿意放的文件夹中。比如我将它移动到/opt下面。

3. 进入到`/opt/android-studio/bin`，里面有一个名为studio.sh的文件，执行它就能运行android studio

	$ ./studio.sh

4. 接下来就是根据提示一步一步走。直到提示要安装sdk，考验的时候到了。因为你懂又不是非常懂的原因呢，链接SDK的网不是很好，所以一定要科学上网，没有什么别的方法，至少我尝试了，传说中的捷径都不行。

5. 当你幸运地通过了上述一关，就迎来了曙光。因为在上述过程中，软件会在另外一个地方，不是在安装android-studio的文件夹内，再建立一个SDK文件夹，可以自己指定。比如，我的是/home/qw/Android/Sdk，在这个文件夹中，有一个名为tools的，进去，运行里面的android，就能启动sdk的tools了。

6. 打开了tools的对话框之后，在上面的菜单中，有tools->Options，打开，可以在里面输入下载SDK的镜像地址。注意，一定要先经过了第四步中的痛苦过程之后，在用镜像下载别的SDK包，才能做到，否则，还会引导你去经历第四步。

以上小结，记录。

