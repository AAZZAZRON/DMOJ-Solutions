from sys import stdin
input = stdin.readline


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children: # if child is already in trie
                node = node.children[char]
            else: # if child is not in trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
    def found(self, x):
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True


x = int(input())
for q in range(1, x + 1):
    tr = Trie()
    counter = 0
    num = int(input())
    for _ in range(num):
        done = False
        word = input()[:-1]
        for i in range(1, len(word)):
            if not tr.found(word[:i]):
                counter += i
                done = True
                break
        tr.insert(word)
        if not done:
            counter += len(word)
    print(f"Case #{q}: {counter}")
