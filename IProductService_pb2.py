#coding= utf-8
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IProductService.proto

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
  name='IProductService.proto',
  package='app',
  syntax='proto3',
  serialized_pb=_b('\n\x15IProductService.proto\x12\x03\x61pp\x1a\x10\x61pp/Entity.proto\"X\n\x17GetProductPagingRequest\x12)\n\rrequestHeader\x18\x01 \x01(\x0b\x32\x12.app.RequestHeader\x12\x12\n\npageNumber\x18\x02 \x01(\x05\"\x97\x01\n\x18GetProductPagingResponse\x12+\n\x0eresponseHeader\x18\x01 \x01(\x0b\x32\x13.app.ResponseHeader\x12#\n\npagingInfo\x18\x02 \x01(\x0b\x32\x0f.app.PagingInfo\x12)\n\x0fproductInfoList\x18\x03 \x03(\x0b\x32\x10.app.ProductInfo\"W\n\x15GetProductInfoRequest\x12)\n\rrequestHeader\x18\x01 \x01(\x0b\x32\x12.app.RequestHeader\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\"\xde\x01\n\x16GetProductInfoResponse\x12+\n\x0eresponseHeader\x18\x01 \x01(\x0b\x32\x13.app.ResponseHeader\x12%\n\x0bproductInfo\x18\x02 \x01(\x0b\x32\x10.app.ProductInfo\x12\x35\n\x15productInvestInfoList\x18\x03 \x03(\x0b\x32\x16.app.ProductInvestInfo\x12\x39\n\x17productQuestionInfoList\x18\x04 \x03(\x0b\x32\x18.app.ProductQuestionInfo\"Y\n\x17SetProductRemindRequest\x12)\n\rrequestHeader\x18\x01 \x01(\x0b\x32\x12.app.RequestHeader\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\"G\n\x18SetProductRemindResponse\x12+\n\x0eresponseHeader\x18\x01 \x01(\x0b\x32\x13.app.ResponseHeader\"\\\n\x1a\x43\x61ncelProductRemindRequest\x12)\n\rrequestHeader\x18\x01 \x01(\x0b\x32\x12.app.RequestHeader\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\"J\n\x1b\x43\x61ncelProductRemindResponse\x12+\n\x0eresponseHeader\x18\x01 \x01(\x0b\x32\x13.app.ResponseHeader\"a\n\x1fGetExperienceProductInfoRequest\x12)\n\rrequestHeader\x18\x01 \x01(\x0b\x32\x12.app.RequestHeader\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\"\x8a\x01\n GetExperienceProductInfoResponse\x12+\n\x0eresponseHeader\x18\x01 \x01(\x0b\x32\x13.app.ResponseHeader\x12\x39\n\x15\x65xperienceProductInfo\x18\x02 \x01(\x0b\x32\x1a.app.ExperienceProductInfo\"]\n\x1bGetNewbieProductInfoRequest\x12)\n\rrequestHeader\x18\x01 \x01(\x0b\x32\x12.app.RequestHeader\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\"\xf0\x01\n\x1cGetNewbieProductInfoResponse\x12+\n\x0eresponseHeader\x18\x01 \x01(\x0b\x32\x13.app.ResponseHeader\x12\x31\n\x11newbieProductInfo\x18\x02 \x01(\x0b\x32\x16.app.NewbieProductInfo\x12\x35\n\x15productInvestInfoList\x18\x03 \x03(\x0b\x32\x16.app.ProductInvestInfo\x12\x39\n\x17productQuestionInfoList\x18\x04 \x03(\x0b\x32\x18.app.ProductQuestionInfo2\xaa\x04\n\x0fIProductService\x12Q\n\x10GetProductPaging\x12\x1c.app.GetProductPagingRequest\x1a\x1d.app.GetProductPagingResponse\"\x00\x12K\n\x0eGetProductInfo\x12\x1a.app.GetProductInfoRequest\x1a\x1b.app.GetProductInfoResponse\"\x00\x12Q\n\x10SetProductRemind\x12\x1c.app.SetProductRemindRequest\x1a\x1d.app.SetProductRemindResponse\"\x00\x12Z\n\x13\x43\x61ncelProductRemind\x12\x1f.app.CancelProductRemindRequest\x1a .app.CancelProductRemindResponse\"\x00\x12i\n\x18GetExperienceProductInfo\x12$.app.GetExperienceProductInfoRequest\x1a%.app.GetExperienceProductInfoResponse\"\x00\x12]\n\x14GetNewbieProductInfo\x12 .app.GetNewbieProductInfoRequest\x1a!.app.GetNewbieProductInfoResponse\"\x00\x42?\n%com.manqian.bao.grpc.api.protobuf.appB\x14IProductServiceProtoP\x01\x62\x06proto3')
  ,
  dependencies=[app_dot_Entity__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETPRODUCTPAGINGREQUEST = _descriptor.Descriptor(
  name='GetProductPagingRequest',
  full_name='app.GetProductPagingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestHeader', full_name='app.GetProductPagingRequest.requestHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pageNumber', full_name='app.GetProductPagingRequest.pageNumber', index=1,
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
  serialized_start=48,
  serialized_end=136,
)


_GETPRODUCTPAGINGRESPONSE = _descriptor.Descriptor(
  name='GetProductPagingResponse',
  full_name='app.GetProductPagingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responseHeader', full_name='app.GetProductPagingResponse.responseHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pagingInfo', full_name='app.GetProductPagingResponse.pagingInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productInfoList', full_name='app.GetProductPagingResponse.productInfoList', index=2,
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
  serialized_start=139,
  serialized_end=290,
)


_GETPRODUCTINFOREQUEST = _descriptor.Descriptor(
  name='GetProductInfoRequest',
  full_name='app.GetProductInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestHeader', full_name='app.GetProductInfoRequest.requestHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productCode', full_name='app.GetProductInfoRequest.productCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=292,
  serialized_end=379,
)


_GETPRODUCTINFORESPONSE = _descriptor.Descriptor(
  name='GetProductInfoResponse',
  full_name='app.GetProductInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responseHeader', full_name='app.GetProductInfoResponse.responseHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productInfo', full_name='app.GetProductInfoResponse.productInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productInvestInfoList', full_name='app.GetProductInfoResponse.productInvestInfoList', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productQuestionInfoList', full_name='app.GetProductInfoResponse.productQuestionInfoList', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=382,
  serialized_end=604,
)


_SETPRODUCTREMINDREQUEST = _descriptor.Descriptor(
  name='SetProductRemindRequest',
  full_name='app.SetProductRemindRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestHeader', full_name='app.SetProductRemindRequest.requestHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productCode', full_name='app.SetProductRemindRequest.productCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=606,
  serialized_end=695,
)


_SETPRODUCTREMINDRESPONSE = _descriptor.Descriptor(
  name='SetProductRemindResponse',
  full_name='app.SetProductRemindResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responseHeader', full_name='app.SetProductRemindResponse.responseHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=697,
  serialized_end=768,
)


_CANCELPRODUCTREMINDREQUEST = _descriptor.Descriptor(
  name='CancelProductRemindRequest',
  full_name='app.CancelProductRemindRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestHeader', full_name='app.CancelProductRemindRequest.requestHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productCode', full_name='app.CancelProductRemindRequest.productCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=770,
  serialized_end=862,
)


_CANCELPRODUCTREMINDRESPONSE = _descriptor.Descriptor(
  name='CancelProductRemindResponse',
  full_name='app.CancelProductRemindResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responseHeader', full_name='app.CancelProductRemindResponse.responseHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=864,
  serialized_end=938,
)


_GETEXPERIENCEPRODUCTINFOREQUEST = _descriptor.Descriptor(
  name='GetExperienceProductInfoRequest',
  full_name='app.GetExperienceProductInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestHeader', full_name='app.GetExperienceProductInfoRequest.requestHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productCode', full_name='app.GetExperienceProductInfoRequest.productCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=940,
  serialized_end=1037,
)


_GETEXPERIENCEPRODUCTINFORESPONSE = _descriptor.Descriptor(
  name='GetExperienceProductInfoResponse',
  full_name='app.GetExperienceProductInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responseHeader', full_name='app.GetExperienceProductInfoResponse.responseHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experienceProductInfo', full_name='app.GetExperienceProductInfoResponse.experienceProductInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1040,
  serialized_end=1178,
)


_GETNEWBIEPRODUCTINFOREQUEST = _descriptor.Descriptor(
  name='GetNewbieProductInfoRequest',
  full_name='app.GetNewbieProductInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestHeader', full_name='app.GetNewbieProductInfoRequest.requestHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productCode', full_name='app.GetNewbieProductInfoRequest.productCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1180,
  serialized_end=1273,
)


_GETNEWBIEPRODUCTINFORESPONSE = _descriptor.Descriptor(
  name='GetNewbieProductInfoResponse',
  full_name='app.GetNewbieProductInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responseHeader', full_name='app.GetNewbieProductInfoResponse.responseHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newbieProductInfo', full_name='app.GetNewbieProductInfoResponse.newbieProductInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productInvestInfoList', full_name='app.GetNewbieProductInfoResponse.productInvestInfoList', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productQuestionInfoList', full_name='app.GetNewbieProductInfoResponse.productQuestionInfoList', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=1276,
  serialized_end=1516,
)

_GETPRODUCTPAGINGREQUEST.fields_by_name['requestHeader'].message_type = app_dot_Entity__pb2._REQUESTHEADER
_GETPRODUCTPAGINGRESPONSE.fields_by_name['responseHeader'].message_type = app_dot_Entity__pb2._RESPONSEHEADER
_GETPRODUCTPAGINGRESPONSE.fields_by_name['pagingInfo'].message_type = app_dot_Entity__pb2._PAGINGINFO
_GETPRODUCTPAGINGRESPONSE.fields_by_name['productInfoList'].message_type = app_dot_Entity__pb2._PRODUCTINFO
_GETPRODUCTINFOREQUEST.fields_by_name['requestHeader'].message_type = app_dot_Entity__pb2._REQUESTHEADER
_GETPRODUCTINFORESPONSE.fields_by_name['responseHeader'].message_type = app_dot_Entity__pb2._RESPONSEHEADER
_GETPRODUCTINFORESPONSE.fields_by_name['productInfo'].message_type = app_dot_Entity__pb2._PRODUCTINFO
_GETPRODUCTINFORESPONSE.fields_by_name['productInvestInfoList'].message_type = app_dot_Entity__pb2._PRODUCTINVESTINFO
_GETPRODUCTINFORESPONSE.fields_by_name['productQuestionInfoList'].message_type = app_dot_Entity__pb2._PRODUCTQUESTIONINFO
_SETPRODUCTREMINDREQUEST.fields_by_name['requestHeader'].message_type = app_dot_Entity__pb2._REQUESTHEADER
_SETPRODUCTREMINDRESPONSE.fields_by_name['responseHeader'].message_type = app_dot_Entity__pb2._RESPONSEHEADER
_CANCELPRODUCTREMINDREQUEST.fields_by_name['requestHeader'].message_type = app_dot_Entity__pb2._REQUESTHEADER
_CANCELPRODUCTREMINDRESPONSE.fields_by_name['responseHeader'].message_type = app_dot_Entity__pb2._RESPONSEHEADER
_GETEXPERIENCEPRODUCTINFOREQUEST.fields_by_name['requestHeader'].message_type = app_dot_Entity__pb2._REQUESTHEADER
_GETEXPERIENCEPRODUCTINFORESPONSE.fields_by_name['responseHeader'].message_type = app_dot_Entity__pb2._RESPONSEHEADER
_GETEXPERIENCEPRODUCTINFORESPONSE.fields_by_name['experienceProductInfo'].message_type = app_dot_Entity__pb2._EXPERIENCEPRODUCTINFO
_GETNEWBIEPRODUCTINFOREQUEST.fields_by_name['requestHeader'].message_type = app_dot_Entity__pb2._REQUESTHEADER
_GETNEWBIEPRODUCTINFORESPONSE.fields_by_name['responseHeader'].message_type = app_dot_Entity__pb2._RESPONSEHEADER
_GETNEWBIEPRODUCTINFORESPONSE.fields_by_name['newbieProductInfo'].message_type = app_dot_Entity__pb2._NEWBIEPRODUCTINFO
_GETNEWBIEPRODUCTINFORESPONSE.fields_by_name['productInvestInfoList'].message_type = app_dot_Entity__pb2._PRODUCTINVESTINFO
_GETNEWBIEPRODUCTINFORESPONSE.fields_by_name['productQuestionInfoList'].message_type = app_dot_Entity__pb2._PRODUCTQUESTIONINFO
DESCRIPTOR.message_types_by_name['GetProductPagingRequest'] = _GETPRODUCTPAGINGREQUEST
DESCRIPTOR.message_types_by_name['GetProductPagingResponse'] = _GETPRODUCTPAGINGRESPONSE
DESCRIPTOR.message_types_by_name['GetProductInfoRequest'] = _GETPRODUCTINFOREQUEST
DESCRIPTOR.message_types_by_name['GetProductInfoResponse'] = _GETPRODUCTINFORESPONSE
DESCRIPTOR.message_types_by_name['SetProductRemindRequest'] = _SETPRODUCTREMINDREQUEST
DESCRIPTOR.message_types_by_name['SetProductRemindResponse'] = _SETPRODUCTREMINDRESPONSE
DESCRIPTOR.message_types_by_name['CancelProductRemindRequest'] = _CANCELPRODUCTREMINDREQUEST
DESCRIPTOR.message_types_by_name['CancelProductRemindResponse'] = _CANCELPRODUCTREMINDRESPONSE
DESCRIPTOR.message_types_by_name['GetExperienceProductInfoRequest'] = _GETEXPERIENCEPRODUCTINFOREQUEST
DESCRIPTOR.message_types_by_name['GetExperienceProductInfoResponse'] = _GETEXPERIENCEPRODUCTINFORESPONSE
DESCRIPTOR.message_types_by_name['GetNewbieProductInfoRequest'] = _GETNEWBIEPRODUCTINFOREQUEST
DESCRIPTOR.message_types_by_name['GetNewbieProductInfoResponse'] = _GETNEWBIEPRODUCTINFORESPONSE

GetProductPagingRequest = _reflection.GeneratedProtocolMessageType('GetProductPagingRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTPAGINGREQUEST,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.GetProductPagingRequest)
  ))
