#coding= utf-8
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import IAppVersionService_pb2 as IAppVersionService__pb2


class IAppVersionServiceStub(object):
  """慢钱宝app版本服务
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetNewVersion = channel.unary_unary(
        '/app.IAppVersionService/GetNewVersion',
        request_serializer=IAppVersionService__pb2.GetNewVersionRequest.SerializeToString,
        response_deserializer=IAppVersionService__pb2.GetNewVersionResponse.FromString,
        )


class IAppVersionServiceServicer(object):
  """慢钱宝app版本服务
  """

  def GetNewVersion(self, request, context):
    """获取app最新版本
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IAppVersionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetNewVersion': grpc.unary_unary_rpc_method_handler(
          servicer.GetNewVersion,
          request_deserializer=IAppVersionService__pb2.GetNewVersionRequest.FromString,
          response_serializer=IAppVersionService__pb2.GetNewVersionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'app.IAppVersionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
