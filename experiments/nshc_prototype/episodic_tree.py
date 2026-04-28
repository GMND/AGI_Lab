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
