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
import datetime
import uuid
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.
logger = logging.getLogger('mylogger')

#登录页面
def Login(request):
    return render(request, "login.html")
#账号登录
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect('/index/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error!'})
#首页
@login_required
def index(request):
    project_number = len(query_json("Project"))
    interface_number = len(query_json("Interface"))
    testcase_number = len(query_json("Testcase"))
    report_number = len(query_json("Report"))
    request.session.set_expiry(0)
    return render(request,'index.html',{"project_number":project_number,"interface_number":interface_number,"testcase_number":testcase_number,"report_number":report_number})
#项目预览页面
def project(request):
    projectid = request.GET.get('projectid')
    #查询当前项目
    project = query_json("Project",{"id":projectid})
    #查询项目接口
    data = query_json("Interface",{"project_id":projectid})
    #查询所有项目
    projects = query_json("Project")
    #数据分页
    paginator = Paginator(data,10)
    page =request.GET.get('page')
    try:
        cases = paginator.page(page)
    except PageNotAnInteger:
        cases = paginator.page(1)
    except EmptyPage:
        cases = paginator.page(paginator.num_pages)



    return render(request,'project.html',{"cases":cases,"id":projectid,"project":project,"projects":projects})
#项目管理页面
def projectMange(request):
     projects = query_json("Project")
     return render(request,"projectManage.html",{"projects":projects})
#添加项目页面
def add_Project(request):
    return render(request,"addProject.html")

#测试报告-列表
#use reserve（）to reverse a list  the more pythonic？ like this
#list[::-1] this is use list slice
def report_list(request):

    '''
    改变了页面设计，删除这部分的代码，
    #最五天的日期的列表
    for i in range(-4,1):
        value ={}
        yesterday =datetime.datetime.now() +datetime.timedelta(days=i)
        time =  yesterday.strftime('%Y-%m-%d')
        value['time'] = time
        #根据日期查看当天的测试报告
        queryset = models.Report.objects.filter(test_time__contains=time)
        datas =[]
        #判断查询结果是否为空，为空则说明当天没有测试报告生成
        if queryset:
            for i in queryset:
                data = {}
                data['id'] = i.id
                data['test_time'] = i.test_time
                datas.append(data)
        else:
            datas.append(u"暂无测试报告")
        #反转列表顺序，将其存入字典
        value['data'] = datas[::-1]
        dates1.append(value)
    dates1.reverse()
    '''
    report_lists = query_json("Report")
    report_lists = report_lists[::-1]
    #数据分页
    paginator = Paginator(report_lists,10)
    page =request.GET.get('page')
    try:
        cases = paginator.page(page)
    except PageNotAnInteger:
        cases = paginator.page(1)
    except EmptyPage:
        cases = paginator.page(paginator.num_pages)
    return render(request,'reportlist.html',{"cases":cases})

#测试报告-详情
def report_detail(request):
    id = request.GET.get('id')
    datas = query_json("Report",{"id":id})
    report_id = datas[0].report_id
    details = query_json("Report_detail",{"report_id":report_id})
    return render(request,'result.html',{"datas":datas,"details":details,"report_id":id})

#测试报告-详情-用例详情
def cases_detail(request):
    id = request.GET.get('id')
    report_id = request.GET.get('report_id')
    interface_id = request.GET.get('interface_id')
    interface =query_json("Interface",{"id":interface_id})
    print interface[0]
    datas = query_json("Report_detail",{"id":id})
    cases_details = datas[0].case_detail
    return render(request,'case_detail.html',{"cases_details":json.loads(cases_details),"interface":interface[0],"report_id":report_id})
#项目列表
def project_list(request):
    projects = query_json("Project")
    datas = []
    try:
        for project in projects:
            detail = {}
            number = len(query_json("Interface",{"project_id":project.id}))
            detail["number"] =  number
            detail["projectName"] = project.name
            detail["projectId"] = project.id
            datas.append(detail)
        print datas
    except:
        print 'aaa'
    return render(request, "projectlist.html",{"datas":datas})
