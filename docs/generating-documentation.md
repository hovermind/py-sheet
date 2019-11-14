## Installations
* `pip install sphinx` (sphinix has: `sphinx-quickstart`)
* `pip install sphinxcontrib-napoleon` (for google style)
* right click on project > show in explorer
* right click > open git bash
  * `mkdir docs`
  * `cd docs/`
  * `sphinx-quickstart`

## Configurations
* [`conf.py`](#)
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
* generating api docs:
