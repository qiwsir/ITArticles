#压力测试工具tsung

tsung是用erlang开发的一款简单易用的压力测试工具，可以生成成千上万的用户模拟对服务器进行访问。目前对tsung的理解也仅限于会简单的应用，其内部结构没有深入研究过。

##1、安装

tsung 是用erlang编写的，所以首先安装erlang的运行环境。然后就是按照tsung的官网下载编译tsung。需要注意的是，生成测试报告需要 gnuplot和perl的支持，其中perl需要安装Template扩展。具体安装过程请看相关手册或者google之。

##2、配置文件

默认情况下，tsung会加载配置文件

    ~/.tsung/tsung.xml

将tsung自带的http的配置示例

    /usr/share/doc/tsung/examples/http_simple.xml

复制到该位置，修改一下即可运行。一个最简单的配置文件：

    <?xml version="1.0"?>
    <!DOCTYPE tsung SYSTEM "/usr/share/tsung/tsung-1.0.dtd">
	<tsung loglevel="notice" version="1.0">
	  <clients>
	    <client host="localhost" use_controller_vm="true" maxusers="100000"/>
	  </clients>
	<servers>
	  <server host="172.16.33.203" port="10013" type="tcp"></server>
	</servers>
	
	  <monitoring>
	    <monitor host="myserver" type="snmp"></monitor>
	  </monitoring>
	
	  <load>
	  <arrivalphase phase="1" duration="1" unit="minute">
	     <users interarrival="0.01" unit="second"></users>
	  </arrivalphase>
	  </load>
	
	 <sessions>
	  <session name="http-example" probability="100" type="ts_http">
	    <request>
	        <http url="/a.php" method="GET" version="1.1"></http>
	    </request>
	    <!--<thinktime value="1" random="true"></thinktime>-->
	    <request>
	        <http url="/b.php" method="GET" version="1.1"></http>
	    </request>
	  </session>
	 </sessions>
	</tsung>

clients：用户产生的方式

servers：被测试的服务器

monitoring：通过一些协议如snmp监控服务器的状态（本人没有使用过）

load：压力配置

sessions：用户所产生的会话

运行命令

    tsung start

压力测试开始，tsung输出一段提示，告知测试记录的位置，可以使用命令

    tsung status

查看tsung当前的状态

##3、压力的生成原理

（本人不是太透彻，大家凑合看吧）

tsung 在运行时，可以由多个虚拟机组成，每个虚拟机可以模拟多个ip地址（测试负载均衡时），每个虚拟机下有很多用户，每个用户可以产生很多session，一 个session由很多request组成，这是一个很典型的树状结构。tsung使用这个树状结构来生成压力。

看client的配置，maxusers指明这个client机器上最多生成多少用户，如果use_controller_vm为true的话，当用户数达到maxusers，tsung会自动生成新的VM（好像需要登录系统的ssh帐号）。

生成用户之后，当然是让这些用户访问被测试的服务器，访问的负载由load段配置。访问可以配置多个阶段，在此建设只有一个阶段。配置

 <users interarrival="0.01" unit="second"></users>
表示每0.01秒产生一个用户，产生的用户按照session的配置顺序执行session中的request，如何计算RPS，有一个公式：

RPS = 每个session的请求数 / interarrival 

以上面的配置为例，RPS = 2 / 0.01 == 200

负载的另外一种配置方式是用户到达率，具体看官方的手册。

##4、生成测试报告

默认安装时，perl文件/usr/lib/tsung/tsung_status.pl用来生成状态报告。

进 入测试日志的路径，如/home/iamlaobie/.tsung/log/20110528-21:07，运行上面的脚本，运行完成之后，在该路径下 生成report.html，如果在linux上不方便查看，可将该路径打包下载本地用浏览器打开report.html查看。

报告中的几个相似概念:

request：类似用php函数file_get_contents请求一个url地址的相应时间

page：一组没有间隔的request请求的时间总和，相当于打开一个页面，除了加载页面的html外，还要加载img、css、js等

session：一个用户从第一个请求开始到最后一个请求结束的时间总和

##5、其他

5.1、 tsung-recorder，通过它可以录制用户的访问过程，然后用tsung回放，让压力测试更逼真。实际上recorder是一个http代理，启 动recorder后，将浏览器的代理指向它，默认端口是8090，用户只需要用浏览器浏览被测试的服务器，tsung-recorder会将这个过程写 入到配置文件中。

5.2、添加请求的变量，在压力测试的过程中，可能需要手机号，用户ID、股票代码之类的变量，tsung支持文件随机读取，可以将这些参数按照一定的规则写入文件，在配置文件中定义读取的规则，就能在请求时拿到文件的内容。定义一个文件服务：

    <options>
       <option name="file_server" id="file1" value="/tmp/x.txt"/>
    </options>
读取，在session段中加入

    <setdynvars sourcetype="file" fileid="file1" delimiter=";" order="random">
               <var name="username" />

    </setdynvars>

    <request>
    <http url="/b.php?username=%%_username%%" method="GET" version="1.1"></http>
    </request>

除了从文件读取，也可以随机产生

    <setdynvars sourcetype="random_string" length="13">
        <var name="rndstring1" />
    </setdynvars>
    <setdynvars sourcetype="random_number" start="3" end="32">
        <var name="rndint" />
    </setdynvars>

来源：http://tiandiou.blog.163.com/blog/static/2355668220115392725727/

