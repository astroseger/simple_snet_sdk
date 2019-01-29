from simple_sdk import get_service_stub
from snet_cli.utils import DefaultAttributeObject

    
stub = get_service_stub(channel_id = 0, price = 10000000, endpoint = "localhost:8080")

request = DefaultAttributeObject(a = 10, b = 32)

rez = stub.add(request)
print(rez)

rez = stub.mul(request)
print(rez)

rez = stub.div(request)
print(rez)

