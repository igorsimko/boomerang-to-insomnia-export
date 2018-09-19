import json
from pprint import pprint
import uuid
import time


def current_milli_time():
    return int(round(time.time() * 1000))

def get_id(prefix):
    return prefix + "_" + str(uuid.uuid4()).replace('-','')

def create_request_group(name, parent):
    nid = get_id("fld")
    group_base = {
			"_id": nid,
			"created": current_milli_time(),
			"description": "",
			"environment": {},
			"metaSortKey": -1537340035588,
			"modified": current_milli_time(),
			"name": name,
			"parentId": parent,
			"_type": "request_group"
		}
    return group_base

def create_request(name, endpoint, parent, body, method, headers, mode):
    request = {
			"_id": get_id("req"),
			"authentication": {},
			"body": {
				"mimeType": mode,
				"text": body},
			"created": current_milli_time(),
			"description": "",
			"headers": headers,
			"isPrivate": False,
			"metaSortKey": -1537340032699.5,
			"method": method,
			"modified": current_milli_time(),
			"name": name,
			"parameters": [],
			"parentId": parent,
			"settingDisableRenderRequestBody": False,
			"settingEncodeUrl": True,
			"settingMaxTimelineDataSize": 1000,
			"settingRebuildPath": True,
			"settingSendCookies": True,
			"settingStoreCookies": True,
			"url": endpoint,
			"_type": "request"
		}
    return request

# add your own environment data
def create_env(name, data, parent):
    env = {
			"_id": get_id("env"),
			"color": None,
			"created": current_milli_time(),
			"data": data,
			"isPrivate": False,
			"metaSortKey": current_milli_time(),
			"modified": current_milli_time(),
			"name": name,
			"parentId": parent,
			"_type": "environment"
		}
    return env


with open('boomerang_export.json', encoding="utf-8") as f:
    data = json.load(f)

insomnia_resources = []

insomnia_data = {}
insomnia_data["_type"] = "export"
insomnia_data["__export_format"] = 3
# optional change
insomnia_data["__export_date"] = "2017-01-10T23:15:55.928Z"
# optional change
insomnia_data["__export_source"] = "insomnia.desktop.app:v6.0.2"
insomnia_data["resources"] = []


insomnia_workspace = {
			"_id": get_id("wrk"),
			"created": current_milli_time(),
			"description": "",
			"modified": current_milli_time(),
            # change workspace name
			"name": "Boomerang export workspace",
			"parentId": None,
			"_type": "workspace"
		}

insomnia_env_parent = {
			"_id": get_id("env"),
			"color": None,
			"created": current_milli_time(),
			"data": {
				"key": "value"
			},
			"isPrivate": False,
			"metaSortKey": current_milli_time(),
			"modified": current_milli_time(),
			"name": "Base environment",
			"parentId": insomnia_workspace["_id"],
			"_type": "environment"
		}

insomnia_resources.append(insomnia_workspace)
insomnia_resources.append(insomnia_env_parent)

# change environment name
# you can append another env with another name and data
env_data = {
				"key": "value"
			}
insomnia_resources.append(create_env("DEV", env_data, insomnia_env_parent["_id"]))

# loop in boomerang export json
for service in data['projects'][0]['_services']:
    # create request_group parents
    print("+" + service["name"])
    request_group_parent_parent = create_request_group(service["name"],insomnia_workspace["_id"])
    insomnia_resources.append(request_group_parent_parent)

    for operation in service['_operations']:
        # create request_group based on parents
        if "_SYSTEM_" not in operation["name"]: 
            print("\t+" + operation["name"])
            request_group_parent = create_request_group(operation["name"],request_group_parent_parent["_id"])
            insomnia_resources.append(request_group_parent)

            for request in operation['_requests']:
                    print("\t|" + request["name"])
                    request_base = create_request(request["name"], request["endpoint"], request_group_parent["_id"], request["payload"]["raw"], request["method"], request["headers"], request["payload"]["mode"])
                    insomnia_resources.append(request_base)

insomnia_data["resources"] = insomnia_resources

# save data to json
with open('insomnia_import.json', 'w') as outfile:
    json.dump(insomnia_data, outfile)
