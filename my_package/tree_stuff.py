# do not use for a phoneme name
VALUE_KEY = '_value'


def getTree():
    return {}


def add(t, path, value):
    current_node = t
    for node in path:
        if node not in current_node:
            current_node[node] = {}
        current_node = current_node[node]
    setValue(current_node, value)


def add_share_first_2_only(t, path, value):
    add_share_first_N_only(t, path, 2, value)


def add_share_first_3_only(t, path, value):
    add_share_first_N_only(t, path, 3, value)


def add_share_first_N_only(t, path, N, value):
    if len(path) <= N:
        add(t, path, value)
        return
    current_node = t
    shared_nodes = path[:N];
    for phoneme in shared_nodes:
        if phoneme not in current_node:
            current_node[phoneme] = {}
        current_node = current_node[phoneme]
    nonshared_nodes = path[N:];
    for phoneme in nonshared_nodes:
        if phoneme not in current_node:
            current_node[phoneme] = {}
            current_node = current_node[phoneme]
        else:
            postfix = 2
            newnode = phoneme + str(postfix)
            while newnode in current_node:
                postfix += 1
                newnode = phoneme + str(postfix)
            current_node[newnode] = {}
            current_node = current_node[newnode]
    setValue(current_node, value)


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
