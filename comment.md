# TOC
* [Comment](#Comment)
* [Doc comment](#Doc-comment)

## Comment
* single line: `# this is single line commenct`
* multi-line:
```python
''' This is 
    Multi-line comment 
    in python
'''

# to avoid new line after """, use '\'
"""\
This is an example
of a multi-line string
in Python.
""" 
```

## Doc comment
**Sample 1**
```python
from typing import List
from src import Info


def get_info(line: str, delimiter: str = " ") -> Info:
    """\
    Splits given line with specified delimiter and returns Info class.
    If no delimiter is given, then space is used by default.

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

**Sample 2**
```python
def complex(real=0.0, imag=0.0):
    """\
    Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...
```
