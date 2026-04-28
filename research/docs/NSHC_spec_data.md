# NSHC Technical Specification: Part 1 - Data Structures

## 1.1 Episodic Node
```python
class EpisodicNode:
    id: str
    content: str
    embedding: np.array
    importance_score: float
    children: list
```

## 1.2 Semantic Concept
```python
class SemanticConcept:
    id: str
    label: str
    definition: str
    relations: dict
    confidence: float
```