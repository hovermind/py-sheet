## Requirement
* project must contain [`setup.py`](/python-world/setup-py.md)
* `pip install --upgrade /path/to/repo` : will use `setup.py` to build `.whl` and put that `.whl` file in site-packages (as like pip install from pypi.org)

## Development installation
* `pip install -e path/to/repo`
* `-e`: flag indicates editable
* pip will constantly look at repo and build wheel and put that wheel to site-packages. So latest code from repo will be always available as lib 

# Production Installation
### Production Installation from script
**1. Use [ensure_packages.py](/python-world/ensure_packages.md) in main script**
`start.py`
```python
from ensure_packages import install_packages

if __name__ == '__main__':
    pkg_name: str = "foo"
    pkg_src_dir: str = "../foo"
    install_packages([(pkg_name, pkg_src_dir)])
```
**2. Use in [pre-installation script](/python-world/pre-and-post-installation-scripts.md#pre-installation-script) `setup.py`**
`setup.py`
```py
def run_pre_setup_tasks():
    pkg_name: str = "foo"
    pkg_src_dir: str = "../foo"
    install_packages([(pkg_name, pkg_src_dir)])
```

## Production Installation from command
manually install lib first in the production machine and then install/use app
* CMD/Termical in project forlder
* `pip install --upgrade path/to/repo`
