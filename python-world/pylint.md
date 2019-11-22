# TOC
* [Pylint PyCharm plugin](#Pylint-PyCharm-plugin)
* [Pylint settings](#Pylint=settings)

## Pylint PyCharm plugin
* cmd: `pip install pylint`
* copy `pylint.exe` path: search pylint > right click > open file location
* install pylint PyCharm plugin: 
  * Settings > Plugins
  * search pylint > install
* set `pylint.exe` location to pylint plugin
  * Settings > Pylint
  * Path to Pylint executable: `C:\Users\hassan\AppData\Local\Programs\Python\Python38-32\Scripts\pylint.exe`
  * test > ok
* View > Tool Windows > Pylint (should show in the bottom left)

## Pylint settings
#### config file: `.pylintrc`
In project folder (CMD): `pylint --generate-rcfile > .pylintrc`    

`.pylintrc`
```text
... ... ...

# Ignore imports when computing similarities.
ignore-imports=yes

... ... ...
```

or create `.pylintrc` manually and copy text from cmd: `pylint --generate-rcfile`

#### Arguments in PyCharm
* Max line length: Settings > Pylint > Arguments: `--max-line-length=120`
