#linux下面用ssh上传和下载文件

##一，ssh上传文件

scp file username@hostIP:文件地址 

例:

    [zhangy@BlackGhost ~]$ scp test.sql root@192.168.1.5:/var/www/zhangying
    zhangying@192.168.1.5's password:
    test.sql                                      100% 7884     7.7KB/s   00:00
    [zhangy@BlackGhost ~]$

##二，ssh下载文件

scp username@hostIP:文件所在地址   文件目录 

例:

    [zhangy@BlackGhost ~]$ scp root@192.168.1.5:/var/www/zhangying/test.sql /home/zhangy/database_bak/
    zhangying@192.168.1.5's password:
    test.sql                                      100% 7884     7.7KB/s   00:00
    [zhangy@BlackGhost ~]$

