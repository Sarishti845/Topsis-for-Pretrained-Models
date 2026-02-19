# Text Classification Model Selection using TOPSIS

## Problem Statement
Select best pretrained model for text classification using TOPSIS method.

## Models Compared
- BERT
- RoBERTa
- DistilBERT
- ALBERT
- XLNet

## Criteria Used
1. Accuracy (+)
2. F1 Score (+)
3. Precision (+)
4. Recall (+)
5. Model Size (-)
6. Inference Time (-)

## Methodology
1. Normalize decision matrix
2. Apply weights
3. Determine ideal best and worst
4. Calculate Euclidean distances
5. Compute TOPSIS score
6. Rank models

## Result
Model with highest TOPSIS score is considered best.

## Conclusion
Based on TOPSIS analysis, the top ranked model provides best balance between performance and efficiency.
