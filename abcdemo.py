import grpc
import IUserService_pb2,IUserService_pb2_grpc
channel = grpc.insecure_channel('baogrpc.devmq.top:24000')
stub = IUserService_pb2_grpc.IUserServiceStub(channel)
request = IUserService_pb2.LoginRequest(mobile='18507097209')
response = stub.Login(request)



print response
