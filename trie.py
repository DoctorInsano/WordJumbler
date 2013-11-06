from __future__ import with_statement
import os.path as path
import pickle
class Trie:
    def __init__(self):
        self._sentinel = Node("", False)
        return
    
    def addWord(self, word):
        current = self._sentinel
        #last letter is a special case
        for letter in word[:-1]:
            current.addChild(Node(letter, False))
            current = current.getChild(letter)
        current.addChild(Node(word[-1], True, word))
        return
    
    def removeWord(self, word):
        current = self._sentinel
        for letter in word:
            current = current.getChild(letter)
        current.endOfWord = False
        current.fullWord = ""
    
    def isWord(self, word):
        current = self._sentinel
        for letter in word:
            current = current.getChild(letter)
        return current.endOfWord
        
class Node:
    def __init__(self, letter, endOfWord, fullWord = ""):
        self.letter = letter
        self.endOfWord = endOfWord
        self.fullWord = fullWord
        self.children = {}
        
    def __eq__(self, toComp):
        return self.letter == toComp.letter and self.endOfWord == toComp.endOfWord and self.fullWord == toComp.fullWord and self.children == toComp.children
    
    def addChild(self, node):
        if self.children.has_key(node.letter): 
            if node.endOfWord:
                toUpdate = self.children[node.letter]
                toUpdate.endOfWord = True
                toUpdate.fullWord = node.fullWord
        else:
            self.children[node.letter] = node
    
    def getChild(self, letter):
        return self.children.get(letter, Node("", False))
 
def makeEnglishTrie():
    res = Trie()
    with open("words.txt", "r") as f:
        for word in f:
            res.addWord(word.strip().lower())
    return res