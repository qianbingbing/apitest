#coding= utf-8
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IActivityService.proto
import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from app import Entity_pb2 as app_dot_Entity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='IActivityService.proto',
  package='app',
  syntax='proto3',
  serialized_pb=_b('\n\x16IActivityService.proto\x12\x03\x61pp\x1a\x10\x61pp/Entity.proto\"Y\n\x18GetActivityPagingRequest\x12)\n\rrequestHeader\x18\x01 \x01(\x0b\x32\x12.app.RequestHeader\x12\x12\n\npageNumber\x18\x02 \x01(\x05\"\x9a\x01\n\x19GetActivityPagingResponse\x12+\n\x0eresponseHeader\x18\x01 \x01(\x0b\x32\x13.app.ResponseHeader\x12#\n\npagingInfo\x18\x02 \x01(\x0b\x32\x0f.app.PagingInfo\x12+\n\x10\x61\x63tivityInfoList\x18\x03 \x03(\x0b\x32\x11.app.ActivityInfo2h\n\x10IActivityService\x12T\n\x11GetActivityPaging\x12\x1d.app.GetActivityPagingRequest\x1a\x1e.app.GetActivityPagingResponse\"\x00\x42@\n%com.manqian.bao.grpc.api.protobuf.appB\x15IActivityServiceProtoP\x01\x62\x06proto3')
  ,
  dependencies=[app_dot_Entity__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETACTIVITYPAGINGREQUEST = _descriptor.Descriptor(
  name='GetActivityPagingRequest',
  full_name='app.GetActivityPagingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestHeader', full_name='app.GetActivityPagingRequest.requestHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pageNumber', full_name='app.GetActivityPagingRequest.pageNumber', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=138,
)


_GETACTIVITYPAGINGRESPONSE = _descriptor.Descriptor(
  name='GetActivityPagingResponse',
  full_name='app.GetActivityPagingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responseHeader', full_name='app.GetActivityPagingResponse.responseHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pagingInfo', full_name='app.GetActivityPagingResponse.pagingInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activityInfoList', full_name='app.GetActivityPagingResponse.activityInfoList', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=295,
)

_GETACTIVITYPAGINGREQUEST.fields_by_name['requestHeader'].message_type = app_dot_Entity__pb2._REQUESTHEADER
_GETACTIVITYPAGINGRESPONSE.fields_by_name['responseHeader'].message_type = app_dot_Entity__pb2._RESPONSEHEADER
_GETACTIVITYPAGINGRESPONSE.fields_by_name['pagingInfo'].message_type = app_dot_Entity__pb2._PAGINGINFO
_GETACTIVITYPAGINGRESPONSE.fields_by_name['activityInfoList'].message_type = app_dot_Entity__pb2._ACTIVITYINFO
DESCRIPTOR.message_types_by_name['GetActivityPagingRequest'] = _GETACTIVITYPAGINGREQUEST
DESCRIPTOR.message_types_by_name['GetActivityPagingResponse'] = _GETACTIVITYPAGINGRESPONSE

GetActivityPagingRequest = _reflection.GeneratedProtocolMessageType('GetActivityPagingRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETACTIVITYPAGINGREQUEST,
  __module__ = 'IActivityService_pb2'
  # @@protoc_insertion_point(class_scope:app.GetActivityPagingRequest)
  ))
_sym_db.RegisterMessage(GetActivityPagingRequest)

GetActivityPagingResponse = _reflection.GeneratedProtocolMessageType('GetActivityPagingResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETACTIVITYPAGINGRESPONSE,
  __module__ = 'IActivityService_pb2'
  # @@protoc_insertion_point(class_scope:app.GetActivityPagingResponse)
  ))
_sym_db.RegisterMessage(GetActivityPagingResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.manqian.bao.grpc.api.protobuf.appB\025IActivityServiceProtoP\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class IActivityServiceStub(object):
    """慢钱宝app精彩活动服务api
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetActivityPaging = channel.unary_unary(
          '/app.IActivityService/GetActivityPaging',
          request_serializer=GetActivityPagingRequest.SerializeToString,
          response_deserializer=GetActivityPagingResponse.FromString,
          )


  class IActivityServiceServicer(object):
    """慢钱宝app精彩活动服务api
    """

    def GetActivityPaging(self, request, context):
      """分页获取精彩活动
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_IActivityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetActivityPaging': grpc.unary_unary_rpc_method_handler(
            servicer.GetActivityPaging,
            request_deserializer=GetActivityPagingRequest.FromString,
            response_serializer=GetActivityPagingResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'app.IActivityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaIActivityServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """慢钱宝app精彩活动服务api
    """
    def GetActivityPaging(self, request, context):
      """分页获取精彩活动
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaIActivityServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """慢钱宝app精彩活动服务api
    """
    def GetActivityPaging(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """分页获取精彩活动
      """
      raise NotImplementedError()
    GetActivityPaging.future = None


  def beta_create_IActivityService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('app.IActivityService', 'GetActivityPaging'): GetActivityPagingRequest.FromString,
    }
    response_serializers = {
      ('app.IActivityService', 'GetActivityPaging'): GetActivityPagingResponse.SerializeToString,
    }
    method_implementations = {
      ('app.IActivityService', 'GetActivityPaging'): face_utilities.unary_unary_inline(servicer.GetActivityPaging),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_IActivityService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('app.IActivityService', 'GetActivityPaging'): GetActivityPagingRequest.SerializeToString,
    }
    response_deserializers = {
      ('app.IActivityService', 'GetActivityPaging'): GetActivityPagingResponse.FromString,
    }
    cardinalities = {
      'GetActivityPaging': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'app.IActivityService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
