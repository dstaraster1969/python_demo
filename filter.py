import json


def filter_data(j, f):
    if f == {}:
        return True
    try:
        key = list(f.keys())[0]
        if not type(f[key]) == dict:
            return j[key] == f[key]
        return filter_data(j[key], f[key])
    except:
        return False


def filter_all(json_objs, filters):
    results = []
    for j in json_objs:
        bools = []
        for f in filters:
            json_string = '{"' + f + '": "' + filters[f] + '"}'
            x = filter_data(j, json.loads(json_string))
            bools.append(x)
        if all(bools):
            results.append(j)
    return results