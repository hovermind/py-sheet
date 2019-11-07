## Data class
```python
from dataclasses import dataclass
from src import DataFormat


@dataclass
class Info():
    project_name: str
    data_format: DataFormat
```
