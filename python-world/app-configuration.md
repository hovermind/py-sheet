# TOC
* [yaml config](#yaml-config)
* [json config](https://martin-thoma.com/configuration-files-in-python/#json)
* courtesy: https://martin-thoma.com/configuration-files-in-python/

## yaml config
#### config file
`foolib/config.yml`
```yml
lib_setup_info:
  name: foolib
  version: 1.0.0
  description: Library for foo analysis
  author: HASSAN
  author_email: hassan@hovermind.com
  url: hovermind.com
  license: free

bar:
  baz1
  baz2
```

#### setup file
`foolib/setup.py`
```python
# -*- encoding: utf-8 -*-
"""
Setup file for foo analysis lib.
"""
from setuptools import setup, find_packages
import yaml

with open("config.yml", 'r') as config_file:
    config = yaml.load(config_file)
    lib_setup_info = config['lib_setup_info']

    setup(name=lib_setup_info['name'],
          version=lib_setup_info['version'],
          description=lib_setup_info['description'],
          author=lib_setup_info['author'],
          author_email=lib_setup_info['author_email'],
          url=lib_setup_info['url'],
          license=lib_setup_info['license'],
          platforms='any',
          zip_safe=False,
          # http://pypi.python.org/pypi?%3Aaction=list_classifiers
          classifiers=['Programming Language :: Python',
                       'Programming Language :: Python :: 3.7',
                       'Programming Language :: Python :: 3.8',
                       ],
          packages=find_packages(exclude=('tests',)),
          include_package_data=True,
          install_requires=['PyYAML'],
          )

```
