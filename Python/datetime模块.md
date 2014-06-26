#Python的datetime模块

Python提供了多个内置模块用于操作日期时间，像calendar，time，datetime。

##datetime模块定义了两个常量：

datetime.MINYEAR和datetime.MAXYEAR，分别表示datetime所能表示的最 小、最大年份。其中，MINYEAR = 1，MAXYEAR = 9999。（对于偶等玩家，这个范围已经足够用矣~~）

datetime模块定义了下面这几个类：

- datetime.date：表示日期的类。常用的属性有year, month, day；
- datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond；
- datetime.datetime：表示日期时间。
- datetime.timedelta：表示时间间隔，即两个时间点之间的长度。
- datetime.tzinfo：与时区有关的相关信息。（这里不详细充分讨论该类，感兴趣的童鞋可以参考python手册）

注：上面这些类型的对象都是不可变（immutable）的。

下面详细介绍这些类的使用方式。

##date类

date类表示一个日期。日期由年、月、日组成（地球人都知道~~）。date类的构造函数如下：

    class datetime.date(year, month, day)：参数的意义就不多作解释了，只是有几点要注意一下：

    - year的范围是[MINYEAR, MAXYEAR]，即[1, 9999]；
    - month的范围是[1, 12]。（月份是从1开始的，不是从0开始的~_~）；
    - day的最大值根据给定的year, month参数来决定。例如闰年2月份有29天；

###date类定义了一些常用的类方法与类属性，方便我们操作：

- date.max、date.min：date对象所能表示的最大、最小日期；
- date.resolution：date对象表示日期的最小单位。这里是天。
- date.today()：返回一个表示当前本地日期的date对象；
- date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象；
- datetime.fromordinal(ordinal)：将Gregorian日历时间转换为date对象；（Gregorian Calendar：一种日历表示方法，类似于我国的农历，西方国家使用比较多，此处不详细展开讨论。）

**使用例子：**

    from datetime import *      
    import time             

    print 'date.max:', date.max      
    print 'date.min:', date.min      
    print 'date.today():', date.today()      
    print 'date.fromtimestamp():', date.fromtimestamp(time.time())             
    # # ---- 结果 ----      
    # date.max: 9999-12-31      
    # date.min: 0001-01-01      
    # date.today(): 2010-04-06      
    # date.fromtimestamp(): 2010-04-06 

###date提供的实例方法和属性：

- date.year、date.month、date.day：年、月、日；
- date.replace(year, month, day)：生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
- date.timetuple()：返回日期对应的time.struct_time对象；
- date.toordinal()：返回日期对应的Gregorian Calendar日期；
- date.weekday()：返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；
- data.isoweekday()：返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；
- date.isocalendar()：返回格式如(year，month，day)的元组；
- date.isoformat()：返回格式如'YYYY-MM-DD’的字符串；
- date.strftime(fmt)：自定义格式化字符串。在下面详细讲解。

**使用例子：**

    now = date(2010, 04, 06)  
    tomorrow = now.replace(day = 07)  
    print 'now:', now, ', tomorrow:', tomorrow  
    print 'timetuple():', now.timetuple()  
    print 'weekday():', now.weekday()  
    print 'isoweekday():', now.isoweekday()  
    print 'isocalendar():', now.isocalendar()  
    print 'isoformat():', now.isoformat()  
      
    # # ---- 结果 ----  
    # now: 2010-04-06 , tomorrow: 2010-04-07  
    # timetuple(): (2010, 4, 6, 0, 0, 0, 1, 96, -1)  
    # weekday(): 1  
    # isoweekday(): 2  
    # isocalendar(): (2010, 14, 2)  
    # isoformat(): 2010-04-06  

date还对某些操作进行了重载，它允许我们对日期进行如下一些操作：

- date2 = date1 + timedelta  # 日期加上一个间隔，返回一个新的日期对象（timedelta将在下面介绍，表示时间间隔）
- date2 = date1 - timedelta   # 日期隔去间隔，返回一个新的日期对象
- timedelta = date1 - date2   # 两个日期相减，返回一个时间间隔对象
- date1 < date2  # 两个日期进行比较

注：对日期进行操作时，要防止日期超出它所能表示的范围。

