from simple_sdk import get_service_stub_for_call_statelessly, get_request_class
from snet_cli.utils import DefaultAttributeObject
from google.protobuf.json_format import MessageToDict    

stub = get_service_stub_for_call_statelessly(channel_id = 0, price = 10000000, endpoint = "localhost:8080")

request_class = get_request_class(channel_id = 0, method_name = "add")
request = request_class(a = 10, b = 32)

rez = stub.add(request)
print(rez)

rez = stub.add(request)
print(rez)

rez = stub.mul(request)
print(rez)

rez = stub.div(request)
print(rez)