#添加接口
def add_interface(request):
    id = request.GET.get('projectid')
    return render(request, 'addInterface.html',{"id":id})

#编辑接口
def edit_interface(request):
    id = request.GET.get('id')
    object = query_json("Interface",{"id":id})
    obj = object[0]
    return render(request,'editInterface.html',{'obj':obj})

#保存接口信息
def save_interface(request):
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
            jsons_data ={}
            jsons_data["project_id"] = project_id
            jsons_data["name"] = name
            jsons_data["url"] = url
            jsons_data["service_name"] = service_name
            jsons_data["func"] = func
            jsons_data["request"] = requestname
            jsons_data["developer"] = developer
            jsons_data["notes"] = notes
            store_json("Interface",jsons_data)
            return HttpResponseRedirect('/project.html/?projectid=%s'%project_id)

    '''
            str = json.dumps(params, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
            jsons_data["params"] = str
            logger.debug(str)
            logger.debug(type(str))
     '''
#保存项目信息
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
    #删除接口时对应删除该接口的所有用例
    delete_json("Interface",{"id":id})
    delete_json("Testcase",{"interface_id":id})
    return HttpResponseRedirect('/project.html/?projectid=%s'%project_id)

#更新接口信息
def update_interface(request,cid):
    if request.method == 'POST':
        project_id = request.POST.get('id', "")
        name = request.POST.get('name', "")
        url = request.POST.get('url', "")
        service_name = request.POST.get('service_name', "")
        func = request.POST.get('func', "")
        requestname = request.POST.get('request', "")
        developer = request.POST.get("developer", "")
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
#用例列表
def case_list(request):
    interface_id = request.GET.get('id')
    projectid = request.GET.get('projectid')
    project = query_json("Project",{"id":projectid})
    testcase = query_json("Testcase",{"interface_id":interface_id})
    return render(request,"testcaselist.html",{"project":project,"cases":testcase,"interface_id":interface_id,
                                               "projectid":projectid})
#删除测试用例
def delete_testcase(request):
    project_id = request.GET.get('project_id')
    interface_id = request.GET.get('interface_id')
    id = request.GET.get('case_id')
    delete_json("Testcase",{"id":id})
    return HttpResponseRedirect('/case_list/?projectid=%s&id=%s'%(project_id,interface_id))
#编辑测试用例
def edit_testcase(request):
    id = request.GET.get('case_id')
    project_id = request.GET.get('project_id')
    interface_id = request.GET.get('interface_id')
    cases = query_json("Testcase",{"id":id})
    case = cases[0]
    return render(request,'editTestcase.html',{'case':case,"project_id":project_id,"interface_id":interface_id})
#更新测试用例
def update_testcase(request):
    project_id = request.GET.get('project_id')
    id = request.GET.get('id')
    case = models.Testcase.objects.get(id = id)
    title = request.POST.get('title',"")
    level = request.POST.get('level',"")
    params = request.POST.get('params',"")
    precondition = request.POST.get('Precondition',"")
    ex_result = request.POST.get('expect_result',"")
    tester = request.POST.get("developer","")
    if title == ''or params == '':
        return JsonResponse({'status':10021,'message':'some paramters is null'})
    else:
        case.title = title
        case.level = level
        case.params = params
        case.ex_result =ex_result
        case.precondition = precondition
        case.tester = tester
        case.save()
        return HttpResponseRedirect('/case_list/?projectid=%s&id=%s'%(project_id,case.interface_id))
