#coding= utf-8
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
import IUserService_pb2 as IUserService__pb2
class IUserServiceStub(object):
  """慢钱宝app用户服务
  """
  def __init__(self, channel):
    """Constructor.
    Args:
      channel: A grpc.Channel.

    """
    self.Login = channel.unary_unary(
        '/app.IUserService/Login',
        request_serializer=IUserService__pb2.LoginRequest.SerializeToString,
        response_deserializer=IUserService__pb2.LoginResponse.FromString,
        )
    self.SendRegistMessageCode = channel.unary_unary(
        '/app.IUserService/SendRegistMessageCode',
        request_serializer=IUserService__pb2.SendRegistMessageCodeRequest.SerializeToString,
        response_deserializer=IUserService__pb2.SendRegistMessageCodeResponse.FromString,
        )
    self.Regist = channel.unary_unary(
        '/app.IUserService/Regist',
        request_serializer=IUserService__pb2.RegistRequest.SerializeToString,
        response_deserializer=IUserService__pb2.RegistResponse.FromString,
        )
    self.GetUserAccountInfo = channel.unary_unary(
        '/app.IUserService/GetUserAccountInfo',
        request_serializer=IUserService__pb2.GetUserAccountInfoRequest.SerializeToString,
        response_deserializer=IUserService__pb2.GetUserAccountInfoResponse.FromString,
        )
    self.SendResetPasswordMessageCode = channel.unary_unary(
        '/app.IUserService/SendResetPasswordMessageCode',
        request_serializer=IUserService__pb2.SendResetPasswordMessageCodeRequest.SerializeToString,
        response_deserializer=IUserService__pb2.SendResetPasswordMessageCodeResponse.FromString,
        )
    self.ResetLoginPassword = channel.unary_unary(
        '/app.IUserService/ResetLoginPassword',
        request_serializer=IUserService__pb2.ResetLoginPasswordRequest.SerializeToString,
        response_deserializer=IUserService__pb2.ResetLoginPasswordResponse.FromString,
        )
    self.CheckPassword = channel.unary_unary(
        '/app.IUserService/CheckPassword',
        request_serializer=IUserService__pb2.CheckPasswordRequest.SerializeToString,
        response_deserializer=IUserService__pb2.CheckPasswordResponse.FromString,
        )
    self.GetUserAssetDetailPaging = channel.unary_unary(
        '/app.IUserService/GetUserAssetDetailPaging',
        request_serializer=IUserService__pb2.GetUserAssetDetailPagingRequest.SerializeToString,
        response_deserializer=IUserService__pb2.GetUserAssetDetailPagingResponse.FromString,
        )


class IUserServiceServicer(object):
  """慢钱宝app用户服务
  """

  def Login(self, request, context):
    """登录
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendRegistMessageCode(self, request, context):
    """发送注册验证码
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Regist(self, request, context):
    """注册
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUserAccountInfo(self, request, context):
    """获取当前用户的账户信息
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendResetPasswordMessageCode(self, request, context):
    """发送重置登录密码的短信验证码
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetLoginPassword(self, request, context):
    """重置登录密码
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckPassword(self, request, context):
    """验证密码（修改手势密码时 验证密码）
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUserAssetDetailPaging(self, request, context):
    """资金明细
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IUserServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Login': grpc.unary_unary_rpc_method_handler(
          servicer.Login,
          request_deserializer=IUserService__pb2.LoginRequest.FromString,
          response_serializer=IUserService__pb2.LoginResponse.SerializeToString,
      ),
      'SendRegistMessageCode': grpc.unary_unary_rpc_method_handler(
          servicer.SendRegistMessageCode,
          request_deserializer=IUserService__pb2.SendRegistMessageCodeRequest.FromString,
          response_serializer=IUserService__pb2.SendRegistMessageCodeResponse.SerializeToString,
      ),
      'Regist': grpc.unary_unary_rpc_method_handler(
          servicer.Regist,
          request_deserializer=IUserService__pb2.RegistRequest.FromString,
          response_serializer=IUserService__pb2.RegistResponse.SerializeToString,
      ),
      'GetUserAccountInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserAccountInfo,
          request_deserializer=IUserService__pb2.GetUserAccountInfoRequest.FromString,
          response_serializer=IUserService__pb2.GetUserAccountInfoResponse.SerializeToString,
      ),
      'SendResetPasswordMessageCode': grpc.unary_unary_rpc_method_handler(
          servicer.SendResetPasswordMessageCode,
          request_deserializer=IUserService__pb2.SendResetPasswordMessageCodeRequest.FromString,
          response_serializer=IUserService__pb2.SendResetPasswordMessageCodeResponse.SerializeToString,
      ),
      'ResetLoginPassword': grpc.unary_unary_rpc_method_handler(
          servicer.ResetLoginPassword,
          request_deserializer=IUserService__pb2.ResetLoginPasswordRequest.FromString,
          response_serializer=IUserService__pb2.ResetLoginPasswordResponse.SerializeToString,
      ),
      'CheckPassword': grpc.unary_unary_rpc_method_handler(
          servicer.CheckPassword,
          request_deserializer=IUserService__pb2.CheckPasswordRequest.FromString,
          response_serializer=IUserService__pb2.CheckPasswordResponse.SerializeToString,
      ),
      'GetUserAssetDetailPaging': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserAssetDetailPaging,
          request_deserializer=IUserService__pb2.GetUserAssetDetailPagingRequest.FromString,
          response_serializer=IUserService__pb2.GetUserAssetDetailPagingResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'app.IUserService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
