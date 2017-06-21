#coding= utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
import json
import time
import logging
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import models
import GrpcUtil
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
    projectid = request.GET.get('projectid')
    project = query_json("Project",{"id":projectid})
    data = query_json("Interface",{"project_id":projectid})
    projects = query_json("Project")
    paginator = Paginator(data,10)
    page =request.GET.get('page')
    try:
        cases = paginator.page(page)
    except PageNotAnInteger:
        cases = paginator.page(1)
    except EmptyPage:
        cases = paginator.page(paginator.num_pages)
    return render(request,'project.html',{"cases":cases,"id":projectid,"project":project,"projects":projects})


#添加项目页面
def add_Project(request):
    return render(request,"addProject.html")


#测试报告页面
def report_list(request):
    dates1 = []
    reports =  query_json("Report")
    for i in reports:
        dates1.append(i.test_time.decode('utf-8')[0:10])
    dates2 = list(set(dates1))
    dates2.sort(key=dates1.index)
    if len(dates2) >5:
        dates2 = dates2[0:4]
    return render(request,'reportlist.html',{"dates":dates2})


def report_detail(request):
    return render(request,'result.html')




#添加接口页面
def add_interface(request):
    id = request.GET.get('projectid')
    logger.debug(id)
    return render(request, 'addInterface.html',{"id":id})



#编辑接口页面
def edit_interface(request):
    id = request.GET.get('id')
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
        requestname = request.POST.get('request',"")
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
            jsons_data["request"] = requestname
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
def update_interface(request,cid):
    if request.method == 'POST':
        project_id = request.POST.get('id',"")
        name = request.POST.get('name',"")
        url = request.POST.get('url',"")
        service_name = request.POST.get('service_name',"")
        func = request.POST.get('func',"")
        requestname = request.POST.get('request',"")
        developer = request.POST.get("developer","")
        notes =request.POST.get("notes","")
        if name == ''or url == ''or service_name == '' or func == '':
            return JsonResponse({'status':10021,'message':'some paramters is null'})
        else:
            interface = models.Interface.objects.get(id = cid)
            interface.name =  name
            interface.url = url
            interface.service_name = service_name
            interface.func = func
            interface.request = requestname
            interface.developer =developer
            interface.notes = notes
            '''
            str = json.dumps(params, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
            cases.params = str
            '''
            interface.save()
            return HttpResponseRedirect('/project.html/?projectid=%s'%project_id)



def case_list(request):
    interface_id = request.GET.get('id')
    projectid = request.GET.get('projectid')
    project = query_json("Project",{"id":projectid})
    testcase = query_json("Testcase",{"interface_id":interface_id})
    return render(request,"testcaselist.html",{"project":project,"cases":testcase,"interface_id":interface_id,
                                               "projectid":projectid})


def delete_testcase(request):
    project_id = request.GET.get('project_id')
    interface_id = request.GET.get('interface_id')
    id = request.GET.get('case_id')
    delete_json("Testcase",id)
    return HttpResponseRedirect('/case_list/?projectid=%s&id=%s'%(project_id,interface_id))





def edit_testcase(request):
    id = request.GET.get('case_id')
    project_id = request.GET.get('project_id')
    interface_id = request.GET.get('interface_id')
    cases = query_json("Testcase",{"id":id})
    case = cases[0]
    return render(request,'editTestcase.html',{'case':case,"project_id":project_id,"interface_id":interface_id})




def update_testcase(request):
    project_id = request.GET.get('project_id')
    id = request.GET.get('id')
    case = models.Testcase.objects.get(id = id)
    title = request.POST.get('title',"")
    level = request.POST.get('level',"")
    params = request.POST.get('params',"")
    ex_result = request.POST.get('expect_result',"")
    tester = request.POST.get("developer","")
    if title == ''or params == ''or ex_result == '':
        return JsonResponse({'status':10021,'message':'some paramters is null'})
    else:
        case.title = title
        case.level = level
        case.params = params
        case.ex_result =ex_result
        case.tester = tester
        case.save()
        return HttpResponseRedirect('/case_list/?projectid=%s&id=%s'%(project_id,case.interface_id))



def run_test(request):
    success = 0
    fail = 0
    total = 0
    test_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    test_detail_list = []
    if request.method == 'POST':
        interface_ids = request.POST.getlist('interface_id',"")
        interface_detail = {}
        for i in interface_ids:
            interface = query_json("Interface",{"id":i})
            testcases = query_json("Testcase",{"interface_id":i})
            func = GrpcUtil.GrpcUtil(interface[0].url,interface[0].service_name)
            case_details = []
            success_case = 0
            fail_case = 0
            for i in testcases:
                jsondata = json.loads(i.params,encoding='utf-8')
                response = func.getResponse(interface[0].func,interface[0].request,jsondata)
                case_detail ={}
                case_detail['title'] = i.title
                case_detail['parms'] = i.params
                case_detail['ex_result'] = i.ex_result
                case_detail['real_result'] = response.resultMsg
                case_details.append(case_detail)
                if i.ex_result == response.resultMsg:
                    success_case += 1
                    success += 1
                else:
                    fail_case += 1
                    fail += 1
            division = format(float(success_case)/float(success_case+fail_case),'.2f')

            if division == 0.00:
                result = u'全部失败'
            elif division == 1.00:
                result = u'全部通过'
            else:
                result = u'部分通过'
            interface_detail['name'] = interface[0].name
            interface_detail['func'] = interface[0].func
            interface_detail['result'] = result
            interface_detail['detail'] = case_details
            test_detail_list.append(interface_detail)


        rate = format(float(success)/float(success+fail),'.2f')
        if rate == 0.00:
            test_result = u'全部失败'
        elif rate == 1.00:
            test_result = u'全部通过'
        else:
            test_result = u'部分通过'

        data ={}
        data['test_time'] = test_time
        data['total_case'] = total
        data['fail_case'] = fail
        data['success_case'] = success
        data['test_result'] = test_result
        data['rate'] = rate
        data['detail_list'] = json.dumps(test_detail_list)
        print data['detail_list']
        store_json("Report",data)
        return HttpResponseRedirect('/index')

def add_testcase(request):
    interface_id = request.GET.get('interface_id')
    project_id = request.GET.get('projectid')
    return render(request,"addtestcase.html",{"interface_id":interface_id,"project_id":project_id})




def save_testcase(request):
    if request.method == 'POST':
        interface_id = request.POST.get('interface_id',"")
        project_id = request.POST.get('project_id',"")
        title = request.POST.get('title',"")
        level = request.POST.get('level',"")
        params = request.POST.get('params',"")
        ex_result = request.POST.get('expect_result',"")
        tester = request.POST.get("developer","")
        if title == ''or params == ''or ex_result == '':
            return JsonResponse({'status':10021,'message':'some paramters is null'})
        else:
            jsons_data ={}
            jsons_data["interface_id"] = interface_id
            jsons_data["title"] = title
            jsons_data["level"] = level
            jsons_data["params"] = params
            jsons_data["ex_result"] = ex_result
            jsons_data["tester"] = tester
            logger.debug(jsons_data)
            store_json("Testcase",jsons_data)
            return HttpResponseRedirect('/case_list/?projectid=%s&id=%s'%(project_id,interface_id))




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