#运行测试用例
def run_test(request):
    success = 0
    fail = 0
    id = str(uuid.uuid4())
    test_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    if request.method == 'POST':
        interface_ids = request.POST.getlist('interface_id',"")
        print interface_ids
        interface_number =len(interface_ids)

        if interface_number == 0:
            return JsonResponse({'status':10021,'message':u'no selected case'})
        else:
            for i in interface_ids:
                interface_detail = {}
                interface = query_json("Interface",{"id":i})
                testcases = query_json("Testcase",{"interface_id":i})
                if testcases:
                    func = GrpcUtil.GrpcUtil(interface[0].url,interface[0].service_name)
                    case_details = []
                    success_case = 0
                    fail_case = 0
                    for j in testcases:
                        jsondata = json.loads(j.params,encoding='utf-8')
                        try:
                            precondition = json.loads(j.precondition,encoding='utf-8')
                            for key in precondition.keys():
                                jsondata[key] = precondition[key]
                        except:
                            pass
                        response = func.getResponse(interface[0].func,interface[0].request,jsondata)
                        case_detail ={}
                        case_detail['case_id'] = j.id
                        case_detail['title'] = j.title
                        case_detail['precondition'] = j.precondition
                        case_detail['parms'] = j.params
                        case_detail['ex_result'] = j.ex_result
                        case_detail['real_result'] = response
                        case_details.append(case_detail)
                        if j.ex_result == response:
                            case_detail['result'] = 'success'
                            success_case += 1
                            success += 1
                        else:
                            case_detail['result'] = 'fail'
                            fail_case += 1
                            fail += 1
                    division = format(float(success_case)/float(success_case+fail_case),'.2f')
                    if division == '0.00':
                        result = u'全部失败'
                    elif division == '1.00':
                        result = u'全部通过'
                    else:
                        result = u'部分通过'
                    interface_detail['report_id'] = id
                    interface_detail['interface_id'] = i
                    interface_detail['interface_name'] = interface[0].name
                    interface_detail['func_name'] = interface[0].func
                    interface_detail['interface_result'] = result
                    interface_detail['case_detail'] = json.dumps(case_details,encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
                    store_json("Report_detail",interface_detail)

            rate = format((float(success)/float(success+fail))*100,'.0f')
            data ={}
            data['report_id'] = id
            data['test_time'] = test_time
            data['total_case'] = fail+success
            data['fail_case'] = fail
            data['success_case'] = success
            data['rate'] = rate
            data['interface_number'] = interface_number
            store_json("Report",data)
            return HttpResponseRedirect('/index')






#跳转到添加测试用例
def add_testcase(request):
    #获取接口id和项目id
    interface_id = request.GET.get('interface_id')
    project_id = request.GET.get('projectid')
    return render(request,"addtestcase.html",{"interface_id":interface_id,"project_id":project_id})
#保存添加测试用例
def save_testcase(request):
    if request.method == 'POST':
        interface_id = request.POST.get('interface_id',"")
        project_id = request.POST.get('project_id',"")
        title = request.POST.get('title',"")
        level = request.POST.get('level',"")
        precondition = request.POST.get('precondition',"")
        params = request.POST.get('params',"")
        ex_result = request.POST.get('expect_result',"")
        tester = request.POST.get("developer","")
        #如果标题或参数为空，给出提示
        if title == ''or params == '':
            return JsonResponse({'status':10021,'message':'some paramters is null'})
        #返回保存用例相关信息，包括接口id，标题，用例等级，参数，预期结果，用例设计者，前置条件
        else:
            jsons_data ={}
            jsons_data["interface_id"] = interface_id
            jsons_data["title"] = title
            jsons_data["level"] = level
            jsons_data["params"] = params
            jsons_data["ex_result"] = ex_result
            jsons_data["tester"] = tester
            jsons_data["precondition"] = precondition
            store_json("Testcase",jsons_data)
            return HttpResponseRedirect('/case_list/?projectid=%s&id=%s'%(project_id,interface_id))




# crate new data into database
def store_json(tablename,jsondata):
    table = getattr(models,tablename)
    table.objects.create(**jsondata)
#delete from database
def delete_json(tablename,query):
    table = getattr(models,tablename)
    table.objects.filter(**query).delete()
#query data from  database
def query_json(tablename,context=None):
    table = getattr(models,tablename)
    if context == None:
        return table.objects.all()
    else:
        return table.objects.filter(**context)






