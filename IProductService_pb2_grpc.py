#coding= utf-8
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import IProductService_pb2 as IProductService__pb2


class IProductServiceStub(object):
  """慢钱宝app产品服务
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetProductPaging = channel.unary_unary(
        '/app.IProductService/GetProductPaging',
        request_serializer=IProductService__pb2.GetProductPagingRequest.SerializeToString,
        response_deserializer=IProductService__pb2.GetProductPagingResponse.FromString,
        )
    self.GetProductInfo = channel.unary_unary(
        '/app.IProductService/GetProductInfo',
        request_serializer=IProductService__pb2.GetProductInfoRequest.SerializeToString,
        response_deserializer=IProductService__pb2.GetProductInfoResponse.FromString,
        )
    self.SetProductRemind = channel.unary_unary(
        '/app.IProductService/SetProductRemind',
        request_serializer=IProductService__pb2.SetProductRemindRequest.SerializeToString,
        response_deserializer=IProductService__pb2.SetProductRemindResponse.FromString,
        )
    self.CancelProductRemind = channel.unary_unary(
        '/app.IProductService/CancelProductRemind',
        request_serializer=IProductService__pb2.CancelProductRemindRequest.SerializeToString,
        response_deserializer=IProductService__pb2.CancelProductRemindResponse.FromString,
        )
    self.GetExperienceProductInfo = channel.unary_unary(
        '/app.IProductService/GetExperienceProductInfo',
        request_serializer=IProductService__pb2.GetExperienceProductInfoRequest.SerializeToString,
        response_deserializer=IProductService__pb2.GetExperienceProductInfoResponse.FromString,
        )
    self.GetNewbieProductInfo = channel.unary_unary(
        '/app.IProductService/GetNewbieProductInfo',
        request_serializer=IProductService__pb2.GetNewbieProductInfoRequest.SerializeToString,
        response_deserializer=IProductService__pb2.GetNewbieProductInfoResponse.FromString,
        )


class IProductServiceServicer(object):
  """慢钱宝app产品服务
  """

  def GetProductPaging(self, request, context):
    """获取慢钱宝产品列表
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProductInfo(self, request, context):
    """获取产品详情
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetProductRemind(self, request, context):
    """设置产品提醒
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelProductRemind(self, request, context):
    """取消产品开售提醒
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetExperienceProductInfo(self, request, context):
    """体验标产品详情
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNewbieProductInfo(self, request, context):
    """新手标产品详情
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IProductServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetProductPaging': grpc.unary_unary_rpc_method_handler(
          servicer.GetProductPaging,
          request_deserializer=IProductService__pb2.GetProductPagingRequest.FromString,
          response_serializer=IProductService__pb2.GetProductPagingResponse.SerializeToString,
      ),
      'GetProductInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetProductInfo,
          request_deserializer=IProductService__pb2.GetProductInfoRequest.FromString,
          response_serializer=IProductService__pb2.GetProductInfoResponse.SerializeToString,
      ),
      'SetProductRemind': grpc.unary_unary_rpc_method_handler(
          servicer.SetProductRemind,
          request_deserializer=IProductService__pb2.SetProductRemindRequest.FromString,
          response_serializer=IProductService__pb2.SetProductRemindResponse.SerializeToString,
      ),
      'CancelProductRemind': grpc.unary_unary_rpc_method_handler(
          servicer.CancelProductRemind,
          request_deserializer=IProductService__pb2.CancelProductRemindRequest.FromString,
          response_serializer=IProductService__pb2.CancelProductRemindResponse.SerializeToString,
      ),
      'GetExperienceProductInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetExperienceProductInfo,
          request_deserializer=IProductService__pb2.GetExperienceProductInfoRequest.FromString,
          response_serializer=IProductService__pb2.GetExperienceProductInfoResponse.SerializeToString,
      ),
      'GetNewbieProductInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetNewbieProductInfo,
          request_deserializer=IProductService__pb2.GetNewbieProductInfoRequest.FromString,
          response_serializer=IProductService__pb2.GetNewbieProductInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'app.IProductService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))