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


def add_share_first_2_only(t, path, value):
    add_share_first_N_only(t, path, 2, value)


def add_share_first_3_only(t, path, value):
    add_share_first_N_only(t, path, 3, value)


def add_share_first_N_only(t, path, N, value):
    if len(path) <= N:
        add(t, path, value)
        return
    shared_nodes = path[:N];
    for node in shared_nodes:
        if node not in t:
            t[node] = {}
        t = t[node]
    nonshared_nodes = path[N:];
    for node in nonshared_nodes:
        if node not in t:
            t[node] = {}
            t = t[node]
        else:
            postfix = 2
            newnode = node + str(postfix)
            while newnode in t:
                postfix += 1
                newnode = node + str(postfix)
            t[newnode] = {}
            t = t[newnode]
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
