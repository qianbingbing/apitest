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
