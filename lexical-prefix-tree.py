import pprint

# http://lxml.de/
import lxml.etree

from my_package import tree_stuff

# cart mapping from cart.phone
cart_from_file = {}

# cart state mapping from cart.state
cart_state_from_file = {}


def get_total_number_of_phonemes_without_sharing(xmlRoot):
    result = 0
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')
            result += len(phoneme_path)
    return result


def get_total_number_of_triphonemes_state_without_sharing(xmlRoot):
    result = 0
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task e) transforms to triphonemes to cart states
            phoneme_path = phonemes_to_triphones(phoneme_path)
            phoneme_path = triphones_to_cart_state(phoneme_path)

            result += len(phoneme_path)
    return result


def phonemes_to_triphones(phonemes):
    triphones = []
    # triphone positions
    pre = "#"
    mid = "#"
    end = "#"
    for i in range(0, len(phonemes)):
        # edge case: beginning
        if (i == 0):
            pre = "#"
        else:
            pre = mid

        mid = phonemes[i]

        # edge case: end
        if (i == len(phonemes) - 1):
            end = "#"
        else:
            end = phonemes[i + 1]

        triphones.append("" + mid + "{" + pre + "+" + end + "}")

    return triphones


def triphones_to_cart(triphones):
    cart = []

    for i in range(0, len(triphones)):
        cart.append(cart_from_file[triphones[i]])

    return cart


def triphones_to_cart_state(triphones):
    cart = []

    for i in range(0, len(triphones)):
        # edge case: silence
        if (triphones[i] == "si{#+#}"):
            cart.append(cart_state_from_file[triphones[i] + ".0"])
        else:
            cart.append(cart_state_from_file[triphones[i] + ".0"])
            cart.append(cart_state_from_file[triphones[i] + ".1"])
            cart.append(cart_state_from_file[triphones[i] + ".2"])

    return cart


def get_total_number_of_triphonemes_without_sharing(xmlRoot):
    result = 0
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task c) transforms to triphonemes
            phoneme_path = phonemes_to_triphones(phoneme_path)

            result += len(phoneme_path)
    return result


def task_b_i(xmlRoot):
    # call factory function to produce a tree
    complete_tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        # special lemmas should be filtered out
        if ('special' in lemma.attrib):
            continue
        # we are interested in real words only
        word = lemma.find('orth').text
        # each word may have multiple pronunciations
        # i.e. there can be multiple <phon> tags inside one <lemma> tag
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')
            # phonemes is an array which corresponds to a path in the tree
            # so we add this path to the tree
            # for example, word = gabrielle
            # phonemes = [g, ae, b, r, iy, eh, l]
            # it means that there should be the path
            # of phonemes in the tree: g -> ae -> b -> r -> iy -> eh -> l
            # if we encounter another word with the same prefix e.g. galus (g ae l ix s)
            # then a part of the path will exist (g -> ae) and
            # a branch will be added (l -> ix -> s) to it
            tree_stuff.add(complete_tree, phoneme_path, word)
    return complete_tree


def task_b_ii(xmlRoot):
    tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')
            tree_stuff.add_share_first_2_only(tree, phoneme_path, word)
    return tree


def task_b_iii(xmlRoot):
    tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')
            tree_stuff.add_share_first_3_only(tree, phoneme_path, word)
    return tree


def task_c_i(xmlRoot):
    complete_tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task c) transforms to triphonemes
            phoneme_path = phonemes_to_triphones(phoneme_path)

            tree_stuff.add(complete_tree, phoneme_path, word)
    return complete_tree


def task_c_ii(xmlRoot):
    tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task c) transforms to triphonemes
            phoneme_path = phonemes_to_triphones(phoneme_path)

            tree_stuff.add_share_first_2_only(tree, phoneme_path, word)
    return tree


def task_c_iii(xmlRoot):
    tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task c) transforms to triphonemes
            phoneme_path = phonemes_to_triphones(phoneme_path)

            tree_stuff.add_share_first_3_only(tree, phoneme_path, word)
    return tree


