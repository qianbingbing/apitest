#coding= 'utf-8'
import grpc

'''
channel = grpc.insecure_channel('120.132.54.79:8001')
grpcfile = __import__("IHelloService_pb2_grpc")
p = getattr(grpcfile,"IHelloServiceStub")
stub =  p(channel)
pb2file = __import__("IHelloService_pb2")
requset = getattr(pb2file,"FindHelloRequest")
start = requset(msg='this is test hello')
stub.findHello(start)
print stub.findHello(start)
'''


class demo(object):
    pb2file = ''
    grpcfile = ''
    stub = ''
    servername =''
    def getStub(self,ip,serverName):
        self.servername = serverName
        self.grpcfile = serverName + '_pb2_grpc'
        self.stub = serverName + 'Stub'
        channel = grpc.insecure_channel(ip)
        file = __import__(self.grpcfile)
        p = getattr(file,self.stub)
        stub =  p(channel)
        return stub

    def getRequest(self,Requsetclass):
        pb2file = self.servername +'_pb2'
        pb2file = __import__(pb2file)
        requset = getattr(pb2file,Requsetclass)
        start = requset(msg='this is hello')
        return start

    def runRequset(self,Requstname):
        stub = self.getStub("120.132.54.79:8001","IHelloService")
        context = self.getRequest("FindHelloRequest")
        requset = getattr(stub,Requstname)
        print requset(context)
        return requset(context)




demo().runRequset('findHello')


'''
stub = getStub("120.132.54.79:8001","IHelloService_pb2_grpc","IHelloServiceStub")
context = getRequest("IHelloService_pb2","FindHelloRequest")
print stub.findHello(context)
'''









'''
def set_impfile():
    #fileName2 = fileName1+"_grpc"
    #print fileName1,fileName2
    #exec "import %s,%s"%(fileName1,fileName2)
    exec "import %s,%s"%('IHelloService_pb2','IHelloService_pb2_grpc')
    #return

def set_channle(serverhost):
    channel = grpc.insecure_channel(serverhost)
    return channel


def stub_gen(serverhost,server_grpc,serverstub):
    stub = object
    channel = set_channle(serverhost)
    str = "stub = %s.%s(channel)"%(server_grpc,serverstub)
    exec str
    return stub


def get_Response(str):
    response = object
    stub = stub_gen('120.132.54.79:8001','IHelloService_pb2_grpc','IHelloServiceStub')
    exec(str)
    print response
    return response

def run():
    stub = stub_gen('120.132.54.79:8001','IHelloService_pb2_grpc','IHelloServiceStub')
    get_Response("response = stub.findHello(IHelloService_pb2.FindHelloRequest(msg='this is test hello'))")




class Grpc(object):
    def __init__(self,serverhost,server_grpc,serverstub):

        stub_gen(serverhost,server_grpc,serverstub)


    def get_response(self):
        get_Response()

if __name__ == '__main__':
    #import IHelloService_pb2,IHelloService_pb2_grpc
    #loadapp('IHelloService_pb2')
    #loadapp('IHelloService_pb2_grpc')
    exec "import %s,%s"%('IHelloService_pb2','IHelloService_pb2_grpc')
    run()
'''