_sym_db.RegisterMessage(GetProductPagingRequest)

GetProductPagingResponse = _reflection.GeneratedProtocolMessageType('GetProductPagingResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTPAGINGRESPONSE,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.GetProductPagingResponse)
  ))
_sym_db.RegisterMessage(GetProductPagingResponse)

GetProductInfoRequest = _reflection.GeneratedProtocolMessageType('GetProductInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTINFOREQUEST,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.GetProductInfoRequest)
  ))
_sym_db.RegisterMessage(GetProductInfoRequest)

GetProductInfoResponse = _reflection.GeneratedProtocolMessageType('GetProductInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPRODUCTINFORESPONSE,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.GetProductInfoResponse)
  ))
_sym_db.RegisterMessage(GetProductInfoResponse)

SetProductRemindRequest = _reflection.GeneratedProtocolMessageType('SetProductRemindRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETPRODUCTREMINDREQUEST,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.SetProductRemindRequest)
  ))
_sym_db.RegisterMessage(SetProductRemindRequest)

SetProductRemindResponse = _reflection.GeneratedProtocolMessageType('SetProductRemindResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETPRODUCTREMINDRESPONSE,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.SetProductRemindResponse)
  ))
_sym_db.RegisterMessage(SetProductRemindResponse)

