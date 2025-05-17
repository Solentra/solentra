# Tools Documentation

The Solentra package provides various tool classes for scientific research, data analysis, and collaboration.

## MLTools

The `MLTools` class provides utilities for machine learning model training, evaluation, and analysis.

### prepare_data

```python
from solentra.tools import MLTools
import numpy as np

# Prepare data for training
X = np.random.randn(100, 4)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

data = MLTools.prepare_data(
    X=X,
    y=y,
    test_size=0.2,
    random_state=42
)
```
