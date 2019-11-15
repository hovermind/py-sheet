# TOC
* [Generating docs by PyCharm (IDE tools)](#Generating-docs-by-PyCharm-IDE)
* [Generating docs by commands in git bash or cmd (commands only)](#Generating-docs-by-commands-in-git-bash-or-cmd)

# Generating docs by PyCharm IDE

## Setup docs folder
* Create 'docs' folder in project folder
* Set Sphinix working directory: 
  * `File > Settings > Tools > Python Integrated Tools > reStructuredText
  * Sphinix working directory: .../<project folder>/docs`
* Sphinx Quickstart:
  * Tools > Sphinx Quickstart
  * Separate source and build directories (y/n) [n]: y
  * Project name: Foo
  * Author name(s): HASSAN
  * Project release []: (press enter for default, you can change `conf.py` later)
  * Project language [en]: en, ja
  * check docs folder:
    * build => generated html (/other) files will be here
	* source => contains [`conf.py`](#) (edit it according to you need), `index.rst` ...
	* `make.bat` => you can run `make html` to generate html (`make.bat` uses Makefile)

## sphinx-apidoc to generate rst files
sphinx-apidoc is part of Sphinx that generates `.rst` files (from docstring in `.py` source code)

#### By sphinx-apidoc command in PyCharm terminal
* set `sphinx-apidoc.exe` location to environment variable
  * copy `sphinx-apidoc.exe` path: `C:\Users\<foo>\AppData\Local\Programs\Python\Python38-32\Scripts\sphinx-apidoc.exe`
  * Environment variables > System variables > Path > Edit > New > Paste: copy `sphinx-apidoc.exe` path
  * now we can execute sphinx-apidoc commands from PyCharm terminal
* open PyCharm termical: `cd docs`
* `sphinx-apidoc -f -o source/ ../`
    * `-f`: file
	* `-o source/`: `.rst` output folder, it is source folder for Sphinx build to generate html or other type file
	* `../`: python module location, in other words `.py` source code location which is project folder

#### By sphinx-apidoc task
* copy `sphinx-apidoc.exe` path: `C:\Users\<foo>\AppData\Local\Programs\Python\Python38-32\Scripts\sphinx-apidoc.exe` (if you click folder icon, PyCharm will not show `.exe` since it is looking for `.py` scripts, so you have to put `sphinx-apidoc.exe` manually)
* Run > Edit Configurations > '+' > select: Python
  * Name: Generate rst files
  * Script path: paste `sphinx-apidoc.exe` path
  * Parameters: `-f -o source/ ../`
    * `-f`: file
    * `-o source/`: `.rst` output folder, it is source folder for Sphinx build to generate html or other type file
    * `../`: python module location, in other words `.py` source code location which is project folder
* View > Tool Windows > Run
* Select : Generate rst files > press: run 
* **trouble shooting**: `PermissionError: [WinError 5] Access is denied: 'source/'`
  * close PyCharm
  * Run PyCharm as Administrator
  * if task does not work, use command aproach

## Sphinx build to generate html files from rst files
#### By command in PyCharm terminal
* Terminal > `cd docs` if not in docs folder (no need if already in docs folder)
* Makefile:
  * Sphinx Quickstart created a `make.bat` for our convinience in docs folder 
  * `make html`
  * html files will be generated in build/html folder
* sphinx-build:
  * `sphinx-build -b html source build/html` (execute command from docs folder)
    *`-b`: builder type
    *`-b html`: html builder
	* `source`: `.rst` fles in source folder
    * `build/htm`: html files will be generated in build/html folder

#### By sphinx task
* Run > Edit Configurations > '+' > select: Python docs > Sphinx task
* Name: Generate html docs
* Command: html
* Input: `C:\Users\hassan\Documents\MyProject\docs\source`
* Output: `C:\Users\hassan\Documents\MyProject\docs\build\html`
* Run: 'Generate html docs' (View > Tool Window > Run)


# Generating docs by commands in git bash or cmd


## Installations
* `pip install sphinx` (sphinix has: `sphinx-quickstart`)
* `pip install sphinxcontrib-napoleon` (for google style)
* right click on project > show in explorer
* right click > open git bash
  * `mkdir docs`
  * `cd docs/`
  * `sphinx-quickstart`

## Configurations
* [`conf.py`](/docs/conf-py.md)
* extensions: https://www.sphinx-doc.org/en/master/usage/extensions/

## Generate sphinix files 
* `.rst`: sphinix file/reStructuredText files
* command: `sphinx-apidoc -o source/ ../<package>` (execute command from docs folder)
  * `sphinx-apidoc`: generates `.rst` files from docstring
  * `-o source/`: `.rst` files (and etc.) will be generated in source folder (docs/source)
  * `../<package>`: `../` is project folder (parent of doc folder) and optinal package name (if not mentioned, all package will be included)

## Generate html files 
* **method 1**: `sphinx-build -b html ./ html` (execute command from docs folder)
  * `-b`: builder type
  * `-b html`: html builder
  * `./`: `.rst` fles in current folder
  * `html`: output folder
  * creates docs in docks/html
* **method 2**: `make html` (execute command from docs folder)
  * (sphinx-quickstart script creates a Makefile and a make.bat which make life even easier )
  * creates docs in docks/_build/html
