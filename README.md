#项目版本规划
##v1.0   (7月15号前完成)
1、项目（基础的增删改查）
2、接口（基础的增删改查）
3、用例（基础的增删改查）
4、测试报告（增删改查）
##v2.0   (8月15号前完成)
1、数据前置和后置功能
2、测试环境/正式环境
3、测试报告图形分析



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

2017-7-12更新日志
1、完成首页访问权限控制，需要用户登录后才可以登录页面
2、完成session过期设置，设置为关闭浏览器session失效
```
yield 简单说明
如下面的代码：

def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        a, b = b, a + b 
        n = n + 1 
for i in fab(5):
    print i
		
```
简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，
下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，
于是函数继续执行，直到再次遇到 yield。
