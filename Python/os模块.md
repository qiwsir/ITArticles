#Python os模块 常用功能小结

os 模块提供了一个统一的操作系统接口函数, 这些接口函数通常是平台指定的,os 模块能在不同操作系统平台如 nt 或 posix中的特定函数间自动切换,从而能实现跨平台操作。

- os.name: 字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
- os.stat(file)：文件属性操作；
- os.getcwd()：得到当前工作目录，即当前Python脚本工作的目录路径；
- os.getdir()：获取当前目录；
- os.getenv()和os.putenv():分别用来读取和设置环境变量；
- os.listdir():返回指定目录下的所有文件和目录名；
- os.makedirs(dirname)和os.removedirs(dirname)：分别生成和删除目录，makedirs可以生成多层递归目录，removedirs可以删除多层递归的空目录，若目录中有文件则无法删除；
- os.remove()：删除一个文件；
- os.rename(file,back)：给文件重命名；
- os.system()：运行shell命令；
- os.linesep：字符串给出当前平台使用的终止符，例如：Windows使用’\r\n’，Linux使用’\n’；

##os.path模块

- os.path.split()：返回一个路径的目录名和文件名；
- os.path.isfile()和os.path.isidr()：分别检验给出的路径是一个文件还是目录；
- os.path.existe()：检验给出的路径是否真的存在
- os.path.isdir(name)：判断name是不是一个目录，name不是目录就返回false；
- os.path.isfile(name)：判断name是不是一个文件，不存在name也返回false；
- os.path.exists(name)：判断是否存在文件或目录name；
- os.path.getsize(name)：获得文件大小，如果name是目录返回0L；
- os.path.abspath(name)：获得绝对路径；
- os.path.normpath(path)：规范path字符串形式；
- os.path.split(name)：分割文件名与目录；
- os.path.splitext()：分离文件名与扩展名；
- os.path.join(path,name)：连接目录与文件名或目录
- os.path.basename(path)：返回文件名；
- os.path.dirname(path)：返回文件路径；

