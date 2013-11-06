import unittest
from trie import Node
from trie import Trie
from trie import makeEnglishTrie
from jumbler import Jumbler
import itertools

class testNode(unittest.TestCase):
    def setUp(self):
        return
    
    def test_creation(self):
        node = Node("b", False)
        self.assertEqual(node.letter, "b")
        self.assertFalse(node.endOfWord)
        self.assertEqual(node.children, {})
        self.assertEqual(node.fullWord, "")
    
    def test_addingChildren(self):
        c = Node("c", False)
        a = Node("a", False)
        t = Node("t", True, "cat")
        c.addChild(a)
        a.addChild(t)
        self.assertEqual(c.children, {"a": a})
        self.assertEqual(a.children, {"t": t})
    
    def test_adding_dupes(self):
        c = Node("c", False)
        a = Node("a", False)
        t = Node("t", True, "cat")
        c.addChild(a)
        a.addChild(t)
        a.addChild(t)
        self.assertEqual(c.children, {"a": a})
        self.assertEqual(a.children, {"t": t})
    
    def test_getting_children(self):
        c = Node("c", False)
        a = Node("a", False)
        t = Node("t", True, "cat")
        c.addChild(a)
        a.addChild(t)
        self.assertEqual(c.getChild("a"), a)
        self.assertEqual(a.getChild("t"), t)
        self.assertEqual(c.getChild("b"), Node("", False))

class testTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.addWord("cat")
    
    def test_check_is_word(self):
        self.assertTrue(self.trie.isWord("cat"))
        self.assertFalse(self.trie.isWord("ca"))
    
    def test_remove_word(self):
        self.trie.removeWord("cat")
        self.assertFalse(self.trie.isWord("cat"))
    
    def test_words_with_shared_letters(self):
        self.trie.addWord("cab")
        self.assertTrue(self.trie.isWord("cat"))
        self.assertFalse(self.trie.isWord("ca"))
        self.assertTrue(self.trie.isWord("cab"))

    def test_node_children(self):
        self.trie.addWord("cab")
        self.trie.addWord("dog")
        self.assertEqual(self.trie._sentinel.children.keys(), ["c","d"])
    
class test_English_language(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trie = makeEnglishTrie()
    
    def test_English_words(self):
        with open("words.txt") as f:
            for word in f:
                self.assertTrue(self.trie.isWord(word.strip().lower()))
        self.assertFalse(self.trie.isWord("asdf"))

class test_Jumbler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trie = makeEnglishTrie()
    
    def test_dog(self):
        jumbler = Jumbler("dog", self.trie)
        jumbler.findAllWords()
        self.assertTrue("dog" in jumbler.wordsFound)
        self.assertTrue("do" in jumbler.wordsFound)
        self.assertTrue("god" in jumbler.wordsFound)
        self.assertTrue("go" in jumbler.wordsFound)
    
    def test_getAllPermutations(self):
        wordtotest = "cat"
        iterToolsResult = []
        for i in range(1,len(wordtotest)+1):
                iterToolsResult += itertools.permutations(wordtotest, i)
        jumbler = Jumbler(wordtotest, self.trie)
        permutations = jumbler._getAllPermutations(wordtotest)
        self.assertEqual(len(permutations), len(set(iterToolsResult)))
        for permutation in ['c', 'a', 't', 'ca', 'ct', 'ac', 'at', 'tc', 'ta', 'cat', 'cta', 'act', 'atc', 'tca', 'tac']:
            self.assertIn(permutation, permutations, msg=permutation + "Not found in list of permutations")

    def test_wordWithDuplicateLetters(self):
        wordtotest = "alley"
        iterToolsResult = []
        for i in range(1,len(wordtotest)+1):
                iterToolsResult += itertools.permutations(wordtotest, i)
        jumbler = Jumbler(wordtotest, self.trie)
        permutations = jumbler._getAllPermutations(wordtotest)
        self.assertEqual(len(permutations), len(set(iterToolsResult)))
            
if __name__ == "__main__":
    unittest.main()