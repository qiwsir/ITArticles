#jQuery日历

基本的使用方法，参考官方网站：http://jqueryui.com/datepicker/

典型样例如下：

    <!doctype html>

    <html lang="en">

    <head>

        <meta charset="utf-8">

        <title>jQuery UI Datepicker - Default functionality</title>

        <link rel="stylesheet" href="//code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css">

        <script src="//code.jquery.com/jquery-1.9.1.js"></script>

        <script src="//code.jquery.com/ui/1.10.4/jquery-ui.js"></script>

        <link rel="stylesheet" href="/resources/demos/style.css">

        <script>

            $(function() { $( "#datepicker" ).datepicker(); });

        </script>

    </head>

    <body>

        <p>Date: <input type="text" id="datepicker"></p>

    </body>

    </html>

对于在中文的呈现，还需要额外的一个脚本：https://github.com/jquery/jquery-ui/blob/master/ui/i18n/jquery.ui.datepicker-zh-CN.js

##选择日期

###使文本框只读

这里需要注意，如果文本框不允许输入的话，需要设置readonly属性：

    $("#datepicker").prop("readOnly", true).datepicker();

另外还需要注意，如非必要，不要直接在文本框的html属性上设置readonly(特别是asp.net TextBox)，否则后台可能不能正常获取。

###控制输入的字符

开启constrainInput属性，就可以控制文本框的输入只能为dateFormat属性中规定的(没启用readonly情况下)：

  $("#datepicker").datepicker({ constrainInput: true });

###显示年、月选择框

默认情况下选择年、月比较麻烦，这里可以开启两个属性是年、月变为下拉框选择：

    $(".dp").datepicker({ changeMonth: true, changeYear: true });

另外还可以把年下拉框显示在月下拉框之前：

    $(".dp").datepicker({ changeMonth: true, changeYear: true, showMonthAfterYear: true });

设置选择的年的范围，可以是具体的年份或者是特定的格式：

- "-nn:+nn"相对于当前年份，当前2012年，如"-5:+5"就是从2007-2017范围

- "c-nn:c+nn"相对于选中的年份，如选中2013，"c-5:c+5"就是从2008-2018范围

-  "nnnn:nnnn"直接指定年份，如"2010-2013"

    $(".dp").datepicker({ changeMonth: true, changeYear: true, showMonthAfterYear: true, yearRange: "-5:+5" });

    $(".dp").datepicker({ changeMonth: true, changeYear: true, showMonthAfterYear: true, yearRange: "c-5:c+5" });

    $(".dp").datepicker({ changeMonth: true, changeYear: true, showMonthAfterYear: true, yearRange: "2010:2013" });

###显示日期的格式

通过设置dateFormat属性来实现，分别用yy、mm、dd来表示年、月、日；默认值为mm/dd/yy，中文环境下一般设置为：

    $(".dp").datepicker({ dateFormat: "yy-mm-dd" });

###控制日期范围

通过minDate/maxDate来设置可以选择的日期范围，可以是日期类型； 或者是特定的格式，使用三个字符来表示：    

1.第一个字符为+或-    

2.第二个字符为数字    

3.第三个字符表示单位如y,m,w,d表示年、月、周、天，可以拼出N中结果如："+1y" "-1m"    

4.而且可以叠加，只要中间空格隔开即可如："+1m +1w +2d"表示一个月+一周+两天

    $(".dp").datepicker({ maxDate: "+1m +1w +1d", minDate: "-1d" });

    $(".dp").datepicker({ maxDate: new Date(2012,12,21), minDate: new Date(2012,12,08) }); 显示今天及确定按钮

    $(".dp").datepicker({ showButtonPanel: true }); 还可以设置点击今天调到当前月份的日历视图：

    $(".dp").datepicker({ showButtonPanel: true, gotoCurrent: true });

##选择时间

jQuery UI Datepicker没有提供选择时间功能，不过有人基于jQuery UI Datepicker创造了timepicker：

[http://trentrichardson.com/examples/timepicker/](http://trentrichardson.com/examples/timepicker/)

可以从[https://github.com/trentrichardson/jQuery-Timepicker-Addon](https://github.com/trentrichardson/jQuery-Timepicker-Addon)获取它的最新版本

###资源引入

除了需要引入上面jQuery UI Datepicker使用的资源以外，还需要一下资源：

    <link href="js/timepicker-addon/jquery-ui-timepicker-addon.css" rel="stylesheet" />

    <script src="js/timepicker-addon/jquery-ui-timepicker-addon.min.js"></script>

    <script src="js/timepicker-addon/jquery-ui-timepicker-zh-CN.min.js"></script>

###使用方法

它的功能分为两部分：

- 一种是可以同时选择日期和时间的datetimepicker，

- 另一种是只能选时间的timepicker  

    $(".dp").datetimepicker();  

    $(".dp").timepicker();

###参数设置

它也有自己的一些参数可以设置，这里仅列出重要的：

    timeFormat 设置时间格式，其中两个相同字母的表示不足两位补0

        H/HH：24小时

        h/hh：12小时

        m/mm：分钟

        s/ss：秒钟

        l：毫秒

        t/tt,T/TT：设置AM/PM即上午/下午

        z：失去

    defaultTimezone：默认时区"+0000"

    showHour/showMinute/showSecond/…showTimezone/showTime分别设置是否显示相应选择

    stepHour/stepMinute/StepSecond…分别设置拖动滑块时增减的数值

    maxDateTime/minDateTime：控制时间范围

    controlType：控件类型："select"(下拉选择)、"slide"(拖动滑块，默认) 

###格式化输入

有时候可能会需要可以选择也可以输入，这时候可以额外附加脚本：http://www.meiocodigo.com/projects/meiomask/或者是其他有mask功能的组件定义好mask格式：

    $(".dp").datepicker().setMask("9999-19-39")

-------------
本文来源：http://www.cnblogs.com/lwme/archive/2012/12/08/jquery-ui-datepicker.html 


