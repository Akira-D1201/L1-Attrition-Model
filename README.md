# L1 Attrition Model

A computational model testing whether L1 Chinese undergoes attrition during L3 Japanese learning in different language environments. The model distinguishes between **performance interference** (temporary access difficulty due to cross-language competition) and **competence attrition** (permanent loss of lexical representations).

## Research Question

Does learning an L3 in an L1-dominant environment cause genuine L1 attrition, or only temporary performance interference?

## Theoretical Framework

Based on:
- BIA+ model (Dijkstra & Van Heuven, 2002)
- Inhibitory Control model (Green, 1998)
- Language Mode hypothesis (Grosjean, 2001)
- Activation Threshold hypothesis (De Bot, 2007)

## Model Design

- **Scenario A (L1 Environment)** : L1 baseline decays minimally (0.001/day), simulating continued L1 use and top-down protection.
- **Scenario B (L2 Environment)** : L1 baseline decays significantly (0.005/day), simulating L1 disuse and sustained inhibition from L2/L3.
- L3 Japanese baseline increases daily at a fixed learning rate in both scenarios.

## Key Findings

1. In the **L1 environment**, L1 activation drops sharply after Month 3 due to intense cross-language competition but **never reaches zero**, indicating that the L1 lexical node remains intact.
2. In the **L2 environment**, L1 activation drops to **zero** by Month 6, indicating complete attrition.
3. The L1 environment protects the **competence** (the mental lexicon) but cannot fully prevent **performance interference** (temporary suppression by a stronger L3).

## Implications

- Explains why advanced L3 learners may show L1 "unusualness" (e.g., reduced readability, code-switching) without actual L1 loss.
- Predicts reversibility in L1 environment: if L3 input stops, L1 performance can recover.
- Predicts irreversibility in L2 environment: once L1 activation reaches zero, recovery is impossible without re-learning.

## File Structure

- `L1_attrition_model.py`: Python implementation of the model.
- `L1_attrition_model.png`: Visualization comparing L1 activation trajectories.

## Author

Wenjing DUAN

## License

This project is shared for academic portfolio purposes. If you use or adapt this code or ideas, please cite this repository.
