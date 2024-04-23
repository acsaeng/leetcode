from utils.trie import TrieNode

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    current_node = self.root

    for char in word:
      if char not in current_node.children:
        current_node.children[char] = TrieNode()
      
      current_node = current_node.children[char]
    
    current_node.end_of_word = True
      
  def search(self, word: str) -> bool:
    current_node = self.root

    for char in word:
      if char not in current_node.children:
        return False
      
      current_node = current_node.children[char]
    
    return current_node.end_of_word
      
  def startsWith(self, prefix: str) -> bool:
    current_node = self.root

    for char in prefix:
      if char not in current_node.children:
        return False
      
      current_node = current_node.children[char]
    
    return True


print('Case 1: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"], [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]')
trie  = Trie()
print([None, trie.insert('apple'), trie.search('apple'), trie.search('app'), trie.startsWith('app'), trie.insert('app'), trie.search('app')])