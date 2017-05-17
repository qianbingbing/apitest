#coding= utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def login(request):
    return render(request, "login.html")
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password =='admin123':
            response = HttpResponseRedirect('/index/')
            response.set_cookie('user',username,3600)
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error!'})
def index(request):
    username = request.COOKIES.get('user','')

    cases =[
    {
    "TestId": "0001",
    "Method": "post",
    "Title": "单独推送消息",
    "Desc": "单独推送消息",
    "Url": "http://xxx.xxx.xxx.xx",
    "InputArg": {
      "action": "44803",
      "account": "1865998xxxx",
      "uniqueid": "00D7C889-06A0-426E-BAB1-5741A1192038",
      "title": "测试测试",
      "summary": "豆豆豆",
      "message": "12345",
      "msgtype": "25",
      "menuid": "203"
    },
    "ExResult": {
      "errorno": "0"
    }
    },
    {
    "TestId": "0002",
    "Method": "post",
    "Title": "单独推送消息",
    "Desc": "单独推送消息",
    "Url": "http://xxx.xxx.xxx.xx",
    "InputArg": {
      "action": "44803",
      "account": "1865998xxxx",
      "uniqueid": "00D7C889-06A0-426E-BAB1-5741A1192038",
      "title": "测试测试",
      "summary": "豆豆豆",
      "message": "12345",
      "msgtype": "25",
      "menuid": "203"
    },
    "ExResult": {
      "errorno": "0"
    }
    },
    {
    "TestId": "0003",
    "Method": "post",
    "Title": "单独推送消息",
    "Desc": "单独推送消息",
    "Url": "http://xxx.xxx.xxx.xx",
    "InputArg": {
      "action": "44803",
      "account": "1865998xxxx",
      "uniqueid": "00D7C889-06A0-426E-BAB1-5741A1192038",
      "title": "测试测试",
      "summary": "豆豆豆",
      "message": "12345",
      "msgtype": "25",
      "menuid": "203"
    },
    "ExResult": {
      "errorno": "0",
      "title": "测试测试",
      "summary": "豆豆豆",
      "message": "12345",
      "msgtype": "25",
      "menuid": "203"
    }
    },
    ]
    return render(request,'index.html',{"cases":cases},{"user":username})
def report(request):
    results=[{"time":"2017-5-11"},{"time":"2017-5-10"},{"time":"2017-5-9"}]
    return render(request,'reportlist.html',{"lists":results})
def add(request):
    return render(request,'add.html')
def save_testcase(request):
    testcaseID = ''
    title = request.POST.get('title','')
    desc = request.POST.get('desc','')
    mothod = request.POST.get('mothod','')
    url = request.POST.get('url','')
    params = request.POST.get('params','')
    ex_result = request.POST.get('ex_result','')


