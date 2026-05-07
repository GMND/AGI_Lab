# Implementation Plan: Hierarchical Action Tokenizer

## 1. Project Structure
- `src/`: Python source code.
  - `__init__.py`: Package initialization.
  - `hierarchical_tokenizer.py`: Core tokenization logic.
  - `hierarchical_env.py`: Gymnasium environment wrapper.
- `RESEARCH/`: Research documents.
- `EXPERIMENTS/`: Experimental logs.

## 2. Module: `src/hierarchical_tokenizer.py`
### Class: `HierarchicalToken`
- Represents a node in the action tree.
- Attributes: `level` (TokenLevel), `value` (str), `vector` (np.ndarray).

### Class: `HierarchicalActionTokenizer`
- `encode(text)`: Parses string to tree.
- `decode(tree)`: Converts tree to valid action dict.
- `get_embeddings(tree)`: Retrieves or projects embeddings.

## 3. Module: `src/hierarchical_env.py`
### Class: `HierarchicalActionWrapper(gym.Wrapper)`
- Wraps any Gymnasium environment.
- Translates hierarchical actions into primitive environment steps.
- Handles errors (e.g., invalid syntax).

## 4. Next Steps
- Implement `encode/decode`.
- Test with dummy environment.
- Integrate with LLM agent.
