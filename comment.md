# TOC

## Doc comment
```python
from typing import List
from src import Info


def get_info(line: str, delimiter: str = " ") -> Info:
    """\
    Splits given line with specified delimiter and returns Info class
    If no delimiter is given, then space is used by default

    Parameters
    ----------
    line : str
        a none empty string to split
    delimiter : str
        optional delimiter for splitting the given string
    """
    if line.strip():
        parts: List[str] = line.split(line, delimiter)
        info = Info(parts[0], parts[1], parts[2], parts[3])
        return info
    return None
```
