#GAE for Ubuntu

1、下载SDK FOR UBUNTU（PYTHON）https://developers.google.com/appengine/downloads?hl=zh-cn

2、将下载的文件解压，并存储到本地计算机中

3、修改ubuntu命令路径。方法是：

用户主目录下的.profile或.bashrc文件，登录到你的用户（非root），在终端输入：

    $ sudo gedit ~/.profile(or .bashrc)

可以在此文件末尾加入PATH的设置如下：

    export PATH=”$PATH:your path1/:your path2/ ...”

保存文件，注销再登录，变量生效。

该方式添加的变量只对当前用户有效。

4、创建一个文件夹，并在文件夹中创建文件app.yaml（必须是这个文件名），其内容如下：

    application: clock  #文件夹名称，可修改
    version: 1  #应用的版本号
    runtime: python  #运行python脚本
    api_version: 1    #python的api version
    threadsafe: yes
    
    handlers:
    - url: /.*    #每个请求都由名字为main.py的脚本处理
      script: main.py

5、进入到clock所在的文件夹，执行：

    dev_appserver.py clock

显示：

INFO     2013-06-15 02:58:26,865 api_server.py:138] Starting API server at: http://localhost:35036

INFO     2013-06-15 02:58:26,875 dispatcher.py:164] Starting server "default" running at: http://localhost:8080   #main.py启动的应用

INFO     2013-06-15 02:58:26,876 admin_server.py:117] Starting admin server at: http://localhost:8000

6、上传文件到gae空间，执行：

    appcfg.py update clock
