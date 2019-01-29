""" Utils related to protobuf """
import sys
from pathlib import Path
import os
from google.protobuf import json_format


def import_protobuf_from_dir_get_all(proto_dir):
    proto_dir = Path(proto_dir)
    # <SERVICE>_pb2_grpc.py import <SERVICE>_pb2.py so we are forced to add proto_dir to path
    sys.path.append(str(proto_dir))    
    grpc_pyfiles = [str(os.path.basename(p)) for p in proto_dir.glob("*_pb2_grpc.py")]
    
    all_rez = {}
    for grpc_pyfile in grpc_pyfiles:
        rez = _import_protobuf_from_file_get_all(grpc_pyfile);
        all_rez = {**all_rez, **rez}        
    return all_rez

def _import_protobuf_from_file_get_all(grpc_pyfile):
    
    prefix = grpc_pyfile[:-12]
    pb2      = __import__("%s_pb2"%prefix)
    pb2_grpc = __import__("%s_pb2_grpc"%prefix) 
    
    
    # we take all objects from pb2_grpc module which endswith "Stub", and we remove this postfix to get service_name
    all_service_names = [stub_name[:-4] for stub_name in dir(pb2_grpc) if stub_name.endswith("Stub")]
    
    rez = { s:[] for s in all_service_names}
    
    for service_name in all_service_names:
        service_descriptor =  getattr(pb2, "DESCRIPTOR").services_by_name[service_name]
        for method in service_descriptor.methods:
            request_class      = getattr(pb2, method.input_type.name)
            response_class     = getattr(pb2, method.output_type.name)
            stub_class         = getattr(pb2_grpc, "%sStub"%service_name)                                                            
            rez[service_name].append({"name": method.name, "request_class":request_class, "response_class": response_class, "stub_class" : stub_class})
    return rez
