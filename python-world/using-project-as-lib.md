## Requirement
* project must contain [`setup.py`](/python-world/setup-py.md)
* `pip install --upgrade /path/to/repo` : will use `setup.py` to build `.whl` and put that `.whl` file in site-packages (as like pip install from pypi.org)

## Development installation
* `pip install -e path/to/repo`
* `-e`: flag indicates editable
* pip will constantly look at repo and build wheel and put that wheel to site-packages. So latest code from repo will be always available as lib 

## Production Installation
Any of the followings:
* use [ensure_packages.py](/python-world/ensure_packages.md) in main script
* use [pre-installation task](/python-world/pre-and-post-installation-scripts.md#pre-installation-script) in `setup.py`
* from command

### [ensure_packages.py](/python-world/ensure_packages.md#ensure-packages-module) in main script   
`start.py`
```python

... ... ...

if __name__ == '__main__':
    pkg_name: str = "foo"
    pkg_src_dir: str = "../foo"
    
    # use ensure_packages.py as module
    from ensure_packages import install_packages
    install_packages([(pkg_name, pkg_src_dir)])
    
    # or run ensure_packages.py with args
    import subprocess
    subprocess.call(['python', './ensure_packages.py', pkg_name, pkg_src_dir])
```

### [pre-installation task](/python-world/pre-and-post-installation-scripts.md#pre-installation-script) in `setup.py`
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

### command
manually install lib first in the production machine and then install/use app
* CMD/Termical in project forlder
* `pip install --upgrade path/to/repo`
