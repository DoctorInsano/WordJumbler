from jumbler import *
from trie import *
import sys
def main(word):
    finder = Jumbler(word, makeEnglishTrie())
    finder.findAllWords()
    print "The following words can be constructed with letters from the string \""+word+"\""
    for i in finder.wordsFound:
        print i
if __name__ == '__main__':
    main(sys.argv[1])