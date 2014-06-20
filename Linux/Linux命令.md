#Linux命令

- shutdown -h now     立刻关机
- shutdown -r now     重启计算机
- reboot              重启计算机

- logout 退出当前用户

- ls
- ls -a    显示隐藏
- ls -l    显示详细

- mkdir    建立目录
- rmdir    删除空目录

- touch    建立空文件
- cp       复制文件
- cp -r dir1 dir2   递归复制（复制子目录）

- mv    移动和修改文件名

- rm    删除文件和目录
- rm -rf   强制删除文件和目录

- grep '要查找的关键词' 文件名       在某个文件中查找某关键词
- grep 'kivi' aa.py > qiwei.text     在aa.py中查找kivi，并把检查结果保存到qiwei.text

- find     查找文件名/目录
- find / -name aaa.py    从根目录开始找名称为aaa.py的文件
- find /root -name aa.py     从目录root中找

- ls -l > a.txt      列表的内容写入到文件a.txt中（覆盖写）
- ls -al >> aa.txt    列表内容追加到文件aa.txt末尾

- history  查看历史执行的命令
- history 5    查看最近的5条命令

