#coding= utf-8
import grpc
class GrpcUtil(object):
    pb2File = ''
    grpcFile = ''
    stub = ''
    serverName =''
    stubObject = object
    def __init__(self,ip,serverName):
        self.serverName = serverName
        self.grpcFile = serverName + '_pb2_grpc'
        self.pb2File = self.serverName +'_pb2'
        self.stub = serverName + 'Stub'
        channel = grpc.insecure_channel(ip)
        file = __import__(self.grpcFile)
        p = getattr(file,self.stub)
        self.stubObject = p(channel)

    def requestBody(self,reuqestName,context):
        pb2file = __import__(self.pb2File)
        requset = getattr(pb2file,reuqestName)
        #重点了解包裹与解包裹的概念
        body = requset(**context)
        return body

#返回response
    def getResponse(self,func,reuqestName,context):
        requset = getattr(self.stubObject,func)
        boby = self.requestBody(reuqestName,context)
        response = requset(boby)
        if response.responseHeader.msg == '':
            return str(response)
        else:
            return response.responseHeader.msg


#调用登录接口获取用户sessionID和platformId
    def login(self,context):
        response= self.getResponse("login","loginRequest",context)
        return response.UserInfo.platformUserId,response.sessionId

'''
a = GrpcUtil("baogrpc.devmq.top:24000","IUserService")
a.setSession("Login","LoginRequest",{"mobile":"18507097209","password":"E10ADC3949BA59ABBE56E057F20F883E"})
'''
