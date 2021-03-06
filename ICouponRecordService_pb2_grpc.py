#coding= utf-8
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ICouponRecordService_pb2 as ICouponRecordService__pb2


class ICouponRecordShowServiceStub(object):
  """慢钱宝app精彩服务api
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getCouponRecordById = channel.unary_unary(
        '/app.ICouponRecordShowService/getCouponRecordById',
        request_serializer=ICouponRecordService__pb2.GetCouponRecordShowInfoByIdRequest.SerializeToString,
        response_deserializer=ICouponRecordService__pb2.CouponRecordShowInfoResponse.FromString,
        )
    self.getCouponRecordByUserIdAndExpiredPaging = channel.unary_unary(
        '/app.ICouponRecordShowService/getCouponRecordByUserIdAndExpiredPaging',
        request_serializer=ICouponRecordService__pb2.GetCouponRecordShowInfoByUserIdAndExpiredPagingRequest.SerializeToString,
        response_deserializer=ICouponRecordService__pb2.GetCouponRecordShowInfoByUserIdAndExpiredPagingResponse.FromString,
        )


class ICouponRecordShowServiceServicer(object):
  """慢钱宝app精彩服务api
  """

  def getCouponRecordById(self, request, context):
    """getCouponRecordById
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getCouponRecordByUserIdAndExpiredPaging(self, request, context):
    """根据用户id和是否失效以及类型获取优惠券记录页
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ICouponRecordShowServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getCouponRecordById': grpc.unary_unary_rpc_method_handler(
          servicer.getCouponRecordById,
          request_deserializer=ICouponRecordService__pb2.GetCouponRecordShowInfoByIdRequest.FromString,
          response_serializer=ICouponRecordService__pb2.CouponRecordShowInfoResponse.SerializeToString,
      ),
      'getCouponRecordByUserIdAndExpiredPaging': grpc.unary_unary_rpc_method_handler(
          servicer.getCouponRecordByUserIdAndExpiredPaging,
          request_deserializer=ICouponRecordService__pb2.GetCouponRecordShowInfoByUserIdAndExpiredPagingRequest.FromString,
          response_serializer=ICouponRecordService__pb2.GetCouponRecordShowInfoByUserIdAndExpiredPagingResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'app.ICouponRecordShowService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
