import numpy as np
class EpisodicNode:
    def __init__(self, content, embedding, importance_score=0.0):
        self.content = content
        self.embedding = np.array(embedding)
        self.importance_score = importance_score
        self.children = []

class EpisodicTree:
    def __init__(self):
        self.root = None

    def insert(self, content, embedding):
        new_node = EpisodicNode(content, embedding)
        if self.root is None:
            self.root = new_node
            return self.root
        target = self.root
        while target.children:
            target = target.children[0]
        target.children.append(new_node)
        return new_node
