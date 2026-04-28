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

    def _sim(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def insert(self, content, embedding):
        emb = np.array(embedding)
        if self.root is None:
            self.root = EpisodicNode(content, emb)
            return self.root
        best_p, max_s = self.root, self._sim(emb, self.root.embedding)
        stack = [self.root]
        while stack:
            curr = stack.pop()
            for c in curr.children:
                s = self._sim(emb, c.embedding)
                if s > max_s:
                    max_s, best_p = s, c
                stack.append(c)
        new_n = EpisodicNode(content, emb, 1.0 - max_s)
        best_p.children.append(new_n)
        return new_n
