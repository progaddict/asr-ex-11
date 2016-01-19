# do not use for a phoneme name
VALUE_KEY = '_value'


def getTree():
    return {}


def add(t, path, value):
    for node in path:
        if node not in t:
            t[node] = {}
        t = t[node]
    setValue(t, value)


def hasValue(t, value):
    return (VALUE_KEY in t)


def setValue(t, value):
    t[VALUE_KEY] = value


def getValue(t, value):
    if not hasValue(t):
        return None
    return t[VALUE_KEY]


def deleteValue(t):
    if not hasValue(t):
        return
    del t[VALUE_KEY]


def count_number_of_nodes(t):
    # this node also counts
    # therefore we initialize with 1
    number_of_nodes = 1
    for node in t:
        if node == VALUE_KEY:
            continue
        number_of_nodes += count_number_of_nodes(t[node])
    return number_of_nodes


def _test():
    pass


if __name__ == '__main__':
    _test()
