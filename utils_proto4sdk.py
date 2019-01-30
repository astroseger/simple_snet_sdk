""" Utils related to protobuf """
import sys
from pathlib import Path
import os
from snet_cli.utils_proto import import_protobuf_from_dir_get_all


def import_protobuf_get_all_method_names(proto_dir, service_name = ""):
    all_services = import_protobuf_from_dir_get_all(proto_dir)
    
    if (service_name):
        if (service_name not in all_services):
            raise Exception("Error while loading protobuf. Cannot find service=%s"%service_name)
        return list(all_service[service_name])
    
    method_names = []
    for service_name in all_services:
        method_names += list(all_services[service_name])
    return method_names
