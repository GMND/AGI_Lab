# Literature Review: Action Tokenization & LAM

## 1. Categorical Action Spaces
- **Standard Tool-Use (e.g., Gorilla, Toolformer):** Uses text-based function calls. *Limitation:* High latency, high token cost, lacks continuous precision.

## 2. Quantized Continuous Actions
- **VQ-VAE/VQ-GAN Approaches:** Maps continuous inputs (like images or robotic joint angles) to discrete codebook indices. *Relevance:* Highly applicable to LAM for parameterizing actions (e.g., mouse coordinates).
- **Residual Vector Quantization (RVQ):** Used in models like SoundStream/EnCodec. It allows representing values with multiple layers of codebooks, increasing precision without exploding vocabulary size. *Key takeaway: We should consider RVQ for our Action Tokenization.*

## 3. Hierarchical Decision Making
- **Hierarchical RL (HRL):** Decomposes tasks into high-level goals and low-level actions. *Relevance:* Our LAM should operate on two levels: Semantic Tokens (High-level) and Parametric Tokens (Low-level).

## 4. Diffusion-based Action Generation
- **Diffusion Policy:** Generates continuous action trajectories. *Conflict/Synergy:* While Diffusion is powerful, it is often non-autoregressive. Integrating Diffusion-like smoothness into a discrete token transformer (our goal) is a potential research gap.

## Summary of Research Gaps
- Most current models focus on *either* text-based tool use *or* purely continuous control (Robotics). A unified transformer architecture that treats both as a single stream of hybrid tokens (Semantic + RVQ-Parametric) is missing.