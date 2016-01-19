import pprint

# http://lxml.de/
import lxml.etree

from my_package import tree_stuff


def get_total_number_of_phonemes_without_sharing(xmlRoot):
    result = 0
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        for phon in lemma.iter('phon'):
            phoneme_path = phon.text.split(' ')
            result += len(phoneme_path)
    return result


# Task 11.1 (b) (i)
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


xmlDoc = lxml.etree.parse('lexicon.xml')
print('parsed lexicon.xml')
total_number_of_lemmas = int(xmlDoc.xpath('count(//lemma)'))
number_of_special_lemmas = int(xmlDoc.xpath('count(//lemma[@special])'))
total_number_of_words = total_number_of_lemmas - number_of_special_lemmas
print('lemmas: ', total_number_of_lemmas)
print('special lemmas: ', number_of_special_lemmas)
print('actual words: ', total_number_of_words)
xmlRoot = xmlDoc.getroot()
print()
print('PART (b) (i)')
complete_tree = task_b_i(xmlRoot)
print('complete tree has been built')
number_of_nodes_in_complete_tree = tree_stuff.count_number_of_nodes(complete_tree)
print('number of nodes in the tree = ', number_of_nodes_in_complete_tree)
number_of_nodes_without_sharing = get_total_number_of_phonemes_without_sharing(xmlRoot)
print('without sharing number of nodes would be = ', number_of_nodes_without_sharing)
print('therefore the compression ratio = ', number_of_nodes_without_sharing / number_of_nodes_in_complete_tree)
print()
print('PART (b) (i)')
print('printing the tree into complete_tree.txt...')
pp = pprint.PrettyPrinter(indent=2, stream=open('complete_tree.txt', 'w', encoding='utf-8'))
pp.pprint(complete_tree)
print('done printing')
print('done')
