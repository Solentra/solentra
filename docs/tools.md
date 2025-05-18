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

### train_model

```python
from sklearn.ensemble import RandomForestClassifier

# Train model with hyperparameter tuning
model = RandomForestClassifier()
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20]
}

training = MLTools.train_model(
    model=model,
    X_train=data['X_train'],
    y_train=data['y_train'],
    param_grid=param_grid,
    cv=5
)
```

### evaluate_model

```python
# Evaluate model performance
metrics = MLTools.evaluate_model(
    model=training['model'],
    X_test=data['X_test'],
    y_test=data['y_test'],
    task_type="classification"
)
```

## DataTools

The `DataTools` class provides utilities for data management and quality control.

### validate_dataset

```python
from solentra.tools import DataTools
import pandas as pd

# Create sample dataset
data = pd.DataFrame({
    'A': [1, 2, 2, 3, None],
    'B': ['x', 'y', 'y', 'z', 'z'],
    'C': [1.1, 2.2, 2.2, 3.3, 4.4]
})

# Validate dataset
rules = {
    'dtypes': {
        'A': 'float64',
        'B': 'object',
        'C': 'float64'
    },
    'required_columns': ['A', 'B', 'C']
}

validation = DataTools.validate_dataset(data, rules)
```

### clean_dataset

```python
# Clean dataset
operations = [
    {'type': 'remove_duplicates'},
    {'type': 'fill_missing', 'method': 'mean'}
]

cleaned = DataTools.clean_dataset(data, operations)
```
