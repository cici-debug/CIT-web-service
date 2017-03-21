#!/usr/bin/python

import json

new_data = []

with open('items.json', 'r') as raw_file:
	raw_data = json.load(raw_file)
	for data in raw_data:
		if data.get("supportRequestFormat", "").find("REST") > 0:
			tmp = dict()
			tmp["name"] = data.get("name", None)
			tmp["primaryCategory"] = data.get("primaryCategory", None)
			tmp["secondaryCategory"] = data.get("secondaryCategory", None)
			tmp["portal"] = data.get("portal", None)
			tmp["docsURL"] = data.get("docsURL", None)
			tmp["termsOfService"] = data.get("termsOfServive", None)
			new_data.append(tmp)

with open('extracted.json', 'w') as new_file:
	json.dump(new_data, new_file)