def task_d_i(xmlRoot):
    complete_tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task d) transforms to triphonemes to cart
            phoneme_path = phonemes_to_triphones(phoneme_path)
            phoneme_path = triphones_to_cart(phoneme_path)

            tree_stuff.add(complete_tree, phoneme_path, word)
    return complete_tree


def task_d_ii(xmlRoot):
    tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task d) transforms to triphonemes to cart
            phoneme_path = phonemes_to_triphones(phoneme_path)
            phoneme_path = triphones_to_cart(phoneme_path)

            tree_stuff.add_share_first_2_only(tree, phoneme_path, word)
    return tree


def task_d_iii(xmlRoot):
    tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task d) transforms to triphonemes to cart
            phoneme_path = phonemes_to_triphones(phoneme_path)
            phoneme_path = triphones_to_cart(phoneme_path)

            tree_stuff.add_share_first_3_only(tree, phoneme_path, word)
    return tree


def task_e_i(xmlRoot):
    complete_tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task e) transforms to triphonemes to cart states
            phoneme_path = phonemes_to_triphones(phoneme_path)
            phoneme_path = triphones_to_cart_state(phoneme_path)

            tree_stuff.add(complete_tree, phoneme_path, word)
    return complete_tree


def task_e_ii(xmlRoot):
    tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task e) transforms to triphonemes to cart states
            phoneme_path = phonemes_to_triphones(phoneme_path)
            phoneme_path = triphones_to_cart_state(phoneme_path)

            tree_stuff.add_share_first_2_only(tree, phoneme_path, word)
    return tree


def task_e_iii(xmlRoot):
    tree = tree_stuff.getTree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')

            # for task e) transforms to triphonemes to cart states
            phoneme_path = phonemes_to_triphones(phoneme_path)
            phoneme_path = triphones_to_cart_state(phoneme_path)

            tree_stuff.add_share_first_3_only(tree, phoneme_path, word)
    return tree


def print_stats_and_stuff(t, output_file_name=None):
    number_of_nodes = tree_stuff.count_number_of_nodes(t)
    print('number of nodes in the tree = ', number_of_nodes)
    if output_file_name is not None:
        print('writing the tree into ' + output_file_name + '...')
        pp = pprint.PrettyPrinter(indent=2, stream=open(output_file_name, 'w', encoding='utf-8'))
        pp.pprint(t)
        print('done')
    print('without sharing number of nodes would be = ', number_of_nodes_without_sharing)
    print('therefore the compression ratio = ', number_of_nodes_without_sharing / number_of_nodes)


xmlDoc = lxml.etree.parse('lexicon.xml')
print('parsed lexicon.xml')
total_number_of_lemmas = int(xmlDoc.xpath('count(//lemma)'))
number_of_special_lemmas = int(xmlDoc.xpath('count(//lemma[@special])'))
total_number_of_words = total_number_of_lemmas - number_of_special_lemmas
print('lemmas: ', total_number_of_lemmas)
print('special lemmas: ', number_of_special_lemmas)
print('actual words: ', total_number_of_words)
xmlRoot = xmlDoc.getroot()
number_of_nodes_without_sharing = get_total_number_of_phonemes_without_sharing(xmlRoot)

print('')
print('PART (b) (i) FULL SHARING')
print('building a tree...')
complete_tree = task_b_i(xmlRoot)
print('done')
print_stats_and_stuff(complete_tree, 'complete_tree.txt')

print('')
print('PART (b) (ii) FIRST TWO PHONEMES ARE SHARED')
print('building a tree...')
tree_with_only_2_first_phonemes_shared = task_b_ii(xmlRoot)
print('done')
print_stats_and_stuff(tree_with_only_2_first_phonemes_shared, 'tree_2_shared.txt')

