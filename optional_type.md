`Optional[X]` is equivalent to `Union[X, None]` where `Union[X, Y]` means a value of type X or Y
```
from typing import Optional

name: Optional[str] = None
id: Optional[int]

def getDatetime(arg: int = None) -> Optional[datetime]:
    # body

```
