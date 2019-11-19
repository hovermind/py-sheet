## Setup file
* `setup.py` in root folder (i.e. repo)
* pip install path/to/root`: uses `setup.py`
* use `packages` param to mention that main src in usb folder of root folder
* use `scripts` param

`setup.py`
```python
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages


setup(name='foo',
      version='1.0',
      description='Foo bar baz',
      author='HASSAN',
      author_email="hassan@hovermind.com",
      home_page='hovermind.com',
      license='free',
      platforms='any',
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   ],
      packages=find_packages(exclude=('tests',)),
      include_package_data=True,
      install_requires=['wheel',
                        'python_world@git+https://github.com/ceddlyburge' \
                         '/python_world#egg=python_world-0.0.1'],
      )
```