print('')
print('PART (b) (iii) FIRST THREE PHONEMES ARE SHARED')
print('building a tree...')
tree_with_only_3_first_phonemes_shared = task_b_iii(xmlRoot)
print('done')
print_stats_and_stuff(tree_with_only_3_first_phonemes_shared, 'tree_3_shared.txt')

print('')
print('')

print('')
print('PART (c) (i) TRIPHONES - FULL SHARING')
print('building a tree...')
complete_tree = task_c_i(xmlRoot)
print('done')
print_stats_and_stuff(complete_tree, 'complete_tree_c.txt')

print('')
print('PART (c) (ii) TRIPHONES - FIRST TWO TRIPHONEMES ARE SHARED')
print('building a tree...')
tree_with_only_2_first_triphonemes_shared = task_c_ii(xmlRoot)
print('done')
print_stats_and_stuff(tree_with_only_2_first_triphonemes_shared, 'tree_2_shared_c.txt')

print('')
print('PART (c) (iii) TRIPHONES - FIRST THREE TRIPHONEMES ARE SHARED')
print('building a tree...')
tree_with_only_3_first_triphonemes_shared = task_c_iii(xmlRoot)
print('done')
print_stats_and_stuff(tree_with_only_3_first_triphonemes_shared, 'tree_3_shared_c.txt')

# read in file for (d)
with open('cart.phone', 'r') as cart:
    for line in cart:
        words = line.split(' ')
        # save mapping from triphones to states
        # [0:-2] to get rid of unnecessary newline symbol
        cart_from_file[words[0]] = words[1][0:-2]

print('')
print('')

print('')
print('PART (d) (i) TRIPHONES CART - FULL SHARING')
print('building a tree...')
complete_tree = task_d_i(xmlRoot)
print('done')
print_stats_and_stuff(complete_tree, 'complete_tree_d.txt')

print('')
print('PART (d) (ii) TRIPHONES CART - FIRST TWO CART TRIPHONEMES ARE SHARED')
print('building a tree...')
tree_with_only_2_first_triphonemes_shared = task_d_ii(xmlRoot)
print('done')
print_stats_and_stuff(tree_with_only_2_first_triphonemes_shared, 'tree_2_shared_d.txt')

print('')
print('PART (d) (iii) TRIPHONES CART - FIRST THREE CART TRIPHONEMES ARE SHARED')
print('building a tree...')
tree_with_only_3_first_triphonemes_shared = task_d_iii(xmlRoot)
print('done')
print_stats_and_stuff(tree_with_only_3_first_triphonemes_shared, 'tree_3_shared_d.txt')

# read in file for (e)
with open('cart.state', 'r') as cart:
    for line in cart:
        words = line.split(' ')
        # save mapping from triphones to states
        # [0:-2] to get rid of unnecessary newline symbol
        cart_state_from_file[words[0]] = words[1][0:-2]

print('')
print('')

xmlRoot = xmlDoc.getroot()
number_of_nodes_without_sharing = get_total_number_of_triphonemes_state_without_sharing(xmlRoot)

print('')
print('PART (e) (i) TRIPHONES CART STATES - FULL SHARING')
print('building a tree...')
complete_tree = task_e_i(xmlRoot)
print('done')
print_stats_and_stuff(complete_tree, 'complete_tree_e.txt')

print('')
print('PART (e) (ii) TRIPHONES CART STATES - FIRST TWO CART TRIPHONEMES STATES ARE SHARED')
print('building a tree...')
tree_with_only_2_first_triphonemes_shared = task_e_ii(xmlRoot)
print('done')
print_stats_and_stuff(tree_with_only_2_first_triphonemes_shared, 'tree_2_shared_e.txt')

print('')
print('PART (e) (iii) TRIPHONES CART STATES - FIRST THREE CART TRIPHONEMES STATES ARE SHARED')
print('building a tree...')
tree_with_only_3_first_triphonemes_shared = task_e_iii(xmlRoot)
print('done')
print_stats_and_stuff(tree_with_only_3_first_triphonemes_shared, 'tree_3_shared_e.txt')
