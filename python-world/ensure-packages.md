## ensure packages module
`ensure_packages.py`
```py
"""
Ensures required packages/libs are installed.
"""
import subprocess
import sys
from subprocess import call
from sys import executable, argv
from typing import List, Tuple


def package_exists(package_name: str) -> bool:
    """
    Checks if the given package is installed (pip install...)

    Args:
        package_name (str): name of the package to check

    Returns:
        bool - True if exists, False otherwise
    """
    requirements = subprocess.check_output([executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in
                          requirements.split()]

    return package_name in installed_packages


def install_packages(package_list: List[Tuple[str, str]]):
    """
    Installs given packages

    Args:
        package_list (List[Tuple[str, str]]): list of (pkg_name, pkg_dir) tuples
    """
    for (package_name, package_src_dir) in package_list:
        if package_name.strip():
            if package_src_dir.strip():
                # install from local dir
                # print(f"pip install {package_src_dir}")
                call([executable, "-m", "pip", "install", "--upgrade",
                      package_src_dir])
            else:
                # install from pypi.org index
                # print(f"pip install {package_name}")
                call(
                    [executable, "-m", "pip", "install", "--upgrade",
                     package_name])


if __name__ == '__main__':
    args_count = len(sys.argv)

    pkg_name: str = "PyYAML"
    pkg_dir: str = None

    # sys.argv[0]: script name
    # sys.argv[1]: package name to install
    # sys.argv[2]: local package dir (when installing a package from source
    #              in local dir)
    if args_count >= 3:
        pkg_name = argv[1]
        pkg_dir = argv[2]
    if args_count >= 2:
        pkg_name = argv[1]

    install_packages(package_list=[(pkg_name, pkg_dir)])

```

## Method 1
use `ensure_packages.install_packages()` in main script    
`start.py`
```py
from ensure_packages import install_packages
    
if __name__ == '__main__':
    pkg_name: str = "foo"
    pkg_src_dir: str = "../foo"

    install_packages([(pkg_name, pkg_src_dir)])
```

## Method 2
run `ensure_packages.py` with args from main script    
`start.py`
```py
import subprocess
    
if __name__ == '__main__':
    pkg_name: str = "foo"
    pkg_src_dir: str = "../foo"

    subprocess.call(['python', './ensure_packages.py', pkg_name, pkg_src_dir])
```

## Method 3
use [pre-installation task](/python-world/pre-and-post-installation-scripts.md#pre-installation-script) in `setup.py`   
`setup.py`
```py
from ensure_packages import install_packages
... ... ...

def run_pre_setup_tasks():
    pkg_name: str = "foo"
    pkg_src_dir: str = "../foo"
    install_packages([(pkg_name, pkg_src_dir)])
    
... ... ...
```
