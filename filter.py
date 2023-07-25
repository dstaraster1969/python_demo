import json


def filter_all(json_objs, filters):
    # We want to run the first filter on all the json objects
    results = apply_filter(json_objs, filters[0])

    # For the rest of the filters, we want to feed it just the json objects that were just returned
    for f in filters:
        results = apply_filter(results, f)
    return results


def apply_filter(json_objs, f):
    results = []
    for j in json_objs:
        if check_for_match(j, f):
            results.append(j)

    return results


def check_for_match(j, f):
    if f == {}:
        return True
    try:
        key = list(f.keys())[0]
        if not type(f[key]) == dict:
            if j[key] == f[key]:
                return True
        else:
            check_for_match(j[key], f[key])
    except KeyError:
        return False
