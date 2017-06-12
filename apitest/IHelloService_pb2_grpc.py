#coding= utf-8
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import IHelloService_pb2 as IHelloService__pb2


class IHelloServiceStub(object):
  """活动服务
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.findHello = channel.unary_unary(
        '/com.manqian.yunke.grpc.demo.api.proto.IHelloService/findHello',
        request_serializer=IHelloService__pb2.FindHelloRequest.SerializeToString,
        response_deserializer=IHelloService__pb2.FindHelloResponse.FromString,
        )


class IHelloServiceServicer(object):
  """活动服务
  """

  def findHello(self, request, context):
    """查询Hello
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IHelloServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'findHello': grpc.unary_unary_rpc_method_handler(
          servicer.findHello,
          request_deserializer=IHelloService__pb2.FindHelloRequest.FromString,
          response_serializer=IHelloService__pb2.FindHelloResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.manqian.yunke.grpc.demo.api.proto.IHelloService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))