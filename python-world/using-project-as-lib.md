## Requirement
* project must contain [`setup.py`](/python-world/setup-py.md)
* `pip install --upgrade /path/to/repo` : will use `setup.py` to build `.whl` and put that `.whl` file in site-packages (as like pip install from pypi.org)

## Installation
#### CMD
* CMD/Termical in project forlder
* `pip install --upgrade path/to/repo`

#### From script
`ensure_lib.py`
```python
"""
Ensure required libs are installed.
"""
import subprocess
from subprocess import call
from sys import executable
from typing import List, Tuple


def pkg_exists(pkg_name: str) -> bool:
    """
    Checks if the given package is installed (pip install...)

    Args:
        pkg_name (str): name of the package to check

    Returns:
        bool - True if exists, False otherwise
    """
    reqs = subprocess.check_output([executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    if pkg_name in installed_packages:
        print(f"{pkg_name} exists.")
        return True
    else:
        print(f"{pkg_name} does not exists.")
        return False


def install_pkg_from_src(pkg_list: List[Tuple[str, str]]):
    """
    Installs packages from src dirs

    Args:
        pkg_list (List[Tuple[str, str]]): list of (pkg, pkg_dir) tuples
    """
    for (pkg_name, pkg_src_dir) in pkg_list:
        # if not pkg_exists(pkg_name): print(f"pip install {pkg_src_dir}")
        # call([executable, "-m", "pip", "install", "--upgrade", pkg_src_dir])
        print(f"installing package {pkg_name}")
        print(f"pip install {pkg_src_dir}")
        call([executable, "-m", "pip", "install", "--upgrade", pkg_src_dir])
```
`app.py`
```python
from ensure_lib import install_pkg_from_src

if __name__ == '__main__':
    pkg_name: str = "foo"
    pkg_src_dir: str = "../foo"
    install_pkg_from_src([(pkg_name, pkg_src_dir)])
```
