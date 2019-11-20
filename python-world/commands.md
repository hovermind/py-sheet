## python
check version: cmd
```cmd
python --version
```

## pip
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

Details: https://packaging.python.org/tutorials/installing-packages/

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
