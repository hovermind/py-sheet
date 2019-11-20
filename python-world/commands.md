# TOC
* [python](#python)
* [pip](#pip)
* [setup.py](#setup)

## python
check version: cmd
```cmd
python --version
```

## pip
* install from git: https://pip.pypa.io/en/stable/reference/pip_install/#git
* details: https://packaging.python.org/tutorials/installing-packages/

version check: cmd
```cmd
pip --version
```

pip not installed (linux)
```cmd
python -m pip install --upgrade pip setuptools wheel
```

pip installed (windows)
```cmd
pip install --upgrade pip setuptools wheel
```

install packages from `requiremetns.txt`
```cmd
pip install -r requirements.txt
```

Check package is installed
```cmd
pip show foo
```

extract requirements
```cmd
pip freeze > requirements.txt
```

install from local git repo
* git repo must contain `setup.py`
* `setup(...)`should not have `script_args=[]`

CMD
```cmd
pip install path/to/repo
pip install .
```

script
```py
from subprocess import call
from sys import executable

call([executable, "-m", "pip", "install", "../my-lib"])
```

## setup
Command: `setup.py ...` (CMD/Terminal in project_dir)
* files are generated in `project_dir/dist`
* `setup.py bdist_egg` -> `.egg` (as like `.jar` in java)
* `setup.py sdist` -> `.tar.gz`
* `setup.py sdist bdist_wheel` -> `.tar.gz` and `. whl`
* `setup.py bdist` -> `.zip`
* `setup.py bdist_wheel` -> `.whl`
* `setup.py bdist_wheel -d target_dir`
