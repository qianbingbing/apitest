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
#首页
def index(request):
    projects = query_json("Project")
    return render(request,'index.html',{"projects":projects})
#接口列表页面
def project(request):
    id = request.GET.get('projectid')
    data = query_json("Interface",{"project_id":id})
    project = query_json("Project",{"id":id})
    projects = query_json("Project")
    paginator = Paginator(data,10)
    page =request.GET.get('page')
    try:
        cases = paginator.page(page)
    except PageNotAnInteger:
        cases = paginator.page(1)
    except EmptyPage:
        cases = paginator.page(paginator.num_pages)
    return render(request,'project.html',{"cases":cases,"id":id,"project":project,"projects":projects})
#添加项目页面
def add_Project(request):
    return render(request,"addProject.html")
#测试报告页面
def report(request):
    dates=[{"time":"2017-5-11"},{"time":"2017-5-10"},{"time":"2017-5-9"}]
    return render(request,'reportlist.html',{"dates":dates})
#添加接口页面
def add_interface(request):
    id = request.GET.get('projectid')
    logger.debug(id)
    return render(request, 'addInterface.html',{"id":id})
#编辑接口页面
def edit_interface(request):
    id = request.GET.get('id')
    logger.debug(id)
    object = query_json("Interface",{"id":id})
    obj = []
    for i in object:
        obj = i
        logger.debug(obj)

    '''
    params = obj.params
    str = json.loads(params)
    logger.debug(str)
    logger.debug(type(str))
    for k,v in str.items():
        logger.debug(k+':'+v)
    '''
    return render(request,'editInterface.html',{'obj':obj})



#登录
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password =='admin123':
            response = HttpResponseRedirect('/index')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error!'})

#保存接口
def save_interface(request):
    if request.method == 'POST':
        project_id = request.POST.get('id',"")
        logger.debug(project_id)
        name = request.POST.get('name',"")
        url = request.POST.get('url',"")
        service_name = request.POST.get('service_name',"")
        func = request.POST.get('func',"")
        developer = request.POST.get("developer","")
        notes =request.POST.get("notes","")
        if name == ''or url == ''or service_name == '' or func == '':
            return JsonResponse({'status':10021,'message':'some paramters is null'})
        else:
            jsons_data ={}
            jsons_data["project_id"] = project_id
            jsons_data["name"] = name
            jsons_data["url"] = url
            jsons_data["service_name"] = service_name
            jsons_data["func"] = func
            jsons_data["developer"] = developer
            jsons_data["notes"] = notes
            logger.debug(jsons_data)
            store_json("Interface",jsons_data)
            return HttpResponseRedirect('/project.html/?projectid=%s'%project_id)

    '''
            str = json.dumps(params, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
            jsons_data["params"] = str
            logger.debug(str)
            logger.debug(type(str))
     '''
#保存项目
def save_project(request):
    if request.method == 'POST':
        name = request.POST.get('projectName',"")
        desc = request.POST.get('projectDesc',"")
        leader =request.POST.get('leader',"")
        notes = request.POST.get('note',"")
        if name == ''or leader == ''or desc == '' :
            return JsonResponse({'status':10021,'message':'some paramters is null'})
        else:
            jsons_data ={}
            jsons_data["id"] = int(time.time())
            jsons_data["name"] = name
            jsons_data["desc"] = desc
            jsons_data["leader"] = leader
            jsons_data["remark"] = notes
            store_json("Project",jsons_data)
            return HttpResponseRedirect('/index')

#删除接口
def delete_interface(requset):
    project_id = requset.GET.get('projectid')
    id = requset.GET.get('id')
    delete_json("Interface",id)
    return HttpResponseRedirect('/project.html/?projectid=%s'%project_id)

#更新接口信息
def updete_interface(request,cid):
    if request.method == 'POST':
        project_id = request.POST.get('id',"")
        name = request.POST.get('name',"")
        url = request.POST.get('url',"")
        service_name = request.POST.get('service_name',"")
        func = request.POST.get('func',"")
        developer = request.POST.get("developer","")
        notes =request.POST.get("notes","")
        if name == ''or url == ''or service_name == '' or func == '':
            return JsonResponse({'status':10021,'message':'some paramters is null'})
        else:
            interface = models.Interface.objects.get(id = cid)
            logger.info(cid)
            logger.info(interface)
            interface.name =  name
            interface.url = url
            interface.service_name = service_name
            interface.func = func
            interface.developer =developer
            interface.notes = notes
            '''
            str = json.dumps(params, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
            cases.params = str
            '''
            interface.save()
            return HttpResponseRedirect('/project.html/?projectid=%s'%project_id)






# crate new into database
def store_json(tablename,jsondata):
    table = getattr(models,tablename)
    table.objects.create(**jsondata)

#delete from database
def delete_json(tablename,index):
    table = getattr(models,tablename)
    table.objects.filter(id=index).delete()

#query data from  database
def query_json(tablename,context=None):
    table = getattr(models,tablename)
    if context == None:
        return table.objects.all()
    else:
        return table.objects.filter(**context)






