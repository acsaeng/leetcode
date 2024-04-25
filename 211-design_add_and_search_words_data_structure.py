from utils.trie import TrieNode

class WordDictionary:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word: str) -> None:
    current_node = self.root

    for char in word:
      if char not in current_node.children:
        current_node.children[char] = TrieNode()
      
      current_node = current_node.children[char]
    
    current_node.end_of_word = True

  def search(self, word: str) -> bool:
    return self.dfs(word, self.root)
  
  def dfs(self, substr, node):
    current_node = node

    for i, char in enumerate(substr):
      if char == '.':
        for child in current_node.children.values():
          if self.dfs(substr[i + 1:], child):
            return True
        
        return False
      else:
        if char not in current_node.children:
          return False
        
        current_node = current_node.children[char]

    return current_node.end_of_word


print('Case 1: ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"], [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]')
wordDictionary  = WordDictionary()
print([None, wordDictionary.addWord('bad'), wordDictionary.addWord('dad'), wordDictionary.addWord('mad'), wordDictionary.search('pad'), wordDictionary.search('bad'), wordDictionary.search('.ad'), wordDictionary.search('b..')])
      