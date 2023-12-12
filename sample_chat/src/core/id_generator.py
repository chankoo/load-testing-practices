import grpc
from . import id_generator_pb2
from . import id_generator_pb2_grpc

from src.config import settings


async def get_snowflake_id(instance: int = 1) -> int:
    with grpc.insecure_channel(f'{settings.id_generator_host}:{settings.grpc_port}') as channel:
        stub = id_generator_pb2_grpc.IDGeneratorStub(channel)
        request = id_generator_pb2.GenerateRequest(instance=instance)
        response = stub.Generate(request)
        return response.id
