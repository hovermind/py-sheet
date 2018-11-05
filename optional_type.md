## Optional type
```python
from typing import Optional

name: Optional[str] = None
id: Optional[int]

# Optional return type
def getDatetime(arg: int = None) -> Optional[datetime]:
    # body

```
**Note: `Optional[X]` is equivalent to `Union[X, None]` where `Union[X, Y]` means a value of type X or Y**
