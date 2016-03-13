class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.dic = dict()
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        n = len(word)
        if n in self.dic:
            self.dic[n].append(word)
        else:
            self.dic[n] = [word]
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        n = len(word)
        res = 0
        
        if n not in self.dic:
            return False
        
        for elem in self.dic[n]:
            if self.isMatch(elem, word):
                res += 1
        return res > 0
        
    def isMatch(self, a, b):
        for i in range(len(a)):
            if b[i] != '.' and a[i] != b[i]:
                return False
        
        return True
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")