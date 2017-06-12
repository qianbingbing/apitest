#coding= 'utf-8'
import grpc



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
    #exec "import %s,%s"%('IHelloService_pb2','IHelloService_pb2_grpc')
    set_impfile()
    channel = set_channle(serverhost)
    str = "stub = %s.%s(channel)"%(server_grpc,serverstub)
    exec str
    return stub




def run(str):
    #exec "import %s,%s"%('IHelloService_pb2','IHelloService_pb2_grpc')
    set_impfile()
    response = object
    exec(str)
    print response
    return response



if __name__ == '__main__':
    #import IHelloService_pb2,IHelloService_pb2_grpc
    #loadapp('IHelloService_pb2')
    #loadapp('IHelloService_pb2_grpc')
    exec "import %s,%s"%('IHelloService_pb2','IHelloService_pb2_grpc')
    stub = stub_gen('120.132.54.79:8001','IHelloService_pb2_grpc','IHelloServiceStub')
    run("response = stub.findHello(IHelloService_pb2.FindHelloRequest(msg='this is test hello'))")