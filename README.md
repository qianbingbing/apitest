# apitest
a  api auto test project
## 问题1：无法使用json.loads() 导入字典类型的数据
这几天被一个问题纠缠了很久，在数据库中取出数据后，在使用json.loads()方法进行反序列化时发现一致在报错
代码如下：


```
    str1 ="{'key1':'value1'}"
    str2 = json.loads(str1)
    return render(request,'edit.html',{'obj':obj,'params':str2})
```
```
ValueError at /edit/
Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
.....
.....
.....
F:\develop\software_dev\Python\apitest\testcase\views.py in edit_testcase
    str = json.loads(s) ...
▶ Local vars
C:\Python27\lib\json\__init__.py in loads
        return _default_decoder.decode(s) ...
▶ Local vars
C:\Python27\lib\json\decoder.py in decode
        obj, end = self.raw_decode(s, idx=_w(s, 0).end()) ...
▶ Local vars
C:\Python27\lib\json\decoder.py in raw_decode
            obj, end = self.scan_once(s, idx) ...
▶ Local vars
```
这个问题，纠缠了很久的原因，就是不知道为什么不可以反序列化成功。最后找到原因是因为json.loads()不支持对单引号。当然英文也提示了这一点.解决这个问题的方法
后面会讲到

```
load和loads都是实现“反序列化”，区别在于（以Python为例）：

loads针对内存对象，即将Python内置数据序列化为字串
如使用json.dumps序列化的对象d_json=json.dumps({'a':1, 'b':2})，在这里d_json是一个字串'{"b": 2, "a": 1}'
d=json.loads(d_json)  #{ b": 2, "a": 1}，使用load重新反序列化为dict
load针对文件句柄
如本地有一个json文件a.json则可以d=json.load(open('a.json'))
相应的，dump就是将内置类型序列化为json对象后写入文件

```
