# apitest
a  api auto test project
## 2017-6-6更新日志
修复了两个问题 
1、json.loads()反序列化字符串时，提示无法使用单引号，所有在存取数据库前使用json.dumps()将其反序列化
2、中文编码问题，在对其反序列化是将unicode转为中文
代码如下：
```
     params[params_key1] = params_value1
     str = json.dumps(params, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
     jsons_data["params"] = str
```
```
def edit_testcase(request):
    id = request.GET.get('id')
    obj = edit_json(id)
    params = obj.params
    str = json.loads(params)
    logger.debug(str)
    logger.debug(type(str))
    for k,v in str.items():
        logger.debug(k+':'+v)
    return render(request,'edit.html',{'obj':obj,'params':str})
```
补充以下知识点，json.load() json.dump() json.loads(),json.dumps()的区别
```
loads针对内存对象，即将Python内置数据序列化为字串
如使用json.dumps序列化的对象d_json=json.dumps({'a':1, 'b':2})，在这里d_json是一个字串'{"b": 2, "a": 1}'
d=json.loads(d_json)  #{ b": 2, "a": 1}，使用loads重新反序列化为dict
load针对文件句柄
如本地有一个json文件a.json则可以d=json.load(open('a.json'))
相应的，dump就是将内置类型序列化为json对象后写入文件
```
## 2017-6-14更新日志
1、完成了grpc工具类的封装。见grpc_util.py文件
2、新增了添加项目页面，添加接口页面
3、数据模型中新增了项目表，接口表

grpc_util工具类主要使用了反射机制。补充反射机制的一些知识点
```
反射的作用就是列出对象的所有属性和方法，反射就是告诉我们，这个对象到底是什么，提供了什么功能 。
下面介绍主要的几个内置反射函数，如dir() getattr() setattr() __import__

如下：

  pb2file = __import__(self.pb2File)
        requset = getattr(pb2file,reuqestName)
        body = requset()
        if isinstance(context,dict):
            for i in  context.keys():
                try:
                    if hasattr(body,i):
                        setattr(body,i,context[i])
                except :
                    print "params is wrong~ please check it "
        else:
            print "params is not a dict ~ please check it"
        return body
 
```
2017-6-15更新日志
1、完成了增加项目
2、完成了新增接口，更新接口
3、完成了删除接口
4、同步数据的脚本写在.bat文件中