CancelProductRemindRequest = _reflection.GeneratedProtocolMessageType('CancelProductRemindRequest', (_message.Message,), dict(
  DESCRIPTOR = _CANCELPRODUCTREMINDREQUEST,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.CancelProductRemindRequest)
  ))
_sym_db.RegisterMessage(CancelProductRemindRequest)

CancelProductRemindResponse = _reflection.GeneratedProtocolMessageType('CancelProductRemindResponse', (_message.Message,), dict(
  DESCRIPTOR = _CANCELPRODUCTREMINDRESPONSE,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.CancelProductRemindResponse)
  ))
_sym_db.RegisterMessage(CancelProductRemindResponse)

GetExperienceProductInfoRequest = _reflection.GeneratedProtocolMessageType('GetExperienceProductInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETEXPERIENCEPRODUCTINFOREQUEST,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.GetExperienceProductInfoRequest)
  ))
_sym_db.RegisterMessage(GetExperienceProductInfoRequest)

GetExperienceProductInfoResponse = _reflection.GeneratedProtocolMessageType('GetExperienceProductInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETEXPERIENCEPRODUCTINFORESPONSE,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.GetExperienceProductInfoResponse)
  ))
_sym_db.RegisterMessage(GetExperienceProductInfoResponse)

GetNewbieProductInfoRequest = _reflection.GeneratedProtocolMessageType('GetNewbieProductInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETNEWBIEPRODUCTINFOREQUEST,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.GetNewbieProductInfoRequest)
  ))
