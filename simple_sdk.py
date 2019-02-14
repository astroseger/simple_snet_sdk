from snet_cli.mpe_client_command import MPEClientCommand
from snet_cli.config import Config
from snet_cli.utils import DefaultAttributeObject
from snet_cli.utils_proto import import_protobuf_from_dir
from utils_proto4sdk import import_protobuf_get_all_method_names
import types
from google.protobuf.json_format import MessageToDict


def get_service_stub_for_call_statelessly(org_id, service_id, service_name = ""):
    conf   = Config()
    client = MPEClientCommand(conf, {})
    all_method_names = import_protobuf_get_all_method_names(client.get_service_spec_dir(org_id, service_id), service_name = service_name)
    
    class service_stub:
        pass
    
    stub = service_stub()
    stub.conf   = conf
    stub.client = client
    
    for method_name in all_method_names:
        
        arg1 = "org_id = '%s', service_id = '%s', method = '%s', service_name= '%s', yes = True"%(org_id, service_id, method_name, service_name)
        code = """
def stub_method(self, request): 
    args   = DefaultAttributeObject(%s)
    client = MPEClientCommand(self.conf, args)
    rez    = client.call_server_statelessly_with_params(MessageToDict(request))
    return rez
stub.%s = types.MethodType(stub_method, stub)
        """%(arg1, method_name)
        exec(code)
    return stub

def get_request_class(org_id, service_id, method_name, service_name = ""):
    conf   = Config()
    client = MPEClientCommand(conf, {})
    _, request_class, _ = import_protobuf_from_dir(client.get_service_spec_dir(org_id, service_id), method_name, service_name = service_name)
    return request_class
            
