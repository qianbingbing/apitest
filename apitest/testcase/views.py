#coding= utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
import json
import time
import logging
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import models
import sys
from django.core.exceptions import ValidationError

# Create your views here.
logger = logging.getLogger('mylogger')

#登录页面
def login(request):
    return render(request, "login.html")

#登录
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password =='admin123':
            response = HttpResponseRedirect('/index/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error!'})

def add_Project(request):
    return render(request,"addProject.html")
#测试报告页面
def report(request):
    dates=[{"time":"2017-5-11"},{"time":"2017-5-10"},{"time":"2017-5-9"}]
    return render(request,'reportlist.html',{"dates":dates})


#跳转添加页面
def add(request):
    return render(request, 'addInterface.html')



#保存功能
def add_testcase(request):
    if request.method == 'POST':
        title = request.POST.get('title',"")
        desc = request.POST.get('desc',"")
        method = request.POST.get('method',"")
        url = request.POST.get('url',"")
        params_key1 = request.POST.get("key1","")
        params_value1 =request.POST.get("value1","")
        ex_result = request.POST.get('ex_result',"")
        if title == ''or desc == ''or method == '' or url == '' or params_key1 == ''or params_value1 == '' or ex_result == '':
            return JsonResponse({'status':10021,'message':'some paramters is null'})

        else:
            params = {}
            jsons_data ={}
            jsons_data["id"] = int(time.time())
            jsons_data["title"] = title
            jsons_data["desc"] = desc
            jsons_data["method"] = method
            jsons_data["url"] = url
            params[params_key1] = params_value1
            str = json.dumps(params, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
            jsons_data["params"] = str
            logger.debug(str)
            logger.debug(type(str))
            jsons_data["ex_result"] = ex_result
            store_json(jsons_data)
            return HttpResponseRedirect('/index/')


#删除功能
def delete_testcase(requset):
    id = requset.GET.get('id')
    delete_json(id)
    return HttpResponseRedirect('/index/')


#编辑
def edit_testcase(request):
    id = request.GET.get('id')
    obj = get_cases(id)
    params = obj.params
    str = json.loads(params)
    logger.debug(str)
    logger.debug(type(str))
    for k,v in str.items():
        logger.debug(k+':'+v)
    return render(request,'edit.html',{'obj':obj,'params':str})


#更新
def updete_testcase(request,cid):
    logger.debug("更新数据开始")
    if request.method == 'POST':
        title = request.POST.get('title',"")
        desc = request.POST.get('desc',"")
        method = request.POST.get('method',"")
        url = request.POST.get('url',"")
        params_key1 = request.POST.get("key1","")
        params_value1 =request.POST.get("value1","")
        ex_result = request.POST.get('ex_result',"")
        if title == ''or desc == ''or method == '' or url == '' or params_key1 == ''or params_value1 == '' or ex_result == '':
            #return JsonResponse({'status':10021,'message':'some paramters is null'})
            return render(request, 'addInterface.html', {'error': 'any empty input?'})
        else:
            params = {}
            cases =get_cases(cid)
            cases.title =  title
            cases.desc = desc
            cases.method = method
            cases.url = url
            cases.ex_result =ex_result
            params[params_key1] = params_value1
            str = json.dumps(params, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
            cases.params = str
            cases.save()
            return HttpResponseRedirect('/index/')







# 保存至数据库
def store_json(jsondata):
    dic ={"case_id":jsondata["id"],"title":jsondata["title"],"desc":jsondata["desc"],"method":jsondata["method"],"url"
    :jsondata["url"],"params":jsondata["params"],"ex_result":jsondata["ex_result"]}
    models.Testcase.objects.create(**dic)

#查看所有的cases集合
def load_json():
    jsondata = models.Testcase.objects.all()
    return jsondata

#根据id，查找case集合
def get_cases(index):
    case = models.Testcase.objects.get(id=index)
    return case

#删除，参数：id
def delete_json(index):
    models.Testcase.objects.filter(id=index).delete()



#用例集合分页展示
def test_cases(request):
    projectName = [u'慢钱',u'有单',u'保理',u'慢钱宝']
    data = load_json()
    paginator = Paginator(data,5)
    page =request.GET.get('page')
    try:
        cases = paginator.page(page)
    except PageNotAnInteger:
        cases = paginator.page(1)
    except EmptyPage:
        cases = paginator.page(paginator.num_pages)
    return render(request,'index.html',{"cases":cases,"projects":projectName})