**使用例子：**

    now = date.today()  
    tomorrow = now.replace(day = 7)  
    delta = tomorrow - now  
    print 'now:', now, ' tomorrow:', tomorrow  
    print 'timedelta:', delta  
    print now + delta  
    print tomorrow > now  
      
    # # ---- 结果 ----  
    # now: 2010-04-06  tomorrow: 2010-04-07  
    # timedelta: 1 day, 0:00:00  
    # 2010-04-07  
    # True  

##time类

time类表示时间，由时、分、秒以及微秒组成。（我不是从火星来的~~）time类的构造函数如下：

class datetime.time(hour[, minute[, second[, microsecond[, tzinfo]]]]) ：各参数的意义不作解释，这里留意一下参数tzinfo，它表示时区信息。注意一下各参数的取值范围：hour的范围为[0, 24)，minute的范围为[0, 60)，second的范围为[0, 60)，microsecond的范围为[0, 1000000)。

###time类定义的类属性：

- time.min、time.max：time类所能表示的最小、最大时间。其中，time.min = time(0, 0, 0, 0)， time.max = time(23, 59, 59, 999999)；
- time.resolution：时间的最小单位，这里是1微秒；

###time类提供的实例方法和属性：

- time.hour、time.minute、time.second、time.microsecond：时、分、秒、微秒；
- time.tzinfo：时区信息；
- time.replace([hour[, minute[, second[, microsecond[, tzinfo]]]]])：创建一个新的时间对象，用参数指定的时、分、秒、微秒代替原有对象中的属性（原有对象仍保持不变）；
- time.isoformat()：返回型如"HH:MM:SS"格式的字符串表示；
- time.strftime(fmt)：返回自定义格式化字符串。在下面详细介绍；

**使用例子：**

    from datetime import *  
    tm = time(23, 46, 10)  
    print 'tm:', tm  
    print 'hour: %d, minute: %d, second: %d, microsecond: %d' /  
            % (tm.hour, tm.minute, tm.second, tm.microsecond)  
    tm1 = tm.replace(hour = 20)  
    print 'tm1:', tm1  
    print 'isoformat():', tm.isoformat()  
      
    # # ---- 结果 ----  
    # tm: 23:46:10  
    # hour: 23, minute: 46, second: 10, microsecond: 0  
    # tm1: 20:46:10  
    # isoformat(): 23:46:10  

    像date一样，也可以对两个time对象进行比较，或者相减返回一个时间间隔对象。这里就不提供例子了。

##datetime类

datetime是date与time的结合体，包括date与time的所有信息。它的构造函数如下：datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])，各参数的含义与date、time的构造函数中的一样，要注意参数值的范围。

datetime类定义的类属性与方法：

- datetime.min、datetime.max：datetime所能表示的最小值与最大值；
- datetime.resolution：datetime最小单位；
- datetime.today()：返回一个表示当前本地时间的datetime对象；
- datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
- datetime.utcnow()：返回一个当前utc时间的datetime对象；
- datetime.fromtimestamp(timestamp[, tz])：根据时间戮创建一个datetime对象，参数tz指定时区信息；
- datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个datetime对象；
- datetime.combine(date, time)：根据date和time，创建一个datetime对象；
- datetime.strptime(date_string, format)：将格式字符串转换为datetime对象；

**使用例子：**

    from datetime import *  
    import time  
      
    print 'datetime.max:', datetime.max  
    print 'datetime.min:', datetime.min  
    print 'datetime.resolution:', datetime.resolution  
    print 'today():', datetime.today()  
    print 'now():', datetime.now()  
    print 'utcnow():', datetime.utcnow()  
    print 'fromtimestamp(tmstmp):', datetime.fromtimestamp(time.time())  
    print 'utcfromtimestamp(tmstmp):', datetime.utcfromtimestamp(time.time())  
      
    # ---- 结果 ----  
    # datetime.max: 9999-12-31 23:59:59.999999  
    # datetime.min: 0001-01-01 00:00:00  
    # datetime.resolution: 0:00:00.000001  
    # today(): 2010-04-07 09:48:16.234000  
    # now(): 2010-04-07 09:48:16.234000  
    # utcnow(): 2010-04-07 01:48:16.234000  # 中国位于+8时间，与本地时间相差8  
    # fromtimestamp(tmstmp): 2010-04-07 09:48:16.234000  
    # utcfromtimestamp(tmstmp): 2010-04-07 01:48:16.234000  

