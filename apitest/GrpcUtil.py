#coding= 'utf-8'
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

    def getResponse(self,func,reuqestName,context):
        requset = getattr(self.stubObject,func)
        boby = self.requestBody(reuqestName,context)
        print requset(boby)
        return requset(boby)

'''
a = GrpcUtil("120.132.54.79:8001","IHelloService")
a.getResponse("findHello","FindHelloRequest",{"msg":"1234"})
'''


