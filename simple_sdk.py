from snet_cli.mpe_client_command import MPEClientCommand
from snet_cli.config import Config
from snet_cli.utils import DefaultAttributeObject
from utils_proto4sdk import import_protobuf_from_dir_get_all
import types

def get_service_stub(channel_id, price, endpoint, service = ""):
    conf   = Config()
    client = MPEClientCommand(conf, DefaultAttributeObject(channel_id = 0))    
    all_services = import_protobuf_from_dir_get_all(client.get_channel_dir())
    if (len(all_services) == 1):
        service = list(all_services.values())[0]
    else:
        service = all_services[service]
        
    class service_stub:
        pass

    stub = service_stub()
    stub.conf   = conf
    stub.client = client
    
    for method in service:
        
        method_name = method["name"]
        arg1 = "channel_id = %i, price = %i, endpoint = '%s', method = '%s'"%(channel_id, price, endpoint, method_name)
        code = """
def stub_method(self, request): 
    args   = DefaultAttributeObject(%s)
    client = MPEClientCommand(self.conf, args)
    rez    = client.call_server_statelessly_with_params(request.__dict__)
    return rez
stub.%s = types.MethodType(stub_method, stub)
        """%(arg1, method_name)
        exec(code)
    return stub
