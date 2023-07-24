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
        x = filter_data(j, json.loads(filters))
        if x:
            results.append(j)
    return results
