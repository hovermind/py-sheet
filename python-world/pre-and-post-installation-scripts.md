## pre-installation script
`fooapp/setup.py`
```py
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Setup file for fooapp.
"""
from setuptools import setup, find_packages
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


def run_pre_setup_tasks():
    print("executing pre setup tasks...")



class PreDevelopCommand(develop):
    """
    Pre-installation for development mode.
    """

    def run(self):
        print("pre install")
        run_pre_setup_tasks()

        print("installing app...")
        develop.run(self)


class PreInstallCommand(install):
    """
    Pre-installation for installation mode.
    """

    def run(self):
        print("pre install")
        run_pre_setup_tasks()

        print("installing app...")
        install.run(self)


setup(name="fooapp",
      version='1.0.0',
      description="This is foo app",
      cmdclass={
          'develop': PreDevelopCommand,
          'install': PreInstallCommand,
      }
      )

```

## post-installation script
See: https://stackoverflow.com/a/36902139
