from concurrent import futures
import grpc
import id_generator_pb2
import id_generator_pb2_grpc
from snowflake import SnowflakeGenerator

class IDGeneratorServicer(id_generator_pb2_grpc.IDGeneratorServicer):
    EPOCH = 1702379129
    
    def Generate(self, request, context):
        generator = SnowflakeGenerator(request.instance, epoch=self.EPOCH)
        new_id = next(generator)
        return id_generator_pb2.GenerateResponse(id=str(new_id))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    id_generator_pb2_grpc.add_IDGeneratorServicer_to_server(IDGeneratorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
