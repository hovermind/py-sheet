# Running script from another script
* https://stackoverflow.com/questions/3781851/run-a-python-script-from-another-python-script-passing-in-arguments
* https://docs.python.org/3/library/runpy.html

## subprocess call
```py
import subprocess

subprocess.call(['python', './foo_lib.py', 'arg1', 'arg2']) # foo_lib is current dir
```

## os.system
```py
import os

os.system("python ./foo_lib.py arg1 arg2")  # foo_lib is current dir
```

## runpy


```py
import runpy

runpy.run_path(path_name='./foo_lib.py')
```
