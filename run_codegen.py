#coding:utf-8
from grpc_tools import protoc
protoc.main(
    (
        '.',
        '-I./protos',
        '--python_out=./python/',
        '--grpc_python_out=./python/',
        './protos/IUserService.proto',
        './protos/IActivityService.proto',
        './protos/IAppVersionService.proto',
        './protos/ICouponRecordService.proto',
        './protos/IMessageService.proto',
        './protos/IOrderService.proto',
        './protos/IProductService.proto',
        './protos/IIndexService.proto',
    )
)
