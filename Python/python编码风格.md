#python编码风格

本文来自：http://web.cutt.com/article/1759187240，总结的很好。有所修改。

##文件头部

    #!/usr/bin/env python           #在文件头部 ( 第一行 ) 加上 设置 Python 解释器
    # -*- coding: utf-8 -*-         #在文件头部 ( 第二行 ) 加上 在编辑器中设置以 UTF-8 默认编码保存文件

##文件说明

- docstring 是 Python 特有的注释风格,它是模 块、类或函数的第一个语句,可以通过 __doc__ 方法访问
- 用英语撰写注释,短注释可以忽略末尾的句号 (.)
- docstring 为每个模块、类或函数撰写 docstring 推荐使用三个双引号 (”””) 来定义 docsting , 不推荐使用三个单引号 (''')
- 模块的 docsting 放在文件头部,版权信息之后

    ”””This is a one line docstring.”””
    ”””The title of a multiline docstring:
    After title is the content.You can write it as long as needed.
    ”””

##import语句

- 把 import 语句放在文件头部,在模块 docstring 之后,在模块全局变量或全局常量之前
- 按照从一般到特殊的原则分组 import 语句,先 import 标准库,然后 import 第三方库,最后 import 程序中的自定义库
- 在不同分组的 import 语句之间加空行
- 每个 import 语句只导入一个模块

    import sys
    import time
    from PyQt.QtCore import SIGNAL, QTimer

##中文字符声明

使用中文字符,在文件头部加上

    # import sys
    # reload(sys)
    # sys.setdefaultencoding('utf-8')

##代码长度

- 一行代码的长度不能超过 79 个字符
- 在括号 ( 圆括号、方括号、花括号 ) 内部折行是 推荐使用的方式

    fooBar(self, width, height, color='balck', design=None, x='foo',
        emphasis=None, highlight=0)

需要时可以在表达式两侧加上额外的括号

    if (width == 0 and height == 0 and
    color == 'red' and empasis == 'strong'):

##括号

括号内的长字符串可以直接写成两个短字符串

    x = ('This will build a very long long '
    'long long long long long long string')

##折行符号

使用续行符号,折行的位置可以在逗号 (,) 后或 运算符前,折行后要多一个缩进

    from PyQt4.QtCore import QTextCodec, SIGNAL, SLOT, \
    QLibraryInfo, QTimer

    veryLongVariableA = veryLongVariableB \

    + verLongVariableC

##缩进和空行

- 使用 4 个空格进行缩进 不要使用 Tab 或者混合使用空格和 Tab
- 适当的空行可以提高代码的可读性 加空行的原则:
- 在不同分组的 import 语句之间加空行
- 在顶层的类或函数定义之间加两个空行
- 在类或函数定义之间加空行
- 相关的函数定义可以放在一起,并使用两个空行来分 隔 ( 应谨慎地使用额外的空行 )
- 在函数或方法内部可以加空行,也就是把相关的代码 紧凑地写在一起,形成逻辑段落,段落之间用空行分 隔 ( 应谨慎地使用额外的空行 )

##加空格的情况:

- 逗号 (,) 、冒号 (:) 后要加空格
- 二元运算符前后要加空格,如赋值运算符 (=) 、比较 运算符 (==, <, >, !=, <=, >=, in, not in, is, is not) 和逻 辑运算符 (and, or, not)
- 算数运算符前后要加空格

##不加空格的情况:

- 逗号 (,) 、冒号 (:) 前不加空格 参数列表、索引 (index) 或切片 (slice) 的前括号 ( 圆括号, 方括号)前不加空格 前括号 ( 圆括号、 方括号、花括号 ) 后不加空格,后括号前不加空格 一元运算符前后不加空格
- 函数或方法定义或调用时参数列表中的等号 (=) 前后 不加空格
- 冒号 (:) 在行尾时不加空格,如类定义、函数定义、 分支语句、循环语句

##谨慎地使用括号

- 不要在返回语句和条件语句中使用括号,除非是 为了换行

    if foo:
        bar()
        return foo

- 可以在元组 (tuple) 两侧使用括号

    for (x, y) in dict.items():

##恰当的命名可以提高代码的可读性 命名时只使用 ASCII 字符,并尽量使用英文单词 命名规则

- 类型 公共 内部包 lower_with_under
- 模块 lower_with_under _lower_with_under
- 类 CapWords _CapWords
- 函数 capWords() _capWords()
- 全局常量 / 类常量 CAPS_WITH_UNDER _CAPS_WITH_UNDER
- 全局变量 / 类变量 capWords _capWords
- 方法 capWrods() _capWords() ( 保护 ) __capWords() ( 私有 )
- 函数参数 / 方法参数 capWords
- 局部变量 capWrods
- 不要使用l(小写的L)、o(小写的O)和I(大写的 i) 作为单字符变量名,因为在某些字体下很难把 它们和数字1、0区分开
- 当需要使用 l( 小写的 L) 时可以使用 L 代替
- 当需要使用保留关键字作为函数名时,可以在名 字后加一个下划线 (_) ,而不要破坏正常的拼写

##模块的主要功能要放在 main() 函数中

    def main():
        //do something

    if __name__ == '__main__':
        main()

