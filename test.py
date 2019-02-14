from simple_sdk import get_service_stub_for_call_statelessly, get_request_class

stub = get_service_stub_for_call_statelessly(org_id = "DappTesOrganization", service_id = "DappTesthttpsService")
request_class = get_request_class(org_id = "DappTesOrganization", service_id = "DappTesthttpsService", method_name = "add")
request = request_class(a = 10, b = 32)

rez = stub.add(request)
print(rez)

rez = stub.add(request)
print(rez)

rez = stub.mul(request)
print(rez)

rez = stub.div(request)
print(rez)

