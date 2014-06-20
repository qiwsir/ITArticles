#纠正jQuery获取radio选中值的写法

先看一段代码

    <input type="radio" name="aaa" value="1" checked="true">aaa    

    <input type="radio" name="aaa" value="2">bbb    

    <input type="radio" name="aaa" value="3">ccc    

    <input type="button" value="ok" onclick="doTest()">    

    <script language="JavaScript">    

    <!--   function doTest()

    {    

        alert($("input[name='aaa'][checked]").val());  

    }   

     //--> </script>

网上流行的说法就是 $(input[name='aaa'][checked]).val() 能取到选中项的value，但我测试后发现只在IE下有效，在firefox和Chrome中不论选中哪一项，或者不选，取到的值都是第一项的value

正确做法应该是 
    
    $("input[name='aaa']:checked").val()

同样对于checkbox也是这种写法 
