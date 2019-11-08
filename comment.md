# TOC
* [Comment](#Comment)
* [Doc comment / docstring](#Doc-comment)
  * [python.org style](#python-official)
  * [google guideline](#google-guideline)
  * [Other doc comment style](#Other-doc-comment-style)

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
* https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
* https://www.datacamp.com/community/tutorials/docstrings-python

#### python official
* https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings
```python

```

#### google guideline
* https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
* http://google.github.io/styleguide/pyguide.html

Module level function
```python
def module_level_function(param1, param2 = None, *args, **kwargs):
    """This is an example of a module level function.

    Function parameters should be documented in the ``Args`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    If \*args or \*\*kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name (type): description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        param1 (int): The first parameter.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
```

#### Other doc comment style
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