_sym_db.RegisterMessage(GetNewbieProductInfoRequest)

GetNewbieProductInfoResponse = _reflection.GeneratedProtocolMessageType('GetNewbieProductInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETNEWBIEPRODUCTINFORESPONSE,
  __module__ = 'IProductService_pb2'
  # @@protoc_insertion_point(class_scope:app.GetNewbieProductInfoResponse)
  ))
_sym_db.RegisterMessage(GetNewbieProductInfoResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.manqian.bao.grpc.api.protobuf.appB\024IProductServiceProtoP\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


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
          request_serializer=GetProductPagingRequest.SerializeToString,
          response_deserializer=GetProductPagingResponse.FromString,
          )
      self.GetProductInfo = channel.unary_unary(
          '/app.IProductService/GetProductInfo',
          request_serializer=GetProductInfoRequest.SerializeToString,
          response_deserializer=GetProductInfoResponse.FromString,
          )
      self.SetProductRemind = channel.unary_unary(
          '/app.IProductService/SetProductRemind',
          request_serializer=SetProductRemindRequest.SerializeToString,
          response_deserializer=SetProductRemindResponse.FromString,
          )
      self.CancelProductRemind = channel.unary_unary(
          '/app.IProductService/CancelProductRemind',
          request_serializer=CancelProductRemindRequest.SerializeToString,
          response_deserializer=CancelProductRemindResponse.FromString,
          )
      self.GetExperienceProductInfo = channel.unary_unary(
          '/app.IProductService/GetExperienceProductInfo',
          request_serializer=GetExperienceProductInfoRequest.SerializeToString,
          response_deserializer=GetExperienceProductInfoResponse.FromString,
          )
      self.GetNewbieProductInfo = channel.unary_unary(
          '/app.IProductService/GetNewbieProductInfo',
          request_serializer=GetNewbieProductInfoRequest.SerializeToString,
          response_deserializer=GetNewbieProductInfoResponse.FromString,
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
            request_deserializer=GetProductPagingRequest.FromString,
            response_serializer=GetProductPagingResponse.SerializeToString,
        ),
        'GetProductInfo': grpc.unary_unary_rpc_method_handler(
            servicer.GetProductInfo,
            request_deserializer=GetProductInfoRequest.FromString,
            response_serializer=GetProductInfoResponse.SerializeToString,
        ),
        'SetProductRemind': grpc.unary_unary_rpc_method_handler(
            servicer.SetProductRemind,
            request_deserializer=SetProductRemindRequest.FromString,
            response_serializer=SetProductRemindResponse.SerializeToString,
        ),
        'CancelProductRemind': grpc.unary_unary_rpc_method_handler(
            servicer.CancelProductRemind,
            request_deserializer=CancelProductRemindRequest.FromString,
            response_serializer=CancelProductRemindResponse.SerializeToString,
        ),
        'GetExperienceProductInfo': grpc.unary_unary_rpc_method_handler(
            servicer.GetExperienceProductInfo,
            request_deserializer=GetExperienceProductInfoRequest.FromString,
            response_serializer=GetExperienceProductInfoResponse.SerializeToString,
        ),
        'GetNewbieProductInfo': grpc.unary_unary_rpc_method_handler(
            servicer.GetNewbieProductInfo,
            request_deserializer=GetNewbieProductInfoRequest.FromString,
            response_serializer=GetNewbieProductInfoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'app.IProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaIProductServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """慢钱宝app产品服务
    """
    def GetProductPaging(self, request, context):
      """获取慢钱宝产品列表
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetProductInfo(self, request, context):
      """获取产品详情
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SetProductRemind(self, request, context):
      """设置产品提醒
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def CancelProductRemind(self, request, context):
      """取消产品开售提醒
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetExperienceProductInfo(self, request, context):
      """体验标产品详情
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetNewbieProductInfo(self, request, context):
      """新手标产品详情
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaIProductServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """慢钱宝app产品服务
    """
    def GetProductPaging(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """获取慢钱宝产品列表
      """
      raise NotImplementedError()
    GetProductPaging.future = None
    def GetProductInfo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """获取产品详情
      """
      raise NotImplementedError()
    GetProductInfo.future = None
    def SetProductRemind(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """设置产品提醒
      """
      raise NotImplementedError()
    SetProductRemind.future = None
    def CancelProductRemind(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """取消产品开售提醒
      """
      raise NotImplementedError()
    CancelProductRemind.future = None
    def GetExperienceProductInfo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """体验标产品详情
      """
      raise NotImplementedError()
    GetExperienceProductInfo.future = None
    def GetNewbieProductInfo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """新手标产品详情
      """
      raise NotImplementedError()
    GetNewbieProductInfo.future = None


  def beta_create_IProductService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('app.IProductService', 'CancelProductRemind'): CancelProductRemindRequest.FromString,
      ('app.IProductService', 'GetExperienceProductInfo'): GetExperienceProductInfoRequest.FromString,
      ('app.IProductService', 'GetNewbieProductInfo'): GetNewbieProductInfoRequest.FromString,
      ('app.IProductService', 'GetProductInfo'): GetProductInfoRequest.FromString,
      ('app.IProductService', 'GetProductPaging'): GetProductPagingRequest.FromString,
      ('app.IProductService', 'SetProductRemind'): SetProductRemindRequest.FromString,
    }
    response_serializers = {
      ('app.IProductService', 'CancelProductRemind'): CancelProductRemindResponse.SerializeToString,
      ('app.IProductService', 'GetExperienceProductInfo'): GetExperienceProductInfoResponse.SerializeToString,
      ('app.IProductService', 'GetNewbieProductInfo'): GetNewbieProductInfoResponse.SerializeToString,
      ('app.IProductService', 'GetProductInfo'): GetProductInfoResponse.SerializeToString,
      ('app.IProductService', 'GetProductPaging'): GetProductPagingResponse.SerializeToString,
      ('app.IProductService', 'SetProductRemind'): SetProductRemindResponse.SerializeToString,
    }
    method_implementations = {
      ('app.IProductService', 'CancelProductRemind'): face_utilities.unary_unary_inline(servicer.CancelProductRemind),
      ('app.IProductService', 'GetExperienceProductInfo'): face_utilities.unary_unary_inline(servicer.GetExperienceProductInfo),
      ('app.IProductService', 'GetNewbieProductInfo'): face_utilities.unary_unary_inline(servicer.GetNewbieProductInfo),
      ('app.IProductService', 'GetProductInfo'): face_utilities.unary_unary_inline(servicer.GetProductInfo),
      ('app.IProductService', 'GetProductPaging'): face_utilities.unary_unary_inline(servicer.GetProductPaging),
      ('app.IProductService', 'SetProductRemind'): face_utilities.unary_unary_inline(servicer.SetProductRemind),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_IProductService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('app.IProductService', 'CancelProductRemind'): CancelProductRemindRequest.SerializeToString,
      ('app.IProductService', 'GetExperienceProductInfo'): GetExperienceProductInfoRequest.SerializeToString,
      ('app.IProductService', 'GetNewbieProductInfo'): GetNewbieProductInfoRequest.SerializeToString,
      ('app.IProductService', 'GetProductInfo'): GetProductInfoRequest.SerializeToString,
      ('app.IProductService', 'GetProductPaging'): GetProductPagingRequest.SerializeToString,
      ('app.IProductService', 'SetProductRemind'): SetProductRemindRequest.SerializeToString,
    }
    response_deserializers = {
      ('app.IProductService', 'CancelProductRemind'): CancelProductRemindResponse.FromString,
      ('app.IProductService', 'GetExperienceProductInfo'): GetExperienceProductInfoResponse.FromString,
      ('app.IProductService', 'GetNewbieProductInfo'): GetNewbieProductInfoResponse.FromString,
      ('app.IProductService', 'GetProductInfo'): GetProductInfoResponse.FromString,
      ('app.IProductService', 'GetProductPaging'): GetProductPagingResponse.FromString,
      ('app.IProductService', 'SetProductRemind'): SetProductRemindResponse.FromString,
    }
    cardinalities = {
      'CancelProductRemind': cardinality.Cardinality.UNARY_UNARY,
      'GetExperienceProductInfo': cardinality.Cardinality.UNARY_UNARY,
      'GetNewbieProductInfo': cardinality.Cardinality.UNARY_UNARY,
      'GetProductInfo': cardinality.Cardinality.UNARY_UNARY,
      'GetProductPaging': cardinality.Cardinality.UNARY_UNARY,
      'SetProductRemind': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'app.IProductService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)