datetime类提供的实例方法与属性（很多属性或方法在date和time中已经出现过，在此有类似的意义，这里只罗列这些方法名，具体含义不再逐个展开介绍，可以参考上文对date与time类的讲解。）：

- datetime.year、month、day、hour、minute、second、microsecond、tzinfo：
- datetime.date()：获取date对象；
- datetime.time()：获取time对象；
- datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])：
- datetime.timetuple()
- datetime.utctimetuple()
- datetime.toordinal()
- datetime.weekday()
- datetime.isocalendar()
- datetime.isoformat([sep])
- datetime.ctime()：返回一个日期时间的C格式字符串，等效于time.ctime(time.mktime(dt.timetuple()))；
- datetime.strftime(format)

像date一样，也可以对两个datetime对象进行比较，或者相减返回一个时间间隔对象，或者日期时间加上一个间隔返回一个新的日期时间对象。这里不提供详细的例子，看客自己动手试一下~~

##格式字符串

datetime、date、time都提供了strftime()方法，该方法接收一个格式字符串，输出日期时间的字符串表示。下表是从python手册中拉过来的，我对些进行了简单的翻译（翻译的有点噢口~~）。

>>格式字符  意义

>>%a星期的简写。如 星期三为Web
>>%A星期的全写。如 星期三为Wednesday
>>%b月份的简写。如4月份为Apr
>>%B月份的全写。如4月份为April
>>%c: 日期时间的字符串表示。（如： 04/07/10 10:43:39）
>>%d: 日在这个月中的天数（是这个月的第几天）
>>%f: 微秒（范围[0,999999]）
>>%H: 小时（24小时制，[0, 23]）
>>%I: 小时（12小时制，[0, 11]）
>>%j: 日在年中的天数 [001,366]（是当年的第几天）
>>%m: 月份（[01,12]）
>>%M: 分钟（[00,59]）
>>%p: AM或者PM
>>%S: 秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
>>%U: 周在当年的周数当年的第几周），星期天作为周的第一天
>>%w: 今天在这周的天数，范围为[0, 6]，6表示星期天
>>%W: 周在当年的周数（是当年的第几周），星期一作为周的第一天
>>%x: 日期字符串（如：04/07/10）
>>%X: 时间字符串（如：10:43:39）
>>%y: 2个数字表示的年份
>>%Y: 4个数字表示的年份
>>%z: 与utc时间的间隔 （如果是本地时间，返回空字符串）
>>%Z: 时区名称（如果是本地时间，返回空字符串）
>>%%: %% => %

**例子：**

    dt = datetime.now()  
    print '(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y-%m-%d %H:%M:%S %f')  
    print '(%Y-%m-%d %H:%M:%S %p): ', dt.strftime('%y-%m-%d %I:%M:%S %p')  
    print '%%a: %s ' % dt.strftime('%a')  
    print '%%A: %s ' % dt.strftime('%A')  
    print '%%b: %s ' % dt.strftime('%b')  
    print '%%B: %s ' % dt.strftime('%B')  
    print '日期时间%%c: %s ' % dt.strftime('%c')  
    print '日期%%x：%s ' % dt.strftime('%x')  
    print '时间%%X：%s ' % dt.strftime('%X')  
    print '今天是这周的第%s天 ' % dt.strftime('%w')  
    print '今天是今年的第%s天 ' % dt.strftime('%j')  
    print '今周是今年的第%s周 ' % dt.strftime('%U')  
      
    # # ---- 结果 ----  
    # (%Y-%m-%d %H:%M:%S %f):  2010-04-07 10:52:18 937000  
    # (%Y-%m-%d %H:%M:%S %p):  10-04-07 10:52:18 AM  
    # %a: Wed   
    # %A: Wednesday   
    # %b: Apr   
    # %B: April   
    # 日期时间%c: 04/07/10 10:52:18   
    # 日期%x：04/07/10   
    # 时间%X：10:52:18   
    # 今天是这周的第3天   
    # 今天是今年的第097天   
    # 今周是今年的第14周  

这些就是datetime模块的基本内容，

