class Jumbler:
    def __init__(self, letters, trie):
        self.letters = letters
        self.trie = trie
        self.wordsFound = []
    
    def findAllWords(self):
        for actualWord in self._getAllPermutations(self.letters):
            if self.trie.isWord(actualWord):
                self.wordsFound.append(actualWord)
    
    #Performance is pretty bad on this. Though finding all permutations of all substrings of a string is going to be, even for itertools.
    def _getAllPermutations(self, word):
        raw = self._getAllPermutationsHelper(word)
        res = []
        for item in raw:
            if type(item) == tuple:
                res.append(item[0])
            else:
                res.append(item)
        return set(res)
        
    #Get all the permutations by taking each individual letter
    #Then adding all the permutations of the remaining letters to it
    def _getAllPermutationsHelper(self, word):
        words = []
        previousStepsWords = []
        currentStepsWords = []
        for letter in xrange(len(word)):
            if letter < len(word) - 1:
                toIns = (word[letter], word[:letter]+word[letter+1:])
            else:
                toIns = (word[letter], word[:letter])
            if toIns not in words:
                words.append(toIns)
        permLength = 1
        previousStepsWords = words[:]
        while permLength < len(word):
            for permutation in previousStepsWords:
                for newPerm in self._getAllPermutationsHelper(permutation[1]):
                    if permutation[0] + newPerm[0] not in words:
                        words.append(permutation[0] + newPerm[0])
                        currentStepsWords.append((permutation[0] + newPerm[0], newPerm[1]))
            previousStepsWords = currentStepsWords[:]
            currentStepsWords = []
            permLength += 1
        return words

