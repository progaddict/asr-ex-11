import collections

# http://lxml.de/
import lxml.etree

# https://gist.github.com/hrldcpr/2012250
def tree():
    return collections.defaultdict(tree)

def add(t, path):
  for node in path:
    t = t[node]

# Task 11.1 (b) (i)
def task_b_i(xmlRoot):
    complete_tree = tree()
    for lemma in xmlRoot.iter('lemma'):
        if ('special' in lemma.attrib):
            continue
        word = lemma.find('orth').text
        phonemes = lemma.find('phon').text.split(' ')
        print(phonemes)

xmlDoc = lxml.etree.parse('lexicon.xml')
print('parsed lexicon.xml')
total_number_of_lemmas = int(xmlDoc.xpath('count(//lemma)'))
number_of_special_lemmas = int(xmlDoc.xpath('count(//lemma[@special])'))
total_number_of_words = total_number_of_lemmas - number_of_special_lemmas
print('lemmas: ', total_number_of_lemmas)
print('special lemmas: ', number_of_special_lemmas)
print('actual words: ', total_number_of_words)
xmlRoot = xmlDoc.getroot()
task_b_i(xmlRoot)
print('done')
