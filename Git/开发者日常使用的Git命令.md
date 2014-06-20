#开发者日常使用的 Git 命令

这些命令分四种类型：

①不需要和其他开发者协作的独立开发者，会经常用到 git init、git show branch、git commit 等命令；

②需要和其他人协作的开发者，会常用到 git clone、git push、git pull、git format patch 。

③在项目中负责接收其他开发者发来更新的核心开发者，会常用到 git am、git pull、git format patch、git revert、git push；

④ 代码仓库管理员常用 git daemon、git shell……

对于任何想做提交的人来说，甚至对于某位单独工作的人来说，【个人开发者（单独开发）】部分命令都是必不可少的。如果你和别人一起工作，你也会需要【个人开发者（参与者）】部分列出的命令。

除了上述的部分，担当【集成人员】角色的人需要知道更多命令。【代码库管理】命令帮助系统管理员负责管理，及向git代码库提交内容。

##个人开发者（单独开发）

单独的个人开发者不会与他人交换修补程序，只用到下列命令，独自在单独的代码库上工作：

    git-init    #用来创建新代码库。

    git-show-branch    #用来查看你在哪里。

    git-log     #查看发生过什么。

    git-checkout    和    git-branch    #用来切换分支。

    git-add    #用来管理索引文件。

    git-diff    和    git-status    #查看你正在做什么。

    git-commit    #将内容推进现分支

    git-reset    和    git-checkout    #（带路径名 参数）放弃修改。

    git-merge    #用来合并本地分支

    git-rebase    #用来维护主题分支

    git-tag    #用来给已知点打标签

##个人开发者（参与开发）

作为在一个团体项目里参与角色的开发人员，需要学习如何与他人沟通，除了那些单独开发者需要掌握的命令以外，还要使用这些命令。

    git-clone    #从上游代码库填充你的本地代码库。

    git-pull    和    git-fetch    #从“origin”得到最新的上游代码库。

    git-push    #用来共享代码库，如果你采用cvs风格的代码库工作流的话。

    git-format-patch    #用来准备e-mail提交，如果你使用Linux内核风格的公共论坛工作流的话。

##集成人员

在一个团队项目中担任集成者的是一名相当重要的人员，他接受别人的修改，评审并且集成并且发布结果，供他人使用；除了那些参与者需要的命令之外，还会使用这些命令。

    git-am    #用来采用你的贡献者发电邮寄来的补丁文件。

    git-pull    #用来从你的可信任的助手处合并内容。

    git-format-patch    #用来准备并向你的贡献者发送建议选项。

    git-revert    #用来撤销不好的提交。

    git-push    #用来发布最新的内容。

##代码库管理

代码库管理员使用下列工具来设置及维护开发者对代码库的访问。

    git-daemon    #允许匿名者从代码库下载 

    git-shell    #可以被用作为限制登录shell，用于共享中央代码库的用户 update hook howto有一个很好的管理共享中央代码库的实例。


原文链接： kernel.org   翻译： 伯乐在线 - cjpan
译文链接： http://blog.jobbole.com/54184/
