#改善jQuery的性能和代码

##1、永远使用最新版本(如果可能的话)  

jQuery在不断的开发与改进，为了避免重复的更新本地版本，可以使用下面的代码片段：

    <script src="//ajax.googleapis.com/ajax/libs/jquery/latest/jquery.js" type="text/javascript"></script>

一个好的建议是，根据你的项目环境，最终选择一个固定的版本。

##2、使用For来代替Each

这是Jon Banner(我的好哥们与前同事)教会我的。    

    var array = new Array ();      

    for (var i=0; i<10000; i++) {

         array[i] = 0;

       }        

有众多来源表明，在线上代码中，使用for循环比Each循环速度要快100%(在毫秒级)。

##3、使用return false  

你是否遇到过为一个或多个元素绑定click事件函数，一旦点击元素后页面跳回到了顶部？当页面很长的时候，这个问题毫无疑问会变得非常烦人。你可以这样：

    $('#element').click(function(){

        // do something...

        return false;

    });        

##4、划分你的代码  

对我来说这条技巧就是大救星。如果你像我一样构建或管理大型网站，你一定不会希望每次页面(或一个特定的页面模板)触发时加载所有的JavaScript文件。  

这个方法与JavaScript或ActionScript语言中的switch函数类似，但与之不同的是你对哪些能够调用拥有控制权，而不是像switch方法是预先定义好的。  

这样一来，浏览器就不需要把JavaScript文件里的所有函数都加载并运行了。    

    var mylib =

    {

        primary_functions :

           {

               init : function()

                  {            // 这里写方法

                   }

            },

         specific_template_functions :

            {

                 init : function()

                      {           // 这里写方法

                       }

              }

        }

    $(window).load(function(){

         // 在HTML载入后再去加载通用脚本会更有效率。

          mylib.primary_functions.init();

       });

 “specific_template_functions”函数可以在特定模板或页面载入时被调用。对于5-10行代码来说，使用这种方式不会起到任何作用，但是它对于那些想要通过划分大块代码来养成良好习惯的人来说是个不错的尝试。

##5、合并压缩你的JavaScript  

当你的网站进入测试阶段时，你可能意识到网站引用了不止一个JavaScript文件或插件。把它们合并成一个文件。合并多个文件与让浏览器加载并读取多个文件相比，始终是更快和更好的做法。

##6、避免操作DOM  

这么做是有原因的，其中一些与网站可访问性有关。例如，当你“绝对需要”一些文字或元素被屏幕阅读软件读取时，如果浏览器禁止了脚本那你就遇到大麻烦了，就像末日来临，世界被黑暗笼罩——你肯定懂我的意思。按照我的经验，当你在做一些动态效果、为页面增加一些装饰时会这么做，但是最终你还是会尽可能的减少这样的操作。  

.append()，.prepend()和.after()(我认为)与.html()相比在相同时间内会消耗更多的资源。在插入前将需要插入的内容构建好会更符合逻辑。所以：    

    var yourlist = '';      

    for (var i=0; i<1000; i++) {

         yourlist += '<li>'+i+'</li>';

       }

    ('#list').html(yourlist); 

##7、通过正确的节点标示符来遍历HTML 

通过ID查找元素比通过class要快很多。没有必要提供例子了，不过如果你真的需要一个例子，请告诉我。

##8、速查表  

这是一个能够让你在写程序时不会忘记大多数可用函数的好办法。这里提供一些(有些是我最喜欢的)：    

- Oscar Otero’s API指南  

- Antonio Lupetti的速查表

##9、在页面底部加载你的jQuery文件  

总之，真的应该在页面底部去加载代码。当然如果你需要在页面中调用经过划分后的代码，可以使用前面介绍过的window的load函数，但也应该放在底部。    

    $(window).load(function() {

       // It's more efficient to load any generic scripts after the HTML has loaded.'

      });

##10、返回页面中元素的个数 

这是找出页面中元素个数的既简单又快捷的方法：

    $('element').size();          
