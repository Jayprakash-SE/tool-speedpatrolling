def get(dict, name):
    """Get a list of IDs by name from a container.

    The list is automatically limited to the 1000 highest IDs.
    """
    ids = dict.get(name, [])
    ids.sort(reverse=True)
    del ids[1000:]
    dict[name] = ids
    return ids


def append(dict, name, id):
    """Append an ID to a list of IDs by that name in a container."""
    ids = dict.get(name, [])
    ids.append(id)
    dict[name] = ids